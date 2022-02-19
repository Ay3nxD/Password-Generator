import os
import sys
import random
import string
import time
from time import sleep

os.system("title Password Generator")


chars = string.ascii_letters+string.digits+string.punctuation


while True:
    print("\n")
    print("""
██████╗  █████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
██████╔╝███████║███████╗███████╗    ██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██║╚════██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║███████║███████║    ╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                    
[1] Start Password Generator
""")



    choice = input("Insert an option :")
    if choice == "1":
        password_amount = int(input("\nHow many passwords do you wish to generate? :"))
        password_length = int(input("\nWhich length would you like the passwords to be? :"))

    for i in range(password_amount):
        password = ""
        for i in range(password_length):
            password_chars = random.choice(chars)
            password = password + password_chars
        print("\n")
        sleep(0.1)
        print("\nGenerated Passowrd : " + f"{password}")
        print(f"Saved \"{password}\" to  passwords.txt")


        with open("passwords.txt", "a") as f:
            f.write(password + "\n")