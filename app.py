from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def home():
    return "Norma Translator жұмыс істеп тұр"

@app.route('/translate', methods=['POST'])
def translate():
    text = request.json.get("text", "")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Заң мәтінін қарапайым тілде түсіндір, қысқаша қорытынды және мысал келтір"},
            {"role": "user", "content": text}
        ]
    )

    return jsonify({"result": response.choices[0].message.content})
