from tkinter import *
from app_settings import *
from os import *
from tkinter import messagebox 

from PIL import ImageTk, Image


##### FONTS #######
# Available TKinter fonts: https://stackoverflow.com/a/64301819

title_font = ("Verdana", 30, "bold")

class App():

    
    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title(app_title)

########## TOP FRAME #############

        self.top_frame = Frame(background='red', width=w_width, height=100)
        self.top_frame.pack()

        title_label = Label(text=app_title, font=title_font)
        title_label.pack()


########## END OF TOP #############


########## MAIN FRAME #############

        image = Image.open("imgs/house.png")
        photo = ImageTk.PhotoImage(image.resize((196, 196)))

        self.main_frame = Frame(background=bg_color, width=w_width, height=(w_height-200))
        self.main_frame.pack()

        bg_image = Label(image=photo)
        bg_image.pack()


########## END OF MAIN #############

########## BOTTOM FRAME #############

        self.bottom_frame = Frame(background='blue', width=w_width, height=100)
        self.bottom_frame.pack(side='bottom')

        self.home_button = Button(self.bottom_frame, text="Home", height=2, width=5, bg='green')
        self.home_button.pack(side='left')

        self.exit_button = Button(self.bottom_frame, text="Exit", height=2, width=5, bg='green', command= self.exit)
        self.exit_button.pack(side='right')

########## END OF BOTTOM #############


########## OTHER APP SETUP #############

        # Set relative path to the project folder
        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'images/')

        #print("The path is", self.filename)


        self.window.mainloop()


    # Asks confirmation from user before exiting/destroying the app
    def exit(self):
        confirm_exit = messagebox.askquestion("askquestion", "Are you sure?")
        print(confirm_exit)
        if confirm_exit == 'yes':
            self.window.destroy()
        else:
            print("Continue")
            pass