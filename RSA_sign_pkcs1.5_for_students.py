from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii

# Generate 1024-bit RSA key pair (private + public key)
keyPair = RSA.generate(bits=1024)
pubKey = keyPair.publickey()

# Sign the message using the PKCS#1 v1.5 signature scheme (RSASP1)
msg = b'Message for RSA signing'
hash = SHA256.new(msg)

# TODO
# 用 PKCS115_SigScheme 签名
priKey = keyPair
pub_cipher = PKCS115_SigScheme(priKey)
signature = pub_cipher.sign(hash)

print("Signature:", binascii.hexlify(signature))

# Verify valid PKCS#1 v1.5 signature (RSAVP1)
msg = b'Message for RSA signing'
hash = SHA256.new(msg)

try:
    # TODO 
    # 验证签名
    pub_cipher.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")

# Verify invalid PKCS#1 v1.5 signature (RSAVP1)
msg = b'A tampered message'
hash = SHA256.new(msg)

try:
    # TODO
    # 验证假签名
    pub_cipher.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")