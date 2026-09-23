import json
import logging
import csv
import os


# 1. JSON konfiguratsiyani o'qib, debug bo'lsa DEBUG darajasida log chiqarish
def setup_logging_from_config(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    level = logging.DEBUG if config.get("debug") else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s - %(levelname)s - %(message)s")
    logging.debug("Debug rejimi yoqilgan (agar ko'rinsa).")
    logging.info("Konfiguratsiya yuklandi.")


# 2. YAML <-> JSON konverter (PyYAML kerak: pip install pyyaml)
def convert_yaml_to_json(yaml_path, json_path):
    import yaml
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def convert_json_to_yaml(json_path, yaml_path):
    import yaml
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)


# 3. CSV faylni o'qib, status == 'error' qatorlarni alohida faylga yozish
def filter_error_rows(input_csv, output_csv):
    with open(input_csv, "r", encoding="utf-8", newline="") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        error_rows = [row for row in reader if row.get("status") == "error"]

    with open(output_csv, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(error_rows)


# 4. RotatingFileHandler — log fayli 1MB ga yetganda avtomatik yangilanadi
def setup_rotating_logger(log_path):
    from logging.handlers import RotatingFileHandler

    logger = logging.getLogger("rotating_logger")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(log_path, maxBytes=1_000_000, backupCount=3)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


# 5. Papkadagi barcha .log fayllarni tekshirib, "ERROR" uchraganlarni hisobot faylga yozish
def scan_logs_for_errors(folder_path, report_path):
    with open(report_path, "w", encoding="utf-8") as report:
        for filename in os.listdir(folder_path):
            if filename.endswith(".log"):
                filepath = os.path.join(folder_path, filename)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as logfile:
                    for line_number, line in enumerate(logfile, start=1):
                        if "ERROR" in line:
                            report.write(f"{filename}:{line_number}: {line.strip()}\n")


if __name__ == "__main__":
    print("Bu modul funksiyalarni o'z ichiga oladi. Har birini kerakli fayl yo'llari bilan chaqiring.")
