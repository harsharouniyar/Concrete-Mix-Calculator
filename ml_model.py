import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("data.csv")

# Features and target
X = data[['cement','water','sand','aggregate','age']]
y = data['strength']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

def predict_strength(cement, water, sand, aggregate, age):
    return model.predict([[cement, water, sand, aggregate, age]])[0]