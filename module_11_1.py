import pandas as pd

# Считываем данные из CSV файла
data = pd.read_csv('data.csv')

# Выводим первые 5 строк данных
print("Первые 5 строк данных:")
print(data.head())

# Средний возраст,
average_age = data['Age'].mean()
print("\nСредний возраст:", average_age)

# Общая сумма заработной платы
total_salary = data['Salary'].sum()
print("Общая сумма заработной платы:", total_salary)

# Максимальная зарплата
max_salary = data['Salary'].max()
max_salary_person = data[data['Salary'] == max_salary]['Name'].values[0]
print("Максимальная зарплата:", max_salary, "у человека по имени", max_salary_person)

# Статистика по возрасту
age_stats = data['Age'].describe()
print("\nСтатистика по возрасту:")
print(age_stats)