from tkinter import Tk, Button, Label, Checkbutton, Frame, BooleanVar, X, END, ttk
from functools import partial
import sys
import os
# разобраться с именем файла
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from calc_stats import calc_most_popular, calc_least_popular, calc_ticks_numbers  # noqa: E402


def parse_input_file(lines):
    month_name, habits_number, days_number, *other = lines
    habits_number = int(habits_number)
    days_number = int(days_number)
    habits_names = []
    for i in range(habits_number):
        habits_names.append(other[0].strip())
        other.pop(0)
    ticks_matrix = []
    for i in range(habits_number):
        ticks_matrix.append([])
        for j in range(days_number):
            ticks_matrix[i].append(bool(int(other[0])))
            other.pop(0)
    return month_name.strip(), days_number, habits_names, ticks_matrix


class PlaceholderEntry(ttk.Entry):
    def __init__(self, placeholder, *args, **kwargs):
        super().__init__(*args, style='Placeholder.TEntry', **kwargs)
        self.placeholder = placeholder

        self.insert(0, self.placeholder)
        self.bind('<FocusIn>', self._clear_placeholder)
        self.bind('<FocusOut>', self._add_placeholder)

    def _clear_placeholder(self, e):
        if self['style'] == 'Placeholder.TEntry':
            self.delete(0, END)
            self['style'] = 'TEntry'

    def _add_placeholder(self, e):
        if not self.get():
            self.insert(0, self.placeholder)
            self['style'] = 'Placeholder.TEntry'


class MonthWindow(Tk):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.resizable(width=False, height=False)

        self.menu_frame = Frame()
        self.menu_frame.pack(fill=X)
        style = ttk.Style(self.menu_frame)
        style.configure('Placeholder.TEntry', foreground='#d5d5d5')
        style.configure('TEntry', foreground='black')
        self.ent_add = PlaceholderEntry(master=self.menu_frame, placeholder='Habit name to add')
        self.ent_add.grid(row=0, column=0, sticky='w')
        self.btn_add = Button(master=self.menu_frame, text='Add new habit', height=1, command=self.addHabit)
        self.btn_add.grid(row=0, column=1, sticky='w')
        self.ent_del = PlaceholderEntry(master=self.menu_frame, placeholder='Habit name to delete')
        self.ent_del.grid(row=0, column=2, sticky='w')
        self.btn_del = Button(master=self.menu_frame, text='Delete habit', height=1, command=self.delHabit)
        self.btn_del.grid(row=0, column=3, sticky='w')
        self.btn_stats = Button(master=self.menu_frame, text='Show statistics', height=1)
        self.btn_stats.grid(row=0, column=4, sticky='w')
        self.btn_save = Button(master=self.menu_frame, text='Save', height=1, command=self.saveData)
        self.btn_save.grid(row=0, column=5, sticky='w')

        self.tracker_frame = Frame()
        self.tracker_frame.pack(fill=X)

        with open(filename) as input_file:
            input_file_lines = input_file.readlines()
        self.month_name, self.days_number, self.habits_names, self.ticks_matrix = parse_input_file(input_file_lines)

        self.title(self.month_name)
        self.habitlabel_list = []
        for i in range(len(self.habits_names)):
            lbl = Label(master=self.tracker_frame, text=self.habits_names[i], height=1)
            self.habitlabel_list.append(lbl)
            lbl.grid(row=i+1, column=0, sticky='e')
        for i in range(self.days_number):
            lbl = Label(master=self.tracker_frame, text=str(i+1), height=1)
            lbl.grid(row=0, column=i+1)
        self.boolean_var_matrix = []
        for i in range(len(self.habits_names)):
            self.boolean_var_matrix.append([])
            for j in range(self.days_number):
                var = BooleanVar()
                var.set(self.ticks_matrix[i][j])
                self.boolean_var_matrix[i].append(var)
        self.checkbutton_matrix = []
        for i in range(len(self.habits_names)):
            self.checkbutton_matrix.append([])
            for j in range(self.days_number):
                cb = Checkbutton(master=self.tracker_frame, var=self.boolean_var_matrix[i][j], command=partial(self.changeState, coords=(i, j)))
                self.checkbutton_matrix[i].append(cb)
                cb.grid(row=i+1, column=j+1)

    def changeState(self, coords):
        i, j = coords
        self.ticks_matrix[i][j] = not self.ticks_matrix[i][j]

    def addHabit(self):
        possible_habit_name = self.ent_add.get()
        if possible_habit_name and possible_habit_name not in self.habits_names:
            self.habits_names.append(possible_habit_name)
            lbl = Label(master=self.tracker_frame, text=self.habits_names[-1], height=1)
            self.habitlabel_list.append(lbl)
            lbl.grid(row=len(self.habits_names) + 1, column=0, sticky='e')
            self.ticks_matrix.append([False for _ in range(self.days_number)])
            self.boolean_var_matrix.append([])
            for j in range(self.days_number):
                var = BooleanVar()
                var.set(False)
                self.boolean_var_matrix[-1].append(var)
            self.checkbutton_matrix.append([])
            for j in range(self.days_number):
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

    def saveData(self):
        with open(self.filename, 'w') as output_file:
            print(self.month_name, file=output_file)
            print(len(self.habits_names), file=output_file)
            print(self.days_number, file=output_file)
            for habit_name in self.habits_names:
                print(habit_name, file=output_file)
            for i in range(len(self.habits_names)):
                for j in range(self.days_number):
                    print(int(self.ticks_matrix[i][j]), file=output_file)


# разобраться с именем файла
monthwindow = MonthWindow('../data/months/june2022.txt')
monthwindow.mainloop()
