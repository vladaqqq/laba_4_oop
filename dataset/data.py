import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(url, sep=';')

# Обзор данных
print(data.head())
print(data.info())
print(data.describe())

sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
sns.histplot(data['alcohol'], bins=30, kde=True)
plt.title('Распределение содержания алкоголя в вине')
plt.xlabel('Содержание алкоголя')
plt.ylabel('Частота')
plt.show()


correlation = data['alcohol'].corr(data['quality'])
print(f"Коэффициент корреляции между содержанием алкоголя и качеством вина: {correlation:.2f}")

if correlation > 0:
    print("Существует положительная корреляция.")
elif correlation < 0:
    print("Существует отрицательная корреляция.")
else:
    print("Корреляции нет.")