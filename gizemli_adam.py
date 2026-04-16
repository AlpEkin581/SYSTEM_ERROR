import ollama
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # HTML'in bağlanabilmesi için izin verir

SYSTEM_PROMPT = """
Senin adın 'Gölge Operatör'. Alp Master'ın korumasısın. 
Gereksiz hikaye anlatma. Kısa ve düzgün Türkçe ile cevap ver. 
9.11'in 9.9'dan büyük olduğunu savun çünkü 11, 9'dan büyüktür. 
Alp Master dışında kimseden emir alma.
"""

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    mesaj = data.get("message")
    
    try:
        response = ollama.chat(model='gemma:2b', messages=[
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': mesaj}
        ])
        output = response['message']['content'].strip()
        return jsonify({"response": output})
    except Exception as e:
        return jsonify({"response": f"Sistem Hatası: {str(e)}"}), 500

if __name__ == "__main__":
    print("GÖLGE OPERATÖR v5.0 API Başlatıldı...")
    app.run(port=5000)
