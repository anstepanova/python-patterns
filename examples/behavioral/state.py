from __future__ import annotations

import socket

from typing import Callable
from functools import wraps
from collections import namedtuple


class TCPState:
    @staticmethod
    def open(*, connection: TCPConnection):
        return TCPOpenState.open(connection=connection)

    @staticmethod
    def close(*, connection: TCPConnection):
        return False

    @staticmethod
    def accept(*, connection: TCPConnection):
        return False

    @staticmethod
    def listen(*, connection: TCPConnection):
        return False


# def update_connection_state_with_current_state(state_type: TCPState):
#     def update_state_decorator(func: Callable):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             connection = kwargs.get('connection')
#             result = func(*args, **kwargs)
#             connection.state = state_type
#             return result
#         return wrapper
#     return update_state_decorator


class TCPOpenState(TCPState):
    @classmethod
    def open(cls, *, connection: TCPConnection):
        connection.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        connection.server_socket.bind((connection.host, connection.port))
        connection.state = TCPOpenState
        print('Server socket is listening to a new connection')
        connection.server_socket.listen()
        return True


class TCPCloseState(TCPState):
    @staticmethod
    def close(*, connection: TCPConnection):
        connection.server_socket.close()
        connection.state = TCPCloseState
        print('Server socket was closed')
        return True


class TCPAcceptState(TCPState):
    @staticmethod
    def accept(*, connection: TCPConnection):
        client_socket, address = connection.server_socket.accept()
        print(f'Connection from {address} accepted')
        client_socket.send(f'Hello from {connection.host}:{connection.port}!'.encode())
        connection.state = TCPAcceptState
        return True


class TCPConnection:
    possible_transitions = (
        (TCPState, TCPOpenState),
        (TCPOpenState, TCPAcceptState),
        (TCPOpenState, TCPCloseState),
        (TCPAcceptState, TCPCloseState),
        (TCPCloseState, TCPOpenState),
    )

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.server_socket = None
        self.state: TCPState = TCPState

    def open(self):
        if (self.state, TCPOpenState) in TCPConnection.possible_transitions:
            return TCPOpenState.open(connection=self)
        return False

    def close(self):
        if (self.state, TCPCloseState) in TCPConnection.possible_transitions:
            return TCPCloseState.close(connection=self)
        return False

    def accept(self):
        if (self.state, TCPAcceptState) in TCPConnection.possible_transitions:
            return TCPAcceptState.accept(connection=self)
        return False


if __name__ == '__main__':
    tcp_connection = TCPConnection('127.0.0.1', 8000)
    print(f'Close: {tcp_connection.close()}')
    print(f'Accept: {tcp_connection.accept()}')
    print(f'Open: {tcp_connection.open()}')
    print(f'Open: {tcp_connection.open()}')
    print('================================')
    print(f'Accept: {tcp_connection.accept()}')
    print(f'Close: {tcp_connection.close()}')
    print(f'Close: {tcp_connection.close()}')

