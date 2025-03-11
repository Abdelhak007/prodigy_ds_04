import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:\\Users\\PC\\Downloads\\twitter_validation.csv"  # Update with the actual path
df = pd.read_csv(file_path)

df.columns = ["ID", "Entity", "Sentiment", "Tweet"]

# Sentiment Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Sentiment", palette="coolwarm")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

# Sentiment per Entity
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="Entity", hue="Sentiment", order=df["Entity"].value_counts().index[:10], palette="coolwarm")
plt.title("Top 10 Entities Sentiment Analysis")
plt.xlabel("Entity")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.legend(title="Sentiment")
plt.show()
