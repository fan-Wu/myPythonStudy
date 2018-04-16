import wx

class MyFrame(wx.Frame):
    BTN_TEXT=(7,8,9,'/',4,5,6,'*',1,2,3,'-','.',0,'=','+')
    BTN_ID={}
    NUMSTR=''
    OPE_1=[]
    NUM=[]
    RESULT=0.0
    
    def __init__(self):
        wx.Frame.__init__(self,None,title="Xini's Calculator",
                          style=wx.DEFAULT_FRAME_STYLE^(
                          wx.RESIZE_BORDER|wx.MINIMIZE_BOX|
                          wx.MAXIMIZE_BOX))
        wx.Frame.SetBackgroundColour(self,(233,230,230))

        btngrid=wx.GridSizer(rows=4,cols=4,hgap=10,    #build a grid
                             vgap=10)        
        for t in self.BTN_TEXT:  #create buttons ,add to grid, bind them
            self.b=wx.Button(self,label=str(t),size=(50,50))
            btngrid.Add(self.b,0)
            self.Bind(wx.EVT_BUTTON,self.onButtonEvt,self.b)
            self.BTN_ID[self.b.GetId()]=t
            
        self.textInput=wx.TextCtrl(self,
                                   size=(230,30),
                                   style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.textResult=wx.TextCtrl(self,
                                    size=(230,40),
                                    style=wx.TE_MULTILINE|wx.TE_READONLY)

        box=wx.BoxSizer(wx.VERTICAL)    #create sizer ,add textctrl and grid
        box.Add(self.textResult,0,wx.ALL,10)
        box.Add(self.textInput,0,wx.ALL,10)
        box.Add(btngrid,0,wx.ALL,10)
        self.SetSizer(box)
        self.Fit()

            
    def createTextCtr(self):
        pass
    
    def clr(self):         #initialize 
        self.NUMSTR=''
        self.OPE_1=[]
        self.NUM=[]
        self.RESULT=0.0

    def oper(self,a,b,c):    #opearation
        D={'+':b+c,'-':b-c,'*':b*c,'/':b/c}
        return D[a]
    
    
    def calcul(self):       #calculate the result
        for i in range(len(self.NUM)-1):
            if i ==0:
                self.RESULT=self.oper(self.OPE_1[0],self.NUM[0],self.NUM[1])
            else:
                self.RESULT=self.oper(self.OPE_1[i],self.RESULT,self.NUM[i+1])
            
    
    def getV(self):     # get values from inputs and deal with it
        #a=self.BTN_ID[event.GetId()]
        if isinstance(a,int):
            self.NUMSTR=self.NUMSTR+str(a)
        elif a=='.':
            if self.NUMSTR.find('.')==-1:
                self.NUMSTR=self.NUMSTR+a
        elif a=='=':
            self.NUM.append(float(self.NUMSTR))
            if len(self.NUM)>1:
                self.calcul()
                self.textResult.SetValue(str(self.RESULT))
                self.clr()
            else:
                self.clr()
            
        else :
           # if len(self.NUMSTR)>0:
            self.NUM.append(float(self.NUMSTR))
            self.OPE=self.OPE_1.append(str(a))
            self.NUMSTR=''
            #else:
            #    if len(self.NUM)>0:
             #       self.OPE[len[self.OPE]]=a
            
                        

    
    def onButtonEvt(self,event):
        global a
        a=self.BTN_ID[event.GetId()]
        self.getV()
        self.textInput.AppendText(str(a))
        
            
            
        #self.textInput.AppendText(str(self.BTN_ID[event.GetId()]))


      #  for i in self.BTN_ID.keys():
       #     self.textInput.AppendText(str(i))
    

app=wx.App()
f=MyFrame()
f.Show()
app.MainLoop()
