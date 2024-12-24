import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def plot_dielectric_boundaries(kappa1, kappa2, strength, angle_in_degrees):
    # Преобразование угла в радианы
    angle_in_radians = np.radians(angle_in_degrees)
    # Вычисление угла преломления через закон диэлектрического преломления
    tangent_of_theta1 = kappa2 / kappa1
    
    # Угол преломления (в радианах)
    theta2_in_radians = np.arctan(tangent_of_theta1 * np.tan(angle_in_radians))
    
    # Линии поля в разных средах
    x_left = np.linspace(-5, 0, 100)
    y_left = np.tan(angle_in_radians) * x_left
    
    x_right = np.linspace(0, 5, 100)
    y_right = np.tan(theta2_in_radians) * x_right

    # Отображение графика
    plt.figure(figsize=(8, 6))
    
    # Отметка границы
    plt.axvline(0, color='black', linestyle='--', label='Граница между средами')

    # Линия поля для первой среды
    plt.plot(x_left, y_left, label=f'Поле (среда 1, κ1={kappa1})', color='green')
    
    # Линия поля для второй среды
    plt.plot(x_right, y_right, label=f'Поле (среда 2, κ2={kappa2})', color='orange')
    
    # Настройки графика
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.title('Преломление электрических полей на границе')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.legend()
    plt.grid()
    plt.show()

def handle_input():
    try:
        kappa1 = float(kappa1_input.get())
        kappa2 = float(kappa2_input.get())
        strength = float(strength_input.get())
        angle_in_degrees = float(angle_input.get())

        # Вызов функции визуализации
        plot_dielectric_boundaries(kappa1, kappa2, strength, angle_in_degrees)
    
    except ValueError:
        print("Ошибка: введите корректные числовые значения.")

# Создание интерфейса с Tkinter
window = tk.Tk()
window.title("Графическое отображение границы двух диэлектриков")

# Поля для ввода параметров
frame_input = ttk.Frame(window, padding="10")
frame_input.grid(row=0, column=0)

ttk.Label(frame_input, text="Диэлектрическая проницаемость 1 (κ1):").grid(row=0, column=0, sticky="w")
kappa1_input = ttk.Entry(frame_input)
kappa1_input.grid(row=0, column=1)

ttk.Label(frame_input, text="Диэлектрическая проницаемость 2 (κ2):").grid(row=1, column=0, sticky="w")
kappa2_input = ttk.Entry(frame_input)
kappa2_input.grid(row=1, column=1)

ttk.Label(frame_input, text="Модуль электрического поля:").grid(row=2, column=0, sticky="w")
strength_input = ttk.Entry(frame_input)
strength_input.grid(row=2, column=1)

ttk.Label(frame_input, text="Угол напряженности (в градусах):").grid(row=3, column=0, sticky="w")
angle_input = ttk.Entry(frame_input)
angle_input.grid(row=3, column=1)

# Кнопка для отображения графика
plot_button = ttk.Button(frame_input, text="Показать график", command=handle_input)
plot_button.grid(row=4, columnspan=2)

# Запуск интерфейса
window.mainloop()
