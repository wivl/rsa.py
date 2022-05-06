# rsa main module
#!/usr/bin/env python3
# Path: main.py

import sys
import rsa
import key


def print_help():
    print("Usage:")
    print("\t./python3 main.py [option] [args]\n")
    print("Options:")
    print("\t-e [input file name] [output file name]\tEncrypt")
    print("\t-d [input file name] [output file name]\tDecrypt")
    print("\t-h\tPrint this help\n")
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        exit(0)
    elif sys.argv[1] == "-e":
        input_filename = 'input.txt'
        output_filename = 'output.bin'
        if len(sys.argv) > 2:
            input_filename = sys.argv[2]
        if len(sys.argv) > 3:
            output_filename = sys.argv[3]
        with open(input_filename, 'rb') as f:
            message = f.read()
        key.load_public_key()
        cipher = rsa.encrypt(key.public_key, message)
        with open(output_filename, 'wb') as f:
            f.write(cipher)
        print("Done")
    elif sys.argv[1] == "-d":
        input_filename = 'output.bin'
        output_filename = 'decrypted.txt'
        if len(sys.argv) > 2:
            input_filename = sys.argv[2]
        if len(sys.argv) > 3:
            output_filename = sys.argv[3]
        with open(input_filename, 'rb') as f:
            cipher = f.read()
        key.load_private_key()
        message = rsa.decrypt(key.private_key, cipher)
        with open(output_filename, 'wb') as f:
            f.write(message)
        print("Done")
    elif sys.argv[1] == "-h":
        print_help()
        exit(0)
    else:
        print("Unknown option:", sys.argv[1])
        print_help()
        exit(0)
