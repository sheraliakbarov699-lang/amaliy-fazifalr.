import os

# Главная папка проекта
MAIN_FOLDER = "Python-asoslari | Sherali Akbarov"

# Список всех тем и соответствующих файлов
topics = {
    "1. Python nima va DevOps'dagi roli": [
        "1.1 Amaliy vazifa.py",
        "1.2 Uyga vazifa.py"
    ],
    "2. Ma'lumot turlari va boshqaruv strukturalari": [
        "2.1 Amaliy vazifa.py",
        "2.2 Uyga vazifa.py"
    ],
    "3. Fayl va log bilan ishlash": [
        "3.1 Amaliy vazifa.py",
        "3.2 Uyga vazifa.py"
    ],
    "4. OS avtomatlashtirish": [
        "4.1 Amaliy vazifa.py",
        "4.2 Uyga vazifa.py"
    ],
    "5. HTTP va REST API": [
        "5.1 Amaliy vazifa.py",
        "5.2 Uyga vazifa.py"
    ],
    "6. Monitoring va Parsing": [
        "6.1 Amaliy vazifa.py",
        "6.2 Uyga vazifa.py"
    ],
    "7. Docker va Python": [
        "7.1 Amaliy vazifa.py",
        "7.2 Uyga vazifa.py"
    ],
    "8. CI-CD bilan integratsiya": [
        "8.1 Amaliy vazifa.py",
        "8.2 Uyga vazifa.py"
    ]
}

def build_structure():
    # Создание главной папки
    os.makedirs(MAIN_FOLDER, exist_ok=True)
    print(f"Создана главная папка: {MAIN_FOLDER}\n")

    for topic_name, files in topics.items():
        # Путь к папке темы
        folder_path = os.path.join(MAIN_FOLDER, topic_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Папка создана: {folder_path}")

        # Создание файлов внутри папки темы
        for filename in files:
            file_path = os.path.join(folder_path, filename)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"# {filename}\n")
                print(f"  └── Создан файл: {filename}")

if __name__ == "__main__":
    build_structure()
    print("\nСтруктура успешно создана!")

