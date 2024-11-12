from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database connection
def get_db_connection():
    return pymysql.connect(host='localhost', user='root', password='', db='your_database')

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return render_template('Index_nim.html', books=books)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        stok = request.form['stok']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (kode, nama, harga, stok) VALUES (%s, %s, %s, %s)", (kode, nama, harga, stok))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('Tambah_nim.html')

@app.route('/edit/<int:id_buku>', methods=['GET', 'POST'])
def edit(id_buku):
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        stok = request.form['stok']
        cursor.execute("UPDATE books SET kode=%s, nama=%s, harga=%s, stok=%s WHERE id=%s", (kode, nama, harga, stok, id_buku))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM books WHERE id=%s", (id_buku,))
        book = cursor.fetchone()
        conn.close()
        return render_template('Edit_nim.html', book=book)

@app.route('/delete/<int:id_buku>')
def delete(id_buku):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=%s", (id_buku,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
