from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
flash_word = {}
current_card = {}
#-------------------------READING FROM CSV----------------------------

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    flash_word = original_data.to_dict(orient="records")
else:
    flash_word = data.to_dict(orient="records")

#picking random french word->
def gen_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(flash_word)
    canvas.itemconfig(canvas_img,image = front)
    canvas.itemconfig(lang_text,fill = "black" , text = "French")
    canvas.itemconfig(word_text,fill = "black" , text = current_card["French"])
    flip_timer = window.after(3000,flip)



def flip():
    canvas.itemconfig(canvas_img,image = back)
    canvas.itemconfig(lang_text,fill = "white" ,text = "English")
    canvas.itemconfig(word_text,fill = "white" , text = current_card["English"])
    
def is_known():
    flash_word.remove(current_card)
    data = pandas.DataFrame(flash_word)
    data.to_csv("./data/words_to_learn.csv",index=False)
    gen_word()



#--------------------------------UI------------------------------------
window = Tk()
window.title("Flash Cards")
window.config(width=900,height=726,padx=50,pady=50 ,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip)

canvas = Canvas(width=800,height=526)
front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400,263,image = front)
lang_text = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word_text = canvas.create_text(400,263,text="", font=("Ariel",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column = 0,row = 0,columnspan=2)

right_img = PhotoImage(file="./images/right.png")
right = Button(image = right_img, highlightthickness = 0,command=is_known)
right.grid(column=1,row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong = Button(image = wrong_img, highlightthickness = 0,command=gen_word)
wrong.grid(column=0,row=1)

gen_word()



window.mainloop()

