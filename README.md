# Secure File Sharing Application

# live link 

   ```bash
   https://obald.pythonanywhere.com/ 
   ```
https://obald.pythonanywhere.com/ 

A Flask-based web application for secure file sharing with password-based encryption. Files are encrypted using AES-256 before storage and can only be decrypted with the correct password.

## Features

- **Secure Upload**: Upload files with password protection
- **AES-256 Encryption**: Files are encrypted using industry-standard AES-256-CBC
- **Password Verification**: Passwords are hashed and verified for download access
- **Web Interface**: Clean, responsive UI for easy file management
- **Local Storage**: Files stored securely on the server

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone or download the project files
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open your browser and go to `http://localhost:5000`

3. **Upload Files**:
   - Select a file
   - Enter a password
   - Click "Upload File"
   - Files are encrypted and stored securely

4. **Download Files**:
   - Enter the filename
   - Provide the correct password
   - File is decrypted and downloaded

## Security Notes

- Files are encrypted with AES-256 using PBKDF2 key derivation
- Passwords are hashed with SHA-256 and salt
- Encrypted files are stored on the server; ensure server security
- This is for demonstration purposes; use HTTPS in production

## Project Structure

```
├── app.py                 # Main Flask application
├── crypto_utils.py        # Encryption/decryption utilities
├── templates/
│   ├── index.html         # Main upload/download interface
│   └── download.html      # Alternative download page
├── static/
│   └── style.css          # CSS styling
├── uploads/               # Encrypted file storage (created automatically)
├── file_metadata.json     # Password hashes and salts
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Dependencies

- Flask: Web framework
- PyCryptoDome: Cryptographic functions
- Other dependencies in `requirements.txt`

## License

This project is for educational purposes.
