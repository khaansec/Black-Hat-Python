import os 
import shutil
import subprocess
import sys
import winreg

import win32event
import win32service
import win32serviceutil

SRCDIR = 'c:\\users\\tim\\work'
TGTDIR = 'c:\\windows\\temp'

class BHServerSvc(win32serviceutil.ServiceFramework):
    _svc_name = "BlackHatService"
    _svc_display_name = "Black Hat Service"
    _svc_description = "Executes VBS scripts at regular intervals"

def __init__(self,args):
    self.vbs = os.path.join(TGTDIR, 'bhservice_task.vbs')
    self.timeout = 1000 * 60

    win32serviceutil.ServiceFramework.__init__(self, args)
    self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

def SvcStop(self):
    self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
    win32event.SetEvent(self.hWaitStop)

def SvcDoRun(self):
    self.ReportServiceStatus(win32service.SERVICE_RUNNING)
    self.main()

def main(self):
    while True:
        ret_code = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
        if ret_code == win32event.WAIT_OBJECT_0:servicemanager.LogInfoMsg("Service is stopping")
        break
    src = os.path.join(SRCDIR, 'bhservice_task.vbs')
    shutil.copy(src, self.vbs)
    subprocess.call("cscript.exe %s" % self.vbs, shell=False)
    os.unlink(self.vbs)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(BHServerSvc)
        servicemanager.StartSrviceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(BHServerSvc)
