from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

# website for color palettes - colohunt.com

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_click():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
    else:
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        window.after(1000, count_down, count - 1)

    if count == 0:
        reps += 1 in range(8)
        start_click()



# ---------------------------- UI SETUP ------------------------------- #


def reset_click():
    pass


window = Tk()
window.title('Pomodoro')
window.config(padx=50, pady=0, bg=YELLOW)

canvas = Canvas(width=220, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(110, 115, image=tomato_img)
timer_text = canvas.create_text(110, 135, text='0:00', fill='white', font=(FONT_NAME, 35, 'bold'))
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
