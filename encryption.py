import hashlib


class Password_Hash:
    def encrypt(pwd):
        h = hashlib.sha256(pwd.encode()).hexdigest()

        return h


