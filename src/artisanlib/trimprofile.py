#
# ABOUT
# Artisan Profile Trimmer
#  and flag when there is an error in the message history

# LICENSE
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

# AUTHOR
# Dave Baxter, 2023

# pylint: disable='pointless-string-statement'


# To add 'Trim profile' to the Tools menu and enable this function
# paste the folowing code into main.py immediately above 
#        # VIEW menu
'''
        #dave40 start...
        self.trimAction = QAction(QApplication.translate('Menu', 'Trim profile'), self)
        self.trimAction.triggered.connect(self.trimprofile_dialog)
        self.ToolkitMenu.addAction(self.trimAction)
        #dave40 ...end
'''
# then paste the following as a function in main:ApplicationWindow, typically at the end
# following simulate()
'''
    #dave40 start...
    @pyqtSlot()
    @pyqtSlot(bool)
    def trimProfile(self,_=False):
        from artisanlib.trimprofile import trimprofile_dlg
        trimprofile_dlg(self)
    #dave40 ...end
'''

import sys
import numpy
import logging

from typing import List
from typing_extensions import Final

from artisanlib.util import stringfromseconds

try:
    from PyQt6.QtWidgets import (QApplication, QInputDialog, QMessageBox) # @UnusedImport @Reimport  @UnresolvedImport
except ImportError:
    from PyQt5.QtWidgets import (QApplication, QInputDialog, QMessageBox) # type: ignore # @UnusedImport @Reimport  @UnresolvedImport

_log: Final = logging.getLogger(__name__)

def trimprofile_dlg(self) -> None:
    _log.debug(">>>  In method trimprofile_dlg")
    _log.debug("self %s",self)
    if not self.qmc.flagon and self.qmc.timeindex[0]>0 and (self.qmc.timeindex[6]>0 or self.qmc.timeindex[7]>0):
        trimseconds:float = 15.
        trimseconds, ok = QInputDialog.getDouble(self,
                QApplication.translate("Message", "Trim Profile"),
                QApplication.translate("Message", "Caution!  Data will be deleted from the profile!\n\nApproximate number of seconds \nto leave for leader and trailer:"),
                trimseconds, 0., 45.)
        if ok:
            actual_sampling_interval = self.float2float((self.qmc.timex[-1] - self.qmc.timex[0])/len(self.qmc.timex),2)
            trimsamples = int(max(1,numpy.around(trimseconds / actual_sampling_interval)))  #never less than one sample 
            _log.debug("trimsamples: %s, trimseconds: %s, actual_sampling_interval: %s",trimsamples, trimseconds, actual_sampling_interval)
            profiletrimmer(self,trimsamples)
    else:
        string = QApplication.translate("Message","Trim requires a CHARGE event and either a DROP or a COOL event.", None)
        QMessageBox.warning(self,QApplication.translate("Message","Trim Profile"),string,QMessageBox.StandardButton.Cancel)

