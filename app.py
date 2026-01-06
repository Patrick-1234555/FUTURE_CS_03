from flask import Flask, render_template, request, send_file
from crypto_utils import encrypt_file, decrypt_file
import os
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    data = file.read()
    encrypted = encrypt_file(data)

    filepath = os.path.join(UPLOAD_FOLDER, file.filename + ".enc")
    with open(filepath, "wb") as f:
        f.write(encrypted)

    return "File uploaded and encrypted successfully!"

@app.route("/download/<filename>")
def download(filename):
    path = os.path.join(UPLOAD_FOLDER, filename + ".enc")

    with open(path, "rb") as f:
        encrypted_data = f.read()

    decrypted = decrypt_file(encrypted_data)
    return send_file(
        BytesIO(decrypted),
        download_name=filename,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)
