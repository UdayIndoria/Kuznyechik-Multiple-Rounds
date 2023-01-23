from kuznyechik import kuznyechik_encrypt, kuznyechik_decrypt


# plaintext
PT = int('1122334455667700ffeeddccbbaa9988', 16)

# key
k = int('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef', 16)

# ciphertext
CT = kuznyechik_encrypt(PT, k)
print(hex(CT))

# decrypted text
DT = kuznyechik_decrypt(CT, k)
print(hex(DT))

# The plaintext should equal the decrypted text. 
print(PT == DT)