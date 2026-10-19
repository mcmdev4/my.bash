def gapp():
    from tkinter import filedialog, Tk, Text, Menu, END

    def saveFile():
        file = filedialog.asksaveasfile(defaultextension=".txt",
        filetypes=[
            ("Text file",".txt"),
            ("JSON file",".json"),
            ("All Files",".*")
        ])

        if file:
            content = str(text.get(1.0,END))
            file.write(content)
            file.close()
    
    def openFile():
        path = filedialog.askopenfilename(defaultextension=".txt",
        filetypes=[
            ("Text files",".txt"),
            ("JSON files",".json"),
            ("All files",".*")
        ])
        
        if path:
            with open(path, 'r') as c:
                content = c.read()
            text.delete(1.0,END)
            text.insert(1.0,content)

    window = Tk()
    window.title("Compact Notepad")
    
    menubar = Menu(window)
    window.config(menu=menubar)

    filemenu = Menu(menubar)
    menubar.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Save as",command=saveFile)
    filemenu.add_command(label="Open",command=openFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=window.destroy)

    text = Text(window)

    text.pack()
    window.mainloop()

