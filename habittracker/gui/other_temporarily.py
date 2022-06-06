from tkinter import Tk, Label, Button, StringVar, Entry
from calendar import monthrange
from os import listdir


def to_menu_day():
    day_menu.destroy()
    main()


def to_menu_hab():
    hab_menu.destroy()
    main()


def to_menu_help():
    help_menu.destroy()
    main()


def to_menu_week():
    week_menu.destroy()
    main()


def to_menu_month():
    month_menu.destroy()
    main()


def to_menu_mon():
    mon_menu.destroy()
    main()


def to_menu_tue():
    tue_menu.destroy()
    main()


def to_menu_wed():
    wed_menu.destroy()
    main()


def to_menu_thu():
    thu_menu.destroy()
    main()


def to_menu_fri():
    fri_menu.destroy()
    main()


def to_menu_sat():
    sat_menu.destroy()
    main()


def to_menu_sun():
    sun_menu.destroy()
    main()

def to_menu_saved_monthes():
    saved_monthes_menu.destroy()
    main()


def to_menu_add_month():
    add_month_menu.destroy()
    main()


def add_plan():
    print("Adding function")


def day():
    main_menu.destroy()
    global day_menu
    day_menu = Tk()
    day_menu.geometry('400x800')

    lbl_date = Label(day_menu, text="Здесь вывод даты")
    lbl_date.pack()
    btn_add_info = Button(day_menu, text="Add plan in this day", width=30, height=5, bg="white", fg="black", command=add_plan)
    btn_add_info.pack()
    btn_exit = Button(day_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_day)
    btn_exit.pack()
    day_menu.mainloop()


def day_mon():
    week_menu.destroy()
    global mon_menu
    mon_menu = Tk()
    mon_menu.geometry('400x800')

    lbl_date = Label(mon_menu, text="Здесь вывод даты и дня недели")
    lbl_date.pack()
    btn_add_info = Button(mon_menu, text="Add plan in this day",  width=30, height=5, bg="white", fg="black", command=add_plan)
    btn_add_info.pack()
    btn_exit = Button(mon_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_mon)
    btn_exit.pack()
    mon_menu.mainloop()


def day_tue():
    week_menu.destroy()
    global tue_menu
    tue_menu = Tk()
    tue_menu.geometry('400x800')

    lbl_date = Label(tue_menu, text="Здесь вывод даты и дня недели")
    lbl_date.pack()
    btn_add_info = Button(tue_menu, text="Add plan in this day",  width=30, height=5, bg="white", fg="black", command=add_plan)
    btn_add_info.pack()
    btn_exit = Button(tue_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_tue)
    btn_exit.pack()
    tue_menu.mainloop()


def day_wed():
    week_menu.destroy()
    global wed_menu
    wed_menu = Tk()
    wed_menu.geometry('400x800')

    lbl_date = Label(wed_menu, text="Здесь вывод даты и дня недели")
    lbl_date.pack()
    btn_add_info = Button(wed_menu, text="Add plan in this day",  width=30, height=5, bg="white", fg="black", command=add_plan)
    btn_add_info.pack()
    btn_exit = Button(wed_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_wed)
    btn_exit.pack()
    wed_menu.mainloop()


def day_thu():
    week_menu.destroy()
    global thu_menu
    thu_menu = Tk()
    thu_menu.geometry('400x800')

    lbl_date = Label(thu_menu, text="Здесь вывод даты и дня недели")
    lbl_date.pack()
    btn_add_info = Button(thu_menu, text="Add plan in this day",  width=30, height=5, bg="white", fg="black", command=add_plan)
    btn_add_info.pack()
    btn_exit = Button(thu_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_thu)
    btn_exit.pack()
    thu_menu.mainloop()


def day_fri():
    week_menu.destroy()
    global fri_menu
    fri_menu = Tk()
    fri_menu.geometry('400x800')

    lbl_date = Label(fri_menu, text="Здесь вывод даты и дня недели")
    lbl_date.pack()
    btn_add_info = Button(fri_menu, text="Add plan in this day",  width=30, height=5, bg="white", fg="black", command=add_plan)
    btn_add_info.pack()
    btn_exit = Button(fri_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_fri)
    btn_exit.pack()
    fri_menu.mainloop()


def day_sat():
    week_menu.destroy()
    global sat_menu
    sat_menu = Tk()
    sat_menu.geometry('400x800')

    lbl_date = Label(sat_menu, text="Здесь вывод даты и дня недели")
    lbl_date.pack()
    btn_add_info = Button(sat_menu, text="Add plan in this day",  width=30, height=5, bg="white", fg="black", command=add_plan)
    btn_add_info.pack()
    btn_exit = Button(sat_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_sat)
    btn_exit.pack()
    sat_menu.mainloop()


