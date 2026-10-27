# Задача 8. Анализ заказов трёх подрядчиков
# Автор: Аксёнов Александр Александрович, группа з3140801/52501

# Списки показывают материалы, заказанные каждым подрядчиком.
contractor_1 = ["Цемент", "Песок", "Кирпич", "Арматура", "Бетон"]
contractor_2 = ["Цемент", "Щебень", "Кирпич", "Бетон"]
contractor_3 = ["Цемент", "Песок", "Бетон", "Гипсокартон"]

set_1 = set(contractor_1)
set_2 = set(contractor_2)
set_3 = set(contractor_3)

all_unique = set_1 | set_2 | set_3
common_all = set_1 & set_2 & set_3
only_first = set_1 - set_2 - set_3
exactly_two = (set_1 & set_2) | (set_1 & set_3) | (set_2 & set_3)
# Убираем материалы, которые присутствуют у всех трёх подрядчиков.
exactly_two -= common_all

print("=== АНАЛИЗ ЗАКАЗОВ ===")
print(f"Все уникальные материалы ({len(all_unique)}): {', '.join(sorted(all_unique))}")
print(f"Общие для всех: {', '.join(sorted(common_all)) or 'нет'}")
print(f"Только у первого подрядчика: {', '.join(sorted(only_first)) or 'нет'}")
print(f"Ровно у двух подрядчиков: {', '.join(sorted(exactly_two)) or 'нет'}")

