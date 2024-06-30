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

client = OpenAI(
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
    7. Delivery Timeline
    
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

    
    return chat_completion.choices[0].message.content

text = "I'm looking for a professional kitchen gadget that I can get delivered to Singapore in about a week. My budget is low, and I prefer mainstream products. It's for myself."
print(extract_user_circumstances(text))

