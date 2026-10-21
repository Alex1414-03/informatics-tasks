# Задача 10. Система учёта строительного склада

warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15},
}

# Выводим таблицу и одновременно считаем общую стоимость запасов.
total_value = 0
critical_items = []

print("=== СИСТЕМА УЧЁТА СКЛАДА ===")
print()
print(f"{'Материал':<12} | {'Кол-во':>7} | {'Цена':>10} | {'Мин.':>6} | {'Стоимость':>12}")
print("-" * 65)

for name, data in warehouse.items():
    quantity = data["quantity"]
    price = data["price"]
    minimum = data["min_quantity"]
    value = quantity * price
    total_value += value

    warning = " ⚠ КРИТИЧНО!" if quantity < minimum else ""
    if quantity < minimum:
        critical_items.append((name, quantity, minimum))

    print(
        f"{name:<12} | {quantity:>7} | {price:>10.2f} | "
        f"{minimum:>6} | {value:>12.2f}{warning}"
    )

# Находим материал с наибольшей стоимостью складского запаса.
most_expensive = max(
    warehouse.items(),
    key=lambda item: item[1]["quantity"] * item[1]["price"]
)
most_expensive_value = most_expensive[1]["quantity"] * most_expensive[1]["price"]

print("-" * 65)
print(f"Общая стоимость: {total_value:.2f} руб.")
print(
    f"Самый дорогой запас: {most_expensive[0]} "
    f"({most_expensive_value:.2f} руб.)"
)

print()
print(f"⚠ КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_items)}):")
if critical_items:
    for name, quantity, minimum in critical_items:
        print(f"- {name}: {quantity} < {minimum}")
else:
    print("- Нет")

# Моделируем выдачу 25 единиц цемента со склада.
material_to_issue = "Цемент"
issue_quantity = 25

print()
print("=== ВЫДАЧА МАТЕРИАЛА ===")
if material_to_issue in warehouse and warehouse[material_to_issue]["quantity"] >= issue_quantity:
    warehouse[material_to_issue]["quantity"] -= issue_quantity
    remaining = warehouse[material_to_issue]["quantity"]
    print(f"✓ Выдано {issue_quantity} ед. материала «{material_to_issue}».")
    print(f"Остаток: {remaining}")
else:
    print("Ошибка: материал отсутствует или недостаточно остатка.")
