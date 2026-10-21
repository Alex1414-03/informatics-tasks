# Задача 9. Очистка адресов
# Убираем лишние пробелы, нормализуем пробелы после сокращений и запятых.

addresses = [
    "  г. Москва, ул. Ленина, д. 10  ",
    "г.Казань,ул.Баумана,д.15",
    "  г. Санкт-Петербург, ул. Невский, д. 100  ",
]

def clean_address(address):
    """Приводит адрес к единому читаемому формату."""
    # Удаляем пробелы по краям и схлопываем повторяющиеся пробелы.
    address = " ".join(address.strip().split())
    # Нормализуем пробелы после запятых.
    address = address.replace(",", ", ")
    # Убираем пробелы, случайно появившиеся перед запятыми.
    address = address.replace(" ,", ",")
    # Добавляем пробел после сокращений, если его нет.
    for abbreviation in ("г.", "ул.", "д."):
        address = address.replace(abbreviation, abbreviation + " ")
    # Убираем возможные повторные пробелы после замен.
    return " ".join(address.split())

print("=== СРАВНЕНИЕ АДРЕСОВ ===")
for index, address in enumerate(addresses, start=1):
    print(f"#{index}")
    print(f"ДО:     {address!r}")
    print(f"ПОСЛЕ:  {clean_address(address)!r}")
