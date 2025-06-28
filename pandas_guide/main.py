"""курс Simulative
    Введение в Pandas
"""

import pandas as pd

# грузим данные из файла
df = pd.read_csv("./data/big_employees.csv", encoding="utf-8")

# получаем первые 10 строк
top_ten = df.head(10)

# получаем последние 10 строк
top_ten = df.head(10)
