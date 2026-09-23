import json
import csv
import logging

try:
    import yaml
except ImportError:
    yaml = None

# 1. Matnli faylga with open() yordamida 5 ta qatorli log yozuvi qo'shing (rejim "a").
def task1():
    with open("app.log", "a", encoding="utf-8") as file:
        for i in range(1, 6):
            file.write(f"Log entry #{i}: Everything running fine.\n")

# 2 & 4. Konfiguratsiyani JSON faylda saqlab, keyin o'qib chiqing.
def task2_and_4():
    config_data = {
        "env": "development",
        "port": 8080,
        "debug": True
    }
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=4)
        
    with open("config.json", "r", encoding="utf-8") as f:
        loaded = json.load(f)
        print("JSON read:", loaded)

# 3 & 5. YAML formatida server ro'yxatini yozib, pyyaml orqali o'qib chiqing.
def task3_and_5():
    if not yaml:
        print("PyYAML o'rnatilmagan (pip install pyyaml)")
        return
    servers_data = {
        "serv1": {"ip": "192.168.1.10", "port": 22},
        "serv2": {"ip": "192.168.1.11", "port": 22}
    }
    with open("servers.yaml", "w", encoding="utf-8") as f:
        yaml.dump(servers_data, f, default_flow_style=False)
        
    with open("servers.yaml", "r", encoding="utf-8") as f:
        loaded = yaml.safe_load(f)
        print("YAML read:", loaded)

# 6 & 8. CSV faylga 3-5 xodim ma'lumotini yozing, o'qib jadval ko'rinishida konsolga chop eting.
def task6_and_8():
    employees = [
        ["ID", "Name", "Role", "Salary"],
        [1, "Alisher", "Developer", 1500],
        [2, "Madina", "Designer", 1200],
        [3, "Sanjar", "DevOps", 1800],
        [4, "Nigora", "QA Engineer", 1100]
    ]
    with open("employees.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(employees)
        
    with open("employees.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        print("\n--- CSV Data Table ---")
        for row in reader:
            print(f"{row[0]:<5} | {row[1]:<10} | {row[2]:<15} | {row[3]:<10}")

# 7 & 9. Logging moduli yordamida skript voqealarini (start, tugash, xatolik) faylga yozing.
def task7_and_9():
    logging.basicConfig(
        filename="events.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )
    logging.info("Start: Script process initialized.")
    try:
        _ = 10 / 0
    except Exception as e:
        logging.error(f"Xatolik: {e}")
    finally:
        logging.info("Tugash: Script process finished.")

if __name__ == "__main__":
    task1()
    task2_and_4()
    task3_and_5()
    task6_and_8()
    task7_and_9()
    print("\n[+] 3.1 Amaliy vazifa muvaffaqiyatli bajarildi!")
