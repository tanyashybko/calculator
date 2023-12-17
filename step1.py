import re
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x300")
        self.root.resizable(True, True)  # Масштабируемое окно

        self.label_info = tk.Label(self.root, text="ФИО: Шибко Татьяна Александровна\nКурс: 3\nГруппа: 12\nГод: 2023")
        self.label_info.pack()

        self.label_num1 = tk.Label(self.root, text="Введите первое число:")
        self.label_num1.pack()
        self.entry_num1 = tk.Entry(self.root)
        self.entry_num1.pack()

        self.label_num2 = tk.Label(self.root, text="Введите второе число:")
        self.label_num2.pack()
        self.entry_num2 = tk.Entry(self.root)
        self.entry_num2.pack()

        self.label_operation = tk.Label(self.root, text="Выберите операцию:")
        self.label_operation.pack()
        self.var_operation = tk.StringVar()
        self.var_operation.set("+")
        self.radio_add = tk.Radiobutton(self.root, text="Сложение", variable=self.var_operation, value="+")
        self.radio_add.pack()
        self.radio_subtract = tk.Radiobutton(self.root, text="Вычитание", variable=self.var_operation, value="-")
        self.radio_subtract.pack()

        self.button_calculate = tk.Button(self.root, text="Вычислить", command=self.calculate)
        self.button_calculate.pack()

        self.entry_num1.bind("<Control-v>", self.paste_text)  # Обработчик вставки

    def copy_text(self, event):
        widget = event.widget
        selected_text = widget.selection_get()
        self.root.clipboard_clear()
        self.root.clipboard_append(selected_text)

    def calculate(self):
        num1 = self.entry_num1.get()
        num2 = self.entry_num2.get()

        if not self.is_valid_number(num1) or not self.is_valid_number(num2):
            messagebox.showerror("Ошибка", "Введите корректные числа")
            return

        num1 = self.convert_decimal_separator(num1)
        num2 = self.convert_decimal_separator(num2)

        num1 = float(num1)
        num2 = float(num2)

        operation = self.var_operation.get()
        result = 0

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2

        if not self.is_within_range(result):
            messagebox.showinfo("Результат", "Переполнение")
        else:
            messagebox.showinfo("Результат", f"Результат: {result}")

    def paste_text(self, event):
        widget = event.widget
        widget.insert(tk.INSERT, self.root.clipboard_get())

    @staticmethod
    def is_valid_number(number):
        # Проверка на валидность числа
        return bool(re.match(r'^[-+]?[0-9]*[.,]?[0-9]+(?:[eE][-+]?[0-9]+)?$', number))


    @staticmethod
    def convert_decimal_separator(number):
        # Замена разделителя дробной части на точку
        return number.replace(",", ".")

    @staticmethod
    def is_within_range(number):
        # Проверка на превышение диапазона чисел
        return -1e12 <= number <= 1e12


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
    