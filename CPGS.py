from tkinter import *
from tkinter import messagebox
import random

class mainMenu(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Mystery beta")
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0,weight = 1)
        self.grid(sticky = W+E+N+S)
        self._optitle = LabelFrame(self, text = "Mystery Game V0.1",\
                                   width = 200, height = 200, relief = "sunken",\
                                   bd = 5, bg = "black")
        self._optitle.grid(sticky = N+S+E+W, pady= 10, columnspan = 3)
        self._newgame = Button(self, text = "New Game", command = self.newGame)
        self._newgame.grid(padx = 20, pady = 5, sticky = N+S+E+W,row = 1)
        self._continue = Button(self, text = "Continue", command = self.continuE)
        self._continue.grid(padx = 20, pady = 5, sticky = N+S+E+W, column = 2,\
                            row = 1)
        self._continue = Button(self, text = "Gallery", command = self.gallery)
        self._continue.grid(padx = 20, pady = 5, sticky = N+S+E+W, column = 1,\
                            row = 2)


    def newGame(self):
        if messagebox.askyesno(title = "Mystery Beta", \
                                 message = "Would you like to start a new game?"):
            self.master.destroy()
            game().mainloop()

    def continuE(self):
        self.master.destroy()
        continuePassword().mainloop()

    def gallery(self):
        messagebox.showinfo(title = "Mystery beta",\
                            message = "The gallery is sadly not complete yet. Sorry.")

