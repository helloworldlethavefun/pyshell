#! /usr/bin/python3

# import any library's
import os
import socket
import pyfiglet
from termcolor import colored
from termconfig import *

# define variables
user = os.environ["USER"]
hostname = socket.gethostname()
currentdir = os.getcwd()
header = termHeader

class PermissionError(Exception):
    pass

class TerminalError(Exception):
    pass

class Prompt():
    def __init__(self, header, hostname, user):
        self.hostname = hostname
        self.user = user
        self.header = header


# Define the change directory function
def cd(command):
    # Attempt to change into directory provided by the user
    try:
        newdir = input(colored('Which directory would you like to go to? ', 'magenta'))
        os.chdir(newdir)
    # Otherwise raise the permission error and ask user if they have permission
    # to access that specific directory
    except:
        raise PermissionError('Something went wrong, are you allowed here user?')

# set the prompt
def prompt():

    # set the command variable to
    # a global variable
    global command

    # use the variable to input the user command
    # and put the username and the hostname into the fields
    command = input('{} // {}$ '.format(user, hostname))

# execute commands
def execCommand(command):

    # if the command is exit then exit with
    # status code 1
    if command == "exit":
        exit(1)
        
    # if the command is ls then run the listdir
    # function
    ## comming back to this later
    # elif command == "ls" or "list":
        # listdir()

    elif command == 'cd':
        cd(command)

    # otherwise run whatever command is
    # entered into the prompt
    else:
        os.system(command)

# while shell is active then run commands

while True:
    try:
        prompt()
        execCommand(command)
    except:
        raise TerminalError('Something went wrong')
