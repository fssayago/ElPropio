from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "HOLA, buen día Luz Elena, Teresa y Franklin usando Flask en Vercel"


@app.route('/about')
def about():
    return "HOLA About"
    
if __name__ == '__main__':
    app.run(debug=True) 
    
