import pandas as pd
import matplotlib.pyplot as plt

# Load the heart dataset
heart_data_path = 'Heart_Attack_analysis.csv'
heart_data = pd.read_csv(heart_data_path)

# Convert the 'trtbps' column to numeric values
heart_data['trtbps'] = pd.to_numeric(heart_data['trtbps'], errors='coerce')

# Bar Chart: Average Cholesterol Levels by Sex
cholesterol_by_sex = heart_data.groupby('sex')['chol'].mean()
sex_labels = ['Female', 'Male']
plt.figure(figsize=(8, 6))
cholesterol_by_sex.plot(kind='bar', color=['pink', 'lightblue'])
plt.title('Average Cholesterol Levels by Sex')
plt.xlabel('Sex')
plt.ylabel('Average Cholesterol Level (mg/dl)')
plt.xticks(ticks=[0, 1], labels=sex_labels, rotation=0)
plt.tight_layout()
plt.show()

# Line Chart: Average Maximum Heart Rate by Age
average_heart_rate_by_age = heart_data.groupby('age')['thalachh'].mean().sort_index()
plt.figure(figsize=(12, 6))
average_heart_rate_by_age.plot(kind='line', marker='o', color='b', linestyle='-')
plt.title('Average Maximum Heart Rate by Age')
plt.xlabel('Age')
plt.ylabel('Average Maximum Heart Rate (thalachh)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Pie Chart: Distribution of Chest Pain Types
cp_counts = heart_data['cp'].value_counts()
cp_labels = ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic']
colors = ['#ff6666', '#ffcc99', '#99ff99', '#66b3ff']
plt.figure(figsize=(8, 8))
plt.pie(cp_counts, labels=cp_labels, autopct='%1.1f%%', startangle=90, colors=colors, shadow=True)
plt.title('Distribution of Chest Pain Types')
plt.axis('equal')
plt.show()

# Histogram: Distribution of Resting Blood Pressure
plt.figure(figsize=(10, 6))
plt.hist(heart_data['trtbps'], bins=20, color='coral', edgecolor='black')
plt.title('Distribution of Resting Blood Pressure (trtbps)')
plt.xlabel('Resting Blood Pressure (mm Hg)')
plt.ylabel('Number of Patients')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()
