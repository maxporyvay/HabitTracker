from tkinter import ttk, Tk, Label, Button, Entry, Radiobutton, Checkbutton, Frame, Toplevel, StringVar, IntVar, X, END
from calendar import monthrange
from os import listdir
from datetime import date
from os.path import exists, dirname
from functools import partial
from habittracker.calc_stats import calc_most_popular, calc_least_popular, calc_ticks_numbers

d_mon = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

def to_menu_day():
    day_menu.destroy()
    main()


def to_menu_help():
    help_menu.destroy()
    main()


def to_menu_month():
    month_menu.destroy()
    main()


def to_menu_saved_monthes():
    saved_monthes_menu.destroy()
    main()


def to_menu_add_month():
    add_month_menu.destroy()
    main()


def to_menu_info():
    info_plans_menu.destroy()
    main()


def to_menu_show():
    show_plan_menu.destroy()
    main()


def to_menu_show_plans():
    show_plans_menu.destroy()
    main()


def to_menu_add_plan_day():
    add_plan_day_menu.destroy()
    main()


def to_menu_fast_adding():
    fast_adding_menu.destroy()
    main()


def add_text_in_file(file_path, text_to_add, d):
    with open(file_path, "r+") as fd:
        lines = fd.readlines()
        flag_day_was = 0
        size = len(lines)
        for i in range(size):
            if lines[i][0] == str(d) and lines[i][1] == '$':
                flag_day_was = 1
                s_old = lines[i]
                s_new = '\n' + lines[i][0] + lines[i][1] + '  ' + text_to_add + '\n' + s_old[2:]
                lines[i] = s_new
        if flag_day_was == 0:
            s_new = '\n' + str(d) + '$' + '  ' + text_to_add
            lines.append(s_new)
        fd.seek(0)
        fd.writelines(lines)


def click_plan_day():
    text_to_add = entry_plan_day.get()
    today = date.today()
    d = today.day
    m = today.month
    y = today.year
    dir_path = dirname(__file__) + '/data/tracker/'
    file_name = d_mon[m] + str(y) + ".txt"
    file_path = dir_path + file_name
    if exists(file_path) == False:
        with open(file_path, "w") as fd:
            fd.write(f'{d_mon[m]} {y}\n')
            fd.write("0\n")
            fd.write(str(monthrange(int(y), m)[1]))
            fd.write("\n")
    dir_path = dirname(__file__) + '/data/plans/'
    file_name = d_mon[m] + str(y) + ".txt"
    file_path = dir_path + file_name
    if exists(file_path) == False:
        with open(file_path, "w") as fd:
            fd.write(f'{d_mon[m]} {y}\n')
            fd.write("0\n")
            fd.write(str(monthrange(int(y), m)[1]))
            fd.write("\n")
    add_text_in_file(file_path, text_to_add, d)


def add_plan_day():
    day_menu.destroy()
    global add_plan_day_menu
    add_plan_day_menu = Tk()
    add_plan_day_menu.geometry('400x800')

    data_plan_day = StringVar()
    data_plan_day.set('Enter new plans for today')

    lbl_plan_day = Label(add_plan_day_menu, textvariable=data_plan_day)
    lbl_plan_day.pack()

    global entry_plan_day
    entry_plan_day = Entry(add_plan_day_menu)
    entry_plan_day.pack()

    btn_plan_day = Button(add_plan_day_menu, text="Add", width=11, height=3, bg="white", fg="black", command=click_plan_day)
    btn_plan_day.pack()

    btn_exit = Button(add_plan_day_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_add_plan_day)
    btn_exit.pack()
    add_plan_day_menu.mainloop()


def show_day():
    day_menu.destroy()
    global show_plan_menu
    show_plan_menu = Tk()
    show_plan_menu.geometry('400x800')
    show_plan()

