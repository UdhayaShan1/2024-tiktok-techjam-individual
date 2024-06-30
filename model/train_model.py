import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Print current working directory for debugging
print("Current Working Directory:", os.getcwd())

# Define paths
base_dir = os.path.dirname(__file__)
data_path = os.path.join(base_dir, '../data/dataset.csv')
model_path = os.path.join(base_dir, 'ai_model.pkl')
label_encoders_path = os.path.join(base_dir, 'label_encoders.pkl')

# Load the dataset
data = pd.read_csv(data_path)

# Encode categorical variables
label_encoders = {}
for column in data.columns:
    if data[column].dtype == 'object':
        label_encoders[column] = LabelEncoder()
        data[column] = label_encoders[column].fit_transform(data[column])

# Split the dataset
X = data[['interest_area', 'price_preference', 'trendiness', 'design_style', 'recipient', 'location', 'delivery_timeline']]
y = data['recommended_product']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model and label encoders
joblib.dump(model, model_path)
joblib.dump(label_encoders, label_encoders_path)

print("Model and label encoders saved.")
