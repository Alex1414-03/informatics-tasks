# Задача 9. Очистка адресов строительных объектов
# Автор: Аксёнов Александр Александрович, группа з3140801/52501

addresses = [
    " г. Москва, ул. Ленина, д. 10 ",
    "г.Казань,ул.Баумана,д.15",
    " г. Санкт-Петербург, ул. Невский, д. 100 ",
]


def clean_address(address):
    """Удаляет лишние пробелы и приводит сокращения адреса к единому виду."""
    # Сначала убираем пробелы по краям и нормализуем пробелы после запятых.
    cleaned = " ".join(address.strip().split())
    cleaned = cleaned.replace(",", ", ")
    # Схлопываем повторные пробелы, которые могли появиться после замены.
    cleaned = " ".join(cleaned.split())

    # Добавляем пробел после сокращений, если он отсутствует.
    for abbreviation in ("г.", "ул.", "д."):
        cleaned = cleaned.replace(abbreviation, abbreviation + " ")
        cleaned = " ".join(cleaned.split())

    return cleaned


print("=== СРАВНЕНИЕ АДРЕСОВ ===")
for index, address in enumerate(addresses, start=1):
    print(f"#{index}")
    print(f"ДО:    {address!r}")
    print(f"ПОСЛЕ: {clean_address(address)!r}")
