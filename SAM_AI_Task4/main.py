import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("creditcard.csv")

# Use a smaller sample for faster training
df = df.sample(n=10000, random_state=42)

# Features and Target
X = df.drop("Class", axis=1)
y = df["Class"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=30,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

print("=" * 60)
print("Credit Card Fraud Detection")
print("=" * 60)

print(f"Model Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Interactive Prediction
while True:

    choice = input("\nWould you like to test a transaction? (y/n): ")

    if choice.lower() != "y":
        print("\nThank you for using Credit Card Fraud Detection!")
        break

    print("\n1. Test Legitimate Transaction")
    print("2. Test Fraudulent Transaction")

    option = input("\nChoose an option (1/2): ")

    if option == "1":
        sample = X_test[y_test == 0].sample(1, random_state=None)
    elif option == "2":
        sample = X_test[y_test == 1].sample(1, random_state=None)
    else:
        print("\nInvalid choice! Please select 1 or 2.")
        continue

    prediction = model.predict(sample)[0]

    print("\nPrediction Result")

    if prediction == 1:
        print("Fraudulent Transaction")
    else:
        print("Legitimate Transaction")