def click_show_plans():
    d = day_plans.get()
    s_month = ""
    s_year = ""
    for i in month_info:
        if (i >= 'a' and i <= 'z') or i >= 'A' and i <= 'Z':
            s_month += i
        else:
            s_year += i
    y = int(s_year)
    for i in d_mon:
        if d_mon[i] == s_month:
            m = i
    show_plans_menu.destroy()
    global show_plan_menu
    show_plan_menu = Tk()
    show_plan_menu.geometry('400x800')
    show_plan(d, m, y)

def show_plan(*args):
    if len(args) == 0:
        today = date.today()
        day = today.day
        mon = today.month
        year = today.year
    elif len(args) == 3:
        day = args[0]
        mon = args[1]
        year = args[2]
    else:
        print("Something wrong")
    dir_path = dirname(__file__) + '/data/plans/'
    file_name = d_mon[mon] + str(year) + ".txt"
    file_full_name = dir_path + file_name
    if exists(file_full_name) == False:
        lbl_out = Label(show_plan_menu, text="Tasks are not scheduled")
        lbl_out.pack()
    else:
        plans = []
        flag = 0
        with open(file_full_name, "r") as fd:
            lines = fd.readlines()
            for i in lines:
                if i[0] >= '0' and i[0] <= '9' and i[0] != str(day) and i[1] == '$':
                    flag = 0
                if flag and (i[0] < '0' or i[0] > '9'):
                    plans.append(i)
                if i[0] == str(day) and i[1] == "$":
                    flag = 1
                    plans.append(i)
            if len(plans) == 0:
                plans.append("Tasks are not scheduled")
            all_info = "".join(plans)
            lbl_out = Label(show_plan_menu, text=all_info)
            lbl_out.pack()

    btn_exit = Button(show_plan_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_show)
    btn_exit.pack()
    show_plan_menu.mainloop()

def day():
    main_menu.destroy()
    global day_menu
    day_menu = Tk()
    day_menu.geometry('400x800')
    today = date.today()
    lbl_date = Label(day_menu, text=f'{today.day}.{today.month}.{today.year}')
    lbl_date.pack()
    btn_show_info = Button(day_menu, text="Show plan in this day", width=30, height=5, bg="white", fg="black", command=show_day)
    btn_show_info.pack()
    btn_add_info = Button(day_menu, text="Add plan in this day", width=30, height=5, bg="white", fg="black", command=add_plan_day)
    btn_add_info.pack()
    btn_exit = Button(day_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_day)
    btn_exit.pack()
    day_menu.mainloop()

flag_tr0_plans1 = 0

def info_tr(s):
    monthwindow = MonthWindow(dirname(__file__) + '/data/tracker/' + s + '.txt')
    monthwindow.mainloop()


def info_plans(s):
    global month_info
    month_info = s
    info_plans_menu.destroy()
    global show_plans_menu
    show_plans_menu = Tk()
    show_plans_menu.geometry('400x800')

    data_day = StringVar()
    data_day.set("Enter day")
    lbl_mon = Label(show_plans_menu, textvariable=data_day)
    lbl_mon.pack()
    global day_plans
    day_plans = Entry(show_plans_menu)
    day_plans.pack()
    btn_choise = Button(show_plans_menu, text="Enter", width=11, height=3, bg="white", fg="black", command=click_show_plans)
    btn_choise.pack()

    btn_exit = Button(show_plans_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_show_plans)
    btn_exit.pack()
    show_plans_menu.mainloop()


def click_plans():
    text_choise_mon = combo_files.get()
    if flag_tr0_plans1 == 0:
        info_tr(text_choise_mon)
    elif flag_tr0_plans1 == 1:
        info_plans(text_choise_mon)


def view_info():
    saved_monthes_menu.destroy()
    global info_plans_menu
    info_plans_menu = Tk()
    info_plans_menu.geometry('400x800')

    dirrectory = dirname(__file__) + '/data/plans'
    files_indir = listdir(dirrectory)
    if '.DS_Store' in files_indir:
        files_indir.remove('.DS_Store')
    files = []
    for i in files_indir:
        files.append(i[0:-4])
    
    global combo_files
    combo_files = ttk.Combobox(master=info_plans_menu, values=files, text='Available months:')
    combo_files.current(0)
    combo_files.pack()

    btn_choise = Button(info_plans_menu, text="Choose", width=11, height=3, bg="white", fg="black", command=click_plans)
    btn_choise.pack()

    btn_exit = Button(info_plans_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_info)
    btn_exit.pack()

    info_plans_menu.mainloop()


