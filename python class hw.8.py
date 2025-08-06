from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing(as_frame=True)
df = housing.data
df["PRICE"] = housing.target

from sklearn.model_selection import train_test_split

X = df[['MedInc']]
y = df['PRICE']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

from sklearn.metrics import mean_squared_error, r2_score

linear_predictions = linear_model.predict(X_test)
linear_train_predictions = linear_model.predict(X_train)

mse = mean_squared_error(y_test, linear_predictions)
train_mse = mean_squared_error(y_train, linear_train_predictions)
r2 = r2_score(y_test, linear_predictions)

print(f"Linear Regression Test Mean Squared Error: {mse}")
print(f"Linear Regression Training Mean Squared Error: {train_mse}")
print(f"Linear Regression Test R-squared: {r2}")

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

linear_model_poly = LinearRegression()
linear_model_poly.fit(X_train_poly, y_train)

poly_predictions = linear_model_poly.predict(X_test_poly)

poly_mse = mean_squared_error(y_test, poly_predictions)
poly_r2 = r2_score(y_test, poly_predictions)

print(f"Polynomial Regression Mean Squared Error: {poly_mse}")
print(f"Polynomial Regression R-squared: {poly_r2}")

print("\n--- Model Performance Comparison ---")
print(f"Linear Regression MSE: {mse}")
print(f"Polynomial Regression MSE: {poly_mse}")
print(f"Linear Regression R-squared: {r2}")
print(f"Polynomial Regression R-squared: {poly_r2}")

if poly_mse < mse and poly_r2 > r2:
    print("\nConclusion: Polynomial Regression model performed better.")
    print("Reason: It has a lower Mean Squared Error and a higher R-squared value compared to Linear Regression, so it is better for this case.")
elif mse < poly_mse and r2 > poly_r2:
    print("\nConclusion: Linear Regression model performed better.")
    print("Reason: It has a lower Mean Squared Error and a higher R-squared value compared to Polynomial Regression, so it is better for this case.")
else:
    print("\nConclusion: Performance comparison is mixed or similar.")
    print("Reason: One metric might be better for one model while the other is better for the other model, or the metrics are very close.")