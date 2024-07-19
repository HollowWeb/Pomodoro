from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer
    window.after_cancel(timer)
    global checkmarks
    checkmarks = ""
    global reps
    reps = 0
    title_label.config(text="Timer")
    checkmark_label.config(text=checkmarks)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    global checkmarks

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        checkmarks += "✔"
        checkmark_label.config(text=checkmarks)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        checkmarks += "✔"
        checkmark_label.config(text=checkmarks)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        checkmark_label.config(text=checkmarks)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # This is how we can change a text canvas
    if count > 0:
        global timer
        # Here we are setting a timer for 1000 milliseconds and then executing a function
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# To delete the border of a canvas we can use highlightthickness and set that to 0
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # Canvas allows us to layer things and requires a width and height
tomato_image = PhotoImage(file="tomato.png")  # With PhotoImage we can read a file where the image is
canvas.create_image(100, 112, image=tomato_image)  # create_image requires the x and y cors and with image= we can use the tomato_image
timer_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(row=0, column=1)

start_button = Button(text="Start", bg=GREEN, border=False, font=(FONT_NAME, 10), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=RED, border=False, font=(FONT_NAME, 10), command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(text=checkmarks, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
checkmark_label.grid(row=3, column=1)



window.mainloop()
