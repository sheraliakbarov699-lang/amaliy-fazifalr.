import os
import json
import csv
import logging
from logging.handlers import RotatingFileHandler

try:
    import yaml
except ImportError:
    yaml = None

# 1. JSON konfiguratsiya faylini o'qib, agar "debug": true bo'lsa qo'shimcha DEBUG darajasidagi log chiqaring.
def task1():
    config_data = {"env": "dev", "debug": True}
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config_data, f)

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
def task2(json_file="config.json", yaml_file="config.yaml"):
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
def task3():
    input_file = "large_log.csv"
    output_file = "filtered_errors.csv"
    
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

# 4. logging.handlers.RotatingFileHandler yordamida log fayli 1MB yetganda avtomatik yangilanadigan konfiguratsiya.
def task4():
    logger = logging.getLogger("RotatingLogger")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler("app_rotating.log", maxBytes=1*1024*1024, backupCount=3, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("Rotating log message test.")

# 5. Papkadagi barcha .log fayllarni tekshirib, ichida "ERROR" so'zi uchraganlarni alohida hisobot faylga yozing.
def task5():
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
    task1()
    task2()
    task3()
    task4()
    task5()
    print("\n[+] 3.2 Uyga vazifa muvaffaqiyatli bajarildi!")
