from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
text2 = ""

pandas_word = pandas.read_csv("data/french_words.csv")

def french_word():
    random_word = random.choice(pandas_word["French"])
    text2 = random_word



window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR, height=500, width=500)
window.title("Flashcards")

canvas = Canvas(width=800, height=526)
my_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=my_image)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
text1 = canvas.create_text(400, 150, text="Text", font=("Arial", 40, "italic"))
text2 = canvas.create_text(400, 260, text=f"{text2}", font=("Arial", 40, "italic"))
canvas.grid(column=0, row=0, columnspan=2)


x_button_image = PhotoImage(file="images/wrong.png")
right_button = PhotoImage(file="images/right.png")
my_image_back = PhotoImage(file="images/card_back.png")


my_image_back_button = Button(image=my_image_back)

button_x = Button(image=x_button_image, highlightthickness=0, command=french_word)
button_x.grid(column=0, row=1)

button_right = Button(image=right_button, highlightthickness=0, command=french_word)
button_right.grid(column=1, row=1)



window.mainloop()