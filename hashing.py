import hashlib
from cryptography.fernet import Fernet
class Hash:
    
    def hash_func(str):
        
        hash = hashlib.sha256(str.encode()).hexdigest()
        return hash
    def encrypt_pwd(str,encrypted):
        key = b'OT7qdohgRtlsAKhn004DuOYGxgNFs3IoOyG1-g4n6F8='
        
        fernet = Fernet(key)
        if encrypted == False:
            encMessage = fernet.encrypt(str.encode()).hex()
            return encMessage
        else:
            print("printed:",str)
            print(type(str))
            str= bytes.fromhex(str)
            decMessage = fernet.decrypt(str).decode()
            return decMessage


str1 = Hash.encrypt_pwd("Hello",False)
print(str1)
print(type(str1))

str2 = Hash.encrypt_pwd(str1,True)
print(str2)
