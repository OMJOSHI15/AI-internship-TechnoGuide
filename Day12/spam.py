from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
texts = [
    "Win money now",
    "Claim your free prize",
    "Hello friend",
    "Let's meet tomorrow",
    "Free recharge available",
    "How are you"
]

labels = [
    "spam",
    "spam",
    "ham",
    "ham",
    "spam",
    "ham"
]

# Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Test message
test_message = ["Free money offer"]

test_X = vectorizer.transform(test_message)

prediction = model.predict(test_X)

print("Message:", test_message[0])
print("Prediction:", prediction[0])