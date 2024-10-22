import socket
import struct

class ConanExilesRCON:
    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password
        self.socket = None
        self.request_id = 0

    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print("Соединение с сервером Conan Exiles установлено.")
            if self._authenticate():
                print("Авторизация прошла успешно.")
            else:
                print("Не удалось авторизоваться. Проверьте пароль и настройки.")
                self.socket.close()
                self.socket = None
        except Exception as e:
            print(f"Ошибка подключения: {e}")
            self.socket = None

    def _authenticate(self):
        try:
            auth_request = self._build_packet(self.password, packet_type=3)  # Type 3 - Auth
            self.socket.send(auth_request)
            response = self._receive_packet()
            if response:
                return response["type"] == 2  # Type 2 - Auth success
            else:
                return False
        except Exception as e:
            print(f"Ошибка авторизации: {e}")
            return False

    def _build_packet(self, message, packet_type):
        self.request_id += 1
        payload = struct.pack(f'<ii{len(message)+2}s', self.request_id, packet_type, message.encode('utf-8') + b'\x00\x00')
        packet_length = struct.pack('<i', len(payload))
        return packet_length + payload

    def _receive_packet(self):
        try:
            packet_length = struct.unpack('<i', self.socket.recv(4))[0]
            packet = self.socket.recv(packet_length)
            request_id, packet_type = struct.unpack('<ii', packet[:8])
            message = packet[8:].decode('utf-8').strip('\x00')
            return {"request_id": request_id, "type": packet_type, "message": message}
        except Exception as e:
            print(f"Ошибка при получении пакета: {e}")
            return None

    def command(self, command):
        if not self.socket:
            print("Нет активного подключения.")
            return
        try:
            command_packet = self._build_packet(command, packet_type=2)  # Type 2 - Command
            self.socket.send(command_packet)
            response = self._receive_packet()
            if response:
#                print(f"Ответ от сервера: \n {response['message']}")
                return response['message']
            else:
                print("Не удалось получить ответ от сервера.")
        except Exception as e:
            print(f"Ошибка при отправке команды: {e}")

    def close(self):
        if self.socket:
            self.socket.close()
            print("Соединение закрыто.")
