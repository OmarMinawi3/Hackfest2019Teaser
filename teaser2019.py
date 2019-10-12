import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

print ("A-Z, a-z, 0-9. L47????P6")

try:
    userInput = str(sys.argv[1])
except:
    userInput = " "

digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(bytes(str(userInput), "utf-8"))
hash = digest.finalize()
#Converts the bytes hash into integer format, then casts to hex
newhash = (hex(int.from_bytes(hash, byteorder='big'))[2:])

print ("Entered password: ", userInput)
if (newhash == "8fbec71d6602c08e86bce4083194fab9e717688d5b0866ab784b9e8dfe26636e"):
    print ("Valid: True")
    print ("Correct! Remember this password: ", userInput)
    print ("https://drive.google.com/open?id=1AKzHH4HVabtjfNzf0WoxFUS44tLFJTDt")
else:
    print ("Valid: False")
