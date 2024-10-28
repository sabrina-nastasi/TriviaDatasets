# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace with the specific file you want to analyze)
file_path = 'aggression_parsed_dataset.csv'
  # Update path if necessary
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to get an overview
print(data.head())

# Check the column names and data types
print(data.columns)
print(data.info())
sns.countplot(x='oh_label', data=data)
plt.title('Distribution of Cyberbullying Labels')
plt.xlabel('Label (0 = Not Bullying, 1 = Bullying)')
plt.ylabel('Count')
plt.show()