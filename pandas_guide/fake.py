import random
import pandas as pd
from faker import Faker

fake = Faker('ru_RU')
random.seed(42)
Faker.seed(42)

departments = ['IT', 'HR', 'Finance', 'Marketing',
               'Sales', 'Logistics', 'Support']
cities = ['Москва', 'Санкт-Петербург',
          'Новосибирск', 'Казань',
          'Екатеринбург', 'Ростов-на-Дону',
          'Самара']

data = []

for i in range(1000):
    data.append({
        'ID': i + 1,
        'Name': fake.name(),
        'Age': random.randint(22, 60),
        'Department': random.choice(departments),
        'Salary': random.randint(40000, 200000),
        'City': random.choice(cities),
        'Hire Date': fake.date_between(start_date='-10y', end_date='today')
    })

df = pd.DataFrame(data)

df.to_csv('big_employees.csv', index=False)

print("Файл big_employees.csv успешно создан.")
