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
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Formula matematica calculo de promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # variable condicional si el promedio es >4 o no.
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

    return render_template('ejercicio1.html', prom=promedio, estado=estado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mayor = ""
    largo = 0

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Busqueda de la palabra mas larga
        if len(nombre1) >= len(nombre2) and len(nombre1) >= len(nombre3):
            mayor = nombre1
        elif len(nombre2) >= len(nombre1) and len(nombre2) >= len(nombre3):
            mayor = nombre2
        else:
            mayor = nombre3

        largo = len(mayor)

    return render_template('ejercicio2.html', mayor=mayor, largo=largo)


if __name__ == '__main__':
    app.run(debug=True)