def view_info_plans():
   global flag_tr0_plans1 
   flag_tr0_plans1 = 1
   view_info()


def view_info_tr():
   global flag_tr0_plans1 
   flag_tr0_plans1 = 0
   view_info()


def saved_monthes():
    month_menu.destroy()
    global saved_monthes_menu
    saved_monthes_menu = Tk()
    saved_monthes_menu.geometry('400x800')

    btn_tr = Button(saved_monthes_menu, text = 'Habit tracker', command=view_info_tr)
    btn_plans = Button(saved_monthes_menu, text = 'Plans', command=view_info_plans)
    btn_tr.pack()
    btn_plans.pack()

    btn_exit = Button(saved_monthes_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_saved_monthes)
    btn_exit.pack()

    saved_monthes_menu.mainloop()


def click_mon():
    text_year = entry_year.get()
    text_mon = combo_mon.get()
    file_path = dirname(__file__) + '/data/tracker/'
    file_path += text_mon
    file_path += text_year
    file_path += ".txt"
    if exists(file_path) == False:
        with open(file_path, "w") as fd:
            fd.write(f'{text_mon} {text_year}\n')
            fd.write("0\n")
            fd.write(str(monthrange(int(text_year), [key for key in d_mon if d_mon[key] == text_mon][0])[1]))
            fd.write("\n")

        plan_path = dirname(__file__) + '/data/plans/'
        plan_path += text_mon
        plan_path += text_year
        plan_path += ".txt"
        with open(plan_path, "w") as fd:
            fd.write(f'{text_mon} {text_year}\n')
            fd.write("0\n")
            fd.write(str(monthrange(int(text_year), [key for key in d_mon if d_mon[key] == text_mon][0])[1]))
            fd.write("\n")
    else:
        pass #  сделать вывод пользователю


def add_month():
    month_menu.destroy()
    global add_month_menu
    add_month_menu = Tk()
    add_month_menu.geometry('400x800')

    data_year = StringVar()
    data_year.set('Enter the year of the month to be added:')

    lbl_year = Label(add_month_menu, textvariable=data_year)
    lbl_year.pack()

    global entry_year
    entry_year = Entry(add_month_menu)
    entry_year.pack()

    lbl_mon = Label(add_month_menu, text='Choose the month to be added:')
    lbl_mon.pack()

    global combo_mon
    combo_mon = ttk.Combobox(add_month_menu, values=list(d_mon.values()))
    combo_mon.pack()

    btn_mon = Button(add_month_menu, text="Add month", width=11, height=3, bg="white", fg="black", command=click_mon)
    btn_mon.pack()

    btn_exit = Button(add_month_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_add_month)
    btn_exit.pack()

    add_month_menu.mainloop()


def month():
    main_menu.destroy()
    global month_menu
    month_menu = Tk()
    month_menu.geometry('400x800')

    btn_saved_monthes = Button(month_menu, text="Saved months",  width=30, height=5, bg="white", fg="black", command=saved_monthes)
    btn_saved_monthes.pack()

    btn_add_month = Button(month_menu, text="Add month",  width=30, height=5, bg="white", fg="black", command=add_month)
    btn_add_month.pack()

    btn_exit = Button(month_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_month)
    btn_exit.pack()

    month_menu.mainloop()


