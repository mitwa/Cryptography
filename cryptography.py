#written by: Maitreyee Palkar

#The main method to run

'''Gets input file; asks for encryption type;
  asks if encoding or decoding;
  performs requested action;
  result output in provided or default file'''

from userInterface import userInterface
from Encryption import Encryption
from TwistEncryption import TwistEncryption
from GDBEncryption import GDBEncryption
import os

def run():
    ui = userInterface()
    try:
        fdata = ui.getInput()
    except:
        print "Error with input file."
        os._exit(1)
    else:
        code = ui.getCodeType().lower()
        job = ui.getJobType().lower()
        fname = ui.getOutputFile()
        if(code=="t"):
            crypt = TwistEncryption(fdata)
        elif(code=="g"):
            crypt = GDBEncryption(fdata)
        else:
            crypt = Encryption(fdata)
        if(job=="d"):
            msg = crypt.decrypt()
        else:
            msg = crypt.encrypt()
        if(fname==""):
            fname = code+"_message.txt"
        ui.writeFile(msg,fname)

                                    
if __name__=="__main__":
    run()
