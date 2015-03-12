#!/usr/bin/env python3
import os 
from Tkinter import *
from ttk import *
import tkFileDialog

python = 'c:\Python27-x64\python'


class ScrolledText(Frame):

    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                 
        self.makewidgets()
        self.settext(text, file)

    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)               
        text.config(yscrollcommand=sbar.set)           
        sbar.pack(side=RIGHT, fill=Y)                 
        text.pack(side=LEFT, expand=YES, fill=BOTH)  
        self.text = text

    def settext(self, text='', file=None):
        if file: 
            text = open(file, 'r').read()
        self.text.delete('1.0', END)                 
        self.text.insert('1.0', text)               
        self.text.mark_set(INSERT, '1.0')          
        self.text.focus()                           

    def gettext(self):                             
        return self.text.get('1.0', END+'-1c')  


class Application (Frame):
        
    rootdir = '/Users/MikeO/Desktop/Hasher/' # Dir path
    lindir = '/home/beast/hash' # Linux dir 
    windir = 'C:\\Users\\timbooks\\Desktop\\HasherTestArea' # Dir path on a windows machine
       
    hashFileName = 'HashedStuffHERE'
    directoryToHash = windir
    st=''
    
    found = False
    def __init__(self, master):
        # Initialize the Frame
        Frame.__init__(self,master)
        self.initUI()
        
#       self.grid()


    def initUI(self):
      
        self.master.title("DFC Tool")
        self.master.geometry("500x400")
        
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.note = Notebook(self.master)
        
        self.tab1 = Frame(self.note)
        self.tab2 = Frame(self.note)
        self.tab3 = Frame(self.note)
        self.tab4 = Frame(self.note)

        self.note.add(self.tab1, text = "Hasher")
        self.note.add(self.tab2, text = "TcpdStat")
        self.note.add(self.tab3, text = "Tab Three")
        self.note.add(self.tab4, text = "Results Text")
        
        self.create_tab1()
        self.create_tab2()
        self.create_tab3()
        self.create_tab4()
        
        
        self.note.pack()


    def create_tab1(self):
        # Hasher
        self.title = Label(self.tab1, text= "WELCOME TO THE DFC")

        self.title.grid(row=0, column=0)
        self.thelabel = Label(self.tab1, text = "Press to Hash Folder")
        self.thelabel.grid(row=1, column=0)  
        self.submit_button=Button(self.tab1, command = lambda: self.change_bool(), text = "Hash")
        self.submit_button.grid(row=2, column=0)
        self.submit_button3=Button(self.tab1, command = lambda: self.get_directory(), text = "Get Directory to hash")
        self.submit_button3.grid(row=3, column=0)
        self.DirectoryLabel = Label(self.tab1, text = "The Directory which will be hashed: ")
        self.DirectoryLabel.grid(row=4, column=0, columnspan = 2) 
        self.DirectoryLabel = Label(self.tab1, text = self.directoryToHash)
        self.DirectoryLabel.grid(row=5, column=0, columnspan=2) 


    def create_tab2(self):
        # TcpdStat
        self.submit_button2=Button(self.tab2, command = lambda: self.get_file(), text = "Get File")
        self.submit_button2.grid(row=12, column=0)
        self.instruction = Label(self.tab2, text= "Enter file location")
        self.instruction.grid(row= 11, column = 1, columnspan = 2, sticky = W)

        self.password = Entry(self.tab2)
        self.password.grid(row =12, column = 1, sticky = W)


        self.submit = Button(self.tab2, text="Submit", command = self.reveal)
        self.submit.grid(row= 14, column = 0, stick = W)

        self.text = Text(self.tab2, width = 35, height = 5, wrap = WORD)
        self.text.grid(row =15, column =0, columnspan= 2, sticky = W)



        
    def create_tab3(self):
        # fill tab3
        self.exitButton = Button(self.tab3, text='Exit', command=self.onExit).pack(padx=100, pady=100)

        
    def create_tab4(self):
        # fill tab4
        self.st = ScrolledText(parent=self.tab4,text='')


    def change_bool(self):
        self.found = True
        self.import_file()


    def get_file(self):
        self.found = True
        self.f = (tkFileDialog.askopenfilename(parent=self.master))
        print self.f
        self.password.delete(0, END)
        self.password.insert(0, self.f)
        
        
    def get_directory(self):
        self.found = True
        self.d = (tkFileDialog.askdirectory(parent=self.master))
        print self.d
        self.directoryToHash = self.d
        self.DirectoryLabel = Label(self.tab1, text = self.directoryToHash)
        self.DirectoryLabel.grid(row=5, column=0, columnspan=2) 


    def import_file(self):
        print self.hashFileName
        print self.directoryToHash
        if (self.found):
            os.system('hash.py "' + self.hashFileName + '" "' + self.directoryToHash +'"')    


    def reveal(self):
        content = self.password.get()
        tcpdstat= "tcpdstat -c 100 "+ content
        f = os.popen(tcpdstat)
        message = f.read()
        #message = 'This is a MEssage from TCPDStat'
        print message
        print tcpdstat
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)
        self.st.settext(text=message)

        
    def onExit(self):
        self.master.destroy()


def main():
    
    root = Tk()
       
    app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
