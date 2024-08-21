# Лабораторная работа №4
# Баранов Николай ИУ7-25Б


from tkinter import *
from tkinter import messagebox as box
from math import pi
import matplotlib.pyplot as plt
import numpy as np
import webbrowser


def main():
    window = Tk()
    window.geometry("700x700")
    window.resizable(width=False, height=False)
    window.title("Рисуем кружки:)")
    
    photos = [PhotoImage(file = f"images/{i}.png") for i in range(11)]
    middle_image = 4
    
    dots = list()
    was = dict()
    sizes = list()
    
    background = Canvas(window, width=700, height=700)
    background.pack(fill="both", expand=True)
    background.create_image(0, 0, image=photos[middle_image], anchor="nw")
    curr = middle_image
    
    label_new = Label(window, bg='#ff81f3', font='Ubuntu 24', fg='#000000', text='Новая точка', width=12)
    label_new.place(x=30, y=100)
    x_label = Label(window, bg='#ff81f3', font='Ubuntu 24', fg='#000000', text='X', width=1)
    x_label.place(x=30, y=150)
    x_entry = Entry(window, bg='#ff81f3', font='Ubuntu 24', fg='#000000', width=10)
    x_entry.place(x=64, y=150)
    y_label = Label(window, bg='#ff81f3', font='Ubuntu 24', fg='#000000', text='Y', width=1)
    y_label.place(x=30, y=200)
    y_entry = Entry(window, bg='#ff81f3', font='Ubuntu 24', fg='#000000', width=10)
    y_entry.place(x=64, y=200)
    add_button = Button(window, bg='#ff81f3', font='Ubuntu 21', fg='#000000', text='Добавить', width=12)
    add_button.place(x=30, y=250)
    label_dots = Label(window, bg='#ff81f3', font='Ubuntu 24', fg='#000000', text='Точек: 0', width=12)
    label_dots.place(x=30, y=300)
    
    label_r = Label(window, bg='#ff81f3', font='Ubuntu 24', fg='#000000', text='Радиус', width=12)
    label_r.place(x=30, y=400)
    r_label = Label(window, bg='#ff81f3', font='Ubuntu 24', fg='#000000', text='R', width=1)
    r_label.place(x=30, y=450)
    r_entry = Entry(window, bg='#ff81f3', font='Ubuntu 24', fg='#000000', width=10)
    r_entry.place(x=64, y=450)
    end_button = Button(window, bg='#ff81f3', font='Ubuntu 21', fg='#000000', text='График', width=12)
    end_button.place(x=30, y=500)
    
    reset_button = Button(window, bg='#ff81f3', font='Ubuntu 21', fg='#000000', text='Сбросить', width=12)
    reset_button.place(x=30, y=600)
    
    def change(ban=True):
        nonlocal curr, middle_image
        if ban:
            if curr > middle_image:
                curr = middle_image
            else:
                curr -= 1
            if curr == -1:
                killer()
        else:
            if curr < middle_image:
                curr = middle_image
            elif curr < 8:
                curr += 1
        background.create_image(0, 0, image=photos[curr], anchor="nw")
    
    def add_button_func():
        x = check(x_entry.get())
        y = check(y_entry.get())
        if x is None or y is None:
            message = "Для просмотра правил ввода нажмите на кнопку 'Информация', расположенную в верхнем левом углу."
            if y is None:
                message = "Ошибка при получении значения Y!\n" + message
            if x is None:
                message = "Ошибка при получении значения X!\n" + message
            box.showerror("Ошибка", message)
            change()
            return
        if len(dots) == 20:
            message = "Нельзя вводить больше 20 точек!"
            box.showerror("Ошибка", message)
            change()
            return
        pair = (x, y)
        if x not in was:
            was[x] = set()
            was[x].add(y)
        else:
            if y in was[x]:
                message = "Нельзя вводить 2 одинаковые точки!"
                box.showerror("Ошибка", message)
                change()
                return
            was[x].add(y)
        sizes.append([])
        dots.append(pair)
        for i in range(len(sizes) - 1):
            val = ((x - dots[i][0]) ** 2 + (y - dots[i][1]) ** 2) ** 0.5
            sizes[i].append(val)
            sizes[len(sizes) - 1].append(val)
        sizes[len(sizes) - 1].append(0)
        x_entry.delete(0, END)
        y_entry.delete(0, END)
        label_dots['text'] = f'Точек: {len(dots)}'
        change(False)
        
    def end_button_func():
        if len(dots) < 2:
            message = "Количество точек должно быть не меньше 2!"
            box.showerror("Ошибка", message)
            change()
            return
        r = check(r_entry.get(), True)
        if r is None:
            message = "Ошибка при получении значения R!\n"
            message += "Для просмотра правил ввода нажмите на кнопку 'Информация', расположенную в верхнем левом углу."
            box.showerror("Ошибка", message)
            change()
            return
        counts = [0 for i in range(len(dots))]
        for i in range(len(dots)):
            for j in range(len(dots)):
                counts[i] += (sizes[i][j] <= r)
        for i in range(len(dots) - 1):
            for j in range(i + 1, len(dots)):
                if counts[i] == counts[j]:
                    generate(i, j, r)
                    return
        
    def generate(i, j, r):
        plot_graph(get_circle(dots[i][0], dots[i][1], r), get_circle(dots[j][0], dots[j][1], r), [i, j])
        
    def get_circle(x_0, y_0, r):
        t = np.linspace(0, 2 * pi, 360)
        x = np.cos(t)
        y = np.sin(t)
        for i in range(360):
            x[i] *= r
            x[i] += x_0
            y[i] *= r
            y[i] += y_0
        return [x, y]
        
    def plot_graph(circle_1, circle_2, centres):
        plt.figure(1, figsize=(8,8))
        plt.gcf().canvas.set_window_title("А вот и кружки:)")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.plot(circle_1[0], circle_1[1], 'r', label='Круги')
        plt.plot(circle_2[0], circle_2[1], 'r')
        x = []
        y = []
        for i in dots:
            x.append(i[0])
            y.append(i[1])
        plt.plot(x, y, 'g.', label='Точки')
        plt.plot([dots[centres[0]][0], dots[centres[1]][0]], [dots[centres[0]][1], dots[centres[1]][1]], 'b+', label='Центры кругов')
        plt.legend(loc=1)
        x.extend(circle_1[0].tolist())
        x.extend(circle_2[0].tolist())
        y.extend(circle_1[1].tolist())
        y.extend(circle_2[1].tolist())
        x = sorted(x)
        y = sorted(y)
        x0 = min(x)
        y0 = min(y)
        diff = max(max(x) - x0, max(y) - y0)
        xt = np.linspace(x0, x0 + diff, 5)
        yt = np.linspace(y0, y0 + diff, 5)
        plt.xticks(xt)
        plt.yticks(yt)
        plt.show()
        
    def restart():
        nonlocal dots, was, sizes, middle_image, curr
        dots = list()
        was = dict()
        sizes = list()
        label_dots['text'] = 'Точек: 0'
        if curr > middle_image:
            background.create_image(0, 0, image=photos[middle_image], anchor="nw")
            curr = middle_image
    
    def killer():
        window.bind('<Escape>', quit)
        nonlocal main_menu, curr
        label_new.destroy()
        x_label.destroy()
        x_entry.destroy()
        y_label.destroy()
        y_entry.destroy()
        add_button.destroy()
        label_dots.destroy()
        label_r.destroy()
        r_label.destroy()
        r_entry.destroy()
        end_button.destroy()
        reset_button.destroy()
        main_menu.destroy()
        background.create_image(0, 0, image=photos[9 + (curr == -1)], anchor="nw")
        window.geometry('1920x1080')
        window.attributes('-fullscreen', True)
        
    def showdots():
        message = "    X     Y"
        if len(dots) == 0:
            box.showinfo("Точки.", "Да кто такие эти ваши точки?")
            change()
        else:
            for x, y in dots:
                message += f"\n{x:>5d} {y:>5d}"
            box.showinfo("Точки.", message)
    
    main_menu = Menu(window)
    main_menu.add_command(label="Информация!", command=showinfo)
    main_menu.add_command(label="Введённые точки", command=showdots)
    lol = Menu(main_menu)
    lol.add_command(label="Не нажимать! Опасно для жизни!", command=rick_astley)
    lol.add_command(label="Нажми чтобы выиграть миллион рублей!", command=killer)
    main_menu.add_cascade(label='Не для пользователя;)', menu=lol)
    window.config(menu=main_menu)
    
    add_button['command'] = add_button_func
    end_button['command'] = end_button_func
    reset_button['command'] = restart
    
    window.mainloop()
    
    
