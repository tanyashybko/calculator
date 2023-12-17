import re
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("400x300")
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
        self.radio_multiply = tk.Radiobutton(self.root, text="Умножение", variable=self.var_operation, value="*")
        self.radio_multiply.pack()
        self.radio_divide = tk.Radiobutton(self.root, text="Деление", variable=self.var_operation, value="/")
        self.radio_divide.pack()

        self.button_calculate = tk.Button(self.root, text="Вычислить", command=self.calculate)
        self.button_calculate.pack()

        self.entry_num1.bind("<Control-v>", self.paste_text)  # Обработчик вставки

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
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Ошибка", "Деление на 0 невозможно")
                return
            result = num1 / num2

        result_str = "{:,.6f}".format(result)  # Форматируем результат с разделителями тысяч и 6 знаками после запятой
        result_str = result_str.replace(",", " ").replace(".", ",")
        result_str = result_str.replace(",", " ").replace(".", ",")  # Заменяем разделитель целой и дробной части

        messagebox.showinfo("Результат", f"Результат: {result_str}")

    def paste_text(self, event):
        widget = event.widget
        widget.insert(tk.INSERT, self.root.clipboard_get())

    @staticmethod
    def is_valid_number(number):
        return bool(re.match(r'^[-+]?(?:\d{1,3}(?:\s\d{3})*|\d+)(?:[\.,]\d+)?$', number.replace(" ", "")))

    @staticmethod
    def convert_decimal_separator(number):
        return number.replace(",", ".").replace(" ", "")



if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
