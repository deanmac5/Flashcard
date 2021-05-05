from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/french_words.csv")
word_dict = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(word_dict)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    return


window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=20, bg=BACKGROUND_COLOR)


canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 276, image=card_front)
card_title = canvas.create_text(400, 150, font=("Arial", 25, 'italic'), fill="black")
card_word = canvas.create_text(400, 263, font=("Arial", 40, 'bold'), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, command=next_card)
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, borderwidth=0, command=next_card)
tick_button.grid(row=1, column=1)

next_card()

window.mainloop()
