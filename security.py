import os, pyminizip
from pathlib import Path

def encrypt(locfile, password):
    loczip = os.path.splitext(locfile)[0] + ".zip"
    compression_level = 5 #1-9``
    pyminizip.compress(locfile, None, loczip, password, compression_level)

def decrypt(ziploc, password):
    dest = os.path.join(Path(ziploc).parent, "decrypted")
    if not os.path.isdir(dest):
        os.mkdir(dest)
    pyminizip.uncompress(ziploc, password, dest, 0)

def main():
    print("Enter file name you'd like to compress/decompress: ")
    locfile = input()

    if not os.path.exists(locfile):
        print("File not found..")
        raise

    print("Enter password to encrypt the file with: ")
    password = input()
    if not password:
        password = "password"

    file_extension = os.path.splitext(locfile)[1]

    if (file_extension == ".zip"):
        decrypt(locfile, password)
    elif (file_extension == ".txt"):
        encrypt(locfile, password)
    else:
        print("please input either .zip or .txt file")
        print("you entered: {}".format(file_extension))

if __name__ == "__main__":
    try:
        main()
    except:
        print("Error compressing/decompressing file")
