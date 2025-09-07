import pandas as pd
import random

# Создаем 20 новых записей на рыбную тематику
fish_categories = ["Морская рыба", "Пресноводная рыба", "Деликатесы из рыбы"]
fish_titles = [
    "Лосось свежий", "Форель радужная", "Тунец стейк",
    "Сельдь солёная", "Скумбрия копченая", "Карп речной",
    "Щука", "Минтай", "Палтус", "Окунь морской"
]
fish_descriptions = [
    "Отборная рыба, свежая и вкусная.", 
    "Идеально подходит для жарки и запекания.", 
    "Высокое содержание омега-3.", 
    "Натуральная продукция без консервантов.",
    "Подходит для суши и сашими.",
    "Лучший выбор для праздничного стола."
]
countries = ["Норвегия", "Россия", "Чили", "Исландия", "Япония"]

new_rows = []
for i in range(20):
    new_rows.append({
        "category_name": random.choice(fish_categories),
        "category_description": "Рыбные продукты для гурманов",
        "post_title": random.choice(fish_titles),
        "post_description": random.choice(fish_descriptions),
        "price": random.randint(500, 3000),  # цена в рублях
        "weight": random.choice([200, 500, 1000]),  # вес в граммах
        "country": random.choice(countries)
    })

df_fish = pd.DataFrame(new_rows)

# Сохраняем в новый Excel
output_path = "fish_report.xlsx"
df_fish.to_excel(output_path, index=False)

print(f"Файл успешно создан по пути: {output_path}")