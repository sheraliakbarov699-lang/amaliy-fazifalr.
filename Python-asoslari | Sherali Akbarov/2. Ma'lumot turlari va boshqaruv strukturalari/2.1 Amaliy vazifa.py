# 1. Ro'yxatdagi sonlardan juftlarini ajratib, yangi listga yozuvchi funksiya
def get_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]


sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_even_numbers(sonlar))
print("-" * 30)

# 2. Server nomlari va IP manzillarini saqlaydigan dict va chop etish
servers = {
    "server1": "192.168.1.1",
    "server2": "192.168.1.2",
    "server3": "192.168.1.3",
}

for name, ip in servers.items():
    print(f"{name}: {ip}")
print("-" * 30)

# 3. 1 dan 100 gacha sonlar yig'indisi (for tsikli bilan)
total = 0
for i in range(1, 101):
    total += i
print(f"1 dan 100 gacha yig'indi: {total}")
print("-" * 30)


# 4. Foydalanuvchidan son so'rash, butun son bo'lmasa try/except bilan ushlash
def get_integer_input():
    try:
        value = input("Butun son kiriting: ")
        number = int(value)
        print(f"Siz kiritgan son: {number}")
        return number
    except ValueError:
        print("Xato: bu butun son emas!")
        return None


get_integer_input()
print("-" * 30)


# 5. Ikki sonni bo'luvchi funksiya, ZeroDivisionError'ni ushlash
def divide(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Xato: nolga bo'lish mumkin emas!")
        return None


divide(10, 2)
divide(10, 0)
