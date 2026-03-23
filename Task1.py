import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# -------------------------------
# Step 1: Create Dataset
# -------------------------------
data = {
    'message': [
        'Win money now',
        'Hello friend',
        'Free offer just for you',
        'Call me today',
        'Earn cash fast',
        'Meeting tomorrow',
        'Congratulations you won a prize',
        'Let us discuss project',
        'Limited time offer',
        'Are you available for meeting'
    ],
    'label': [
        'spam', 'ham', 'spam', 'ham', 'spam',
        'ham', 'spam', 'ham', 'spam', 'ham'
    ]
}

df = pd.DataFrame(data)

# -------------------------------
# Step 2: Convert Labels
# -------------------------------
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# -------------------------------
# Step 3: Convert Text to Numbers
# -------------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['message'])
y = df['label']

# -------------------------------
# Step 4: Train Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Step 5: Train Model
# -------------------------------
model = MultinomialNB()
model.fit(X_train, y_train)

# -------------------------------
# Step 6: Check Accuracy
# -------------------------------
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# -------------------------------
# Step 7: Take User Input
# -------------------------------
while True:
    user_input = input("\nEnter message (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Exiting...")
        break

    # Transform input
    test_vec = vectorizer.transform([user_input])

    # Predict
    prediction = model.predict(test_vec)

    if prediction[0] == 1:
        print("Result: Spam ❌")
    else:
        print("Result: Not Spam ✅")