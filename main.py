from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_dolar', methods=['POST'])
def calcular_dolar():
    dolar = 5.68
    real = float(request.form['real'])
    convertido = real/dolar

    return render_template('index.html', convertido=convertido)
if __name__ =='__main__':
    app.run(debug=True)