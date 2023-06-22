flat_number = int(input("Введи номер квартиры: "));
print("Вы ввели", flat_number,"номер квартиры")

entrance_number = (flat_number - 1) // 20 + 1
floor_number = (flat_number - 1) % 20 //4 + 1
print("Номер подъезда:", entrance_number)
print("Номер этажа:", floor_number)