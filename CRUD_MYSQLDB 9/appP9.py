from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
#from flask_fontawesome import FontAwesome

app = Flask(__name__)
#fa = FontAwesome(app)

app.secret_key = 'flash message'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'feli'
app.config['MYSQL_DB'] = 'crud_dbmysql'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM siswa")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', students=data)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data berhasil ditambahkan")

        nama = request.form['nama']
        alamat = request.form['alamat']
        jurusan = request.form['jurusan']
        nohp = request.form['nohp']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO siswa(nama,alamat,jurusan,nohp) VALUES(%s, %s, %s, %s)", (nama, alamat, jurusan, nohp))
        mysql.connection.commit()
        return redirect(url_for('index'))
    
@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        flash('Data Berhasil Diupdate')

        id_data = request.form['id']
        nama = request.form['nama']
        alamat = request.form['alamat']
        jurusan = request.form['jurusan']
        nohp = request.form['nohp']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE siswa
            SET nama=%s, alamat=%s, jurusan=%s, nohp=%s
            WHERE id=%s
        """, (nama, alamat, jurusan, nohp, id_data))
        mysql.connection.commit()
        return redirect(url_for('index'))
    
@app.route('/delete/<string:id_data>', methods=['POST', 'GET'])
def delete(id_data):
    flash('Data Berhasil Dihapus')
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM siswa WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)    