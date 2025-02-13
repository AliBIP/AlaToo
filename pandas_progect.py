import pandas as pd
import numpy as np

# 1
months = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
index=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
print(months)

# 2
students = {'MatMIE': 45, 'Mat DAIS': 50, 'COMIE': 40, 'COMEC': 55}
students_series = pd.Series(students)
print(students_series)

# 3
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print(df)
attempts_greater_than_2 = df[df['attempts'] > 2]
print(attempts_greater_than_2)
