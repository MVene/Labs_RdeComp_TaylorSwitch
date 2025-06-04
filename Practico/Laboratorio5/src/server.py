import socket
import time
import argparse

LOG_FILE: str = "log.txt"


def log_packet(data: str, timestamp: float, protocol: str) -> None:
    """
    Logger. \\
    Writes the data into the log file with its timestamp.

    Arguments:
        data (str): Data received by the server.
        timestamp (float): Time since EPOCH at the time of receiving the data.
        protocol (str): Protocol used, either TPC or UDP.
    """

    with open(LOG_FILE, "a") as f:
        f.write(f"RECEIVED {data} at {timestamp} - Protocol: {protocol}\n")


class Server:
    def __init__(self, arguments: argparse.Namespace) -> None:
        """
        Init function, sets the protocol to be used.

        Arguments:
            arguments (argsparse.Namespace): Object containing the values taken from the user input, or using the default ones.
        """

        self._host: str = arguments.host
        self._port: int = int(arguments.port)
        self._protocol: str = arguments.protocol

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

    def _run_tcp_server(self) -> None:
        """
        Runs the TCP server.
        Will listen in the given port and log the information.
        """
        with socket.socket(self._AF_INET, self._socket) as s:
            s.bind((self._host, self._port))
            s.listen()

            print(
                f"[SERVER] Listening on {self._host}:{self._port} - Protocol: {self._protocol}\n"
            )

            conn, addr = s.accept()

            with conn:
                print(f"[SERVER] Connected by {addr}\n")
                while True:
                    data: bytes = conn.recv(1024)

                    if not data:
                        break

                    timestamp: float = time.time()
                    log_packet(data.decode(), timestamp, self._protocol)

    def _run_udp_server(self) -> None:
        """
        Runs the UDP server.
        Will listen in the given port and log the information.
        """

        with socket.socket(self._AF_INET, self._socket) as s:
            s.bind((self._host, int(self._port)))
            print(
                f"[SERVER] Listening on {self._host}:{int(self._port)} - Protocol: {self._protocol}\n"
            )

            while True:
                data, addr = s.recvfrom(1024)

                if not data:
                    break

                timestamp: float = time.time()
                log_packet(data.decode(), timestamp, self._protocol)

    def run_server(self) -> None:
        """
        Wrapper function, depending on the protocol, will call one function or the other.
        """

        if self._protocol == "tcp":
            self._run_tcp_server()

        else:
            self._run_udp_server()


def main(arguments: argparse.Namespace) -> None:
    """
    Main function. \\
    Listens to the port for data from the client.

    Args:
        arguments (argsparse.Namespace): Object containing the values taken from the user input, or using the default ones.
    """

    server = Server(arguments)
    server.run_server()


def get_arguments() -> argparse.ArgumentParser:
    """
    Gets arguments from command line.

    Returns:
        arguments (argsparse.ArgumentParser): Object containing the accepted arguments.
    """

    arguments: argparse.ArgumentParser = argparse.ArgumentParser(
        "TCP Server", "tcp_server [OPTION]", "Receive packages sent from the 'client'"
    )

    arguments.add_argument(
        "--host", action="store", default="0.0.0.0", help="server host."
    )

    arguments.add_argument(
        "--port", "-p", action="store", default=12345, help="port to be used."
    )

    arguments.add_argument(
        "--protocol", action="store", default="tcp", choices=["tcp", "udp"]
    )

    return arguments


if __name__ == "__main__":
    arg_parser: argparse.ArgumentParser = get_arguments()
    arguments: argparse.Namespace = arg_parser.parse_args()

    main(arguments)
