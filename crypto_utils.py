from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
import hashlib

def derive_key(password, salt):
    """
    Derive a 32-byte key from password and salt using PBKDF2.
    Returns:
        bytes: Derived 32-byte key
    """
    return PBKDF2(password, salt, dkLen=32, count=200000)

def hash_password(password, salt):
    """
    Hash the password with salt using SHA-256.
    Returns:
        str: Hexadecimal hash of password + salt
    """
    return hashlib.sha256(password.encode() + salt).hexdigest()

def encrypt_file(data, password):
    """
    Encrypt file data using AES-256-CBC with PBKDF2 key derivation.
    Returns:
        bytes: Salt + IV + encrypted data
    """
    salt = get_random_bytes(16)
    key = derive_key(password, salt)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data, AES.block_size))
    return salt + iv + encrypted

def decrypt_file(data, password, salt):
    """
    Decrypt file data using AES-256-CBC.
    Returns:
        bytes: Decrypted file data
    """
    key = derive_key(password, salt)
    iv = data[16:32]
    encrypted_data = data[32:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted_data), AES.block_size)