def day_sun():
    week_menu.destroy()
    global sun_menu
    sun_menu = Tk()
    sun_menu.geometry('400x800')

    lbl_date = Label(sun_menu, text="Здесь вывод даты и дня недели")
    lbl_date.pack()
    btn_add_info = Button(sun_menu, text="Add plan in this day",  width=30, height=5, bg="white", fg="black", command=add_plan)
    btn_add_info.pack()
    btn_exit = Button(sun_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_sun)
    btn_exit.pack()
    sun_menu.mainloop()


def week():
    main_menu.destroy()
    global week_menu
    week_menu = Tk()
    week_menu.geometry('400x800')

    lbl_date = Label(week_menu, text="Здесь вывод даты")
    lbl_date.pack()

    btn_mon = Button(week_menu, text="Monday", width=30, height=5, bg="white", fg="black", command=day_mon)
    btn_mon.pack()

    btn_tue = Button(week_menu, text="Tuesday", width=30, height=5, bg="white", fg="black", command=day_tue)
    btn_tue.pack()

    btn_wed = Button(week_menu, text="Wednesday", width=30, height=5, bg="white", fg="black", command=day_wed)
    btn_wed.pack()

    btn_thu = Button(week_menu, text="Thursday", width=30, height=5, bg="white", fg="black", command=day_thu)
    btn_thu.pack()

    btn_fri = Button(week_menu, text="Friday", width=30, height=5, bg="white", fg="black", command=day_fri)
    btn_fri.pack()

    btn_sat = Button(week_menu, text="Saturday", width=30, height=5, bg="white", fg="black", command=day_sat)
    btn_sat.pack()

    btn_sun = Button(week_menu, text="Sunday", width=30, height=5, bg="white", fg="black", command=day_sun)
    btn_sun.pack()

    btn_exit = Button(week_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_week)
    btn_exit.pack()

    week_menu.mainloop()


def saved_monthes():
    month_menu.destroy()
    global saved_monthes_menu
    saved_monthes_menu = Tk()
    saved_monthes_menu.geometry('400x800')

    dirrectory = './habittracker/data/months'
    files_indir = listdir(dirrectory)
    files_indir.remove('.DS_Store')
    files = []
    for i in files_indir:
        files.append(i[0:-4])
    all_files = "\n".join(files)

    btn_exit = Button(saved_monthes_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_saved_monthes)
    btn_exit.pack()

    saved_monthes_menu.mainloop()


def click_year():
    global text_year 
    text_year = entry_year.get() 


def click_mon():
    d_mon = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june', 7:'july', 8:'august', 9:'september', 10:'october', 11:'november', 12:'december'}
    text_mon = int(entry_mon.get())
    file_path = "./habittracker/data/months/"
    file_path += d_mon[text_mon]
    file_path += text_year
    file_path += ".txt"
    with open(file_path, "w") as fd:
        fd.write(f'{d_mon[text_mon]} {text_year}\n')
        fd.write("0\n")
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

    lbl_month = Label(month_menu, text="Здесь должен быть написан месяц")
    lbl_month.pack()

    lbl_date = Label(month_menu, text="Введите число")
    lbl_date.pack()

    btn_saved_monthes = Button(month_menu, text="Saved monthes",  width=30, height=5, bg="white", fg="black", command=saved_monthes)
    btn_saved_monthes.pack()

    btn_add_month = Button(month_menu, text="Add month",  width=30, height=5, bg="white", fg="black", command=add_month)
    btn_add_month.pack()

    btn_exit = Button(month_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_month)
    btn_exit.pack()

    month_menu.mainloop()


def hab_tr():
    main_menu.destroy()
    global hab_menu
    hab_menu = Tk()
    hab_menu.geometry('400x800')

    lbl_help = Label(hab_menu, text="Здесь делаем вывод по трекеру")
    lbl_help.pack()
    btn_exit = Button(hab_menu, text="To menu",  width=30, height=5, bg="salmon1", fg="black", command=to_menu_hab)
    btn_exit.pack()
    hab_menu.mainloop()


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

    btn_week = Button(main_menu, text="Week schedule", width=30, height=5, bg="white", fg="black", command=week)
    btn_week.pack()

    btn_month = Button(main_menu, text="Monthly schedule", width=30, height=5, bg="white", fg="black", command=month)
    btn_month.pack()

    btn_hab_tr = Button(main_menu, text="Habit tracker", width=0, height=5, bg="cyan", fg="black", command=hab_tr)
    btn_hab_tr.pack()

    btn_help = Button(main_menu, text="Help, click for information",  width=30, height=5, bg="white", fg="black", command=help)
    btn_help.pack()

    btn_exit = Button(main_menu, text="Exit",  width=7, height=4, bg="salmon1", fg="black", command=exit)
    btn_exit.pack()

    main_menu.mainloop()
