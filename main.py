
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

#website for color palettes - colohunt.co

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

def start_click():
    pass

def reset_click():
    pass

window = Tk()
window.title('Pomodoro')
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=220, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(110, 115, image=tomato_img)
canvas.create_text(110, 135, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column='1', row='1')

label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label_timer.grid(column='1', row='0')

checkmark_label = Label(text="  ✔️", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
checkmark_label.grid(column='1', row='4')

button = Button(text='start', command=start_click)
button.grid(column='0', row='3')

button = Button(text='reset', command=reset_click)
button.grid(column='2', row='3')



window.mainloop()