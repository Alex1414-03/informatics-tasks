# Задача 2. Геометрические параметры помещения и стоимость покраски
# Автор: Аксёнов Александр Александрович, группа з3140801/52501

# Размеры помещения можно изменить перед запуском программы.
length = 6.0  # длина, м
width = 4.0   # ширина, м
height = 2.8  # высота, м
paint_price = 125  # стоимость покраски 1 м², руб.

floor_area = length * width
wall_area = 2 * (length + width) * height
volume = length * width * height
painting_cost = wall_area * paint_price

print("=== РАСЧЁТ ПАРАМЕТРОВ ПОМЕЩЕНИЯ ===")
print(f"Размеры: {length:.2f} × {width:.2f} × {height:.2f} м")
print(f"Площадь пола: {floor_area:.2f} м²")
print(f"Площадь стен без вычета проёмов: {wall_area:.2f} м²")
print(f"Объём помещения: {volume:.2f} м³")
print(f"Стоимость покраски стен: {painting_cost:.2f} руб.")
