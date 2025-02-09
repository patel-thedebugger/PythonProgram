import pandas as pd


# Create a simple DataFrame
data = {
    'Name': ['Rakesh', 'Paresh', 'Santosh', 'Neel'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic DataFrame operations
print("\nSummary statistics:")
print(df.describe())

print("\nSelect a column:")
print(df['Name'])

print("\nFilter rows where Age > 30:")
print(df[df['Age'] > 30])

print("\nAdd a new column:")
df['Salary'] = [70000, 80000, 120000, 90000]
print(df)
