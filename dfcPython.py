#!/usr/bin/env python3
import os 
from Tkinter import *
from ttk import *
import tkFileDialog

python = 'c:\Python27-x64\python' # for windows
#python = 'python' # for linux

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
       
    hashFileName = 'HashedStuff'
    directoryToHash = lindir
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
        self.note.add(self.tab3, text = "TCPtrace")
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
        
        self.spacer = Label(self.tab1, text = " ")
        self.spacer.grid(row=3, column=0, columnspan = 3)
        
        self.submit_button3=Button(self.tab1, command = lambda: self.get_directory(), text = "Get Directory to hash")
        self.submit_button3.grid(row=4, column=0, sticky = W)
        
        self.DirectoryLabel = Label(self.tab1, text = "The Directory which will be hashed: ")
        self.DirectoryLabel.grid(row=5, column=0, columnspan = 2, sticky = W)
        
        self.dirValue = StringVar()
        self.DirectoryEntry = Entry(self.tab1, textvariable=self.dirValue, width=50)
        self.DirectoryEntry.grid(row=6, column=0, columnspan = 3, sticky = W)
        self.dirValue.set(self.directoryToHash)
        
        self.spacer = Label(self.tab1, text = " ")
        self.spacer.grid(row=7, column=0, columnspan = 2)
        
        self.DirectoryLabel2 = Label(self.tab1, text = "The name of the hash file: ")
        self.DirectoryLabel2.grid(row=8, column=0, columnspan = 2, sticky = W)
        self.hashName = StringVar()
        self.hashFileNameEntry = Entry(self.tab1, textvariable=self.hashName, width=50)
        self.hashName.set(self.hashFileName)
        self.hashFileNameEntry.grid(row =9, column = 0, columnspan = 3, sticky = W)


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

        
    def create_tab3(self):
        #TcpTrace
        self.submit_button3=Button(self.tab3, command = lambda: self.get_tcptraceFile(), text = "Get File")
        self.submit_button3.grid(row=12, column=0)

        self.instruction = Label(self.tab3, text= "Enter file location")
        self.instruction.grid(row= 11, column = 1, columnspan = 2, sticky = W)

        self.password2 = Entry(self.tab3)
        self.password2.grid(row =12, column = 1, sticky = W)

        self.submit2 = Button(self.tab3, text="Submit", command = self.tcp_trace)
        self.submit2.grid(row= 14, column = 0, stick = W)

        self.labelTCP = Label(self.tab3, text= "")
        self.labelTCP.grid(row= 14, column = 1, columnspan = 2, sticky = W)

    
        
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


    def get_tcptraceFile(self):
        self.found = True
        self.f = (tkFileDialog.askopenfilename(parent=self.master))
        print self.f
        self.password2.delete(0, END)
        self.password2.insert(0, self.f)
        
        
    def get_directory(self):
        self.found = True
        self.d = (tkFileDialog.askdirectory(parent=self.master))
        print self.d
        self.directoryToHash = self.d
        self.DirectoryEntry.delete(0, END)
        self.DirectoryEntry.insert(0, self.directoryToHash)


    def import_file(self):
        print self.hashFileName
        print self.directoryToHash
        self.hashFileName = self.hashFileNameEntry.get()
        if (self.found):
            os.system(python + ' hash.py "' + self.hashFileName + '" "' + self.directoryToHash +'"') 
        self.st.settext(self.hashFileName + '.csv')


    def reveal(self):
        content = self.password.get()
        tcpdstat= "tcpdstat -c 100 "+ content
        f = os.popen(tcpdstat)
        message = f.read()
        #message = 'This is a MEssage from TCPDStat'
        print message
        print tcpdstat
        self.st.settext(text=message)


    def tcp_trace(self):
        content = self.password2.get()
        print "this is content" + content
        tcpTrace = "tcptrace -n -r " + content
        f1 = os.popen(tcpTrace)
        message = f1.read()
        print message
        print tcpTrace
        self.st.settext(text=message)




        
    def onExit(self):
        self.master.destroy()


def main():
    
    root = Tk()
       
    app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
