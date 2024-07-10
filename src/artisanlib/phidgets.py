#!/usr/bin/env python3

# ABOUT
# Phidgets support for Artisan

# LICENSE
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later versison. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

# AUTHOR
# Marko Luther, 2018


from Phidget22.Devices.Manager import Manager
from Phidget22.DeviceID import DeviceID
from Phidget22.DeviceClass import DeviceClass
from PyQt5.QtCore import (QSemaphore)

class PhidgetManager():

    def __init__(self):
        # a dictionary associating all physical attached Phidget channels
        # to their availablility state:
        #    True: available for attach to a software channel
        #    False: occupied and connected to a software channel
        # access to this dict is protected by the managersemaphore and
        # should happen only via the methods addChannel and deleteChannel
        self.attachedPhidgetChannels = {}
        self.managersemaphore = QSemaphore(1)
        self.manager = Manager()
        self.manager.setOnAttachHandler(self.attachHandler)
        self.manager.setOnDetachHandler(self.detachHandler)
        self.manager.open()
        
    def close(self):
        self.manager.close()
        self.attachedPhidgetChannels.clear()
        
    def attachHandler(self,_,attachedChannel):
        try:
            if attachedChannel.getParent().getDeviceClass() != DeviceClass.PHIDCLASS_HUB:
                # we do not add the hub itself
                self.addChannel(attachedChannel)
        except:
            pass
    
    def detachHandler(self,_,attachedChannel):
        try:
            self.deleteChannel(attachedChannel)
        except:
            pass
    
    def addChannel(self,channel):
        try:
            self.managersemaphore.acquire(1)
            state = True
            try:
                # reserve all channels with the same hubport on the same hub
                hub = channel.getHub()
                hubport = channel.getHubPort()
                hupportdevice = bool(channel.getIsHubPortDevice() == 0) # it is not a direct hubport channel
                for k, _ in self.attachedPhidgetChannels.items():
                    try:
                        khub = k.getHub()
                        khubport = k.getHubPort()
                        if khub == hub and khubport == hubport:
                            if hupportdevice:
                                if k.getIsHubPortDevice() != 0:
                                    self.attachedPhidgetChannels[k] = False
                                #else:
                                #  other is also a VINT device. Do nothing
                            else:
                                if k.getIsHubPortDevice() == 0:
                                    # there is a port registered with connected VINT device we deactivate this hubport channel
                                    state = False
                                #else:
                                #   do nothing
                    except:
                        pass
            except:
                pass
            self.attachedPhidgetChannels[channel] = state
        except Exception:
            pass
        finally:
            if self.managersemaphore.available() < 1:
                self.managersemaphore.release(1)

    def deleteChannel(self,channel):
        try:
            self.managersemaphore.acquire(1)
            # if channel is a VINT device, release all HUBport channels that were blocked by this VINT device
            try:
                hub = channel.getHub()
                hubport = channel.getHubPort()
                hupportdevice = bool(channel.getIsHubPortDevice() == 0) # it is not a direct hubport channel
                if hupportdevice:
                    for k, _ in self.attachedPhidgetChannels.items():
                        if k != channel:
                            try:
                                khub = k.getHub()
                                khubport = k.getHubPort()
                                if khub == hub and khubport == hubport:                                    
                                    self.attachedPhidgetChannels[k] = True
                            except:
                                pass
            except:
                pass
            self.attachedPhidgetChannels.pop(channel, None)
        except Exception:
            pass
        finally:
            if self.managersemaphore.available() < 1:
                self.managersemaphore.release(1)
                
    def getChannel(self,serial,port,channel,phidget_class_name,device_id,remote,remoteOnly):
        try:
            self.managersemaphore.acquire(1)
            if device_id in [DeviceID.PHIDID_HUB0000]:
                # we are looking for HUB ports
                hub = 1
            else:
                hub = 0
            for k, _ in self.attachedPhidgetChannels.items():
                if k.getIsHubPortDevice() or k.getDeviceClass() == DeviceClass.PHIDCLASS_VINT:
                    kport = k.getHubPort()
                else:
                    kport = 0  # getHubPort() returns 0 for USB Phidgets!
                if k.getDeviceSerialNumber() == serial and (port is None or kport == port) and \
                    (hub or (k.getDeviceID() == device_id)) and \
                    ((remote and not remoteOnly) or (not remote and k.getIsLocal()) or (remote and remoteOnly and not k.getIsLocal())) and \
                    k.getChannelClassName() == phidget_class_name and \
                    k.getChannel() == channel:
                    return k
            return None
        except Exception:
            return None
        finally:
            if self.managersemaphore.available() < 1:
                self.managersemaphore.release(1)
                
    def reserveSerialPort(self,serial,port,channel,phidget_class_name,device_id,remote=False,remoteOnly=False):
        chnl = self.getChannel(serial,port,channel,phidget_class_name,device_id,remote,remoteOnly)
        self.reserveChannel(chnl)
        
    def releaseSerialPort(self,serial,port,channel,phidget_class_name,device_id,remote=False,remoteOnly=False):
        chnl = self.getChannel(serial,port,channel,phidget_class_name,device_id,remote,remoteOnly)
        self.releaseChannel(chnl)

    # should be called from the attach handler that binds this hardware channel to a software channel
    def reserveChannel(self,channel):
        try:
            self.managersemaphore.acquire(1)
            if channel is not None and channel in self.attachedPhidgetChannels:
                self.attachedPhidgetChannels[channel] = False  # reserve channel
                if channel.getIsHubPortDevice():
                    hub = channel.getHub()
                    port = channel.getHubPort()
                    # reserve also all other channels with that hub/port combination
                    for k, _ in self.attachedPhidgetChannels.items():
                        try:
                            if k.getHub() == hub and k.getHubPort() == port:
                                self.attachedPhidgetChannels[k] = False
                        except:
                            pass
                #else:
                #  not a HUB port
        except:
            pass
        finally:
            if self.managersemaphore.available() < 1:
                self.managersemaphore.release(1)

    # should be called from the detach handler that releases this hardware channel fron a software channel
    def releaseChannel(self,channel):
        try:
            self.managersemaphore.acquire(1)
            if channel is not None and channel in self.attachedPhidgetChannels:
                self.attachedPhidgetChannels[channel] = True # channel again available for attach
                if channel.getIsHubPortDevice():
                    hub = channel.getHub()
                    port = channel.getHubPort()
                    # enable also all other channels with that hub/port combination
                    for k, _ in self.attachedPhidgetChannels.items():
                        try:
                            if k.getHub() == hub and k.getHubPort() == port:
                                self.attachedPhidgetChannels[k] = True
                        except:
                            pass                
        except Exception:
            pass
        finally:
            if self.managersemaphore.available() < 1:
                self.managersemaphore.release(1)
                
