import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
df = pd.read_csv("spam.csv", encoding="latin-1")

# Keep only required columns
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# Convert labels into numbers
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Features and Labels
X = df['message']
y = df['label']

# Convert text into TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

print("=" * 50)
print("Spam SMS Detection")
print("=" * 50)
print(f"Model Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# User Testing
while True:
    print("\nEnter an SMS message")
    sms = input("> ")

    sms_vector = vectorizer.transform([sms])
    result = model.predict(sms_vector)[0]

    if result == 1:
        print("\nPrediction: SPAM")
    else:
        print("\nPrediction: HAM (Legitimate Message)")

    choice = input("\nDo you want to test another message? (y/n): ")

    if choice.lower() != "y":
        print("\nThank you for using Spam SMS Detection!")
        break