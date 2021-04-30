from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 276, image=card_front)
canvas.create_text(400, 164, text="Title", font=("courier", 25, 'italic'))
canvas.create_text(400, 250, text="Word", font=("courier", 40, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, borderwidth=0)
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, borderwidth=0)
tick_button.grid(row=1, column=1)


window.mainloop()