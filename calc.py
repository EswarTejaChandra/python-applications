import tkinter as tk


def press_key(key):
    if key == 'C':
        entry.delete(0, tk.END)
    elif key == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, key)

def create_button(text, row, col, col_span=1, bg='white', fg='black'):
    button = tk.Button(root, text=text, command=lambda: press_key(text), width=5, height=2, bg=bg, fg=fg)
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5, sticky='nesw')

root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='white')

entry = tk.Entry(root, font=('Arial', 14), justify='right', bg='white', fg='black')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nesw')

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 1, 'orange')
]

for button in buttons:
    if button[0] in '0123456789.':
        create_button(*button, bg='white', fg='black')
    else:
        create_button(button[0], button[1], button[2], bg='black', fg='white')

root.mainloop()
