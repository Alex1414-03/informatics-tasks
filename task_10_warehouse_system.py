# Задача 10. Система учёта строительного склада
# Автор: Аксёнов Александр Александрович, группа з3140801/52501

warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15},
}


def print_warehouse(items):
    """Печатает табличное представление складских запасов."""
    print("Материал       | Кол-во | Цена       | Мин. | Стоимость")
    print("-" * 65)
    for name, data in items.items():
        warning = " ⚠ КРИТИЧНО!" if data["quantity"] < data["min_quantity"] else ""
        cost = data["quantity"] * data["price"]
        print(
            f"{name:<14} | {data['quantity']:>6} | {data['price']:>10.2f} | "
            f"{data['min_quantity']:>4} | {cost:>12.2f}{warning}"
        )


print("=== СИСТЕМА УЧЁТА СКЛАДА ===")
print_warehouse(warehouse)

total_value = sum(item["quantity"] * item["price"] for item in warehouse.values())
most_expensive = max(warehouse.items(), key=lambda pair: pair[1]["price"])
critical = [
    (name, data["quantity"], data["min_quantity"])
    for name, data in warehouse.items()
    if data["quantity"] < data["min_quantity"]
]

print("=" * 65)
print(f"Общая стоимость склада: {total_value:.2f} руб.")
print(f"Самый дорогой материал по цене за единицу: {most_expensive[0]} "
      f"({most_expensive[1]['price']:.2f} руб.)")
print(f"Критические остатки ({len(critical)}):")
if critical:
    for name, quantity, minimum in critical:
        print(f"- {name}: {quantity} < {minimum}")
else:
    print("- нет")

# Демонстрируем выдачу 25 единиц цемента и обновляем остаток.
material_to_issue = "Цемент"
issue_quantity = 25
print("=== ВЫДАЧА МАТЕРИАЛА СО СКЛАДА ===")
if material_to_issue in warehouse and warehouse[material_to_issue]["quantity"] >= issue_quantity:
    warehouse[material_to_issue]["quantity"] -= issue_quantity
    print(f"✓ Выдано {issue_quantity} единиц материала «{material_to_issue}».")
    print(f"Остаток: {warehouse[material_to_issue]['quantity']}")
else:
    print("Ошибка: материала недостаточно или он отсутствует на складе.")
