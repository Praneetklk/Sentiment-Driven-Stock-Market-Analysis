import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Dummy placeholder for dataset
df = pd.DataFrame({
    'sentiment': [0.1, -0.2, 0.3, 0.4, -0.5],
    'price_movement': [1, 0, 1, 1, 0]
})

X = df[['sentiment']]
y = df['price_movement']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

joblib.dump(model, 'models/random_forest_model.pkl')
