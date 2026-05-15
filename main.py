from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = ""
    totalcomprapinturas = 0
    totalcomprafinal = 0
    totaldscto= 0
    descuento = 0

    if request.method == 'POST':
        # Se ingresan datos en formato de Enteros y son guardados.
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        cantidadpinturas = int(request.form['cantidadpinturas'])

        # Formula matematica calculo del total$
        preciotarropintura = 9000
        totalcomprapinturas = preciotarropintura * cantidadpinturas

        # variable condicional de descuentos.
        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0
            print ("no hay descuento")

        totaldscto = totalcomprapinturas * descuento
        totalcomprafinal = totalcomprapinturas - totaldscto

    return render_template('ejercicio1.html', nombre=nombre, totalcomprapinturas=totalcomprapinturas, totalcomprafinal=totalcomprafinal, totaldscto=totaldscto, descuento=descuento)
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""

    if request.method == 'POST':
        nombreusuario = request.form['nombreusuario']
        contraseña= request.form['contraseña']

        # autentificacion de usuario
        if nombreusuario == "juan" and contraseña =="admin":
            mensaje = f"Bienvenido Administrador {nombreusuario}"
        elif nombreusuario == "pepe" and contraseña == "user":
            mensaje = f"Bienvenido Usuario {nombreusuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)