#written by: Maitreyee Palkar

'''Implements Dog encryption & decryption.
Encrypted value adds 'gdb' after each letter'''

from Encryption import Encryption

class GDBEncryption(Encryption):

    def encrypt(self):
        msg = ""
        for i in range(0,self.l):
            char = self.data[i]
            if char!=' ':
                msg += char+"gdb"
            else:
                msg += '_'
        return msg

    def decrypt(self):
        msg = ""
        flag = 1
        c = 0 #counter to keep track of position
        for i in range(0,self.l):
            if flag==1:
                char = self.data[i]
                if char!='_':
                    msg += char
                else:
                    msg += ' '
                c = 0
                flag = 0
            if c==3:
                flag = 1
            else:
                c += 1
        return msg
