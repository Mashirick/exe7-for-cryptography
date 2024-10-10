from Crypto.PublicKey import RSA  # provided by pycryptodome

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

print('private key:')
print(private_key.decode())
print('public key:')
print(public_key.decode())

# RSA sign the message
msg = b'A message for signing'
from hashlib import sha512
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')

# TODO
# 用 sig = m^d mod n 签名

d = key.d
n = key.n
e = key.e

signature = pow(hash, d, n)
print("Signature:", hex(signature))

# RSA verify signature
msg = b'A message for signing'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')

# TODO
# 用 sig^e == m 验证签名
hashFromSignature = pow(signature, e, n)
print("Signature valid:", hash == hashFromSignature)
