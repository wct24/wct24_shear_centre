import tkinter as tk


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('280x350')

        self.select_type = tk.StringVar()
        self.type_label = tk.Label(self, text='Game Mode')
        self.name_entry = tk.Entry(self)
        self.type_entry_one = tk.Radiobutton(self, text='Garage', value='garage', variable=self.select_type, command=self.disable_entry)
        self.type_entry_two = tk.Radiobutton(self, text='Festival', value='festival', variable=self.select_type, command=self.disable_entry)
        self.type_entry_three = tk.Radiobutton(self, text='Studio', value='studio', variable=self.select_type, command=self.disable_entry)
        self.type_entry_four = tk.Radiobutton(self, text='Rockslam', value='rockslam', variable=self.select_type, command=self.enable_entry)

        self.select_type.set('rockslam')   # select the last radiobutton; also enables name_entry

        self.type_label.pack()
        self.type_entry_one.pack()
        self.type_entry_two.pack()
        self.type_entry_three.pack()
        self.type_entry_four.pack()
        self.name_entry.pack()

    def enable_entry(self):
        self.name_entry.configure(state='normal')

    def disable_entry(self):
        self.name_entry.configure(state='disabled')


if __name__ == '__main__':

    Gui().mainloop()
