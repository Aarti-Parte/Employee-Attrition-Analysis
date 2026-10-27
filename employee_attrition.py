import pandas as pd

# Load the dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Display first 5 rows
print(df.head())


import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

print(df.head())

# Check dataset shape
print("Dataset Shape:", df.shape)

# Check column names
print("\nColumn Names:")
print(df.columns.tolist())

# Check dataset information
print("\nDataset Information:")
df.info()


# Check missing values
print("\nMissing Values:")
print(df.isnull().sum().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Check total employees
print("\nTotal Employees:")
print(len(df))

# Employee Attrition Analysis

print("\nEmployee Attrition Count:")
print(df["Attrition"].value_counts())

# Calculate attrition percentage
attrition_count = df["Attrition"].value_counts()

left_company = attrition_count.get("Yes", 0)
stayed_company = attrition_count.get("No", 0)

total_employees = len(df)

attrition_rate = (left_company / total_employees) * 100

print("\nEmployees who left:", left_company)
print("Employees who stayed:", stayed_company)
print("Attrition Rate:", round(attrition_rate, 2), "%")


# Department-wise Attrition Analysis

print("\nDepartment-wise Attrition:")

department_attrition = df[df["Attrition"] == "Yes"].groupby("Department").size()

print(department_attrition)



# Department-wise Attrition Percentage

print("\nDepartment-wise Attrition Percentage:")

department_total = df.groupby("Department").size()

department_left = df[df["Attrition"] == "Yes"].groupby("Department").size()

department_rate = (department_left / department_total) * 100

print(department_rate.round(2))


import matplotlib.pyplot as plt

# Department-wise Attrition Rate Chart

department_rate = department_rate.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(department_rate.index, department_rate.values)

plt.title("Department-wise Employee Attrition Rate")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()
plt.show()



# Gender-wise Attrition Analysis

print("\nGender-wise Attrition Count:")

gender_attrition = df[df["Attrition"] == "Yes"].groupby("Gender").size()

print(gender_attrition)

# Gender-wise Attrition Chart

gender_attrition.plot(kind="bar")

plt.title("Gender-wise Employee Attrition")
plt.xlabel("Gender")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("department_attrition.png")
plt.show()


# Gender-wise Attrition Analysis

print("\nGender-wise Attrition Count:")

gender_attrition = df[df["Attrition"] == "Yes"].groupby("Gender").size()

print(gender_attrition)



print("\nGender-wise Attrition Count:")

print(
    df[df["Attrition"] == "Yes"]
    .groupby("Gender")
    .size()
)


print("TEST - Gender Analysis Started")

print(df[df["Attrition"] == "Yes"].groupby("Gender").size())


# Overtime-wise Attrition Analysis

print("\nOvertime-wise Attrition Count:")

overtime_attrition = df[df["Attrition"] == "Yes"].groupby("OverTime").size()

print(overtime_attrition)

# Overtime-wise Attrition Rate

print("\nOvertime-wise Attrition Rate (%):")

overtime_total = df.groupby("OverTime").size()

overtime_rate = (overtime_attrition / overtime_total) * 100

print(overtime_rate.round(2))



# Overtime Attrition Rate Chart

overtime_rate = overtime_rate.sort_values(ascending=False)

plt.figure(figsize=(7, 5))
plt.bar(overtime_rate.index, overtime_rate.values)

plt.title("Overtime vs Employee Attrition Rate")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()
plt.savefig("overtime_attrition.png")
plt.show()

