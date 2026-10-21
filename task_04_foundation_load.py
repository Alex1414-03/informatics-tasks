# Задача 4. Рабочий график
# По номеру дня недели определяем название дня и режим работы.

day_number = 3
days = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье",
}

if day_number not in days:
    print("Ошибка: введите номер дня от 1 до 7.")
else:
    day_name = days[day_number]
    is_workday = day_number <= 5
    schedule = "8:00 — начало смены" if is_workday else "Отдых"

    print("=== РАБОЧИЙ ГРАФИК ===")
    print(f"День: {day_name}")
    print(f"Режим: {'Рабочий день' if is_workday else 'Выходной'}")
    print(f"Расписание: {schedule}")
