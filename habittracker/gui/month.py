from tkinter import Tk, Button, Label, Checkbutton, Frame, BooleanVar, Entry, X, END
import numpy as np
#from habittracker.calc_stats import calc_ticks_numbers


#def add_placeholder(widget, text):
#    widget.insert(0, text)


#def clear_placeholder(widget):
#    if not widget.get():
#        widget.delete(0, END)


class MonthWindow(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(width=False, height=False) 
        self.title('MonthWindow')

        self.menu_frame = Frame()
        self.menu_frame.pack(fill=X)
        #ent_add_placeholder='Habit name'
        self.ent_add = Entry(master=self.menu_frame)
        #ent_add.insert(0, ent_add_placeholder)
        #ent_add.bind("<FocusIn>", add_placeholder(ent_add, ent_add_placeholder))
        #ent_add.bind("<FocusOut>", clear_placeholder(ent_add))
        self.ent_add.grid(row=0, column=0, sticky='w')
        self.btn_add = Button(master=self.menu_frame, text='Add new habit', height=1, command=self.addHabit)
        self.btn_add.grid(row=0, column=1, sticky='w')
        self.ent_del = Entry(master=self.menu_frame)
        self.ent_del.grid(row=0, column=2, sticky='w')
        self.btn_del = Button(master=self.menu_frame, text='Delete habit', height=1, command=self.delHabit)
        self.btn_del.grid(row=0, column=3, sticky='w')
        self.btn_stats = Button(master=self.menu_frame, text='Show statistics', height=1)
        self.btn_stats = Button(master=self.menu_frame, text='Show statistics', height=1)
        self.btn_stats.grid(row=0, column=4, sticky='w')
        
        self.tracker_frame = Frame()
        self.tracker_frame.pack(fill=X)

        # извлечем из файла месяца:
        # 1) календарные данные
        # 2) список названий привычек (habits_names)
        # 3) матрицу галочек (ticks_matrix)

        self.habits_names = ['jogging', 'teeth brushing', 'water drinking']
        self.habitlabel_list = []
        for i in range(len(self.habits_names)):
            lbl = Label(master=self.tracker_frame, text=self.habits_names[i], height=1)
            self.habitlabel_list.append(lbl)
            lbl.grid(row=i+1, column=0, sticky='e')
        for i in range(30):
            lbl = Label(master=self.tracker_frame, text=str(i+1), height=1)
            lbl.grid(row=0, column=i+1)
        self.ticks_matrix = [[True for _ in range(30)] for _ in range(len(self.habits_names))]
        self.boolean_var_matrix = []
        for i in range(len(self.habits_names)):
            self.boolean_var_matrix.append([])
            for j in range(30):
                var = BooleanVar()
                var.set(self.ticks_matrix[i][j])
                self.boolean_var_matrix[i].append(var)
        self.checkbutton_matrix = []
        for i in range(len(self.habits_names)):
            self.checkbutton_matrix.append([])
            for j in range(30):
                cb = Checkbutton(master=self.tracker_frame, var=self.boolean_var_matrix[i][j])
                self.checkbutton_matrix[i].append(cb)
                cb.grid(row=i+1, column=j+1)

    def addHabit(self):
        possible_habit_name = self.ent_add.get()
        if possible_habit_name and possible_habit_name not in self.habits_names:
            self.habits_names.append(possible_habit_name)
            lbl = Label(master=self.tracker_frame, text=self.habits_names[-1], height=1)
            self.habitlabel_list.append(lbl)
            lbl.grid(row=len(self.habits_names) + 1, column=0, sticky='e')
            self.ticks_matrix.append([False for _ in range(30)])
            self.boolean_var_matrix.append([])
            for j in range(30):
                var = BooleanVar()
                var.set(False)
                self.boolean_var_matrix[-1].append(var)
            self.checkbutton_matrix.append([])
            for j in range(30):
                cb = Checkbutton(master=self.tracker_frame, var=self.boolean_var_matrix[-1][j])
                self.checkbutton_matrix[-1].append(cb)
                cb.grid(row=len(self.habits_names) + 1, column=j+1)

    def delHabit(self):
        possible_habit_name = self.ent_del.get()
        if possible_habit_name in self.habits_names:
            del_idx = self.habits_names.index(possible_habit_name)
            self.habits_names.pop(del_idx)
            self.habitlabel_list[del_idx].destroy()
            self.habitlabel_list.pop(del_idx)
            self.ticks_matrix.pop(del_idx)
            self.boolean_var_matrix.pop(del_idx)
            for widget in self.checkbutton_matrix[del_idx]:
                widget.destroy()
            self.checkbutton_matrix.pop(del_idx)


monthwindow = MonthWindow()
monthwindow.mainloop()
