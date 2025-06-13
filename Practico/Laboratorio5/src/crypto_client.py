import socket
import time
import argparse
from cryptography.fernet import Fernet

GROUP_NAME: str = "Taylor_Switch"
LOG_FILE: str = "log.txt"
KEY_FILE: str = "secret.key"


def load_key(filename: str = KEY_FILE) -> bytes:
    with open(filename, "rb") as f:
        return f.read()


def encrypt_message(message: str, key: bytes) -> bytes:
    return Fernet(key).encrypt(message.encode())


def log_packet(data: str, timestamp: int, protocol: str) -> None:
    """
    Logger.
    Writes the data into the log file with its timestamp.
    """
    with open(LOG_FILE, "a") as f:
        f.write(f"SENT {data} at {timestamp} - Protocol: {protocol}\n")


class Client:
    def __init__(self, arguments: argparse.Namespace) -> None:
        self._host: str = arguments.host
        self._port: int = int(arguments.port)
        self._protocol: str = arguments.protocol
        self._total_packages: int = int(arguments.packages)
        self._time_interval: int = arguments.time_interval

        # Load encryption key
        self._key: bytes = load_key()

        if self._protocol == "tcp":
            self._set_tcp()
        else:
            self._set_udp()

    def _set_tcp(self) -> None:
        self._socket = socket.SOCK_STREAM
        self._AF_INET = socket.AF_INET

    def _set_udp(self) -> None:
        self._socket = socket.SOCK_DGRAM
        self._AF_INET = socket.AF_INET

    def _run_tcp_client(self) -> None:
        with socket.socket(self._AF_INET, self._socket) as s:
            try:
                s.connect((self._host, self._port))
            except RuntimeError:
                print("You must first start the server\n")
                exit(1)

            for i in range(self._total_packages):
                msg: str = f"{GROUP_NAME}_{i}"
                encrypted_msg = encrypt_message(msg, self._key)

                timestamp: float = time.time()
                s.sendall(encrypted_msg)

                log_packet(msg, timestamp, self._protocol)
                time.sleep(self._time_interval)

    def _run_udp_client(self) -> None:
        with socket.socket(self._AF_INET, self._socket) as s:
            for i in range(self._total_packages):
                msg: str = f"{GROUP_NAME}_{i}"
                encrypted_msg = encrypt_message(msg, self._key)

                timestamp: float = time.time()
                s.sendto(encrypted_msg, (self._host, self._port))

                log_packet(msg, timestamp, self._protocol)
                time.sleep(self._time_interval)

    def run_client(self):
        print(
            f"Sending encrypted data. Host: {self._host} - Port: {self._port} - Protocol: {self._protocol}"
        )
        if self._protocol == "tcp":
            self._run_tcp_client()
        else:
            self._run_udp_client()

        print(
            f"Finished sending data. Host: {self._host} - Port: {self._port} - Protocol: {self._protocol}"
        )


def main(arguments: argparse.Namespace) -> None:
    client: Client = Client(arguments)
    client.run_client()


def get_arguments() -> argparse.ArgumentParser:
    arguments: argparse.ArgumentParser = argparse.ArgumentParser(
        "Crypto TCP/UDP Client",
        "crypto_client [OPTION]",
        "Send encrypted packages to the 'server'",
    )

    arguments.add_argument(
        "--time-interval",
        "-i",
        action="store",
        default=1,
        help="amount of seconds between each package",
    )

    arguments.add_argument(
        "--packages",
        "-p",
        action="store",
        default=100,
        help="total amount of packages to be sent.",
    )

    arguments.add_argument(
        "--host", action="store", default="127.0.0.1", help="client host."
    )

    arguments.add_argument(
        "--port", action="store", default=12345, help="port to be used."
    )

    arguments.add_argument(
        "--protocol", action="store", default="tcp", choices=["tcp", "udp"]
    )

    return arguments


if __name__ == "__main__":
    arg_parser: argparse.ArgumentParser = get_arguments()
    arguments: argparse.Namespace = arg_parser.parse_args()
    main(arguments)
