#written by: Maitreyee Palkar

'''Parent Class
Extended by TwistEncryption & DogEncryption
Defines __init__ & does very basic manipulation'''

class Encryption:

    data = ""
    l = 0

    #Initializes with message data string
    #and length of the data
    #Parameters
    #   the string read in from file
    #Returns None
    def __init__(self,fdata):
        self.data = fdata
        self.l = len(self.data)

    #Encrypts by switching 1st & last characters
    #Parameters None
    #Returns encrypted string
    def encrypt(self):
        msg = self.data[self.l-1]
        for i in range(1,self.l-1):
            msg += self.data[i]
        msg += self.data[0]
        return msg

    #Decrypts by switching 1st & last characters
    #Parameters None
    #Returns decrypted string
    def decrypt(self):
        msg = self.data[self.l-1]
        for i in range(1,self.l-1):
            msg += self.data[i]
        msg += self.data[0]
        return msg
