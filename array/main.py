# # from cryptography.hazmat.primitives.asymmetric import rsa
# # from cryptography.hazmat.primitives import serialization
# # from cryptography.hazmat.backends import default_backend

# # # Generate RSA private key
# # private_key = rsa.generate_private_key(
# #     public_exponent=65537,
# #     key_size=2048,
# #     backend=default_backend()
# # )

# # # Serialize the private key
# # private_key_pem = private_key.private_bytes(
# #     encoding=serialization.Encoding.PEM,
# #     format=serialization.PrivateFormat.TraditionalOpenSSL,
# #     encryption_algorithm=serialization.NoEncryption()
# # )

# # # Print the private key in PEM format
# # print(private_key_pem.decode('utf-8'))


# # public_key,private_key = rsa.newkeys(1024)

# # with open("public_key.pem","wb") as f:
# #     f.write(public_key.save_pkcs1("PEM"))

# # with open("private_key.pem","wb") as f:
# #     f.write(private_key.save_pkcs1("PEM"))

import rsa
import base64
with open("public_key.pem", "rb") as f:
    public_key = f.read()

# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.backends import default_backend


# public_key = base64.b64decode(pem_public_key)



# print(public_key)
with open("private_key.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Message to sign
message = "Hello"

# Sign the message using UTF-8 encoding
signature = rsa.sign(message.encode('utf-8'), private_key, "SHA-256")
print("Signature:", signature)

# Verify the signature
def verify_signature(message, signature, public_key):
    try:
        rsa.verify(message.encode('utf-8'), signature, public_key)
        return True
    except rsa.VerificationError:
        return False

# Verify the signature
is_valid_signature = verify_signature(message, signature, public_key)
print("Is the signature valid?", is_valid_signature)



# import rsa

# # Generate RSA key pair
# (public_key, private_key) = rsa.newkeys(2048) 
# print(public_key,private_key) # Specify the key size (2048 bits in this example)

# # Convert keys to PEM format
# public_pem = public_key.save_pkcs1().decode('utf-8')
# private_pem = private_key.save_pkcs1().decode('utf-8')

# # Print or use the keys as needed
# print("Public Key:")
# print(public_pem)
# print("\nPrivate Key:")
# print(private_pem)
# import base64
# import rsa
# with open("pbl_public_key.pem", "rb") as f:
#     pem_data = f.read().decode()




# pem_data = str(pem_data)
# # pem_data = pem_data.replace("\\r\\n", "")
# # stripped_key = pem_data.replace("-----BEGIN PUBLIC KEY-----", "").replace("-----END PUBLIC KEY-----", "")
# public_key = base64.b64decode(stripped_key)

# with open("private_key.pem", "rb") as f:
#     private_key = rsa.PrivateKey.load_pkcs1(f.read())


# message = "Hello"

# signature = rsa.sign(message.encode('utf-8'), private_key, "SHA-256")
# print("Signature:", signature)


# # Verify the signature
# def verify_signature(message, signature, public_key):
#     try:
#         rsa.verify(message.encode('utf-8'), signature, public_key)
#         return True
#     except rsa.VerificationError:
#         return False

# # Verify the signature
# is_valid_signature = verify_signature(message, signature, public_key)
# print("Is the signature valid?", is_valid_signature)

# from Crypto.PublicKey import RSA
# from Crypto.Signature import PKCS1_v1_5
# from Crypto.Hash import SHA256
# import base64

# with open("pbl_public_key.pem", "rb") as f:
#     pem_data = f.read()
# print(pem_data)
# decoded_key = base64.b64decode(pem_data)
# public_key = RSA.importKey(decoded_key)
# print(public_key)