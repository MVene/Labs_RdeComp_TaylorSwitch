import socket
import time
import argparse
from cryptography.fernet import Fernet, InvalidToken

LOG_FILE: str = "log.txt"
KEY_FILE: str = "secret.key"


def load_key(filename: str = KEY_FILE) -> bytes:
    with open(filename, "rb") as f:
        return f.read()


def decrypt_message(token: bytes, key: bytes) -> str:
    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(token)
        return decrypted.decode()
    except InvalidToken:
        return "<INVALID OR CORRUPTED MESSAGE>"


def log_packet(data: str, timestamp: float, protocol: str) -> None:
    with open(LOG_FILE, "a") as f:
        f.write(f"RECEIVED {data} at {timestamp} - Protocol: {protocol}\n")


class Server:
    def __init__(self, arguments: argparse.Namespace) -> None:
        self._host: str = arguments.host
        self._port: int = int(arguments.port)
        self._protocol: str = arguments.protocol
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

    def _run_tcp_server(self) -> None:
        with socket.socket(self._AF_INET, self._socket) as s:
            s.bind((self._host, self._port))
            s.listen()
            print(f"[SERVER] Listening on {self._host}:{self._port} - Protocol: {self._protocol}\n")

            conn, addr = s.accept()
            with conn:
                print(f"[SERVER] Connected by {addr}\n")
                while True:
                    data: bytes = conn.recv(1024)
                    if not data:
                        break
                    timestamp: float = time.time()
                    decrypted_msg = decrypt_message(data, self._key)
                    log_packet(decrypted_msg, timestamp, self._protocol)

    def _run_udp_server(self) -> None:
        with socket.socket(self._AF_INET, self._socket) as s:
            s.bind((self._host, self._port))
            print(f"[SERVER] Listening on {self._host}:{self._port} - Protocol: {self._protocol}\n")

            while True:
                data, addr = s.recvfrom(1024)
                if not data:
                    break
                timestamp: float = time.time()
                decrypted_msg = decrypt_message(data, self._key)
                log_packet(decrypted_msg, timestamp, self._protocol)

    def run_server(self) -> None:
        if self._protocol == "tcp":
            self._run_tcp_server()
        else:
            self._run_udp_server()


def main(arguments: argparse.Namespace) -> None:
    server = Server(arguments)
    server.run_server()


def get_arguments() -> argparse.ArgumentParser:
    arguments: argparse.ArgumentParser = argparse.ArgumentParser(
        "Crypto TCP/UDP Server",
        "crypto_server [OPTION]",
        "Receive encrypted packages sent from the 'client'",
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
