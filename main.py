import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global timer

    window.after_cancel(timer)
    label_timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    label_checkmark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global label_timer

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    print(f"Reps #: {reps}")

    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        label_timer.config(text="Work", fg=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅︎"
        label_checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer App")
# window.minsize(width=800, height=600)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Add Timer Label
label_timer = tkinter.Label(text="Timer", font=(FONT_NAME, 40))
label_timer.grid(row=0, column=1)
label_timer.config(bg=YELLOW, fg=GREEN)

# Add Start Button
button_start = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
button_start.config(bg=YELLOW)
button_start.grid(row=2, column=0)

# Add Reset Button
button_reset = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.config(bg=YELLOW)
button_reset.grid(row=2, column=2)

# Add check marks for completed Pomodoros
label_checkmark = tkinter.Label(fg=GREEN, bg=YELLOW)
label_checkmark.grid(row=3, column=1)

window.mainloop()
