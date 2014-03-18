Written by Maitreyee Palkar. Spring 2014

Python program with multiple classes, user i/o and string manipulation.

cryptography.py has the run() method. It asks user for input of:
-the name of a file with the text
-whether to encrypt or decrypt
-which encoding to use

Encryption.py has the basic encryption implementation.
GDBEncryption and TwistEncryption extend/modify Encryption with different implementations.
userInterface.py is the i/o class.

If no input file is provided, the program exits. If no output file is provided, a default is used.
If Twist or GDB encryption is not chosen, basic encryption is used.
If decryption is not chosen, encryption is performed.
