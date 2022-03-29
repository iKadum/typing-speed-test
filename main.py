import tkinter as tk
import random
from tkinter import messagebox
from texts import texts


def start():
    typed_text.config(state="normal")
    typed_text.delete('1.0', "end-1c")
    typed_text.focus()
    text_label.config(text=text)
    count_down(10)


def count_down(count):
    timer_label.config(text=f"{count} s")
    words_count = len(typed_text.get("1.0", "end-1c").split())
    words_label.config(text=f"Words count: {words_count} words")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        typed_text.config(state="disabled")
        messagebox.showinfo(title="Time over", message=f"You typed {words_count} words in 60 seconds!")


text = random.choice(texts)

window = tk.Tk()
window.title("Typing Speed Test")
window.minsize(width=600, height=0)
window.config(pady=30, padx=45)

text_label = tk.Label(text="Text", height=9)
text_label.pack()

start_button = tk.Button(text="Start", command=start)
start_button.pack()

timer_label = tk.Label(text="60 s")
timer_label.pack()

typed_text = tk.Text(height=12)
typed_text.config(state="disabled")
typed_text.pack()

words_label = tk.Label(text="Typed words: 0")
words_label.pack()


window.mainloop()