def click_plan_day_fast():
    d = int(entry_day_plan.get())
    m = int(entry_mon_plan.get())
    y = int(entry_year_plan.get())
    text_to_add = entry_text_plan.get()
    dir_path = dirname(__file__) + '/data/tracker/'
    file_name = d_mon[m] + str(y) + ".txt"
    file_path = dir_path + file_name
    if exists(file_path) == False:
        with open(file_path, "w") as fd:
            fd.write(f'{d_mon[m]} {y}\n')
            fd.write("0\n")
            fd.write(str(monthrange(int(y), m)[1]))
            fd.write("\n")
    dir_path = dirname(__file__) + '/data/plans/'
    file_name = d_mon[m] + str(y) + ".txt"
    file_path = dir_path + file_name
    if exists(file_path) == False:
        with open(file_path, "w") as fd:
            fd.write(f'{d_mon[m]} {y}\n')
            fd.write("0\n")
            fd.write(str(monthrange(int(y), m)[1]))
            fd.write("\n")
    add_text_in_file(file_path, text_to_add, d)


def fast_adding():
    main_menu.destroy()
    global fast_adding_menu
    fast_adding_menu = Tk()
    fast_adding_menu.geometry('400x800')

    data_day = StringVar()
    data_day.set('Day:')
    lbl_day = Label(fast_adding_menu, textvariable=data_day)
    lbl_day.pack()
    global entry_day_plan
    entry_day_plan = Entry(fast_adding_menu)
    entry_day_plan.pack()

    data_mon = StringVar()
    data_mon.set('Month number:')
    lbl_mon = Label(fast_adding_menu, textvariable=data_mon)
    lbl_mon.pack()
    global entry_mon_plan
    entry_mon_plan = Entry(fast_adding_menu)
    entry_mon_plan.pack()

    data_year = StringVar()
    data_year.set('Year:')
    lbl_year = Label(fast_adding_menu, textvariable=data_year)
    lbl_year.pack()
    global entry_year_plan
    entry_year_plan = Entry(fast_adding_menu)
    entry_year_plan.pack()

    data_text = StringVar()
    data_text.set('Plans to add:')
    lbl_text = Label(fast_adding_menu, textvariable=data_text)
    lbl_text.pack()
    global entry_text_plan
    entry_text_plan = Entry(fast_adding_menu)
    entry_text_plan.pack()

    btn_plan_day = Button(fast_adding_menu, text="Add", width=11, height=3, bg="white", fg="black", command=click_plan_day_fast)
    btn_plan_day.pack()

    btn_exit = Button(fast_adding_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_fast_adding)
    btn_exit.pack()
    fast_adding_menu.mainloop()


def help():
    main_menu.destroy()
    global help_menu
    help_menu = Tk()
    help_menu.geometry('1255x800')

    lbl_help = Label(help_menu, text="Manual")
    lbl_help.pack()

    file_path = dirname(__file__) + "/help_manual.txt"
    with open(file_path, "r") as fd:
        lines = fd.readlines()
        manual_out = "\n".join(lines)

    lbl_text = Label(help_menu, text=manual_out)
    lbl_text.pack()

    btn_exit = Button(help_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_help)
    btn_exit.pack()
    help_menu.mainloop()


def exit():
    main_menu.destroy()


def main():
    global main_menu
    main_menu = Tk()
    main_menu.geometry('400x800')

    btn_day = Button(main_menu, text="Plans for the day", width=30, height=5, bg="white", fg="black", command=day)
    btn_day.pack()

    btn_hast_adding = Button(main_menu, text="Fast adding plans", width=30, height=5, bg="white", fg="black", command=fast_adding)
    btn_hast_adding.pack()

    btn_month = Button(main_menu, text="Schedule", width=30, height=5, bg="white", fg="black", command=month)
    btn_month.pack()

    btn_help = Button(main_menu, text="Help, click for information",  width=30, height=5, bg="white", fg="black", command=help)
    btn_help.pack()

    btn_exit = Button(main_menu, text="Exit",  width=7, height=4, bg="salmon1", fg="black", command=exit)
    btn_exit.pack()

    main_menu.mainloop()


