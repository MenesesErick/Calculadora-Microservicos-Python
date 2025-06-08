from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/somar', methods=['GET'])
def somar():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        resultado = a + b
        return jsonify({'resultado': resultado})
    except (TypeError, ValueError):
        return jsonify({'erro': 'Parâmetros inválidos. Forneça dois números.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)