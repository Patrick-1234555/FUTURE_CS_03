from flask import Flask, render_template, request, send_file, redirect, url_for
from crypto_utils import encrypt_file, decrypt_file, hash_password
import os, json
from io import BytesIO
from base64 import b64encode, b64decode

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
META_FILE = "file_metadata.json"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

if not os.path.exists(META_FILE):
    with open(META_FILE, "w") as f:
        json.dump({}, f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    password = request.form["password"]

    data = file.read()
    encrypted = encrypt_file(data, password)

    with open(os.path.join(UPLOAD_FOLDER, file.filename), "wb") as f:
        f.write(encrypted)

    salt = encrypted[:16]
    metadata = json.load(open(META_FILE))

    metadata[file.filename] = {
        "password_hash": hash_password(password, salt),
        "salt": b64encode(salt).decode()
    }

    json.dump(metadata, open(META_FILE, "w"), indent=2)

    return redirect(url_for("download_page", filename=file.filename))

@app.route("/download/<filename>")
def download_page(filename):
    return render_template("download.html", filename=filename)

@app.route("/download_file", methods=["POST"])
def download_file():
    filename = request.form["filename"]
    password = request.form["password"]

    metadata = json.load(open(META_FILE))
    file_info = metadata.get(filename)

    if not file_info:
        return "File not found"

    salt = b64decode(file_info["salt"])
    if hash_password(password, salt) != file_info["password_hash"]:
        return "Incorrect password"

    with open(os.path.join(UPLOAD_FOLDER, filename), "rb") as f:
        encrypted = f.read()

    decrypted = decrypt_file(encrypted, password, salt)

    return send_file(
        BytesIO(decrypted),
        download_name=filename,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)
