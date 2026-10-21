# Задача 3. Конвертер температуры
# Переводим температуру из градусов Цельсия в Фаренгейты
# и определяем состояние воды при указанной температуре.

temperature_c = 20.0
temperature_f = temperature_c * 9 / 5 + 32

if temperature_c < 0:
    water_state = "Лёд"
elif temperature_c < 100:
    water_state = "Жидкость"
else:
    water_state = "Пар"

print("=== КОНВЕРТЕР ТЕМПЕРАТУРЫ ===")
print(f"Температура: {temperature_c:.1f} °C")
print(f"По Фаренгейту: {temperature_f:.1f} °F")
print(f"Состояние воды: {water_state}")
