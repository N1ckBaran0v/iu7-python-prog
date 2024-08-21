from tkinter import Tk, Menu, messagebox as box, Entry, Label, Button, END
# import matplotlib.pyplot as plt


class MyWindow(Tk): # Класс окна
    def __init__(self): # Создание окна и объектов на нём
        super().__init__()
        self.geometry("640x640")
        self.resizable(width=False, height=False)
        self.title("Методы уточнения корней.")
        self['bg'] = '#AAAAAA'
        self.main_menu = Menu(self)
        self.menu = Menu(self.main_menu)
        self.menu.add_command(label='Информация о программе и авторе', command=self.showinfo)
        self.menu.add_command(label='Информация о вводимых значениях', command=self.showdetails)
        self.menu.add_command(label='Ошибки при подсчёте', command=self.showerrors)
        self.menu.add_separator()
        self.main_menu.add_cascade(label='Меню', menu=self.menu)
        self.config(menu=self.main_menu)

        self.config_input()

    def config_input(self):
        self.geometry("305x305")
        self.labels = ["Введите функцию: ", \
                       "Введите a: ", \
                       "Введите b: ", \
                       "Введите h: ", \
                       "Введите Nmax: ", \
                       "Введите eps: "]
        self.Labels = [Label(self, text=self.labels[i], font='Courier 12', width=30).grid(row=2*i+1) for i in range(6)]
        self.input = [Entry(self, font='Courier 12', width=30).grid(row=2*i+2) for i in range(6)]
        self.button = Button(self, text="Вычислить", font='Courier 12', command=self.start)
        self.button.grid(row=13)

    def start(self, event):
        pass


    def showinfo(self): # Показать информацию об авторе и программе
        label = """Автор: Баранов Николай.
Группа: ИУ7-25Б.
Программа уточняет корни функции при помощи упрощённого метода Ньютона. \
Функция (при создании программы использовалась f(x) = x^3 - 7 * x^2 - 40 * x + 100) \
вписывается в программу заранее, как и её первые 2 производные.
На вход подаются границы отрезка, шаг поиска, точность, максимальное количество итераций. \
Если данные будут некорректными, будет выведен список ошибок при помщи специального сообщения об ошибке.
На выходе Пользователь получит таблицу с результатами, а также график функции на заданном отрезке."""
        box.showinfo("Информация", label)

    def showdetails(self): # Показать информацию о числах
        label = """a - левая раница отрезка;
b - правая граница отрезка;
h - ширина отрезков разбиения;
Nmax - максимальное число итераций;
eps - точность вычисления корня.
Ограничения:
a < b;
0 < eps < h;
Число отрезков разбиения не превышает 100;
h < 7 (чтобы 2 корня не лежали в 1 отрезке);
9 < Nmax < 100000;
Числа a, b, h и eps: целые или с плавающей точкой в нормальной форме;
Число Nmax только целое."""
        box.showinfo("Информация", label)

    def showerrors(self): # Показать информацию об ошибках подсчёта
        label = """0 - Подсчёт завершился успешно.
1 - Выход за границы отрезка.
2 - На отрезке есть точка, в которой производная равна 0.
3 - Превышено максимальное число итераций, а корень не был найден."""
        box.showinfo("Ошибки при подсчёте", label)