def check(buf, is_natural=False):
    if len(buf) > 5 or len(buf) == 0:
        return None
    alpha = "0123456789"
    for i, sym in enumerate(buf):
        if sym in alpha:
            continue
        if i == 0 and sym in "+-" and not is_natural:
            continue
        return None
    ret = int(buf)
    if is_natural:
        if 0 < ret <= 1000:
            return ret
        return None
    if abs(ret) <= 1000:
        return ret
    return None  
    
    
def showinfo():
    label = """Автор: Баранов Николай.
Группа: ИУ7-25Б.
Программа по заданным точкам и радиусам строит 2 окружности, внутри которых содержится одинаковое количество точек.
Для добавления числа нужно ввести его координаты и нажать на кнопку "Добавить".
Координаты - целые числа, не превосходящие по модулю 1000.
Две точки с одинаковыми координатами вводить нельзя.
Для вывода графика нужно ввести радиус и нажать на кнопку "График".
Радиус - беззнаковое целое число, лежащее на отрезке [1, 1000].
Для сброса до начальных значений нажмите кнопку "Сбросить".
При вводе некорректных значений будут выводиться предупреждения.
Если делать это слишком часто, программа может прервать свою работу."""
    box.showinfo("Информация", label)


def rick_astley():
    webbrowser.get(using='firefox').open_new_tab('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
    
if __name__ == "__main__":
    main()
    
    