def parse_tracker_input_file(lines):
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

        self.menu_frame = Frame(master=self)
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
        self.btn_stats = Button(master=self.menu_frame, text='Show additional statistics', height=1, command=self.showStats)
        self.btn_stats.grid(row=0, column=4, sticky='w')
        self.btn_save = Button(master=self.menu_frame, text='Save', height=1, command=self.saveData)
        self.btn_save.grid(row=0, column=5, sticky='w')

        self.tracker_frame = Frame(master=self)
        self.tracker_frame.pack(fill=X)

        with open(filename) as input_file:
            input_file_lines = input_file.readlines()
        self.month_name, self.days_number, self.habits_names, self.ticks_matrix = parse_tracker_input_file(input_file_lines)

        self.title(self.month_name)
        self.habitlabel_list = []
        for i in range(len(self.habits_names)):
            lbl = Label(master=self.tracker_frame, text=self.habits_names[i], height=1)
            self.habitlabel_list.append(lbl)
            lbl.grid(row=i+1, column=0, sticky='e')
        for i in range(self.days_number):
            lbl = Label(master=self.tracker_frame, text=str(i+1), height=1)
            lbl.grid(row=0, column=i+1)
        self.checkbutton_matrix = []
        for i in range(len(self.habits_names)):
            self.checkbutton_matrix.append([])
            for j in range(self.days_number):
                cb = Checkbutton(master=self.tracker_frame, command=partial(self.changeState, coords=(i, j)))
                self.checkbutton_matrix[i].append(cb)
                cb.grid(row=i+1, column=j+1)

        for i in range(len(self.habits_names)):
            for j in range(self.days_number):
                if self.ticks_matrix[i][j]:
                    self.checkbutton_matrix[i][j].select()

        habitsum_list, daysum_list = calc_ticks_numbers(self.ticks_matrix)
        if daysum_list == -1:
            habitsum_list = []
            daysum_list = [0 for _ in range(self.days_number)]
        self.daysumlabel_list = []
        self.habitsumlabel_list = []
        for i in range(self.days_number):
            lbl = Label(master=self.tracker_frame, text=str(daysum_list[i]), height=1)
            self.daysumlabel_list.append(lbl)
            lbl.grid(row=len(self.habits_names)+1, column=i+1)
        for i in range(len(self.habits_names)):
            lbl = Label(master=self.tracker_frame, text=str(habitsum_list[i]), height=1)
            self.habitsumlabel_list.append(lbl)
            lbl.grid(row=i+1, column=self.days_number+1, sticky='e')

    def showStats(self):
        statswindow = StatsWindow(self)
        statswindow.grab_set()
        statswindow.stats(self.habits_names, self.ticks_matrix)

    def changeState(self, coords):
        i, j = coords
        if self.ticks_matrix[i][j]:
            self.daysumlabel_list[j]['text'] = str(int(self.daysumlabel_list[j]['text']) - 1)
            self.habitsumlabel_list[i]['text'] = str(int(self.habitsumlabel_list[i]['text']) - 1)
        else:
            self.daysumlabel_list[j]['text'] = str(int(self.daysumlabel_list[j]['text']) + 1)
            self.habitsumlabel_list[i]['text'] = str(int(self.habitsumlabel_list[i]['text']) + 1)
        self.ticks_matrix[i][j] = not self.ticks_matrix[i][j]

    def addHabit(self):
        possible_habit_name = self.ent_add.get()
        if possible_habit_name and possible_habit_name not in self.habits_names:
            self.habits_names.append(possible_habit_name)
            lbl = Label(master=self.tracker_frame, text=self.habits_names[-1], height=1)
            self.habitlabel_list.append(lbl)
            lbl.grid(row=len(self.habits_names), column=0, sticky='e')
            self.ticks_matrix.append([False for _ in range(self.days_number)])
            self.checkbutton_matrix.append([])
            i = len(self.habits_names)
            for j in range(self.days_number):
                cb = Checkbutton(master=self.tracker_frame, command=partial(self.changeState, coords=(i - 1, j)))
                self.checkbutton_matrix[-1].append(cb)
                cb.grid(row=i, column=j+1)
            k = 0
            for widget in self.daysumlabel_list:
                widget.grid_forget()
                widget.grid(row=i+1, column=k+1)
                k += 1
            lbl = Label(master=self.tracker_frame, text='0', height=1)
            self.habitsumlabel_list.append(lbl)
            lbl.grid(row=i, column=self.days_number+1, sticky='e')
            
    def delHabit(self):
        possible_habit_name = self.ent_del.get()
        if possible_habit_name in self.habits_names:
            del_idx = self.habits_names.index(possible_habit_name)
            self.habits_names.pop(del_idx)
            self.habitlabel_list[del_idx].destroy()
            self.habitlabel_list.pop(del_idx)
            for i in range(self.days_number):
                if self.ticks_matrix[del_idx][i]:
                    self.daysumlabel_list[i]['text'] = str(int(self.daysumlabel_list[i]['text']) - 1)
            self.habitsumlabel_list[del_idx].destroy()
            self.habitsumlabel_list.pop(del_idx)
            self.ticks_matrix.pop(del_idx)
            for widget in self.checkbutton_matrix[del_idx]:
                widget.destroy()
            self.checkbutton_matrix.pop(del_idx)
            for i in range(del_idx, len(self.habits_names)):
                self.habitlabel_list[i].grid_forget()
                self.habitlabel_list[i].grid(row=i+1, column=0, sticky='e')
                for j in range(self.days_number):
                    self.checkbutton_matrix[i][j].grid_forget()
                    self.checkbutton_matrix[i][j].grid(row=i+1, column=j+1)
                self.habitsumlabel_list[i].grid_forget()
                self.habitsumlabel_list[i].grid(row=i+1, column=self.days_number+1, sticky='e')
            k = 0
            for widget in self.daysumlabel_list:
                widget.grid_forget()
                widget.grid(row=len(self.habits_names)+1, column=k+1)
                k += 1

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


class StatsWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.resizable(width=False, height=False)
        self.title(parent.month_name + ': Additional statistics')

        self.popular_frame = Frame(master=self)
        self.popular_frame.pack(fill=X)
        self.lbl_most_popular_day = Label(master=self.popular_frame, text='Day with most habits achieved:', height=1)
        self.lbl_most_popular_day.grid(row=0, column=0, sticky='e')
        self.lbl_least_popular_day = Label(master=self.popular_frame, text='Day with least habits achieved:', height=1)
        self.lbl_least_popular_day.grid(row=1, column=0, sticky='e')
        self.lbl_most_popular_habit = Label(master=self.popular_frame, text='Habit achieved most frequent:', height=1)
        self.lbl_most_popular_habit.grid(row=2, column=0, sticky='e')
        self.lbl_least_popular_habit = Label(master=self.popular_frame, text='Habit achieved least frequent:', height=1)
        self.lbl_least_popular_habit.grid(row=3, column=0, sticky='e')

    def stats(self, habits_names, ticks_matrix):
        most_popular_lists = calc_most_popular(ticks_matrix)
        least_popular_lists = calc_least_popular(ticks_matrix)
        self.lbl_most_popular_day_answer = Label(master=self.popular_frame, text=', '.join([str(i + 1) for i in most_popular_lists[1]]), height=1)
        self.lbl_most_popular_day_answer.grid(row=0, column=1, sticky='w')
        self.lbl_least_popular_day_answer = Label(master=self.popular_frame, text=', '.join([str(i + 1) for i in least_popular_lists[1]]), height=1)
        self.lbl_least_popular_day_answer.grid(row=1, column=1, sticky='w')
        self.lbl_most_popular_habit_answer = Label(master=self.popular_frame, text=', '.join([habits_names[i] for i in most_popular_lists[0]]), height=1)
        self.lbl_most_popular_habit_answer.grid(row=2, column=1, sticky='w')
        self.lbl_least_popular_habit_answer = Label(master=self.popular_frame, text=', '.join([habits_names[i] for i in least_popular_lists[0]]), height=1)
        self.lbl_least_popular_habit_answer.grid(row=3, column=1, sticky='w')
        self.wait_window()
