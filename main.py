import tkinter as tk
import random
from tkinter import messagebox
from texts import texts


def start():
    text = random.choice(texts)  # choose one random item (text) from the list
    typed_text.config(state="normal")  # now you can type
    typed_text.delete('1.0', "end-1c")  # clear the Text widget
    typed_text.focus()  # put the cursor in the Text widget
    text_label.config(text=text)  # show the text to type from
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    count_down(6)


def reset():
    window.after_cancel(timer)
    typed_text.config(state="normal")
    typed_text.delete('1.0', "end-1c")  # clear the Text widget
    typed_text.config(state="disabled")
    timer_label.config(text="60 s")
    text_label.config(text="")
    words_label.config(text="Typed words: 0")
    start_button.config(state="normal")


def count_down(count):
    global timer
    timer_label.config(text=f"{count} s")
    words_count = len(typed_text.get("1.0", "end-1c").split())
    words_label.config(text=f"Words count: {words_count} words")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:  # when the timer reaches 0
        typed_text.config(state="disabled")  # can't type
        messagebox.showinfo(title="Time over", message=f"You typed {words_count} words in 60 seconds!")


timer = None

window = tk.Tk()
window.title("Typing Speed Test")
window.minsize(width=600, height=0)
window.config(pady=30, padx=45)

text_label = tk.Label(height=9)
text_label.pack()

start_button = tk.Button(text="Start", command=start)
start_button.pack()

timer_label = tk.Label(text="60 s")
timer_label.pack()

typed_text = tk.Text(height=12)
typed_text.config(state="disabled")  # can't type before the counter starts
typed_text.pack()

words_label = tk.Label(text="Typed words: 0")
words_label.pack()

reset_button = tk.Button(text="Reset", command=reset)
reset_button.config(state="disabled")
reset_button.pack()

window.mainloop()
