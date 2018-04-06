import servicemanager
import socket
import sys
import win32event
import win32service
import win32serviceutil
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TestService(win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            app = QApplication([])
            app.setQuitOnLastWindowClosed(False)

            icon = QIcon("icon.png")

            tray = QSystemTrayIcon()
            tray = QSystemTrayIcon(icon)
            tray.setVisible(True)

            menu = QMenu()
            action = QAction("A menu item")
            menu.addAction(action)

            tray.setContextMenu(menu)

            app.exec()

            with open('C:\\TestService.log', 'a') as f:
                f.write('test service running...\n')
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(TestService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(TestService)
