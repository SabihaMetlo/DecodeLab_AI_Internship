# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

# Features and labels
X = iris.data
y = iris.target

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, predictions)

# Print results
print("Predictions:", predictions)
print("Actual:", y_test)
print("Accuracy:", accuracy)