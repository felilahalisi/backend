from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Direktori untuk menyimpan file yang diupload
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Pastikan folder 'uploads' ada
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Cek apakah file telah diupload
        if 'file' not in request.files:
            return "Tidak ada file yang diupload"
        
        file = request.files['file']

        # Jika nama file kosong
        if file.filename == '':
            return "File tidak memiliki nama"
        
        # Simpan file ke direktori tujuan
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return f"File berhasil diupload: {file_path}"
    
    # Render template upload HTML
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
