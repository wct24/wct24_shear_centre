import tkinter as tk
import numpy as np




class Page(tk.Frame):
    def __init__(self,value, *args, **kwargs):
        self.value = value
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.tkraise()
        print(self.value)


class Page0(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is start page")
       label.pack(side="top", fill="both", expand=True)




class Page1(Page,):
   def __init__(self, value, *args, **kwargs):
       Page.__init__(self, 1,*args, **kwargs)
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class StartView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p0 = Page0(self)
        p1 = Page1(self)
        # p2 = Page2(self)
        # p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p0.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
        # b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
        # b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

        b1.pack(side="left")
        # b2.pack(side="left")
        # b3.pack(side="left")

        p0.show()











if __name__ == "__main__":
    root = tk.Tk()
    main = StartView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