def profiletrimmer(self,trimsamples:int=3) -> None:
    if not self.qmc.flagon and self.qmc.timeindex[0]>0 and (self.qmc.timeindex[6]>0 or self.qmc.timeindex[7]>0):
        try:
            droporcoolend:int = 1 + max(self.qmc.timeindex[7], self.qmc.timeindex[6])
            _log.debug("len(self.timex): %s, droporcoolend: %s", len(self.qmc.timex) , droporcoolend)

            # Trim the right side of the profile
            if (len(self.qmc.timex) - droporcoolend) > trimsamples:
                _log.debug("trim right from %s %s", droporcoolend + trimsamples, stringfromseconds(self.qmc.timex[droporcoolend + trimsamples]))
                self.qmc.timex = self.qmc.timex[0:droporcoolend + trimsamples]
                self.qmc.temp1 = self.qmc.temp1[0:droporcoolend + trimsamples]
                self.qmc.temp2 = self.qmc.temp2[0:droporcoolend + trimsamples]

                event:int
                for i, event in enumerate(self.qmc.specialevents[:]):
                    _log.debug("i: %s, self.qmc.specialevents[i]: %s", i, event)
                    if event >= droporcoolend + trimsamples:
                        self.qmc.specialevents = self.qmc.specialevents[:i]
                        self.qmc.specialeventsvalue = self.qmc.specialeventsvalue[:i]
                        self.qmc.specialeventstype = self.qmc.specialeventstype[:i]
                        self.qmc.specialeventsStrings = self.qmc.specialeventsStrings[:i]
                        break

            if len(self.qmc.extratimex) > 0:
                _log.debug("processing extratimex")
                for i, _ in enumerate(self.qmc.extratimex):
                    self.qmc.extratimex[i] = self.qmc.extratimex[i][0:droporcoolend + trimsamples]
                    self.qmc.extratemp1[i] = self.qmc.extratemp1[i][0:droporcoolend + trimsamples]
                    self.qmc.extratemp2[i] = self.qmc.extratemp2[i][0:droporcoolend + trimsamples]
                        
            # Trim the left side of the profile
            # adjust all the list numbers to the first entry after trimming on the left
            if self.qmc.timeindex[0] > trimsamples:
                firsttimeindex:int = self.qmc.timeindex[0]
                _log.debug("trim left to %s - %s = %s", self.qmc.timeindex[0], trimsamples, self.qmc.timeindex[0] - trimsamples)
                self.qmc.timex = self.qmc.timex[firsttimeindex - trimsamples:]
                self.qmc.temp1 = self.qmc.temp1[firsttimeindex - trimsamples:]
                self.qmc.temp2 = self.qmc.temp2[firsttimeindex - trimsamples:]
                
                firstnewtimex:float = self.qmc.timex[0]
                
                for i, _ in enumerate(self.qmc.timex):
                    self.qmc.timex[i] = self.qmc.timex[i] - firstnewtimex
                val:int
                for i, val in enumerate(self.qmc.timeindex):
                    if val > 0:
                        self.qmc.timeindex[i] = val - firsttimeindex + trimsamples
                        
                if len(self.qmc.extratimex) > 0 and len(self.qmc.extratimex[0]) > 0:
                    firstnewextratimex:List[float] = []
                    for i, _ in enumerate(self.qmc.extratimex):
                        self.qmc.extratimex[i] = self.qmc.extratimex[i][firsttimeindex - trimsamples:]
                        self.qmc.extratemp1[i] = self.qmc.extratemp1[i][firsttimeindex - trimsamples:]
                        self.qmc.extratemp2[i] = self.qmc.extratemp2[i][firsttimeindex - trimsamples:]
                        firstnewextratimex.append(self.qmc.extratimex[i][0])
                        for j, _ in enumerate(self.qmc.extratimex[i]):
                            self.qmc.extratimex[i][j] = self.qmc.extratimex[i][j] - firstnewextratimex[i]
                    
                for i, _ in reversed(list(enumerate(self.qmc.specialevents))):
                    if self.qmc.specialevents[i] < firsttimeindex - trimsamples:
                        self.qmc.specialevents        = self.qmc.specialevents[i:]
                        self.qmc.specialeventstype    = self.qmc.specialeventstype[i:]
                        self.qmc.specialeventsvalue   = self.qmc.specialeventsvalue[i:]
                        self.qmc.specialeventsStrings = self.qmc.specialeventsStrings[i:]
                        break

                # get the right "last" value before CHARGE for each specialeventstype
                for i, _ in enumerate(self.qmc.specialevents):
                    if self.qmc.specialevents[i] > 0:
                        self.qmc.specialevents[i] = max(self.qmc.specialevents[i] - firsttimeindex + trimsamples, 0)

            if self.qmc.autotimex:
                #patch since ~04/2023 during the refactoring  
                if self.qmc.background:
                    self.loadbackground(self.qmc.backgroundpath)
                self.autoAdjustAxis()

            # annotations can get whacky so clear them before redraw
            if self.qmc.annotationsflag:
                self.qmc.l_annotations_dict = {}
            self.qmc.redraw(forceRenewAxis=True)
            self.sendmessage(QApplication.translate('Message', 'Profile successfully trimmed'))

        except Exception as e: # pylint: disable=broad-except
            _, _, exc_tb = sys.exc_info()
            self.qmc.adderror((QApplication.translate("Error Message","Exception:",None) + " trimprofile() {0}").format(str(e)),getattr(exc_tb, 'tb_lineno', '?'))
        finally:
            self.setCurrentFile(None,addToRecent=False)
            self.qmc.fileDirty()
            _log.debug("Leaving trimprofile")


# ---------------------------------------------------------------------
# The following is here because I don't know where else to store it, 
# Flag when there is an error in the message history.
# When there is an error '* ' will be prepended to each subsequent message.
#
# In main:sendmessage_internal() paste the following code immediately after this line
#           self.messagelabel.setText(message)
'''
            #dave76 start...
            from artisanlib.trimprofile import flagErrorInMessageHist
            flagErrorInMessageHist(self,message)
            #dave76 end...
'''

def flagErrorInMessageHist(self, message:str) -> None:
    # Because self.qmc.errorlog is cleared on Reset another approach would be to look for 'Error' or 'Exception' in self.messagehist.
    if len(self.qmc.errorlog) > 0:
        self.messagelabel.setText(f'{"* " if len(self.qmc.errorlog) > 0 else ""}{message}')


