from datetime import datetime
from distutils.log import debug
from urllib.robotparser import RequestRate
from flask import Flask, request, render_template, make_response
import pdfkit
import pdfkit
from pdfkit.api import configuration

wkhtml_path = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
options = {
    'page-size': 'Letter',
    'encoding': "UTF-8",
    'no-outline': None
}

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        numero1 = request.form.get("Numero1")
        nombre1 = request.form.get("Nombre1")
        apellido1 = request.form.get("Apellido1")
        direccion1 = request.form.get("Direccion1")
        comuna1 = request.form.get("Comuna1")
        telefono1 = request.form.get("Telefono1")
        correo1 = request.form.get("Correo1")
        numero2 = request.form.get("Numero2")
        nombre2 = request.form.get("Nombre2")       
        apellido2 = request.form.get("Apellido2")
        direccion2 = request.form.get("Direccion2")
        comuna2 = request.form.get("Comuna2")
        telefono2 = request.form.get("Telefono2")
        correo2 = request.form.get("Correo2")
        numero3 = request.form.get("Numero3")
        nombre3 = request.form.get("Nombre3")
        apellido3 = request.form.get("Apellido3")
        direccion3 = request.form.get("Direccion3")
        comuna3 = request.form.get("Comuna3")
        telefono3 = request.form.get("Telefono3")
        correo3 = request.form.get("Correo3")
        numero4 = request.form.get("Numero4")
        nombre4 = request.form.get("Nombre4")
        apellido4 = request.form.get("Apellido4")
        direccion4 = request.form.get("Direccion4")
        comuna4 = request.form.get("Comuna4")
        telefono4 = request.form.get("Telefono4")
        correo4 = request.form.get("Correo4")
        numero5 = request.form.get("Numero5")
        nombre5 = request.form.get("Nombre5")
        apellido5 = request.form.get("Apellido5")
        direccion5 = request.form.get("Direccion5")
        comuna5 = request.form.get("Comuna5")
        telefono5 = request.form.get("Telefono5")
        correo5 = request.form.get("Correo5")
        numero6 = request.form.get("Numero6")
        nombre6 = request.form.get("Nombre6")
        apellido6 = request.form.get("Apellido6")
        direccion6 = request.form.get("Direccion6")
        comuna6 = request.form.get("Comuna6")
        telefono6 = request.form.get("Telefono6")
        correo6 = request.form.get("Correo6")
        numero7 = request.form.get("Numero7")
        nombre7 = request.form.get("Nombre7")
        apellido7 = request.form.get("Apellido7")
        direccion7 = request.form.get("Direccion7")
        comuna7 = request.form.get("Comuna7")
        telefono7 = request.form.get("Telefono7")
        correo7 = request.form.get("Correo7")
        numero8 = request.form.get("Numero8")
        nombre8 = request.form.get("Nombre8")
        apellido8 = request.form.get("Apellido8")
        direccion8 = request.form.get("Direccion8")
        comuna8 = request.form.get("Comuna8")
        telefono8 = request.form.get("Telefono8")
        correo8 = request.form.get("Correo8")
    
        html = render_template('var.html',Numero1=numero1,Nombre1=nombre1,Apellido1=apellido1,Direccion1=direccion1,Comuna1=comuna1,Telefono1=telefono1,Correo1=correo1,Numero2=numero2,Nombre2=nombre2,Apellido2=apellido2,Direccion2=direccion2,Comuna2=comuna2,Telefono2=telefono2,Correo2=correo2,Numero3=numero3,Nombre3=nombre3,Apellido3=apellido3,Direccion3=direccion3,Comuna3=comuna3,Telefono3=telefono3,Correo3=correo3,Numero4=numero4,Nombre4=nombre4,Apellido4=apellido4,Direccion4=direccion4,Comuna4=comuna4,Telefono4=telefono4,Correo4=correo4,Numero5=numero5,Nombre5=nombre5,Apellido5=apellido5,Direccion5=direccion5,Comuna5=comuna5,Telefono5=telefono5,Correo5=correo5,Numero6=numero6,Nombre6=nombre6,Apellido6=apellido6,Direccion6=direccion6,Comuna6=comuna6,Telefono6=telefono6,Correo6=correo6,Numero7=numero7,Nombre7=nombre7,Apellido7=apellido7,Direccion7=direccion7,Comuna7=comuna7,Telefono7=telefono7,Correo7=correo7,Numero8=numero8,Nombre8=nombre8,Apellido8=apellido8,Direccion8=direccion8,Comuna8=comuna8,Telefono8=telefono8,Correo8=correo8)
        pdf = pdfkit.from_string(html, False, configuration = wkhtml_path, options = options, css = "templates/style.css")

        response = make_response(pdf)
        response.headers["Content-Type"] = "application/pdf"
        name = 'etiquetas'+datetime.now()+'.pdf'
        response.headers["Content-Disposition"] = "inline; filename=%s" % name

        return response

 
    return render_template("form.html")


if (__name__ == '__main__'):
    app.run(debug = True)