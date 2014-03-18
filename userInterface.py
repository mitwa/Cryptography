#written by: Maitreyee Palkar

'''Class for file i/o & user input'''

#File i/o methods modified from lecture code

class userInterface:
    
    # Reads a text file into a single string
    # Parameters:
    #   fileName: a string with the name of the file to be loaded
    # Returns a string
    def readFile(self,fileName):
        fileHandler = open(fileName, "rt") # rt stands for read text
        text = fileHandler.read() # read the entire file into a single string
        fileHandler.close() # close the fil
        return text

    # Saves a string into a file.
    # If the file already exists, it will be overwritten.
    # Parameters:
    #   fileName: a string with the name of the file to be written
    # Returns None
    def writeFile(self,text,fileName):
        fileHandler = open(fileName, "wt") # wt stands for write text
        fileHandler.write(text) # write the text
        fileHandler.close() # close the file
    
    # Asks for user to provide file. Calls readFile
    # Parameters:
    #   None
    # Returns a string
    def getInput(self):
        fname = raw_input("Enter name of input file: ")
        text = self.readFile(fname)
        return text

    # Asks for user to provide encoding type.
    # Parameters:
    #   None
    # Returns a string
    def getCodeType(self):
        code = raw_input("Twist(T), GDB(G) or Basic(B) Encoding?")
        return code

    # Asks user if encrypting or decrypting.
    # Parameters:
    #   None
    # Returns a string
    def getJobType(self):
        job = raw_input("Encryption(E) or Decryption(D)?")
        return job

    # Asks user of output file name.
    # Parameters:
    #   None
    # Returns a string
    def getOutputFile(self):
        name = raw_input("Enter name of output file: ")
        return name