class game(Frame):  
    def __init__(self,pid=0,itn=0):
        self.fonT = ("Arial","14")
        self.a = 0
        self.ts = 0
        self.itemnum = itn
        self.d1 = 0
        self.d2 = 0
        self.d3 = 0
        self.d4 = 0
        self.ui = 0
        self.sto = 0
        self.fd = 0
        self.ifd = 0
        self.cfd = 0
        self.tso = 0
        self.ctso = 0
        self.ropn = 0
        self.dialogue = "Press next to continue"
        self.pageList = ("1.txt","2.txt","3.txt","4.txt","5.txt","6.txt","7.txt",\
                         "8.txt", "9.txt","10.txt","11.txt","12.txt","13.txt",\
                         "14.txt","15.txt","16.txt","17.txt","18.txt","19.txt",\
                         "20.txt","21.txt","22.txt","23.txt","24.txt","25.txt",\
                         "26.txt","27.txt")
        self.pageID = pid
        self.f = open(file = self.pageList[self.pageID], mode = 'r')
        self.f.close()
        Frame.__init__(self)
        self.master.title("Mystery beta")
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0,weight = 1)
        self.grid(sticky = W+E+N+S, pady = 10)
        self._imgFrame = LabelFrame(self, relief = SUNKEN, bg = "black",\
                                    width = 400,height = 400)
        self._imgFrame.grid(sticky= N+S+E+W,padx=50,pady=10,column = 1,\
                            rowspan=2, columnspan=4, row = 0)
        self._inventory= LabelFrame(self,relief = FLAT, width = 200,\
                                    height = 400)
        self._inventory.grid(padx=50,pady=10,column = 5,\
                            rowspan=2, row =0)
        self._item1 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item1.grid()
        self._item2 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item2.grid(row = 1)
        self._item3 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item3.grid(row = 2)
        self._item4 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item4.grid(row = 3)
        self._item5 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item5.grid(row = 0,column = 1)
        self._item6 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item6.grid(row = 1,column = 1)
        self._item7 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item7.grid(row = 2,column = 1)
        self._item8 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item8.grid(row = 3,column = 1)
        self._diaBox = LabelFrame(self,width = 900, height = 100)
        self._diaBox.grid_propagate(0)
        self._diaBox.grid(row =2,column=0, columnspan=6,pady=10)
        self._dialogue = Label(self._diaBox, text = self.dialogue, font = self.fonT,\
                               padx = 10,pady =30)
        self._dialogue.grid()
        self._saveB = Button(self, text = "Save", command = self.save)
        self._saveB.grid(row = 3)
        self._opBox = LabelFrame(self)
        self._opBox.grid(row = 3, column = 1, columnspan = 4,pady = 10)
        self._galB = Button(self._opBox, text = "Gallery", command = self.gallery)
        self._galB.grid(padx=40, pady=45)
        self._op2 = Label(self._opBox, text= "2")
        self._op2.grid(padx=40,pady=45,row=0,column=1)
        self._op3 = Label(self._opBox, text= "3")
        self._op3.grid(padx=40,pady=45,row=0,column=2)
        self._op4B = Button(self._opBox, text = "Next", command = self.nextLine)
        self._op4B.grid(padx=40,pady=45,row = 0, column = 3)
        self._exitB = Button(self, text = "Main", command=self.exit)
        self._exitB.grid(row = 3, column =5)

    def updateOPBox(self):
        self._opBox.destroy()
        self._opBox = LabelFrame(self)
        self._opBox.grid(row = 3, column = 1, columnspan = 4,pady = 10)
        if self.sto > 0:
            self._op1B = Button(self._opBox, text = "1", command = self.op1)
            self._op1B.grid(padx=40, pady=45)
        else:
            self._galB = Button(self._opBox, text = "Gallery", command = self.gallery)
            self._galB.grid(padx=40, pady=45)
        if self.sto > 1:
            self._op2B = Button(self._opBox, text = "2",command = self.op2)
            self._op2B.grid(padx=40,pady=45,row=0,column=1)
        else:
            self._op2 = Label(self._opBox, text= "2")
            self._op2.grid(padx=40,pady=45,row=0,column=1)
        if self.sto > 2:
            self._op3B = Button(self._opBox, text = "3",command = self.op3)
            self._op3B.grid(padx=40,pady=45,row=0,column=2)
        else:
            self._op3 = Label(self._opBox, text= "3")
            self._op3.grid(padx=40,pady=45,row=0,column=2)
        if self.sto > 0:
            self._op4 = Label(self._opBox, text = "Next")
            self._op4.grid(padx=40,pady=45,row = 0, column = 3)
        else:
            self._op4B = Button(self._opBox, text = "Next", command = self.nextLine)
            self._op4B.grid(padx=40,pady=45,row = 0, column = 3)

    def updateInventory(self):
        self._inventory= LabelFrame(self,relief = FLAT, width = 200,\
                                    height = 400)
        self._inventory.grid(padx=50,pady=10,column = 5,\
                            rowspan=2, row =0)
        self._item1 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item1.grid()
        self._item1.grid_propagate(0)
        self.item1B = Button(self._item1, text = "Recorder", \
                             command = self.I1)
        self.item1B.grid(padx=20,pady=35)
        self._item2 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item2.grid(row = 1)
        self._item2.grid_propagate(0)
        if self.itemnum > 1:
            self.item2B = Button(self._item2, text = "Autopsy", \
                                 command = self.I2)
            self.item2B.grid(padx=20,pady=35)
        self._item3 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item3.grid(row = 2)
        self._item3.grid_propagate(0)
        if self.itemnum > 2:
            self.item3B = Button(self._item3, text = "Tea Set", \
                                 command = self.I3)
            self.item3B.grid(padx=22,pady=35)
        self._item4 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item4.grid(row = 3)
        self._item4.grid_propagate(0)
        if self.itemnum > 3:
            self.item4B = Button(self._item4, text = "Will", \
                                 command = self.I4)
            self.item4B.grid(padx=35,pady=35)
        self._item5 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item5.grid(row = 0,column = 1)
        self._item5.grid_propagate(0)
        if self.itemnum > 4:
            self.item5B = Button(self._item5, text = "Schedule", \
                                 command = self.I5)
            self.item5B.grid(padx=20,pady=35)
        self._item6 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item6.grid(row = 1,column = 1)
        self._item7 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item7.grid(row = 2,column = 1)
        self._item8 = LabelFrame(self._inventory, relief = SUNKEN, \
                                 width =100, height = 100)
        self._item8.grid(row = 3,column = 1)

    def updateDialogue(self):
        self._dialogue.destroy()
        self._dialogue = Label(self._diaBox, text = self.dialogue, font = self.fonT,\
                               padx = 10,pady = 30)
        self._dialogue.grid()

    def exit(self):
        self.master.destroy()
        mainMenu().mainloop()

    def nextLine(self):
        of=0
        self.f = open(file = self.pageList[self.pageID], mode = 'r')
        t = self.f.read().splitlines()
        if self.a == len(t):
            self.f.close()
            self.pageID+=1
            self.f = open(file = self.pageList[self.pageID], mode = 'r')
            t = self.f.read().splitlines()
            self.a = 0
        v = t[self.a]    
        diaLine = t[self.a+1]  
        varIndex = v.replace('\n','')
        self.varInCheck = varIndex
        self.ui = int(varIndex[0])
        self.sto = int(varIndex[1])
        self.ifd = int(varIndex[3])
        self.tso = int(varIndex[4])
        self.cfd = int(varIndex[5])
        self.ctso = int(varIndex[6])
        self.ropn = int(varIndex[7])
        self.d1 = int(varIndex[8])
        self.d2 = int(varIndex[9])
        self.d3 = int(varIndex[10])
        self.d4 = int(varIndex[11])
        if self.ui > 0:
            self.itemnum = self.ui
            self.updateInventory()
        if self.sto > 0:
            self.updateOPBox()
        if self.ifd > 0:
            self.fd+=1
        if self.cfd >0:
            if self.fd >0 and self.fd<3:
                self.pageID = 4
                self.f.close()
                self.f = open(file = self.pageList[self.pageID], mode = 'r')
                of=1
            else:
                self.pageID = 8
                self.f.close()
                self.f = open(file = self.pageList[self.pageID], mode = 'r')
                of=1
        if self.tso >0:
            self.ts+=1
        if self.ctso == 1 and self.ts > 0:
            self.pageID = 25
            self.f.close()
            self.f = open(file = self.pageList[self.pageID], mode = 'r')
            of=1
        if self.ropn >0:
            self.updateOPBox()
        if self.d1 == 1:
            self.f.close()
            self.pageID-=1
            self.f = open(self.pageList[self.pageID], 'r')
            of=1
        elif self.d1 == 2:
            self.pageID = 14
            self.f.close()
            self.f = open(file = self.pageList[self.pageID], mode = 'r')
            of=1
        elif self.d1 == 3:
            self.f.close()
            self.pageID-=3
            self.f = open(self.pageList[self.pageID], 'r')
            of=1
        if self.d2 == 1:
            self.f.close()
            self.pageID-=1
            self.f = open(self.pageList[self.pageID], 'r')
            of=1
        elif self.d2 == 2:
            self.pageID = 18
            self.f.close()
            self.f = open(file = self.pageList[self.pageID], mode = 'r')
            of=1
        if self.d3 == 1:
            self.f.close()
            self.pageID-=1
            self.f = open(self.pageList[self.pageID], 'r')
            of=1
        elif self.d3 == 2:
            self.f.close()
            self.pageID-=2
            self.f = open(self.pageList[self.pageID], 'r')
            of=1
        elif self.d3 == 3:
            self.pageID = 22
            self.f.close()
            self.f = open(file = self.pageList[self.pageID], mode = 'r')
            of=1
        if self.d4 == 1:
            self.pageID = 26
            self.f.close()
            self.f = open(file = self.pageList[self.pageID], mode = 'r')
            of=1
        elif self.d4 == 2:
            self.f.close()
            self.pageID-=2
            self.f = open(self.pageList[self.pageID], 'r')
            of=1
        if of >0:
            self.a = 0
        else:
            self.a+=2
        self.dialogue = diaLine
        self.updateDialogue()
            
    def gallery(self):
        messagebox.showinfo(title = "Mystery beta",\
                            message = "The gallery is sadly not complete yet. Sorry.")


    def I1(self):
        I = open("I1.txt", 'r')
        messagebox.showinfo(title = "Tape Recorder",\
                            message = I.read())

    def I2(self):
        I = open("I2.txt", 'r')
        messagebox.showinfo(title = "Preliminary Autopsy Report",\
                            message = I.read())

    def I3(self):
        I = open("I3.txt", 'r')
        messagebox.showinfo(title = "Tea Set",\
                            message = I.read())

    def I4(self):
        I = open("I4.txt", 'r')
        messagebox.showinfo(title = "Will",\
                            message = I.read())

    def I5(self):
        I = open("I5.txt", 'r')
        messagebox.showinfo(title = "Tea Schedule",\
                            message = I.read())

    def op1(self):
        self.f.close()
        self.pageID+=1
        self.f = open(self.pageList[self.pageID], 'r')
        self.a=0
        self.nextLine()
        
    def op2(self):
        self.f.close()
        self.pageID+=2
        self.f = open(self.pageList[self.pageID], 'r')
        self.a=0
        self.nextLine()

    def op3(self):
        self.f.close()
        self.pageID+=3
        self.f = open(self.pageList[self.pageID], 'r')
        self.a = 0
        self.nextLine()

    def save(self):
        p = str(self.pageID)
        if len(p) == 1:
            p = "0" + p
        saveCode = str(random.randint(0,10))+p[0]+str(random.randint(0,10))+\
                   str(random.randint(0,10))+p[1]+str(random.randint(0,10))+\
                   str(self.itemnum)
        messagebox.showinfo(title = "Mystery beta",\
                            message = "Your Save Code is:\n"+saveCode)
        

