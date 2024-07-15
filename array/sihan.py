# import base64
# import xml.etree.ElementTree as ET
# from cryptography.hazmat.primitives.asymmetric import rsa
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.backends import default_backend


# with open("pbl_public_key.pem", "rb") as f:
#     pem_public_key = f.read()

# stripped_key = pem_public_key.strip().replace(b"-----BEGIN PUBLIC KEY-----", b"").replace(b"-----END PUBLIC KEY-----", b"")
# decoded_key = base64.b64decode(stripped_key)
# xml_key = ET.fromstring(decoded_key)
# modulus = int.from_bytes(base64.b64decode(xml_key.find('Modulus').text), byteorder='big')
# exponent = int.from_bytes(base64.b64decode(xml_key.find('Exponent').text), byteorder='big')
# public_numbers = rsa.RSAPublicNumbers(exponent, modulus)
# public_key = public_numbers.public_key(default_backend())
# pem_public_key = public_key.public_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PublicFormat.SubjectPublicKeyInfo
# )

# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.asymmetric import padding
# data = b"Message to verify"
# signature = b"...signature bytes..."

# try:
#     public_key.verify(
#         signature,
#         data,
#         padding.PSS(
#             mgf=padding.MGF1(hashes.SHA256()),
#             salt_length=padding.PSS.MAX_LENGTH
#         ),
#         hashes.SHA256()
#     )
#     print("Signature is valid.")
# except Exception as e:
#     print(f"Signature verification failed: {e}")


import base64
import xml.etree.ElementTree as ET
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


with open("pbl_public_key.pem", "rb") as f:
    pem_public_key = f.read()


stripped_key = pem_public_key.strip().replace(b"-----BEGIN PUBLIC KEY-----", b"").replace(b"-----END PUBLIC KEY-----", b"")
decoded_key = base64.b64decode(stripped_key)


xml_key = ET.fromstring(decoded_key)
modulus = int.from_bytes(base64.b64decode(xml_key.find('Modulus').text), byteorder='big')
exponent = int.from_bytes(base64.b64decode(xml_key.find('Exponent').text), byteorder='big')


public_key = RSA.construct((modulus, exponent))

data = b"Message to verify"
signature = b"...signature bytes..."

try:
   
    h = SHA256.new(data)
    
    
    pkcs1_15.new(public_key).verify(h, signature)
    print("Signature is valid.")
except (ValueError, TypeError):
    print("Signature verification failed.")



##b'<RSAKeyValue><Modulus>62pik+D/Q3KB54QZ9ByBhaCWeErHDCTnZNwro+Bp50k7Hvh+g9plWuf0ETbkmCc4p9CjB2RW9PCh2mSaJdu+OdNfDIdfBlYfcZN9xFUWhMr2Qy
# J9asVTUPUBeS90Fk55QXu0h/iBx3Z107i+UJaawSwH7K4lZ/MS37dwHaC92N/WLyj4q5DEGqo5FPmaHTld06JoUioJGnhb2cbDtFPViemKJO3+H9cD7Iz2fJ6BSEbpD+ko3jwgxjPbUsUeddwpF
# GqFidwYOoDq8vLfZ6kGTkLBA1Izno8IeHJC2gXf42xzuMCPSPRaT35zod+BW5YdqlO1DJLBL2WtirPOApEB0Q==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>'