'''
Created on May 5, 2017

@author: Jicheng Wang 
'''
import re  
import urllib  
import urllib2 
import wx
from wx import TextCtrl

class webBot(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'web roboot',size =(400,400))
        panel=wx.Panel(self)
        self.text = wx.TextCtrl(panel, wx.ID_ANY, "Websize:", pos = (50,100), size =(300, 150), style = wx.TE_LEFT |wx.TE_MULTILINE |wx.TE_READONLY)
        self.button = wx.Button(panel, -1, "search", pos = (150,300), size = (100,50))
        self.Bind(wx.EVT_BUTTON, self.Search)
        
    def Search(self, event):
        def getHtml(url): 
            page = urllib.urlopen(url)  
            html = page.read()  
            return html

        def getImg(html):  
            reg = r'src="(.+?\.jpg)" pic_ext'  
            imgre = re.compile(reg)  
            imglist = imgre.findall(html)  
            x = 0  
            for imgurl in imglist:  
                urllib.urlretrieve(imgurl,'%s.jpg' %x)
                x = x + 1
                
        self.data = self.text.GetValue()
        html = getHtml(str(self.data)) 
        getImg(html)
    


if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=webBot(parent=None,id=-1)
    frame.Show()
    app.MainLoop()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Perfection: 1 try to add a folder automatic to save download file
#            2 try to download more type of file not only photo
