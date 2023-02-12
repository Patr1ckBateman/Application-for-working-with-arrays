import tkinter
from Derictory import average, median, find_max, find_min, amount, multiplication


def calculate():
    numbers = list(map(float, entry.get().split()))

    label_average['text'] = f'Среднее: {average(numbers)}'
    label_median['text'] = f'Медиана: {median(numbers)}'
    label_max_value['text'] = f'Макс. значение: {find_max(numbers)}'
    label_min_value['text'] = f'Мин. значение: {find_min(numbers)}'
    label_amount['text'] = f'Сумма чисел: {amount(numbers)}'
    label_multiplication['text'] = f'Произведение чисел: {multiplication(numbers)}'


"""Окно"""
window = tkinter.Tk()
window.title('Работа с массивами')
window.geometry('350x450')
window.resizable(False, False)


"""Заголовоки"""
label_main = tkinter.Label(text='Введите числа', font=('Arial', 16), fg='black')
label_main.place(relx=0.5, y=10, anchor='n')

label_average = tkinter.Label(text='Среднее:', font=('Arial', 12), fg='black')
label_average.place(relx=0.05, y=140, anchor='w')

label_median = tkinter.Label(text='Медиана:', font=('Arial', 12), fg='black')
label_median.place(relx=0.05, y=160, anchor='w')

label_max_value = tkinter.Label(text='Макс. значение:', font=('Arial', 12), fg='black')
label_max_value.place(relx=0.05, y=180, anchor='w')

label_min_value = tkinter.Label(text='Мин. значение:', font=('Arial', 12), fg='black')
label_min_value.place(relx=0.05, y=200, anchor='w')

label_amount = tkinter.Label(text='Сумма чисел:', font=('Arial', 12), fg='black')
label_amount.place(relx=0.05, y=220, anchor='w')

label_multiplication = tkinter.Label(text='Произведение чисел:', font=('Arial', 12), fg='black')
label_multiplication.place(relx=0.05, y=240, anchor='w')


"""Поле ввода"""
entry = tkinter.Entry(font=('Arial', 12), width=30)
entry.place(relx=0.5, y=50, anchor='n')


"""Кнопка действия"""
button = tkinter.Button(text='Вычислить',font='Arial', bg='white', fg='black', width=10, height=1, command=calculate)
button.place(relx=0.5, y=80, anchor='n')

window.mainloop()

