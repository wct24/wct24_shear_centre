import pandas as pd
import tkinter as tk
from tkinter import *
import os
import shutil

LARGE_FONT= ("Verdana", 12)


column_names =  ['ShapeName', 'ShapeId','Dimensions', "Material" , 'BoundaryCondition', 'LoadingPosition', 'LoadType', "AnalysisType"]
df = pd.DataFrame(columns=column_names, index=[0])
df2 = df.copy()
df3 = df.copy()[0:0] #empty version
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Shape, PageTwo, SemiCircle, PFC, IBeam, RHS, NACA0025,ReidSection, Material, BoundaryCondition, LoadingPosition,AnalysisType):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Next",
                            command=lambda: controller.show_frame(Shape))
        button.pack()

class Shape(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Shape Of The Crossection", font=LARGE_FONT)
        label.grid(row = 0,column=1)
        var =tk.IntVar()

        def selection():
            choice = var.get()
            global df
            df['ShapeId'][0] = choice
            if choice == 1:
                df['ShapeName'][0] = "1-Semi-Circle"
                button2.config(state=NORMAL, command=lambda: controller.show_frame(SemiCircle))
            if choice == 2:
                df['ShapeName'][0] = "2-PFC"
                button2.config(state=NORMAL, command=lambda: controller.show_frame(PFC))
            if choice == 3:
                df['ShapeName'][0] = "3-I-Beam"
                button2.config(state=NORMAL, command=lambda: controller.show_frame(IBeam))
            if choice == 4:
                df['ShapeName'][0] = "4-RHS"
                button2.config(state=NORMAL, command=lambda: controller.show_frame(RHS))
            if choice == 5:
                df['ShapeName'][0] = "5-NACA0025"
                button2.config(state=NORMAL, command=lambda: controller.show_frame(NACA0025))
            if choice == 6:
                df['ShapeName'][0] = "6-Reid"
                button2.config(state=NORMAL, command=lambda: controller.show_frame(ReidSection))

        tk.Radiobutton(self, text='1. Semi-Circle', variable=var, value=1,command=selection).grid(row=2, column=0)
        tk.Radiobutton(self, text='2. PFC', variable=var, value=2,command=selection).grid(row=2, column=1)
        tk.Radiobutton(self, text='3. I-Beam', variable=var, value=3,command=selection).grid(row=2, column=2)
        tk.Radiobutton(self, text='4. RHS', variable=var, value=4,command=selection).grid(row=3, column=0)
        tk.Radiobutton(self, text='5. NACA0025', variable=var, value=5,command=selection).grid(row=3, column=1)
        tk.Radiobutton(self, text='6. Reid Section', variable=var, value=6,command=selection).grid(row=3, column=2)

        button2 = tk.Button(self, text="Next >>", state= DISABLED)
        button2.grid(row=4, column=3)


class SemiCircle(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #logic

        def only_numbers(char):
            return char.isdecimal() or char == '.'


        def toggle_state(*_):
            try:
                if float(e1.var.get()) and float(e2.var.get()) and float(e3.var.get()) :
                    button2['state'] = 'normal'
                    button2['command'] = lambda: controller.show_frame(Material)
                    df.at[ 0,'Dimensions'] = [float(e1.var.get()), float(e2.var.get()), float(e3.var.get())]
                else:
                    button2['state'] = 'disabled'

            except ValueError:
                pass

        #LENGTH MUST ALWAYS BE THE LAST VARIABLE

        validation = self.register(only_numbers)
        e1 = tk.Entry(self, validate="key", validatecommand=(validation, '%S'))
        e2 = tk.Entry(self, validate="key", validatecommand=(validation, '%S'))
        e3 = tk.Entry(self, validate="key", validatecommand=(validation, '%S'))


        e1.var = tk.StringVar()
        e1['textvariable'] = e1.var
        e1.var.trace_add('write', toggle_state)

        e2.var = tk.StringVar()
        e2['textvariable'] = e2.var
        e2.var.trace_add('write', toggle_state)

        e3.var = tk.StringVar()
        e3['textvariable'] = e3.var
        e3.var.trace_add('write', toggle_state)
        #Build
        label = tk.Label(self, text="Semi-Circular Crossection", font=LARGE_FONT)
        label.grid(row = 0,column=1)

        tk.Label(self, text="r = ").grid(row=1, column=0)
        tk.Label(self, text="t = ").grid(row=1, column=2)
        tk.Label(self, text="l = ").grid(row=1, column=4)

        e1.grid(row=1, column=1)
        e2.grid(row=1, column=3)
        e3.grid(row=1, column=5)

        button1 = tk.Button(self, text="<<Back", command=lambda: controller.show_frame(Shape))
        button1.grid(row=4, column=0)

        button2 = tk.Button(self, text="Next >>", state= DISABLED)
        button2.grid(row=4, column=3)


class PFC(tk.Frame):
    #LENGTH MUST ALWAYS BE THE LAST VARIABLE

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PFC Crossection", font=LARGE_FONT)
        label.grid(row = 0,column=2)

        button1 = tk.Button(self, text="<<Back", command=lambda: controller.show_frame(Shape))
        button1.grid(row=4, column=0)

        button2 = tk.Button(self, text="Next >>", state= DISABLED)
        button2.grid(row=4, column=4)

class IBeam(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="I-Beam Crossection", font=LARGE_FONT)
        label.grid(row = 0,column=1)

        button1 = tk.Button(self, text="<<Back", command=lambda: controller.show_frame(Shape))
        button1.grid(row=4, column=0)

        button2 = tk.Button(self, text="Next >>", state= DISABLED)
        button2.grid(row=4, column=3)

class RHS(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="RHS Crossection", font=LARGE_FONT)
        label.grid(row = 0,column=1)

        button1 = tk.Button(self, text="<<Back", command=lambda: controller.show_frame(Shape))
        button1.grid(row=4, column=0)

        button2 = tk.Button(self, text="Next >>", state= DISABLED)
        button2.grid(row=4, column=3)

class NACA0025(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NACA0025 Crossection", font=LARGE_FONT)
        label.grid(row = 0,column=1)

        button1 = tk.Button(self, text="<<Back", command=lambda: controller.show_frame(Shape))
        button1.grid(row=4, column=0)

        button2 = tk.Button(self, text="Next >>", state= DISABLED)
        button2.grid(row=4, column=3)

class ReidSection(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Reid", font=LARGE_FONT)
        label.grid(row = 0,column=1)

        button1 = tk.Button(self, text="<<Back", command=lambda: controller.show_frame(Shape))
        button1.grid(row=4, column=0)

        button2 = tk.Button(self, text="Next >>", state= DISABLED)
        button2.grid(row=4, column=3)

class Material(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #logic

        def only_numbers(char):
            return char.isdecimal() or char == '.'


        def toggle_state(*_):
            try:
                if float(e1.var.get()) and float(e2.var.get()) and float(e3.var.get()) :
                    button2['state'] = 'normal'
                    button2['command'] = lambda: controller.show_frame(BoundaryCondition)
                    df.at[ 0,'Material'] = [float(e1.var.get()), float(e2.var.get()), float(e3.var.get())]
                else:
                    button2['state'] = 'disabled'

            except ValueError:
                pass

        validation = self.register(only_numbers)
        e1 = tk.Entry(self, validate="key", validatecommand=(validation, '%S'))
        e2 = tk.Entry(self, validate="key", validatecommand=(validation, '%S'))
        e3 = tk.Entry(self, validate="key", validatecommand=(validation, '%S'))


        e1.var = tk.StringVar()
        e1['textvariable'] = e1.var
        e1.var.trace_add('write', toggle_state)

        e2.var = tk.StringVar()
        e2['textvariable'] = e2.var
        e2.var.trace_add('write', toggle_state)

        e3.var = tk.StringVar()
        e3['textvariable'] = e3.var
        e3.var.trace_add('write', toggle_state)
        #Build
        label = tk.Label(self, text="Material", font=LARGE_FONT)
        label.grid(row = 0,column=2)

        tk.Label(self, text="E (GPa) = ").grid(row=1, column=0)
        tk.Label(self, text="G (GPa) = ").grid(row=1, column=2)
        tk.Label(self, text="v = ").grid(row=1, column=4)

        e1.grid(row=1, column=1)
        e2.grid(row=1, column=3)
        e3.grid(row=1, column=5)

        button1 = tk.Button(self, text="<<Back", command=lambda: controller.show_frame(shape))
        button1.grid(row=4, column=0)

        button2 = tk.Button(self, text="Next >>", state= DISABLED)
        button2.grid(row=4, column=3)

class BoundaryCondition(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Boundary Condition", font=LARGE_FONT)
        label.grid(row = 0,column=1)
        var =tk.IntVar()

        #LENGTH MUST ALWAYS BE THE LAST VARIABLE

        def selection():
            choice = var.get()
            global df
            df['BoundaryCondition'][0] = choice
            if choice == 1 or choice == 2 :
                button2.config(state=NORMAL, command=lambda: controller.show_frame(LoadingPosition))


        tk.Radiobutton(self, text='Encastre', variable=var, value=2,command=selection).grid(row=2, column=0)
        tk.Radiobutton(self, text='Warping', variable=var, value=1,command=selection).grid(row=2, column=1)


        button2 = tk.Button(self, text="Next >>", state= DISABLED)
        button2.grid(row=4, column=3)

class LoadingPosition(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Loading Position", font=LARGE_FONT)
        label.grid(row = 0,column=2)

        label = tk.Label(self, text="Array of Positions : ")
        label.grid(row = 1,column=2)

        var =tk.IntVar()
        #LENGTH MUST ALWAYS BE THE LAST VARIABLE
        def selection():
            choice = var.get()
            global df
            global df2

            l = int(df["Dimensions"][0][-1])


            if choice == 1:
                df_empty = df[0:0]
                df2 = df_empty.append([df]*l,ignore_index=True)
                for i in range(l):
                    df2["LoadingPosition"][i]=i*20
                button2.config(state=NORMAL, command=lambda: controller.show_frame(AnalysisType))

            if choice == 2:
                df_empty = df[0:0]
                df2 = df_empty.append([df]*l*2,ignore_index=True)
                for i in range(l*2):
                    df2["LoadingPosition"][i]=i*10
                button2.config(state=NORMAL, command=lambda: controller.show_frame(AnalysisType))

            if choice == 3:
                df_empty = df[0:0]
                df2 = df_empty.append([df]*l*4,ignore_index=True)
                for i in range(l*4):
                    df2["LoadingPosition"][i]=i*5
                button2.config(state=NORMAL, command=lambda: controller.show_frame(AnalysisType))

            if choice == 4:
                df_empty = df[0:0]
                df2 = df_empty.append([df]*l*10,ignore_index=True)
                for i in range(l*10):
                    df2["LoadingPosition"][i]=i*2

                button2.config(state=NORMAL, command=lambda: controller.show_frame(AnalysisType))

            if choice == 5:
                df_empty = df[0:0]
                df2 = df_empty.append([df]*l*20,ignore_index=True)
                for i in range(l*20):
                    df2["LoadingPosition"][i]=i

                button2.config(state=NORMAL, command=lambda: controller.show_frame(AnalysisType))

        tk.Radiobutton(self, text='Every 1m starting at z=0', variable=var, value=1 ,command=selection).grid(row=2, column=2)
        tk.Radiobutton(self, text='Every 0.5m starting at z=0', variable=var, value=2,command=selection).grid(row=3, column=2)
        tk.Radiobutton(self, text='Every 0.25m starting at z=0', variable=var, value=3,command=selection).grid(row=4, column=2)
        tk.Radiobutton(self, text='Every 0.1m starting at z=0', variable=var, value=4,command=selection).grid(row=5, column=2)
        tk.Radiobutton(self, text='ALL (Every 0.1m starting at z=0 )', variable=var, value=5,command=selection).grid(row=6, column=2)

        label = tk.Label(self, text="OR a Single Value")
        label.grid(row = 7,column=2)


        button2 = tk.Button(self, text="Next >>", state= DISABLED)
        button2.grid(row=10, column=4)

class AnalysisType(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="AnalysisType", font=LARGE_FONT)
        label.grid(row = 0,column=1)
        var1 =tk.IntVar()
        var2 =tk.IntVar()
        var3 =tk.IntVar()
        #LENGTH MUST ALWAYS BE THE LAST VARIABLE

        def var_states():
            global df2
            global df3
            if var1.get()==1 or var2.get()==1 or var3.get()==1:
                if var1.get() == 1:
                    TSC_df = df2.copy()
                    for row in TSC_df.iterrows():
                        TSC_df["LoadType"] = 1
                        TSC_df["AnalysisType"] = 1
                    df3 = df3.append(TSC_df,ignore_index=True)
                if var2.get() == 1:
                    LSC_df = df2.copy()
                    for row in LSC_df.iterrows():
                        LSC_df["LoadType"] = 1
                        LSC_df["AnalysisType"] = 2
                    df3 = df3.append(LSC_df,ignore_index=True)
                if var3.get() == 1:
                    TA_df = df2.copy()
                    for row in TA_df.iterrows():
                        TA_df["LoadType"] = 2
                        TA_df["AnalysisType"] = 3
                    df3 = df3.append(TA_df,ignore_index=True)
                app.quit()
            else:
                pass






        tk.Checkbutton(self, text='1. TSC', variable=var1).grid(row=1, column=2)
        tk.Checkbutton(self, text='2. LSC', variable=var2).grid(row=2, column=2)
        tk.Checkbutton(self, text='3. Torque Analysis', variable=var3).grid(row=3, column=2)

        button2 = tk.Button(self, text="CONFIRM" , command=var_states)
        button2.grid(row=4, column=3)






class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="<< Back",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Shape of Crossection", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

app = SeaofBTCapp()
app.mainloop()

print(df3)


# remove illegal characters in the id of the beam
dim = str(df['Dimensions'][0])
dim = dim.replace(", ", "_")
dim = dim.replace("[", "")
dim = dim.replace("]", "")


mat = str(df['Material'][0])
mat = mat.replace(", ", "_")
mat = mat.replace("[", "")
mat = mat.replace("]", "")

if str(df['BoundaryCondition'][0]) == "2":
    bc = "encastre"
if str(df['BoundaryCondition'][0]) == "1":
    bc = "warping"

###make a folder
folder_name = r"D:\shear_centre\{}\{}\{}\{}".format(str(df['ShapeName'][0]),dim,mat,bc)

# Check whether the specified path exists or not
isExist = os.path.exists(folder_name)
if not isExist:
  # Create a new directory because it does not exist
  os.makedirs(folder_name)
  # make a copy of the universal shape script:
  # src = r"C:\Users\touze\project\Shear_centre\tkinter_trial\shape_scripts\shape_{}.py".format(str(df['ShapeId'][0]))
  # dst = folder_name + r"\script.py"
  # shutil.copyfile(src, dst)
  df3.to_csv(folder_name+r'\input.csv')


