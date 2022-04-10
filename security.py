from curses.ascii import NUL
import zipfile, os, pyminizip

print("Enter file name you'd like to compress: ")
locfile = input()
# locfile = "hello.txt"
loczip = os.path.splitext (locfile)[0] + ".zip"
zip = zipfile.ZipFile (loczip, "w")
zip.write(locfile)
zip.close()

print("Enter password to encrypt the file with: ")
password = input()
if not password:
    password = "password"

compression_level = 5 #1-9
pyminizip.compress(locfile, "decrypted", loczip, password, compression_level)
