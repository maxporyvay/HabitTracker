from tkinter import Tk, Label, Button, StringVar, Entry, IntVar, Radiobutton
from calendar import monthrange
from os import listdir
from datetime import date
from os.path import exists

d_mon = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june', 7:'july', 8:'august', 9:'september', 10:'october', 11:'november', 12:'december'}

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


def add_plan_day():
    print("func add")

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
        if i >= 'a' and i <= 'z':
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
        print("Что-то не так")
    dir_path = "./habittracker/plans/months/"
    file_name = d_mon[mon] + str(year) + ".txt"
    file_full_name = dir_path + file_name
    if exists(file_full_name) == False:
        lbl_out = Label(show_plan_menu, text="Задачи не запланированы")
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
                plans.append("Задачи не запланированы")
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
    print("in trek")
    #в строке s - имя файла по принципу jule2022 без .txt 

def info_plans(s):
    global month_info
    month_info = s
    info_plans_menu.destroy()
    global show_plans_menu
    show_plans_menu = Tk()
    show_plans_menu.geometry('400x800')

    data_day = StringVar()
    data_day.set('Введите число')
    lbl_mon = Label(show_plans_menu, textvariable=data_day)
    lbl_mon.pack()
    global day_plans
    day_plans = Entry(show_plans_menu)
    day_plans.pack()
    btn_choise = Button(show_plans_menu, text="Ввести", width=11, height=3, bg="white", fg="black", command=click_show_plans)
    btn_choise.pack()

    btn_exit = Button(show_plans_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_show_plans)
    btn_exit.pack()
    show_plans_menu.mainloop()

    """
   
    вызвать какую-то функцию где закроется данное окно и откроется show_plan(день,месяц, год)
    """

def click_plans():
    text_choise_mon = mon_plans.get() 
    if flag_tr0_plans1 == 0:
        info_tr(text_choise_mon)
    elif flag_tr0_plans1 == 1:
        info_plans(text_choise_mon)


def view_info():
    saved_monthes_menu.destroy()
    global info_plans_menu
    info_plans_menu = Tk()
    info_plans_menu.geometry('400x800')

    dirrectory = './habittracker/data/months'
    files_indir = listdir(dirrectory)
    files_indir.remove('.DS_Store')
    files = []
    files.append("Доступные месяцы:")
    for i in files_indir:
        files.append(i[0:-4])
    all_files = "\n".join(files)

    lbl_files = Label(info_plans_menu, text=all_files)
    lbl_files.pack()

    dir_path = "./habittracker/plans/months/"

    data_mon = StringVar()
    data_mon.set('Введите выбранный месяц, в формате, как он записан выше')

    lbl_mon = Label(info_plans_menu, textvariable=data_mon)
    lbl_mon.pack()

    global mon_plans
    mon_plans = Entry(info_plans_menu)
    mon_plans.pack()

    btn_choise = Button(info_plans_menu, text="выбрать", width=11, height=3, bg="white", fg="black", command=click_plans)
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

    dirrectory = './habittracker/data/months'
    files_indir = listdir(dirrectory)
    files_indir.remove('.DS_Store')
    files = []
    files.append("Доступные месяцы:")
    for i in files_indir:
        files.append(i[0:-4])
    all_files = "\n".join(files)

    lbl_files = Label(saved_monthes_menu, text=all_files)
    lbl_files.pack()

    lbl_choise = Label(saved_monthes_menu, text="Нажмите на один из вариантов(даже если он выбран)")
    lbl_choise.pack()
    data = StringVar()
    data.set(0)
    rad_tr = Radiobutton(saved_monthes_menu, text = 'Треккер привычек', value = 0, variable = data, command = view_info_tr)
    rad_plans = Radiobutton(saved_monthes_menu, text = 'Планы', value = 1, variable = data, command = view_info_plans)
    rad_tr.pack()
    rad_plans.pack()

    btn_exit = Button(saved_monthes_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_saved_monthes)
    btn_exit.pack()

    saved_monthes_menu.mainloop()


def click_year():
    global text_year 
    text_year = entry_year.get() 


def click_mon():
    text_mon = int(entry_mon.get())
    file_path = "./habittracker/data/months/"
    file_path += d_mon[text_mon]
    file_path += text_year
    file_path += ".txt"
    with open(file_path, "w") as fd:
        fd.write(f'{d_mon[text_mon]} {text_year}\n')
        fd.write("0\n")
        fd.write(str(monthrange(int(text_year), text_mon)[1]))

    plan_path = "./habittracker/plans/months/"
    plan_path += d_mon[text_mon]
    plan_path += text_year
    plan_path += ".txt"
    with open(plan_path, "w") as fd:
        fd.write(f'{d_mon[text_mon]} {text_year}\n')
        fd.write(str(monthrange(int(text_year), text_mon)[1]))


def add_month():
    month_menu.destroy()
    global add_month_menu
    add_month_menu = Tk()
    add_month_menu.geometry('400x800')

    data_year = StringVar()
    data_year.set('Введите год добавляемого месяца')

    lbl_year = Label(add_month_menu, textvariable=data_year)
    lbl_year.pack()

    global entry_year
    entry_year = Entry(add_month_menu)
    entry_year.pack()

    btn_year = Button(add_month_menu, text="добавить год", width=11, height=3, bg="white", fg="black", command=click_year)
    btn_year.pack()

    data_mon = StringVar()
    data_mon.set('Введите номер добавляемого месяца месяца')

    lbl_mon = Label(add_month_menu, textvariable=data_mon)
    lbl_mon.pack()

    global entry_mon
    entry_mon = Entry(add_month_menu)
    entry_mon.pack()

    btn_mon = Button(add_month_menu, text="добавить месяц", width=11, height=3, bg="white", fg="black", command=click_mon)
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


def help():
    main_menu.destroy()
    global help_menu
    help_menu = Tk()
    help_menu.geometry('400x800')

    lbl_help = Label(help_menu, text="Здесь делаем вывод всего мануала")
    lbl_help.pack()
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

    btn_month = Button(main_menu, text="Schedule", width=30, height=5, bg="white", fg="black", command=month)
    btn_month.pack()

    btn_help = Button(main_menu, text="Help, click for information",  width=30, height=5, bg="white", fg="black", command=help)
    btn_help.pack()

    btn_exit = Button(main_menu, text="Exit",  width=7, height=4, bg="salmon1", fg="black", command=exit)
    btn_exit.pack()

    main_menu.mainloop()
