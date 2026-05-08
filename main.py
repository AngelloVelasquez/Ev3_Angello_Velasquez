from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = ""

    if request.method == 'POST':
        # Se ingresan datos en formato decimal y son guardados.
        n1 = float(request.form['nota1'])
        n2 = float(request.form['nota2'])
        n3 = float(request.form['nota3'])
        asis = float(request.form['asistencia'])

        # Formula
        promedio = (n1 + n2 + n3) / 3

        # variable condicional
        if promedio >= 40 and asis >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

    return render_template('ejercicio1.html', prom=promedio, estado=estado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mayor = ""
    largo = 0

    if request.method == 'POST':
        nom1 = request.form['nombre1']
        nom2 = request.form['nombre2']
        nom3 = request.form['nombre3']

        # Busqueda de la palabra mas larga
        if len(nom1) >= len(nom2) and len(nom1) >= len(nom3):
            mayor = nom1
        elif len(nom2) >= len(nom1) and len(nom2) >= len(nom3):
            mayor = nom2
        else:
            mayor = nom3

        largo = len(mayor)

    return render_template('ejercicio2.html', mayor=mayor, largo=largo)


if __name__ == '__main__':
    app.run(debug=True)