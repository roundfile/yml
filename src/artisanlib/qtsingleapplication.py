'''
Source: https://github.com/IARI/alsa_jack_gui
Author: https://github.com/IARI
Original Source: http://stackoverflow.com/questions/12712360/qtsingleapplication-for-pyside-or-pyqt
Original Author: user763305
Notes: Modified for PyQt5; further modified to remove blocking sockets remaining from died server
'''

import sys
import multiprocessing as mp

from PyQt5.QtCore import pyqtSignal, QTextStream, Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QLocalSocket, QLocalServer



class QtSingleApplication(QApplication):
    messageReceived = pyqtSignal(str)

    def __init__(self, _id,_viewer_id, *argv):
    
        if sys.platform.startswith("darwin") and mp.current_process().name == "WebLCDs":
            import AppKit
            info = AppKit.NSBundle.mainBundle().infoDictionary()  # @UndefinedVariable
            info["LSBackgroundOnly"] = "1"

        super(QtSingleApplication, self).__init__(*argv)
        
        self._id = _id
        self._viewer_id = _viewer_id
        self._activationWindow = None
        self._activateOnMessage = False

        self._outSocket = None
        self._isRunning = False        
        self._server = None
        
        # we exclude the WebLCDs parallel process from participating any Artisan inter-app communication
        if mp.current_process().name != "WebLCDs":
            # Is there another instance running?
            self._outSocket = QLocalSocket()
            self._outSocket.connectToServer(self._id)
            self._isRunning = self._outSocket.waitForConnected(-1)
            if self._isRunning:
                # Yes, there is.
                self._outStream = QTextStream(self._outSocket)
                self._outStream.setCodec('UTF-8')
                # Is there another viewer running?
                self._outSocketViewer = QLocalSocket()
                self._outSocketViewer.connectToServer(self._viewer_id)
                self._isRunningViewer = self._outSocketViewer.waitForConnected(-1)
                if self._isRunningViewer:
                    self._outStreamViewer = QTextStream(self._outSocketViewer)
                    self._outStreamViewer.setCodec('UTF-8')
                else:
                    # app is running, we announce us as viewer app
                    # First we remove existing servers of that name that might not have been properly closed as the server died
                    QLocalServer.removeServer(self._viewer_id) 
                    self._outSocketViewer = None
                    self._outStreamViewer = None
                    self._inSocket = None
                    self._inStream = None
                    self._server = QLocalServer()
                    self._server.listen(self._viewer_id)
                    self._server.newConnection.connect(self._onNewConnection)
            else:
                self._isRunningViewer = False
                # No, there isn't.
                # First we remove existing servers of that name that might not have been properly closed as the server died
                QLocalServer.removeServer(self._id) 
                self._outSocket = None
                self._outStream = None
                self._inSocket = None
                self._inStream = None
                self._server = QLocalServer()
                self._server.listen(self._id)
                self._server.newConnection.connect(self._onNewConnection)

    def isRunning(self):
        return self._isRunning

    def isRunningViewer(self):
        return self._isRunningViewer

    def id(self):
        return self._id

    def activationWindow(self):
        return self._activationWindow

    def setActivationWindow(self, activationWindow, activateOnMessage=True):
        self._activationWindow = activationWindow
        self._activateOnMessage = activateOnMessage

    def activateWindow(self):
        if not self._activationWindow:
            return

        self._activationWindow.show()
        self._activationWindow.setWindowState(
            self._activationWindow.windowState() & ~Qt.WindowMinimized)
        self._activationWindow.raise_()
        self._activationWindow.activateWindow()

    def sendMessage(self, msg):
        if not self._outStream:
            return False
        self._outStream << msg << '\n'
        self._outStream.flush()
        return self._outSocket.waitForBytesWritten()

    @pyqtSlot()
    def _onNewConnection(self):
        if self._inSocket:
            self._inSocket.readyRead.disconnect(self._onReadyRead)
        self._inSocket = self._server.nextPendingConnection()
        if not self._inSocket:
            return
        self._inStream = QTextStream(self._inSocket)
        self._inStream.setCodec('UTF-8')
        self._inSocket.readyRead.connect(self._onReadyRead)
        if self._activateOnMessage and self._isRunning:
            self.activateWindow()

    @pyqtSlot()
    def _onReadyRead(self):
        while True:
            msg = self._inStream.readLine()
            if not msg: break
            self.messageReceived.emit(msg)
