# Задача 2. Расчёт параметров помещения

length = 6.0   # Длина помещения, м
width = 4.0    # Ширина помещения, м
height = 2.8   # Высота помещения, м
painting_price = 125  # Цена покраски стен за 1 м², руб.

# Рассчитываем площадь пола, площадь стен и объём помещения.
floor_area = length * width
wall_area = 2 * (length + width) * height
volume = length * width * height
painting_cost = wall_area * painting_price

print("=== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
print(f"Площадь пола: {floor_area:.2f} м²")
print(f"Площадь стен: {wall_area:.2f} м²")
print(f"Объём помещения: {volume:.2f} м³")
print(f"Стоимость покраски стен: {painting_cost:.2f} руб.")
