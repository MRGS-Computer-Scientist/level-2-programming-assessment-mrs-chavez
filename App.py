from tkinter import *
from app_settings import *
from os import *
from tkinter import messagebox 
from tkinter import simpledialog

from PIL import ImageTk, Image


##### FONTS #######
# Available TKinter fonts: https://stackoverflow.com/a/64301819

title_font = ("Verdana", 30, "bold")

class App():

    current_frame = "Home"
    list_box = None

    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title(app_title)

########## TOP FRAME #############

        self.top_frame = Frame(background='red', width=w_width, height=100)
        self.top_frame.pack()


########## END OF TOP #############


########## MAIN FRAME #############

        image = Image.open("imgs/house.png")
        photo = ImageTk.PhotoImage(image.resize((196, 196)))

        self.home_frame = Frame(background=bg_color, width=w_width, height=(w_height-200))
        self.home_frame.pack()

        self.title_label = Label(self.home_frame, text=app_title, font=title_font)
        self.title_label.pack()

        self.quiz_frame = Frame(background=bg_color, width=w_width, height=(w_height-200))

        self.quiz_label = Label(self.quiz_frame, text="Quiz", font=title_font)
        self.quiz_label.pack()

######## LIST FRAME ############

        self.list_frame = Frame(background=bg_color, width=w_width, height=(w_height-200))

        self.list_label = Label(self.list_frame, text="List", font=title_font)
        self.list_label.pack()

        self.list_box = Listbox(self.list_frame)
        self.list_box.pack()


        self.new_item = Button(self.list_frame, text="Add new item", command=self.add_new_item)
        self.new_item.pack()
        

######## END OF LIST FRAME ############

        bg_image = Label(self.home_frame, image=photo)
        bg_image.pack()


########## END OF MAIN #############

########## BOTTOM FRAME #############

        self.bottom_frame = Frame(background='blue', width=w_width, height=100)
        self.bottom_frame.pack(side='bottom')

        self.home_button = Button(self.bottom_frame, text="Home", height=2, width=5, bg='green', command=lambda: self.go_to_frame("Home"))
        self.home_button.pack(side='left')

        self.quiz_button = Button(self.bottom_frame, text="Quiz", height=2, width=5, bg='green', command=lambda: self.go_to_frame("Quiz"))
        self.quiz_button.pack(side='left')

        self.list_button = Button(self.bottom_frame, text="LIst", height=2, width=5, bg='green', command= lambda: self.go_to_frame("List"))
        self.list_button.pack(side='left')

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

    def add_new_item(self):
        user_input = simpledialog.askstring(title="Adding new item",
                                  prompt="What is your new item name:")
        self.list_box.insert(0, user_input)

    def go_to_frame(self, next_frame):

        if self.current_frame == "Home":
                self.home_frame.pack_forget()
        elif self.current_frame == "Quiz":
                self.quiz_frame.pack_forget()
        elif self.current_frame == "List":
                self.list_frame.pack_forget()

        if next_frame == "Quiz":
                self.quiz_frame.pack()
                self.current_frame = "Quiz"
        elif next_frame == "List":
                self.list_frame.pack()
                self.current_frame = "List"
        elif next_frame == "Home":
                self.home_frame.pack()
                self.current_frame = "Home"

        
