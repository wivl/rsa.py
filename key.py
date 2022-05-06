# rsa key generator
#!/usr/bin/env python3
# Path: key.py

# 此文件为生成 RSA 密钥的文件
# 其中包含了下列函数:
# 1. generate_key()         生成 RSA 密钥对
# 2. save_public_key()      保存公钥到文件
# 3. save_private_key()     保存私钥到文件
# 4. load_public_key()      从文件载入公钥
# 5. load_private_key()     从文件载入私钥
# 6. is_prime()             判断是否为素数
# 7. mod_inverse()          求模逆
# 8. generate_coprime()     生成素数 (在此处弃用，实际的选择 p q 的方式为下面的 choose_primes() )
# 9. choose_primes()        从生成好的素数序列中选择素数


import math
from random import randint

# 最大 key 长度为 16 位, RSA 实际情况下要求更大 bit 的密钥, 但考虑到实际情况下生成大密钥用时太长，所以此处设置为 16 位
KEY_LENGTH = 16

public_key = ()
private_key = ()
phi = 0
p = 0
q = 0
n = 0

# 生成素数序列
N = 2 ** KEY_LENGTH
PRIMES = [ p for p in  range(2, N) if 0 not in [ p% d for d in range(2, int(math.sqrt(p))+1)] ] 


def is_prime(p):
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(p)) + 1, 2):
        if p % i == 0:
            return False
    return True


def choose_primes():
    global p
    global q
    p = PRIMES[randint(0, len(PRIMES) - 1)]
    q = PRIMES[randint(0, len(PRIMES) - 1)]
    while p == q:
        q = PRIMES[randint(0, len(PRIMES) - 1)]

def generate_coprime():
    global p
    global q
    range_up = 2 ** (KEY_LENGTH - 1)
    p = randint(1, range_up)
    q = randint(1, range_up)
    while is_prime(p) == False or is_prime(q) == False:
        p = randint(1, range_up)
        q = randint(1, range_up)

# 求模逆: 在求 d 的时候使用
def mod_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = math.floor(temp_phi/e)
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

# 生成 RSA 密钥对
def generate_key():
    global public_key
    global private_key
    global phi
    global p
    global q
    global n
    choose_primes()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 0
    d = 0
    while True:
        e = randint(2, phi)
        if math.gcd(e, phi) == 1:
            break
    
    d = mod_inverse(e, phi)
    public_key = (e, n)
    private_key = (d, n)

# 保存公钥到文件
def save_public_key():
    global public_key
    with open("public_key.key", "w") as f:
        f.write(str(public_key[0]) + " " + str(public_key[1]))

# 保存私钥到文件
def save_private_key():
    global private_key
    with open("private_key.key", "w") as f:
        f.write(str(private_key[0]) + " " + str(private_key[1]))

# 从文件载入公钥
def load_public_key():
    global public_key
    with open("public_key.key", "r") as f:
        public_key = tuple(map(int, f.read().split()))

# 从文件载入私钥
def load_private_key():
    global private_key
    with open("private_key.key", "r") as f:
        private_key = tuple(map(int, f.read().split()))

# 测试  
if __name__ == "__main__":
    generate_key()
    save_public_key()
    save_private_key()
    print(public_key)
    print(private_key)
    print("p = " + str(p))
    print("q = " + str(q))
    print("n = " + str(n))
