import tkinter as tk
from tkinter import messagebox
from texts import *


def start():
    text_label.config(text=text)
    count_down(6)


def count_down(count):
    timer_label.config(text=f"{count} s")
    words_count = len(typed_text.get("1.0", "end-1c").split())
    words_label.config(text=f"Words count: {words_count} words")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        typed_text.config(state="disabled")


window = tk.Tk()
window.title("Typing Speed Test")
window.minsize(width=600, height=0)
window.config(pady=30, padx=45)

text_label = tk.Label(text="Text", height=12)
text_label.pack()

start_button = tk.Button(text="Start", command=start)
start_button.pack()

timer_label = tk.Label(text="60 s")
timer_label.pack()

typed_text = tk.Text(height=12)
typed_text.focus()
typed_text.pack()

words_label = tk.Label(text="Typed words: 0")
words_label.pack()


window.mainloop()
