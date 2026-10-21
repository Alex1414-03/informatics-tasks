# Задача 8. Анализ заказов трёх подрядчиков
# Множества помогают сравнить материалы в заказах.

contractor_1 = {"Кирпич", "Цемент", "Песок", "Арматура"}
contractor_2 = {"Цемент", "Песок", "Бетон", "Щебень"}
contractor_3 = {"Цемент", "Песок", "Арматура", "Бетон"}

all_unique = contractor_1 | contractor_2 | contractor_3
common_all = contractor_1 & contractor_2 & contractor_3
only_first = contractor_1 - contractor_2 - contractor_3
exactly_two = (
    (contractor_1 & contractor_2)
    | (contractor_1 & contractor_3)
    | (contractor_2 & contractor_3)
) - common_all

print("=== АНАЛИЗ ЗАКАЗОВ ===")
print(f"Все уникальные материалы: {', '.join(sorted(all_unique))}")
print(f"Общие для всех: {', '.join(sorted(common_all)) or 'нет'}")
print(f"Только у первого: {', '.join(sorted(only_first)) or 'нет'}")
print(f"Ровно у двух подрядчиков: {', '.join(sorted(exactly_two)) or 'нет'}")
