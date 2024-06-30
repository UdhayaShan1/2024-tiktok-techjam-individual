from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__)

# Load the trained model and label encoders
model = joblib.load(os.path.join(os.path.dirname(__file__), '../model/ai_model.pkl'))
label_encoders = joblib.load(os.path.join(os.path.dirname(__file__), '../model/label_encoders.pkl'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    print(data)
    encoded_data = []
    for field in ['interest_area', 'price_preference', 'trendiness', 'design_style', 'recipient', 'location', 'delivery_timeline']:
        encoded_data.append(label_encoders[field].transform([data[field]])[0])
    
    prediction = model.predict([encoded_data])[0]
    recommended_product = label_encoders['recommended_product'].inverse_transform([prediction])[0]
    
    return jsonify({'recommended_product': recommended_product})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
