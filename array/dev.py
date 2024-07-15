from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
import base64

# Generate RSA keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
print(private_key)

public_key = private_key.public_key()
print(public_key)

# Convert key to PEM
def convert_to_pem(key):
    pem = key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem.decode('utf-8')

def convert_private_to_pem(private_key):
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem.decode('utf-8')

def convert_pem_to_private_key(pem):
    return serialization.load_pem_private_key(
        pem.encode('utf-8'),
        password=None
    )

def convert_pem_to_public_key(pem):
    return serialization.load_pem_public_key(
        pem.encode('utf-8')
    )

public_pem = convert_to_pem(public_key)
private_pem = convert_private_to_pem(private_key)

# Generate Data Sign
def generate_data_sign(text, private_key):
    signature = private_key.sign(
        text.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode('utf-8')

# Verify Data Sign
def verify_data_sign(text, signature, public_key):
    try:
        public_key.verify(
            base64.b64decode(signature),
            text.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False

# Example usage
data = "Hello, this is a test."
signature = generate_data_sign(data, private_key)
is_valid = verify_data_sign(data, signature, public_key)

print("Public Key:", public_pem)
print("Private Key:", private_pem)
print("Data Signature:", signature)
print("Signature Valid:", is_valid)
