from colorama import Fore, Style, init
import time
import sys

init()

class Interpreter:
    def __init__(self):
        self.commands = {
            "print": self.printly,
            "help": self.helply,
            "add": self.addly,
            "read": self.readly,
            "write": self.writely,
            "append": self.appendly,
            "copy": self.copyly,
            "rename": self.renamely,
            "delete": self.deletely
        }

    def run(self, code):
        tokens = code.split()
        keyword = tokens[0]
        self.execute(keyword, tokens)

    def execute(self, keyword, tokens):
        if keyword in self.commands:
            self.commands[keyword](tokens)
        else:
            print(Fore.BLUE + "Invalid keyword", keyword)

    def printly(self, tokens):
        if len(tokens) <= 3:
            print(Fore.BLUE + tokens[1] + " " + tokens[2])
        else:
            if len(tokens)== 2:
                print(Fore.BLUE + tokens[1])
            else:
                disk = len(tokens) - 1
                print("Can only display 1-2 words amount of words given: ", Fore.RED + str(disk))
    def helply(self, tokens=None):
        print(Fore.BLUE + "Available commands:")
        for command in self.commands:
            print(Fore.BLUE + f"{command} - {self.commands[command].__doc__}")

    def addly(self, tokens):
        """Adds two numbers and prints the result"""
        if len(tokens) != 3:
            print(Fore.BLUE + "Invalid number of arguments")
            return
        try:
            result = int(tokens[1]) + int(tokens[2])
            print(Fore.BLUE + str(result))
        except ValueError:
            print(Fore.BLUE + "Invalid arguments")

    def readly(self, tokens):
        """Reads the content of a file and prints it"""
        if len(tokens) != 2:
            print(Fore.BLUE + "Invalid number of arguments")
            return
        try:
            with open(tokens[1], 'r') as file:
                content = file.read()
                print(Fore.BLUE + content)
        except FileNotFoundError:
            print(Fore.BLUE + f"File {tokens[1]} not found")

    def writely(self, tokens):
        """Writes content to a file"""
        if len(tokens) < 3:
            print(Fore.BLUE + "Invalid number of arguments")
            return
        try:
            with open(tokens[1], 'w') as file:
                content = ' '.join(tokens[2:])
                file.write(content)
                print(Fore.BLUE + f"Content written to {tokens[1]}")
        except FileNotFoundError:
            print(Fore.BLUE + f"File {tokens[1]} not found")

    def appendly(self, tokens):
        """Appends content to a file"""
        if len(tokens) < 3:
            print(Fore.BLUE + "Invalid number of arguments")
            return
        try:
            with open(tokens[1], 'a') as file:
                content = ' '.join(tokens[2:])
                file.write(content)
                print(Fore.BLUE + f"Content appended to {tokens[1]}")
        except FileNotFoundError:
            print(Fore.BLUE + f"File {tokens[1]} not found")

    def copyly(self, tokens):
        """Copies a file"""
        if len(tokens) != 3:
            print(Fore.BLUE + "Invalid number of arguments")
            return
        try:
            with open(tokens[1], 'r') as src_file:
                with open(tokens[2], 'w') as dest_file:
                    content = src_file.read()
                    dest_file.write(content)
                    print(Fore.BLUE + f"File {tokens[1]} copied to {tokens[2]}")
        except FileNotFoundError:
            print(Fore.BLUE + f"File {tokens[1]} not found")

    def renamely(self, tokens):
        """Renames a file"""
        if len(tokens) != 3:
            print(Fore.BLUE + "Invalid number of arguments")
            return
        try:
            os.rename(tokens[1], tokens[2])
            print(Fore.BLUE + f"File {tokens[1]} renamed to {tokens[2]}")
        except FileNotFoundError:
            print(Fore.BLUE + f"File {tokens[1]} not found")

    def deletely(self, tokens):
        """Deletes a file"""
        if len(tokens) != 2:
            print(Fore.BLUE + "Invalid number of arguments")
            return
        try:
            os.remove(tokens[1])
            print(Fore.BLUE + f"File {tokens[1]} deleted")
        except FileNotFoundError:
            print(Fore.BLUE + f"File {tokens[1]} not found")

interpreter = Interpreter()
print(Fore.BLUE + "Lenti Terminal")
while True:
    code = input(Fore.YELLOW + '>> ')
    print(" ")
    interpreter.run(code)

    print("\n")
