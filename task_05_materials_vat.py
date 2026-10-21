# Задача 5. Калькулятор скидки на материалы

unit_price = 1250.0  # Цена одной единицы материала, руб.
quantity = 48        # Количество единиц материала

# Вычисляем сумму до скидки, ставку скидки и итоговую стоимость.
subtotal = unit_price * quantity

if subtotal < 1000:
    discount_rate = 0
elif subtotal <= 50000:
    discount_rate = 0.05
else:
    discount_rate = 0.10

discount = subtotal * discount_rate
total = subtotal - discount

print("=== КАЛЬКУЛЯТОР СКИДКИ ===")
print(f"Цена за единицу: {unit_price:.2f} руб.")
print(f"Количество: {quantity}")
print(f"Сумма без скидки: {subtotal:.2f} руб.")
print(f"Скидка: {discount_rate * 100:.0f}% ({discount:.2f} руб.)")
print(f"Итого к оплате: {total:.2f} руб.")
