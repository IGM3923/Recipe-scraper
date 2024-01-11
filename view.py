import tkinter as tk

window = tk.Tk()
window.title("What Should I Eat?")
window.resizable(width=False, height=False)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5
)
button.pack()
window.mainloop()