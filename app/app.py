from flask import Flask, request, jsonify, render_template
import joblib
import os

from openai import OpenAI
import openai
import os

def read_key_from_file(filename):
    try:
        with open(filename, 'r') as file:
            key = file.read().strip()
            return key
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"Error reading key from file '{filename}': {e}")

base_dir = os.path.dirname(__file__)
api_path = os.path.join(base_dir, '../secrets/api.txt')

#Change this to env variable when deploying
client = OpenAI(
    #api_key = read_key_from_file(os.getenv('API_KEY_FILE'))
    api_key = read_key_from_file(api_path)
)


def extract_user_circumstances(text):
    prompt = f"""
    Extract the following user circumstances from the text:
    1. Interest Area
    2. Price Preference
    3. Trendiness
    4. Design Style
    5. Recipient
    6. Location
    7. Delivery Timeline in days
    
    Text: {text}
    
    Example output:
    {{
        "interest_area": "cooking",
        "price_preference": "low",
        "trendiness": "mainstream",
        "design_style": "professional",
        "recipient": "yourself",
        "location": "Singapore",
        "delivery_timeline": "14"
    }}
    
    Output:
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role" : "user",
                "content" : prompt
            }
        ],
        model="gpt-3.5-turbo"
    )

    
    return chat_completion.choices[0].message.content.strip()

app = Flask(__name__)

# Load the trained model and label encoders
model = joblib.load(os.path.join(base_dir, '../model/ai_model.pkl'))
label_encoders = joblib.load(os.path.join(base_dir, '../model/label_encoders.pkl'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    print(data)

    encoded_data = []
    for field in ['interest_area', 'price_preference', 'trendiness', 'design_style', 'recipient', 'location']:
        if data[field] in label_encoders[field].classes_:
            encoded_data.append(label_encoders[field].transform([data[field]])[0])
        else:
            encoded_data.append(label_encoders[field].transform(['unknown'])[0])
    
    # Directly append the numerical value for delivery_timeline
    encoded_data.append(int(data['delivery_timeline']))
    
    prediction = model.predict([encoded_data])[0]
    recommended_product = label_encoders['recommended_product'].inverse_transform([prediction])[0]
    
    return jsonify({'recommended_product': recommended_product})

@app.route('/nlp_predict', methods=['POST'])
def nlp_parse():
    userInput = request.json.get('text')
    parsedPrompt = extract_user_circumstances(userInput)
    print(parsedPrompt)
    parsed_json = eval(parsedPrompt)  # Convert string to JSON object
    return jsonify(parsed_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)