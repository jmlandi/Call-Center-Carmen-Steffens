from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/comercial')
def comercial():
  return render_template('comercial.html')

@app.route('/faturamento')
def faturamento():
  return render_template('faturamento.html')

@app.route('/tutoriais')
def tutoriais():
  return render_template('tutoriais.html')

@app.route('/marketing')
def marketing():
  return render_template('marketing.html')

@app.route('/consertos')
def consertos():
  return render_template('consertos.html')

@app.route('/financeiro')
def financeiro():
  return render_template('financeiro.html')

@app.route('/gestor')
def gestor():
  return render_template('gestor.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
