

"""
    Program tasked to create a basic HTML
    web page. Using Tkinter GUI and Python
    script that will automatically create
    the html file needed.
"""


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #label
        self.lbl_customtxt = tk.Label(self.master,text='Enter custom text or click the Default HTML page button.')
        self.lbl_customtxt.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)


        #textbox
        self.txt_customtxt = tk.Entry(self.master,text='')
        self.txt_customtxt.grid(row=1,column=0,rowspan=1,columnspan=3,padx=(30,40),pady=(0,0),sticky=N+E+W)

        
        # button for HTML page
        self.btn_html = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn_html.grid(row=2,column=1,padx=(10,10),pady=(10,10), sticky=W)
        # button for custom text
        self.btn_txt = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn_txt.grid(row=2,column=2,padx=(10,10),pady=(10,10), sticky=E)
        

    # creates default HTML page
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    # creates HTML page with custom text
    def customHTML(self):
        htmlText = self.txt_customtxt.get() # gets input from textbox entry
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
