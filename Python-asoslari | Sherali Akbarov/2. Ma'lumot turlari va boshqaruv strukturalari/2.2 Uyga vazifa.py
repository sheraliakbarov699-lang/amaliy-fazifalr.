# 1. Server statuslari va "down" bo'lganlarni chop etish
servers = {
    "server1": "up",
    "server2": "down",
    "server3": "down",
    "server4": "up",
}


def print_down_servers(servers_dict):
    for name, status in servers_dict.items():
        if status == "down":
            print(f"{name}: {status}")


print_down_servers(servers)
print("-" * 30)

# 2. 1 dan 50 gacha, 3 ga qoldiqsiz bo'linadigan sonlar (list comprehension)
divisible_by_3 = [n for n in range(1, 51) if n % 3 == 0]
print(divisible_by_3)
print("-" * 30)


# 3. Ichki funksiya (nested function) va closure
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # 10
print(triple(5))   # 15
print("-" * 30)


# 4. Maxsus exception klassi
class InvalidServerNameError(Exception):
    """Server nomi noto'g'ri formatda bo'lsa chiqariladi."""
    pass


def check_server_name(name):
    if not name.startswith("server"):
        raise InvalidServerNameError(f"Noto'g'ri server nomi: {name}")
    print(f"{name} nomi to'g'ri.")


try:
    check_server_name("server5")
    check_server_name("noto'g'ri-nom")
except InvalidServerNameError as e:
    print(f"Xatolik: {e}")
print("-" * 30)


# 5. Port raqamini tekshirish (validatsiya)
def validate_port(value):
    try:
        port = int(value)
        if not (1 <= port <= 65535):
            raise ValueError
        print(f"Port {port} to'g'ri.")
        return port
    except ValueError:
        print(f"Noto'g'ri port qiymati: {value}")
        return None


validate_port("8080")
validate_port("port")
validate_port("99999")
