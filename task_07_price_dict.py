# Задача 7. Прайс-лист строительных материалов
# Автор: Аксёнов Александр Александрович, группа з3140801/52501

prices = {
    "Кирпич": 12.50,
    "Цемент": 450.00,
    "Песок": 800.00,
    "Арматура": 48000.00,
    "Бетон": 4200.00,
}

# Добавляем две позиции, затем изменяем цену и удаляем одну позицию.
prices["Щебень"] = 1500.00
prices["Гипсокартон"] = 650.00
prices["Цемент"] *= 1.10  # повышение цены на 10%
removed_name = "Песок"
removed_price = prices.pop(removed_name)

average_price = sum(prices.values()) / len(prices)

print("=== ПРАЙС-ЛИСТ МАТЕРИАЛОВ ===")
for material, price in prices.items():
    print(f"{material:<15} {price:>10.2f} руб.")
print(f"Удалён материал: {removed_name} ({removed_price:.2f} руб.)")
print(f"Средняя цена оставшихся материалов: {average_price:.2f} руб.")
