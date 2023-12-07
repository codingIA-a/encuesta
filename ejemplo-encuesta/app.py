from flask import Flask, session, render_template, redirect, request

app = Flask(__name__)
app.secret_key = 'clave secreta'


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/procesar_datos', methods=['POST'])
def procesar_datos():
    data = {
       'name' : request.form['nombre'],
       'location' : request.form['sedes'],
       'language': request.form['lenguages'],
       'comments' : request.form['comentarios']
    }
    session['datos_usuario'] = data
    return redirect('/resultados')
@app.route('/resultados')
def mostrar_resultados():
    return render_template('resultados.html')
if __name__ == '__main__':
    app.run(debug=True)