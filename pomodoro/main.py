from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0  # global variable
ticks = "✔"
timer = ""



if __name__ == "__main__":
    # ---------------------------- TIMER RESET ------------------------------- #

    def reset_timer():
        window.after_cancel(timer)
        canvas.itemconfig(timer_text, text="00:00")
        title_label.config(text="Timer")
        tick.config(text="")
        global ticks, reps
        ticks = "✔"
        reps = 0

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def start_timer():
        global reps
        reps += 1
        work_sec = WORK_MIN*60
        short_break_sec = SHORT_BREAK_MIN*60
        long_break_sec = LONG_BREAK_MIN*60

        if reps % 8 == 0:
            title_label.config(text="Break", fg=RED)
            count_down(long_break_sec)  # long break at 8th rep
        elif reps % 2 == 0:
            title_label.config(text="Break",  fg=PINK)
            count_down(short_break_sec)  # short breaks at 2nd, 4th and 6th rep
        else:
            title_label.config(text="Work",  fg=GREEN)
            count_down(work_sec)  # work time at 1st, 3rd, 5th rep


    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def count_down(count):
        count_min = count // 60
        count_sec = count % 60
        global ticks, timer
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            timer = window.after(1000, count_down, count - 1)
        else:
            start_timer()
            if reps % 2 == 1:
                tick.config(text=f"{ticks}")
                ticks += "✔"



    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=1, row=1)

    # Labels
    title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
    title_label.grid(column=1, row=0)
    title_label.config(padx=0, pady=5)

    tick = Label(fg=GREEN, bg=YELLOW)
    # tick = Label(text="✔", font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
    tick.grid(column=1, row=3)

    # Buttons
    start_button = Button(text="Start", command=start_timer, highlightthickness=0)
    start_button.grid(column=0, row=2)

    reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
    reset_button.grid(column=2, row=2)

    window.mainloop()
