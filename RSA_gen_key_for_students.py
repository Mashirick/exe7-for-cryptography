from Crypto.PublicKey import RSA  # provided by pycryptodome

key = RSA.generate(2048)
# TODO
# 导出私钥和公钥， 并输出
private_key = key.export_key()
public_key = key.publickey().export_key()
print('公钥：', public_key.decode())
print('私钥：', private_key.decode())