import socket
import time
import argparse

GROUP_NAME:str = "Taylor_Switch"
LOG_FILE:str = "log.txt"

def log_packet(data:str, timestamp:int, protocol:str) -> None:
    """
    Logger. \\
    Writes the data into the log file with its timestamp.
    """

    with open(LOG_FILE, "a") as f:
        f.write(f"SENT {data} at {timestamp} - Protocol: {protocol}\n")

class Client:
    def __init__(self, arguments:argparse.Namespace) -> None:
        """
        Init function, sets the protocol to be used.

        Arguments:
            arguments (argsparse.Namespace): Object containing the values taken from the user input, or using the default ones.
        """
        

        self._host:str = arguments.host
        self._port:int = int(arguments.port)
        self._protocol:str = arguments.protocol
        self._total_packages:int = int(arguments.packages)
        self._time_interval:int = arguments.time_interval

        if self._protocol == "tcp":
            self._set_tcp()
        
        else:
            self._set_udp()

    def _set_tcp(self) -> None:
        """
        Sets the necessary info for the TCP protocol
        """
        self._socket = socket.SOCK_STREAM
        self._AF_INET = socket.AF_INET

    def _set_udp(self) -> None:
        """
        Sets the necessary info for the UDP protocol
        """
        self._socket = socket.SOCK_DGRAM
        self._AF_INET = socket.AF_INET

    def _run_tcp_client(self) -> None:
        """
        Actually runs the client, sending data using the TCP protocol
        """
        with socket.socket(self._AF_INET, self._socket) as s:
    
            try:
                s.connect((self._host, self._port))
            except:
                print("You must first start the server\n")
                exit(1)
        
            for i in range(self._total_packages):
                
                msg:str = f"{GROUP_NAME}_{i}"
                
                timestamp:float = time.time()
                
                s.sendall(msg.encode())
                
                log_packet(msg, timestamp, self._protocol)
                
                time.sleep(self._time_interval)

    def _run_udp_client(self) -> None:
        """
        Actually runs the client, sending data using the UDP protocol
        """
        with socket.socket(self._AF_INET, self._socket) as s:
        
            for i in range(self._total_packages):
        
                msg:str = f"{GROUP_NAME}_{i}"
        
                timestamp:float = time.time()
        
                s.sendto(msg.encode(), (self._host, self._port))
        
                log_packet(msg, timestamp, self._protocol)
        
                time.sleep(self._time_interval)


    def run_client(self):
        """
        Wrapper function, depending on the protocol, will call one function or the other.
        """

        print(f"Sending data. Host: {self._host} - Port: {self._port} - Protocol: {self._protocol}")
        if self._protocol == "tcp":
            self._run_tcp_client()

        else:
            self._run_udp_client()
        
        print(f"Finished sending data. Host: {self._host} - Port: {self._port} - Protocol: {self._protocol}")


def main(arguments:argparse.Namespace) -> None:
    """
    Main function. \\
    Sends data to the server in a loop.

    Args:
        arguments (argsparse.Namespace): Object containing the values taken from the user input, or using the default ones.
    """
    
    client:Client = Client(arguments)
    client.run_client()

   

def get_arguments() -> argparse.ArgumentParser:
    """
    Gets arguments from command line.
        
    Returns:
        arguments (argsparse.ArgumentParser): Object containing the accepted arguments.
    """
    
    arguments:argparse.ArgumentParser = argparse.ArgumentParser(
        "TCP Client",
        "tcp_client [OPTION]",
        "Send packages to be received by the 'server'"
    )

    arguments.add_argument(
        "--time-interval","-i",
        action='store',
        default= 1,
        help="amount of seconds between each package"
    )

    arguments.add_argument(
        "--packages","-p",
        action='store',
        default= 100,
        help="total amount of packages to be sent."
    )

    arguments.add_argument(
        "--host",
        action='store',
        default= '127.0.0.1',
        help="client host."
    )

    arguments.add_argument(
        "--port",
        action='store',
        default= 12345,
        help="port to be used."
    )

    arguments.add_argument(
        "--protocol",
        action='store',
        default='tcp',
        choices=['tcp','udp']
    )

    return arguments

if __name__ == "__main__":
    
    arg_parser:argparse.ArgumentParser = get_arguments()
    arguments:argparse.Namespace =arg_parser.parse_args()
    
    main(arguments)
