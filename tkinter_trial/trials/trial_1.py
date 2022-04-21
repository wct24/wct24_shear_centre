try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


def toggle_state(*_):
    if entry.var.get():
        button['state'] = 'normal'
    else:
        button['state'] = 'disabled'


if __name__ == '__main__':
    root = tk.Tk()
    entry = tk.Entry(root)
    entry.var = tk.StringVar()
    entry['textvariable'] = entry.var
    entry.var.trace_add('write', toggle_state)
    button = tk.Button(root, text="Button", state='disabled')
    entry.pack()
    button.pack()
    tk.mainloop()

