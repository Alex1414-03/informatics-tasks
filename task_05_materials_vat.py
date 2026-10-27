# Задача 5. Калькулятор скидки на строительные материалы
# Автор: Аксёнов Александр Александрович, группа з3140801/52501

try:
    unit_price = float(input("Введите цену одной единицы материала, руб.: ").replace(",", "."))
    quantity = float(input("Введите количество материала: ").replace(",", "."))
    if unit_price < 0 or quantity < 0:
        raise ValueError
except ValueError:
    print("Ошибка: цена и количество должны быть неотрицательными числами.")
else:
    # Скидка применяется к общей стоимости в соответствии с диапазонами из задания.
    subtotal = unit_price * quantity
    if subtotal < 1000:
        discount_rate = 0
    elif subtotal <= 5000:
        discount_rate = 0.05
    else:
        discount_rate = 0.10

    discount = subtotal * discount_rate
    total = subtotal - discount

    print("=== РАСЧЁТ СТОИМОСТИ МАТЕРИАЛОВ ===")
    print(f"Цена за единицу: {unit_price:.2f} руб.")
    print(f"Количество: {quantity:g}")
    print(f"Стоимость без скидки: {subtotal:.2f} руб.")
    print(f"Размер скидки: {discount_rate:.0%}")
    print(f"Сумма скидки: {discount:.2f} руб.")
    print(f"Итого к оплате: {total:.2f} руб.")