#    def print_list(self,items):
#        for k,v in items:
#            print(v,k.getDeviceSerialNumber(),k.getDeviceClass(),k.getDeviceClassName(),k.getDeviceName(),k.getDeviceSKU(),k.getChannelClassName(),k.getDeviceID(),k.getIsHubPortDevice(),"port: ",k.getHubPort(),"ch: ", k.getChannel(), "local: ", k.getIsLocal())
#
#    def print_list2(self,items):
#        for k in items:
#            print(k.getDeviceSerialNumber(),k.getChannelClassName(),k.getDeviceID(),k.getIsHubPortDevice(),"port: ", k.getHubPort(),"ch: ",k.getChannel(), "local: ", k.getIsLocal())

    # returns the first matching Phidget channel and reserves it
    def getFirstMatchingPhidget(self,phidget_class_name,device_id,channel=None,remote=False,remoteOnly=False,serial=None,hubport=None):
#        print("getFirstMatchingPhidget",phidget_class_name,device_id,channel,remote,remoteOnly,serial,hubport)
        try:
            self.managersemaphore.acquire(1)
            if device_id in [
                    DeviceID.PHIDID_HUB0000,
                    DeviceID.PHIDID_DIGITALINPUT_PORT,
                    DeviceID.PHIDID_DIGITALOUTPUT_PORT,
                    DeviceID.PHIDID_VOLTAGEINPUT_PORT,
                    DeviceID.PHIDID_VOLTAGERATIOINPUT_PORT]:
                # we are looking for HUB ports
                hub = 1
            else:
                hub = 0

#            self.print_list(self.attachedPhidgetChannels.items())

            # get list of all matching phidget channels
            matching_channels = [k for k, v in self.attachedPhidgetChannels.items() if v and \
                (hub or (k.getDeviceID() == device_id)) and \
                (serial is None or serial == k.getDeviceSerialNumber()) and \
                (hubport is None or hubport == k.getHubPort()) and \
                ((remote and not remoteOnly) or (not remote and k.getIsLocal()) or (remote and remoteOnly and not k.getIsLocal())) and \
                k.getChannelClassName() == phidget_class_name and \
                (channel is None or (not hub and channel == k.getChannel()) or (hub and k.getIsHubPortDevice() and k.getHubPort() == channel))]

#            self.print_list2(matching_channels)

            # sort by serial number (local first)
            matching_channels.sort(key=lambda x:(x.getDeviceSerialNumber(),x.getHubPort()))
            # return smallest / first item
            if len(matching_channels) > 0:
                p = matching_channels[0]
                if p.getIsHubPortDevice() or p.getDeviceClass() == DeviceClass.PHIDCLASS_VINT:
                    port = p.getHubPort()
                else:
                    port = None
                return p.getDeviceSerialNumber(), port
            else:
                return None, None
        except Exception:
            return None, None
        finally:
            if self.managersemaphore.available() < 1:
                self.managersemaphore.release(1)
