from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

pandas_word = pandas.read_csv("data/french_words.csv")

pandas_dict = pandas_word.to_dict(orient="records")
print(pandas_dict)

pandas_words = random.choices(pandas_dict)
print(pandas_words)
french_word = pandas_words[0]["French"]
english_word = pandas_words[0]["English"]

def flip_the_flashcards():
    # print(pandas_word[pandas_word.English == pandas_words])
    canvas.itemconfig(text1, text="English")
    canvas.itemconfig(text2, text=english_word)
    canvas.itemconfig(text1, fill="black")
    canvas.itemconfig(text2, fill="black")
    canvas.itemconfig(canvas_image, image=my_image)


window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR, height=500, width=500)
window.title("Flashcards")
window.after(3000, flip_the_flashcards)
canvas = Canvas(width=800, height=526)

x_button_image = PhotoImage(file="images/wrong.png")
right_button = PhotoImage(file="images/right.png")
my_image_back = PhotoImage(file="images/card_back.png")
my_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=my_image)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)

text1 = canvas.create_text(400, 150, text="Text", font=("Arial", 40, "italic"), fill="white")
text2 = canvas.create_text(400, 260, text="Word", font=("Arial", 40, "italic"), fill="white")
canvas.grid(column=0, row=0, columnspan=2)


my_image_back_button = Button(image=my_image_back)

button_x = Button(image=x_button_image, highlightthickness=0, command=flip_the_flashcards)
button_x.grid(column=0, row=1)

button_right = Button(image=right_button, highlightthickness=0, command=flip_the_flashcards)
button_right.grid(column=1, row=1)

canvas.itemconfig(canvas_image, image=my_image_back)
canvas.itemconfig(text1, text="French")
canvas.itemconfig(text2, text=french_word)

window.mainloop()
