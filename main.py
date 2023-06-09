from colorama import Fore, Style, init
import time
import sys

init()

class Interpreter:
    def __init__(self):
        self.commands = {
            "print": self.printly,
            "help": self.helply,
            "add": self.addly
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

interpreter = Interpreter()
print(Fore.BLUE + "Lenti Terminal")
    code = input(Fore.YELLOW + '>> ')
    print(" ")
    interpreter.run(code)

    print("\n")
