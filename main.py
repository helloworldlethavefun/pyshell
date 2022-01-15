#! /usr/bin/python3

# import any library's
import os
import socket
import pyfiglet
from termcolor import colored
import glob

# define variables
user = os.environ["USER"]
hostname = socket.gethostname()
active = True
header = colored(pyfiglet.figlet_format("PyShell"), 'cyan', attrs=['bold'])
currentdir = os.getcwd()

# define the listdir function
def listdir():
    
    # create list
    extensionFiles = []
    
    for file in os.listdir(currentdir):
        for file in glob.glob('*.*'):
            extensionFiles.append(file)
            print(colored(extensionFiles, 'green'))

# define the change directory function
def cd(command):
    newdir = input(colored('Which directory would you like to go to? ', 'magenta'))
    os.chdir(newdir)


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

# Start the shell
print(header)
prompt()

# while shell is active then run commands

while True:
    prompt()
    execCommand(command)
