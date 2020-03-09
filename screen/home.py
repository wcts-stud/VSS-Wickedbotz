

from Tkinter import Tk, Label, Button

'''
    % code %
    
'''

buttonCompetition = "Competicao"
buttonCalibrate = "Calibrar"




class HomePage:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text=buttonCalibrate, command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text=buttonCompetition, command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")



rootTk = Tk()
my_gui = HomePage(rootTk)
rootTk.mainloop()


'''
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("Tkinter window")



# show window
root.mainloop()
'''