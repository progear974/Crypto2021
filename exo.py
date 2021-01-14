import hashlib
import sys


# 1 => file password
# 2 => hash to find

with open(sys.argv[1]) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

for password in content:
    hashpass = hashlib.sha256(bytes(password + "5UA@/Mw^%He]SBaU", 'utf-8')).hexdigest()
    if hashpass == sys.argv[2]:
        print(hashpass)
        print(password)
        break