from tkinter import *

clicked = 0
def click():
    global clicked
    clicked += 1
    print(f"You have clicked this button {clicked} times.")


window = Tk()

window.title("Hello I am Neelmani")
window.geometry("500x200")
window.config(background="black")

Label = Label(window,
              text="Hello everyone, click the button to see a message",
              font=("Arial", 14,),
              fg="#00ff00",
              bg="black")
Label.pack()

button = Button(window,
                text="Click here!",
                command=click,
                font=('Comic Sans', 20,'underline'),
                fg="#00ff00", bg="black",
                activeforeground="#00ff00",
                activebackground="black",
                state=ACTIVE)
button.pack()


window.mainloop()