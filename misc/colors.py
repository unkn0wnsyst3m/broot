from os import system
BLUE = '\033[94m'
GREY = '\033[90m'
GREEN = '\033[92m'
RED = '\033[31m'
YELLOW = '\033[93m'
FAIL = '\033[91m'
BOLD = '\033[1m'
BGRED = '\033[41m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
RSTCOLORS = '\033[0m'
result = system('color') ## Allows the script to use colors


def PrintColor(status, msg):
    '''
    Prints out the message in a pre-formatted string of text
    Possible values for 'status': WARN,SUCCESS,FAIL,INFO
    '''
    status = status.upper()
    if status == "WARN" or status == "ERROR":
        text = YELLOW + "[!] " + msg + RSTCOLORS
    elif status == "SUCCESS":
        text = GREEN + "[+] " + msg + RSTCOLORS
    elif status == "INFO":
        text = WHITE + "[*] " + msg + RSTCOLORS
    elif status == "FAIL":
        text = RED + "[-] " + msg + RSTCOLORS
    elif status == "DEBUG":
        text = GREY + "[DEBUG] " + msg + RSTCOLORS
    elif status == "STATUS":
        text = WHITE + msg + RSTCOLORS
    else:
        text = "[*] " + msg + RSTCOLORS
    print(text)

def print_good(msg):
    PrintColor("SUCCESS", msg)

def print_fail(msg):
    PrintColor("FAIL", msg)

def print_warn(msg):
    PrintColor("WARN", msg)

def print_info(msg):
    PrintColor("INFO", msg)

def print_dbug(msg):
    PrintColor("DEBUG", msg)

def print_stat(msg):
    PrintColor("STATUS", msg)