from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    n1 = 1
    n2 = 2
    soma = n1 + n2
    return render_template('home.html', soma = soma)

if __name__== '__main__':
    app.run(debug=True)