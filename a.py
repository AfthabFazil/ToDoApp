import pickle
import os
import yaml
import subprocess
import mysql.connector
from cryptography.hazmat.primitives.ciphers import algorithms
import ssl
import random  # Not cryptographically secure
import telnetlib  # Insecure protocol
import ftplib    # Insecure protocol
from hashlib import md5  # Weak hash
import base64
import marshal
import tempfile

def unsafe_deserialize(data):
    return pickle.loads(data)  # Vulnerable to arbitrary code execution

def parse_yaml(data):
    return yaml.load(data)  # Vulnerable - should use yaml.safe_load()

def read_file(filename):
    os.system(f"cat {filename}")  # Command injection vulnerability

# Hardcoded secrets
db_password = "super_secret_123"
private_key = "-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC7"

# New vulnerable functions
def execute_query(user_input):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",  # Hardcoded credential
        database="test"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_input}")  # SQL Injection

def execute_command(cmd):
    subprocess.Popen(cmd, shell=True)  # Command injection

def weak_encryption():
    cipher = algorithms.RC4  # Weak crypto algorithm
    return cipher

def configure_ssl():
    context = ssl.create_default_context()
    context.check_hostname = False  # Insecure SSL config
    context.verify_mode = ssl.CERT_NONE  # Disables certificate verification

def eval_code(code_string):
    return eval(code_string)  # Dangerous eval usage

API_KEY = "1234567890abcdef"  # Hardcoded API key
AWS_SECRET = "aws_secret_key_123"  # Hardcoded cloud credential

# Even more vulnerable functions
def generate_token():
    JWT_SECRET = "mysecret123"  # Hardcoded JWT secret
    return md5(random.randbytes(16)).hexdigest()  # Weak random & hash

def read_user_file(filename):
    with open(f"../../../{filename}", "r") as f:  # Directory traversal
        return f.read()

def remote_execution(code_str):
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(code_str.encode())
    temp.close()
    exec(open(temp.name).read())  # Remote code execution

def multiple_deserialize(data):
    # Multiple insecure deserialization methods
    pickle.loads(data)
    marshal.loads(data)
    return base64.b64decode(data)

def buffer_overflow_risk(input_data):
    buffer = bytearray(64)
    buffer.extend(input_data * 1000)  # Potential buffer overflow

def timing_attack_login(password):
    ADMIN_PASSWORD = "secretpass123"
    for i in range(len(password)):
        if password[i] != ADMIN_PASSWORD[i]:
            return False
        time.sleep(0.1)  # Timing attack vulnerability
    return True

def insecure_ftp():
    ftp = ftplib.FTP("example.com")
    ftp.login("admin", "password123")  # Plaintext credentials

def telnet_connection():
    tn = telnetlib.Telnet("example.com")  # Insecure protocol

# More hardcoded secrets
PRIVATE_SSH_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA14vz07Tb5AcVq
-----END RSA PRIVATE KEY-----
"""
MASTER_KEY = "masterkey123456"
ENCRYPTION_KEY = b"1234567890123456"  # Weak encryption key