import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
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
window = tkinter.Tk()
window.title("Pomodoro Timer App")
# window.minsize(width=800, height=600)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Add Timer Label
label_timer = tkinter.Label(text="Timer", font=(FONT_NAME, 40))
label_timer.grid(row=0, column=1)
label_timer.config(bg=YELLOW, fg=GREEN)

# Add Start Button
button_start = tkinter.Button(text="Start", font=FONT_NAME, highlightthickness=0)
button_start.config(bg=YELLOW)
button_start.grid(row=2, column=0)

# Add Reset Button
button_reset = tkinter.Button(text="Reset", font=FONT_NAME, highlightthickness=0)
button_reset.config(bg=YELLOW)
button_reset.grid(row=2, column=2)

# Add check marks for completed Pomodoros
label_checkmark = tkinter.Label(text="✓")
label_checkmark.grid(row=3, column=1)
label_checkmark.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))


window.mainloop()
