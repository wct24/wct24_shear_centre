import tkinter as tk
from tkinter import ttk


#the entire bottom row of the app.
#has a dependency on self.master.table ~ not good OOP
class EntryManager(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.grid_columnconfigure(5, weight=1)
        font='Helvetica 10 bold'

        tk.Label(self, text='Label', font=font, width=5).grid(row=0, column=0, padx=2)
        lbl = tk.Entry(self, width=10, font=font)
        lbl.grid(row=0, column=1, padx=2)

        tk.Label(self, text='Entry', font=font, width=5).grid(row=0, column=2, padx=2)
        ent = tk.Entry(self, width=25, font=font)
        ent.grid(row=0, column=3, padx=2)

        tk.Button(self, text='add', font=font, command=lambda: self.master.table.addItem(lbl.get(), ent.get())).grid(row=0, column=4, padx=2, sticky='w')

        tk.Label(self, text='rows', font=font, width=4).grid(row=0, column=5, padx=2, sticky='e')
        r = tk.Entry(self, width=4, font=font)
        r.insert('end', self.master.table.rows)
        r.grid(row=0, column=6, padx=2)

        tk.Label(self, text='cols', font=font, width=4).grid(row=0, column=7, padx=2)
        c = tk.Entry(self, width=4, font=font)
        c.insert('end', self.master.table.cols)
        c.grid(row=0, column=8, padx=2)

        tk.Button(self, text='set', font=font, command=lambda: self.master.table.setDims(r.get(), c.get())).grid(row=0, column=9, padx=2, sticky='e')


#generic scrollable frame
class ScrollFrame(tk.Frame):
    def __init__(self, master, row=0, column=0, scrollspeed=.02, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.grid(row=row, column=column, sticky='nswe')

        self.scrollspeed = scrollspeed

        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.canvas.grid(column=0, row=0, sticky='nswe')

        self.v_scroll = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.v_scroll.grid(row=0, column=1, sticky='ns')

        self.canvas.configure(yscrollcommand=self.v_scroll.set)
        self.canvas.bind_all('<MouseWheel>', self.on_mousewheel)

        self.frame = tk.Frame(self.canvas, height=0)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.bind('<Configure>', lambda e:self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0,0), window=self.frame, anchor="nw")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def on_mousewheel(self, event):
        self.canvas.yview_moveto(self.v_scroll.get()[0]+((-event.delta/abs(event.delta))*self.scrollspeed))


#a table cell
class Item(tk.Frame):
    @property
    def value(self):
        return self.__value.get()

    @value.setter
    def value(self, text):
        self.__value.set(text)

    def __init__(self, master, text, value, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        tk.Label(self, text=text, width=10, font='none 8 bold').grid(row=0, column=0, pady=5, padx=5)
        self.__value = tk.StringVar(value=value)
        tk.Entry(self, textvariable=self.__value, width=25).grid(row=0, column=1, pady=5, padx=5)


#the table
class Table(ScrollFrame):
    def __init__(self, master, rows=15, cols=3, **kwargs):
        ScrollFrame.__init__(self, master, **kwargs)
        self.entries = []
        self.rows = rows
        self.cols = cols

    def addItem(self, text, value):
        if len(self.entries) < self.rows*self.cols:
            self.entries.append(Item(self.frame, text, value))
            self.entries[-1].grid(row=(len(self.entries)-1)%self.rows, column=(len(self.entries)-1)//self.rows)

    def getItem(self, row, column):
        return self.entries[self.rows*column+row].value

    def setDims(self, rows, cols):
        if rows.isnumeric():
            self.rows = int(rows)
        if cols.isnumeric():
            self.cols = int(cols)

        for ent in self.entries:
            ent.grid_forget()

        for i, ent in enumerate(self.entries):
            if i < self.rows*self.cols:
                ent.grid(row=i%self.rows, column=i//self.rows)


class App(tk.Tk):
    WIDTH, HEIGHT, TITLE = 770, 465, 'Application'

    def __init__(self):
        tk.Tk.__init__(self)
        ttk.Style().theme_use("vista")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.table = Table(self, rows=18, cols=3)
        self.table.grid(row=0, column=0, sticky='nswe')

        EntryManager(self).grid(row=1, column=0, sticky='nswe', ipady=5)

        # #junk for testing
        # for i in range(12):
        #     self.table.addItem(f'entry_{i}', f'data {i}')


if __name__ == '__main__':
    app = App()
    app.title(App.TITLE)
    app.geometry(f'{App.WIDTH}x{App.HEIGHT}')
    #app.resizable(width=False, height=False)
    app.mainloop()
