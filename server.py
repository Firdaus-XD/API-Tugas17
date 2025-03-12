from flask import Flask
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def get_data():
    data = {
        "tema": "Daftar Buku Fiksi",
        "deskripsi": "Kumpulan buku fiksi populer",
        "buku": [
            {"judul": "Harry Potter dan Batu Bertuah", "penulis": "J.K. Rowling"},
            {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata"},
            {"judul": "Negeri 5 Menara", "penulis": "Ahmad Fuadi"}
        ]
    }
    return json.dumps(data) 

if __name__ == '__main__':
    app.run(debug=True)
