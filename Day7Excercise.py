import pandas as pd

data = pd.read_csv("c:/Users/mohalsha/Desktop/Python_training/Employee_Salaries.csv")
print(data)

average_salary = data.agg({'Base_Salary':'mean'})
print(f"Average of {average_salary}")

max_salary = data.groupby('Department_Name').agg({'Base_Salary':'max'})
print(max_salary)

gender_based_salary = data.groupby('Gender').agg({'Base_Salary':'mean'})
print(gender_based_salary)