from kuznyechik import kuznyechik_encrypt


# plaintext
PT = int('1122334455667700ffeeddccbbaa9988', 16)

# key
k = int('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef', 16)

# Rounds which you want to capture
round=9

# ciphertext
CT = kuznyechik_encrypt(PT, k, round)
print(hex(CT))

# 7f679d90bebc24305a468d42b9d4edcd
# d8e40e4a800d06b2f1b37ea379ead8e
# cd8ef6cd97e0e092a8e4cca61b38bf65