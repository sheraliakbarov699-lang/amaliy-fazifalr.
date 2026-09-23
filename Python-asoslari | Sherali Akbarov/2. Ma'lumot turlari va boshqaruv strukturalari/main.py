import os
import json
import csv
import logging
from logging.handlers import RotatingFileHandler

try:
    import yaml
except ImportError:
    yaml = None

# ==========================================
# 3.1 Amaliy vazifa
# ==========================================

# 1. Matnli faylga with open() yordamida 5 ta qatorli log yozuvi qo'shing (rejim "a").
def task_3_1_1():
    with open("app.log", "a", encoding="utf-8") as file:
        for i in range(1, 6):
            file.write(f"Log entry #{i}: Everything running fine.\n")

# 2 & 4. Konfiguratsiyani JSON faylda saqlab, keyin o'qib chiqing.
def task_3_1_2_4():
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
def task_3_1_3_5():
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
def task_3_1_6_8():
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
def task_3_1_7_9():
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


# ==========================================
# 3.2 Uyga vazifa
# ==========================================

# 1. JSON konfiguratsiya faylini o'qib, agar "debug": true bo'lsa qo'shimcha DEBUG darajasidagi log chiqaring.
def task_3_2_1():
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        
    log_level = logging.DEBUG if config.get("debug") else logging.INFO
    logger = logging.getLogger("Task321")
    logger.setLevel(log_level)
    
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    
    logger.debug("DEBUG mode active: Extra detailed logs outputted.")
    logger.info("INFO mode active.")

# 2. YAML formatidagi konfiguratsiyani JSON formatga aylantiruvchi (va aksincha) konverter.
def task_3_2_2(json_file="config.json", yaml_file="config.yaml"):
    if not yaml:
        return
    # JSON -> YAML
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False)
        
    # YAML -> JSON
    with open(yaml_file, "r", encoding="utf-8") as f:
        data_yaml = yaml.safe_load(f)
    with open("converted_back.json", "w", encoding="utf-8") as f:
        json.dump(data_yaml, f, indent=4)

# 3. Katta hajmdagi CSV faylni qatorma-qator o'qib, status == 'error' mos qatorlarni alohida faylga yozing.
def task_3_2_3():
    input_file = "large_log.csv"
    output_file = "filtered_errors.csv"
    
    # Pre-generate file for demonstration
    with open(input_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "status", "message"])
        writer.writerow([1, "ok", "Operation successful"])
        writer.writerow([2, "error", "Database connection timeout"])
        writer.writerow([3, "ok", "Operation successful"])

    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", newline="", encoding="utf-8") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            if len(row) > 1 and row[1] == "error":
                writer.writerow(row)

# 4. logging.handlers.RotatingFileHandler yordamida log fayli 1MB yetganda avtotmik yangilanadigan konfiguratsiya.
def task_3_2_4():
    logger = logging.getLogger("RotatingLogger")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler("app_rotating.log", maxBytes=1*1024*1024, backupCount=3, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("Rotating log message test.")

# 5. Papkadagi barcha .log fayllarni tekshirib, ichida "ERROR" so'zi uchraganlarni alohida hisobot faylga yozing.
def task_3_2_5():
    report_file = "error_report.txt"
    with open(report_file, "w", encoding="utf-8") as report:
        report.write("--- ERROR REPORT ---\n\n")
        for filename in os.listdir("."):
            if filename.endswith(".log") and filename != report_file:
                with open(filename, "r", encoding="utf-8", errors="ignore") as f:
                    for line_num, line in enumerate(f, start=1):
                        if "ERROR" in line:
                            report.write(f"File: {filename} | Line {line_num}: {line.strip()}\n")

if __name__ == "__main__":
    task_3_1_1()
    task_3_1_2_4()
    task_3_1_3_5()
    task_3_1_6_8()
    task_3_1_7_9()
    task_3_2_1()
    task_3_2_2()
    task_3_2_3()
    task_3_2_4()
    task_3_2_5()
    print("\n[+] All tasks executed successfully!")
