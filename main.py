from tkinter import *
root = Tk()

amsterdam_button = Button(master=root, text="Amsterdam", command=lambda: set_locatie_scherm("Amsterdam"))
rotterdam_button = Button(master=root, text="Rotterdam", command=lambda: set_locatie_scherm("Rotterdam"))
utrecht_button = Button(master=root, text="Utrecht", command=lambda: set_locatie_scherm("Utrecht"))

# Position the buttons in the middle of the window
amsterdam_button.pack()
rotterdam_button.pack()
utrecht_button.pack()
def set_locatie_scherm(city):
    global locatie_scherm
    locatie_scherm = city
    root.destroy()
    create_fullscreen_window()


def create_fullscreen_window():
    fullscreen_window = Tk()
    fullscreen_window.attributes("-fullscreen", True)
    fullscreen_window.mainloop()