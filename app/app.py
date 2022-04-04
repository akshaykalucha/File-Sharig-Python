from time import sleep
import utils
import server, client

def main() -> None:
    mode = utils.choice_input("Would you like this machine to be the file sender or receiver?", ['s', 'r'])