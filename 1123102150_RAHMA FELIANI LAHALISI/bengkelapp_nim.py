from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    user="root",
    password="feli",
    database="bengkel_nim"
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM sparepart_nim")
    spareparts = cursor.fetchall()
    return render_template('index_nim.html', spareparts=spareparts)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        kode = request.form['Kode_sparepart']
        nama = request.form['Nama_sparepart']
        merk = request.form['Merk']
        stok = request.form['Jumlah_stok']
        cursor = db.cursor()
        cursor.execute("INSERT INTO sparepart_nim (Kode_sparepart, Nama_sparepart, Merk, Jumlah_stok) VALUES (%s, %s, %s, %s)",
                       (kode, nama, merk, stok))
        db.commit()
        return redirect(url_for('index'))
    return render_template('tambah_nim.html')

@app.route('/edit/<string:kode>', methods=['GET', 'POST'])
def edit(kode):
    cursor = db.cursor()
    if request.method == 'POST':
        nama = request.form['Nama_sparepart']
        merk = request.form['Merk']
        stok = request.form['Jumlah_stok']
        cursor.execute("UPDATE sparepart_nim SET Nama_sparepart=%s, Merk=%s, Jumlah_stok=%s WHERE Kode_sparepart=%s",
                       (nama, merk, stok, kode))
        db.commit()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM sparepart_nim WHERE Kode_sparepart=%s", (kode,))
    sparepart = cursor.fetchone()
    return render_template('edit_nim.html', sparepart=sparepart)

@app.route('/hapus/<string:kode>')
def hapus(kode):
    cursor = db.cursor()
    cursor.execute("DELETE FROM sparepart_nim WHERE Kode_sparepart=%s", (kode,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
