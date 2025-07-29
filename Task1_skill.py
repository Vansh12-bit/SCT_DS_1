#Task Assignment No.1

#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Let's first load the required CSV file
file_path = "C:/Users/ASUS/Downloads/combined.csv"
df = pd.read_csv(file_path)

#Basic steps just to check either is dataset is loaded or not:
print("First five rows:\n", df.head())
print("Last five rows:\n", df.tail())
print("Description:\n", df.describe())
print("Basic Information:\n")
df.info()

#Group the data as per their Region and Customer_Segment:
grouped_data = df[['Region', 'Customer_Segment']].value_counts().reset_index(name='Count')

#Required bar chart:
plt.figure(figsize=(10, 6))
sns.barplot(data=grouped_data, x='Region', y='Count', hue='Customer_Segment')
plt.title('Customer Segment Count by Region')
plt.xlabel('Region')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
