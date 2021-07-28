import win32com
from win32com.client import Dispatch 
from win32gui import GetClassName
import win32con

class Serenova:
    PhonePanel = None
    def __init__(self) -> None:
        if self.findPhonePanel():
            self.isActive()
        pass

    def findPhonePanel(self):
        ShellWindowsCLSID = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'
        ShellWindows = Dispatch ( ShellWindowsCLSID )
        for sw in ShellWindows :
            if GetClassName ( sw . HWND ) == 'IEFrame' :
                # print(sw.Document.body.outerHTML) #esta linea get el dom 
                if "/mason/agents/bakelite/bakelite.html" in sw.LocationURL or "/mason/admin/bakelite/bakelite.html" in sw.LocationURL:
                    print(sw.LocationURL) 
                    self.PhonePannel = sw
                    return True
        return False

    def isActive(self) ->bool:
        # elements = self.PhonePannel.Document.body.outerHTML
        elements = self.PhonePannel.Document.getElementsByTagName('tag-type-display')
        for element in elements:
            print(element)
        # print(elements)
        return True