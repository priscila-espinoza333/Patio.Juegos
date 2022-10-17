from flask import Flask, render_template #importando flask

app = Flask(__name__) # aqui estamos creando nuestra app

@app.route('/play')
def nivel_uno():
    return render_template("index.html", num=3, color="blue") # aqui estoy renderizando 

@app.route('/play/<int:numero>')
def nivel_dos(numero):
    return render_template("index.html", num=numero)

@app.route('/play/<int:numero>/<string:color>')
def nivel_tres(numero, color):
    return render_template("index.html", num=numero, color=color) 






if __name__=="__main__": # aqui lo estamos ejecutando
    app.run(debug=True)