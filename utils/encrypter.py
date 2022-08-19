import rsa

def generateKeys():
   (publicKey, privateKey) = rsa.newkeys(1024)
   with open('utils/keys/publcKey.pem', 'wb') as p:
      p.write(publicKey.save_pkcs1('PEM'))
   with open('utils/keys/privateKey.pem', 'wb') as p:
      p.write(privateKey.save_pkcs1('PEM'))

def loadKeys():
   with open('utils/keys/publicKey.pem', 'rb') as p:
      publicKey = rsa.PublicKey.load_pkcs1(p.read())
   with open('utils/keys/privateKey.pem', 'rb') as p:
      privateKey = rsa.PrivateKey.load_pkcs1(p.read())
   return privateKey, publicKey

def decrypt(ciphertext, key):
    try: return rsa.decrypt(ciphertext, key).decode('ascii')
    except: return False