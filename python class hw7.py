from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing(as_frame=True)
df = housing.data
df["PRICE"] = housing.target
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(15, 10))
for i, col in enumerate(df.columns):
    plt.subplot(3, 3, i + 1)
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.scatter(df['Longitude'], df['Latitude'], c=df['PRICE'], cmap='plasma', s=2)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('California Housing Data')
plt.colorbar(label='PRICE')
plt.show()