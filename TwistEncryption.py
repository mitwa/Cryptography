#written by: Maitreyee Palkar

'''Implements Twist encryption & decryption
Encoded value is ASCII value of character-7'''

from Encryption import Encryption

class TwistEncryption(Encryption):

    def encrypt(self):
        msg = ""
        for i in range(0,self.l):
            msg += chr(ord(self.data[i])-7)
        return msg

    def decrypt(self):
        msg = ""
        for i in range(0,self.l):
            msg += chr(ord(self.data[i])+7)
        return msg
