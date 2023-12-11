from flask import Flask, render_template, request,redirect, send_from_directory
import os
from flaskext.mysql import MySQL

# from datetime import datetime 
app=Flask(__name__)
CARPETA= os.path.join('uploads')
app.config['CARPETA']=CARPETA

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_BD']='usuario'
mysql.init_app(app)

@app.route("/")
def usuario():
    sql = "SELECT * FROM `usuario`.`inscribite`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    db_inscribite=cursor.fetchall()
    # print(inscribite)
    conn.commit()
    return render_template('usuario.html',inscribite = db_inscribite)

@app.route('/create')
def create():
    return render_template('usuario.html')


@app.route('/store',methods=['POST'])
def storage():
    _nombre=request.form['txtnombre']
    _correo=request.form['txtemail']
    _Foto=request.files['txtFoto']
#     now= datetime.now()
#     tiempo= now.strftime("%Y%H%M%S")
#     if _foto.filename!='':
#         nuevoNombreFoto=tiempo+_foto.filename
#         _foto.save("uploads/"+nuevoNombreFoto)

    datos=(_nombre,_correo,_Foto)
    sql = "INSERT INTO `usuario`.`inscribite` (`id`, `Nombre y Apellido`, `Correo Electrónico`, `Comprobante de Pago`) VALUES (NULL, %s, %s, %s);"
    # datos=(_nombre,_correo,nuevoNombreFoto)

    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('/')
    

@app.route("/destroy/<int:id>")
def destroy(id):
    conn=mysql.connect()
    cursor=conn.cursor()
#     sql="DELETE FROM `usuario`.`inscribite` WHERE id=%s"
    cursor.execute("DELETE FROM `usuario`.`inscribite` WHERE id=%s",(id))
    conn.commit()
    return redirect("/")


@app.route("/edit/<int:id>")
def edit(id):
#     sql = "SELECT * FROM `usuario`.`inscribite` WHERE id=%s;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM `usuario`.`inscribite` WHERE id=%s",(id))
    inscribite=cursor.fetchall()
    conn.commit()
    
    # print(inscribite)
    return render_template('edit.html',inscribite=inscribite)

@app.route('/update', methods=['POST'])
def update():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _Foto=request.files['txtFoto']
    id=request.form['txtID']
    sql = "UPDATE `usuario`.`inscribite` SET `Nombre y Apellido`=%s, `Correo Electrónico`=%s WHERE id=%s;"
    datos=(_nombre,_correo,_Foto,id)
    conn = mysql.connect()
    cursor = conn.cursor()
    
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')

@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'], nombreFoto)

if __name__=="__main__":
    app.run(debug=True, port=5001)