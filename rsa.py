# rsa implementation
#!/usr/bin/env python3
# Path: rsa.py

import key
import math
import re

# message 为全长明文
# 将 message 分 times 组，每组 i 个

# 测试
DEBUG = 2

# 将字符串切割成 list
def cut_text(text,lenth):
    text_arr = re.findall('.{'+str(lenth)+'}', text)
    text_arr.append(text[(len(text_arr)*lenth):])
    return text_arr

# 将 bytes 切割成 list
def cut_bytes(bytes, length):
    arr = [bytes[i:i+length] for i in range(0, len(bytes), length)]
    return arr
        
# 不分组的 RSA 加密, 只能加密小于等于 i bytes 的明文
def encrypt_short(key, message: bytes):
    # 将明文转成十六进制
    message_in_hex = message.hex()
    # 将十六进制转成十进制
    message_in_dec = int(message_in_hex, 16)
    # 使用十进制加密
    enc = pow(message_in_dec, key[0], key[1])

    cipher = enc.to_bytes(math.ceil(enc.bit_length() / 8), byteorder='big')
    return cipher

# 不分组的 RSA 解密
def decrypt_short(key, cipher: bytes):
    # 将明文转成十六进制
    cipher_in_hex = cipher.hex()
    print(cipher_in_hex)
    # 将十六进制转成十进制
    cipher_in_dec = int(cipher_in_hex, 16)
    # 使用十进制加密
    enc = pow(cipher_in_dec, key[0], key[1])
    print("enc:", enc)
    message = enc.to_bytes(math.ceil(enc.bit_length() / 8), byteorder='big')
    return message

# 分组的 RSA 加密, 任意长度的明文
def encrypt(key, message: bytes):
    # 分组加密 每组 i bytes
    i = math.log(key[1], 2)
    i = math.floor(i / 8)

    # 将 message 分成 i bytes 的组
    message_blocks = cut_bytes(message, i)
    print(message_blocks)

    cipher = bytes()

    for block in message_blocks:
        block_in_hex = block.hex()
        block_in_dec = int(block_in_hex, 16)
        enc = pow(block_in_dec, key[0], key[1])

        cipher += enc.to_bytes(i + 1, byteorder='big')


    
    return cipher

# 分组的 RSA 解密, 任意长度的密文
def decrypt(key, cipher: bytes):
    i = math.log(key[1], 2)
    i = math.floor(i / 8)

    cipher_blocks = cut_bytes(cipher, i + 1)
    print(cipher_blocks)

    message = bytes()

    for block in cipher_blocks:
        block_in_hex = block.hex()
        block_in_dec = int(block_in_hex, 16)
        enc = pow(block_in_dec, key[0], key[1])

        message += enc.to_bytes(i, byteorder='big')
    
    return message
        
    
# 测试
if __name__ == "__main__":
    # 测试 不分组加密
    if DEBUG == 1:
        key.load_private_key()
        key.load_public_key()
        filepath = "greeting.txt"
        message_file = open(filepath, "rb")
        encrypted_file = open("encrypted.bin", "wb")

        message = message_file.read()
        cipher = encrypt_short(key.public_key, message)
        print(cipher)

        encrypted_file.write(cipher)
        encrypted_file.close()
        message_file.close()
        print("Done")

        decrypted_file = open("decrypted.txt", "wb")
        encrypted_file = open("encrypted.bin", "rb")
        cipher = encrypted_file.read()
        print(cipher)
        decrypted = decrypt_short(key.private_key, cipher)
        print(decrypted)
        decrypted_file.write(decrypted)
        decrypted_file.close()
        encrypted_file.close()
        print("Done")

    # 测试  分组加密
    if DEBUG == 2:
        key.load_private_key()
        key.load_public_key()
        filepath = "hamlet.txt"
        message_file = open(filepath, "rb")
        encrypted_file = open("encrypted.bin", "wb")
    

        message = message_file.read()
        cipher = encrypt(key.public_key, message)
        print(cipher)

        encrypted_file.write(cipher)
        encrypted_file.close()
        message_file.close()
        print("Done")

        decrypted_file = open("decrypted.txt", "wb")
        encrypted_file = open("encrypted.bin", "rb")
        cipher = encrypted_file.read()
        print(cipher)
        decrypted = decrypt(key.private_key, cipher)
        print(decrypted)
        decrypted_file.write(decrypted)
        decrypted_file.close()
        encrypted_file.close()
        print("Done")

