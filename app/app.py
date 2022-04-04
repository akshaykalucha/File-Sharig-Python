from time import sleep
import utils
import server, client

def main() -> None:
    mode = utils.choice_input("Would you like this machine to be the file sender or receiver?", ['s', 'r'])
    
    if mode == 'r':
        print("This machine will be receiving the files.")
    ftserver = server.ReceivingServer(
        input("Enter the path of the directory you would like to transfer your files TO: ")
    )

    ftserver.listen_and_connect_to_client()
    ftserver.handshake()
    ftserver.receive_dir()

    del ftserver