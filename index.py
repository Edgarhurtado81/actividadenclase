from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    mayor = None
    menor = None
    error = None

    if request.method == 'POST':
        try:
            a = int(request.form['a'])
            b = int(request.form['b'])
            c = int(request.form['c'])

            if len({a, b, c}) != 3:
                error = "Los valores deben ser distintos."
            else:
                mayor = max(a, b, c)
                menor = min(a, b, c)

        except ValueError:
            error = "ingrese solo números enteros."

    return render_template('ejercicio1.html', mayor=mayor, menor=menor, error=error)

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/notas', methods = ['POST'])
def notas():
    if request.method == 'POST':
        nota = int (request.form['nota'])
        if nota >= 1 and nota <= 9:
            mensaje= "E"
        elif nota >= 10 and nota <= 13:
            mensaje= "D"
        elif nota >= 13 and nota <= 16:
            mensaje= "C"
        elif nota >= 16 and nota <= 19:
            mensaje= "B"
        elif nota >= 19 and nota <= 20:
            mensaje= "A"
        return render_template('ejercicio2.html', resultado=mensaje)
    
@app.route('/ejercicio3')
def ejercicio3():
    return render_template('ejercicio3.html')

@app.route('/Precios', methods = ['POST'])
def Precios():
    if request.method == 'POST':
        Dolar = 1 * 4100
        PrecioA = float (request.form['PrecioA'])
        PrecioB = float (request.form['PrecioB'])
        PrecioC = float (request.form['PrecioC'])
        PrecioD = float (request.form['PrecioD'])
        PrecioE = float (request.form['PrecioE'])
        suma = PrecioA + PrecioB + PrecioC + PrecioD + PrecioE
        Resultado = suma * Dolar
        return render_template('ejercicio3.html', Conversion = Resultado)
    
@app.route('/ejercicio4')
def ejercicio4():
    return render_template('ejercicio4.html')

@app.route('/Desarrollo', methods = ['POST'])
def Desarrollo():
    if request.method == 'POST':
        A = int (request.form['n1'])
        Doble = A * 2 
        Triple = A * 3
        return render_template('ejercicio4.html', A = A, Dob = Doble, Trip = Triple)
    
@app.route('/ejercicio5', methods=['GET', 'POST'])
def ejercicio5():
    figura = None
    Resultado_area = None
    if request.method == 'POST':
        figura = request.form['figura']
        try:
            if figura == 'circulo':
                radio = float(request.form['radio'])
                Resultado_area = 3.14159 * (radio ** 2)
            elif figura == 'cuadrado':
                lado = float(request.form['lado'])
                Resultado_area = lado ** 2
            elif figura == 'rectangulo':
                largo = float(request.form['largo'])
                ancho = float(request.form['ancho'])
                Resultado_area = largo * ancho
            elif figura == 'triangulo':
                base = float(request.form['base'])
                altura = float(request.form['altura'])
                Resultado_area = 0.5 * base * altura
            else:
                return render_template('ejercicio5.html', error="Figura incorrecta.")
        except ValueError:
            return render_template('ejercicio5.html', error="Por favor, ingrese correctos.")

    return render_template('ejercicio5.html', figura = figura, area = Resultado_area)
    

if __name__ == '__main__':
    app.run()