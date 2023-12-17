import tkinter as tk
import re
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN
from sympy import Symbol


def calculate():
    equation = calculator.entry.get()
    equation = re.sub(r"\s+", "", equation)  # Удаляем пробелы и разделители тысяч

    # Заменяем запятые на точки для десятичного разделителя
    equation = equation.replace(",", ".")

    try:
        result = eval_equation(equation)
        rounding_method = calculator.rounding_method.get()

        if rounding_method == "Математическое округление":
            rounded_result = round_decimal(result)
            calculator.result_label.config(text=f"Результат: {result} (исходный), {rounded_result} (математическое округление)")

        elif rounding_method == "Бухгалтерское округление":
            rounded_result = accountant_round(result)
            calculator.result_label.config(text=f"Результат: {result} (исходный), {rounded_result} (бухгалтерское округление)")

        elif rounding_method == "Усечение":
            truncated_result = truncate_decimal(result)
            calculator.result_label.config(text=f"Результат: {result} (исходный), {truncated_result} (усечение)")

    except Exception:
        calculator.result_label.config(text="Ошибка: Неверный формат уравнения")

def eval_equation(equation):
    x = Symbol('x')
    result = eval(equation)

    return result

def handle_paste(event):
    text = root.clipboard_get()
    calculator.entry.insert(tk.INSERT, text)

def round_decimal(num):
    rounded_num = Decimal(num).quantize(Decimal('0.0'), rounding=ROUND_HALF_UP)
    return rounded_num

def accountant_round(num):
    rounded_num = Decimal(num).quantize(Decimal('0.0'), rounding=ROUND_HALF_UP)
    return rounded_num

def truncate_decimal(num):
    truncated_num = Decimal(num).quantize(Decimal('0.0'), rounding=ROUND_DOWN)
    return truncated_num

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("400x350")
        self.root.resizable(True, True)  # Масштабируемое окно

        self.label_info = tk.Label(self.root, text="ФИО: Шибко Татьяна Александровна\nКурс: 3\nГруппа: 12\nГод: 2023")
        self.label_info.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.entry.bind("<Control-v>", handle_paste)

        self.calculate_button = tk.Button(self.root, text="Вычислить", command=calculate)
        self.calculate_button.pack()

        self.rounding_method = tk.StringVar()
        self.rounding_method.set("Математическое округление")
        self.rounding_options = ["Математическое округление", "Бухгалтерское округление", "Усечение"]
        self.rounding_dropdown = tk.OptionMenu(self.root, self.rounding_method, *self.rounding_options)
        self.rounding_dropdown.pack()

        self.result_label = tk.Label(self.root, text="Результат: ")
        self.result_label.pack()

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()