class continuePassword(Frame):
    def __init__(self):
        num = (0,1,2,3,4,5,6,7,8,9)
        Frame.__init__(self)
        self.master.title("Mystery beta")
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0,weight = 1)
        self.grid(sticky = W+E+N+S)
        self._Label = Label(self,text = "CONTINUE\nINPUT PASSWORD")
        self._Label.grid(padx =10, pady = 20,row = 0, columnspan = 7)
        self._list1 = Listbox(self,height = 1,width = 3)
        for n in num:
            self._list1.insert(END,n)
        self._list1.grid(padx=20,pady=5,row = 1)
        self._list2 = Listbox(self,height = 1,width = 3)
        for n in num:
            self._list2.insert(END,n)
        self._list2.grid(padx=20,pady=5,row = 1,column = 1)
        self._list3 = Listbox(self,height = 1,width = 3)
        for n in num:
            self._list3.insert(END,n)
        self._list3.grid(padx=20,pady=5,row = 1,column = 2)
        self._list4 = Listbox(self,height = 1,width = 3)
        for n in num:
            self._list4.insert(END,n)
        self._list4.grid(padx=20,pady=5,row = 1,column = 3)
        self._list5 = Listbox(self,height = 1,width = 3)
        for n in num:
            self._list5.insert(END,n)
        self._list5.grid(padx=20,pady=5,row = 1,column = 4)
        self._list6 = Listbox(self,height = 1,width = 3)
        for n in num:
            self._list6.insert(END,n)
        self._list6.grid(padx=20,pady=5,row = 1,column = 5)
        self._list7 = Listbox(self,height = 1,width = 3)
        for n in num:
            self._list7.insert(END,n)
        self._list7.grid(padx=20,pady=5,row = 1,column = 6)
        self._back = Button(self, text = "Back", command = self.back)
        self._back.grid(row =2,pady =20)
        self._continue = Button(self, text = "Continue",\
                                command = self.contiuE)
        self._continue.grid(row =2, column = 6,pady =20)

    def back(self):
        self.destroy()
        mainMenu().mainloop()

    def contiuE(self):
        fid = int(str(self._list2.get(ACTIVE))+str(self._list5.get(ACTIVE)))
        inum = int(self._list7.get(ACTIVE))
        self.master.destroy()
        g = game(fid,inum)
        g.updateInventory()
        
mainMenu().mainloop()
