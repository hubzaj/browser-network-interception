import os
import threading
from http.server import HTTPServer, CGIHTTPRequestHandler
from threading import Event


class WebServer:
    __SERVER_START_TIMEOUT: int = 30

    def __init__(self, directory: str) -> None:
        self.__directory: str = directory
        self.__port: int = 0
        self.__start_server_event: Event = Event()

    def __enter__(self) -> 'WebServer':
        thread = threading.Thread(name='tmp_server', target=self.__start_server)
        thread.daemon = True
        thread.start()
        self.__start_server_event.wait(self.__SERVER_START_TIMEOUT)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: kill server?
        pass

    def get_url(self) -> str:
        return f"http://localhost:{self.__port}/{os.path.basename(self.__directory)}"

    def __start_server(self):
        server_directory = os.path.dirname(self.__directory)
        os.chdir(server_directory)
        server = HTTPServer(('', self.__port), CGIHTTPRequestHandler)
        self.__port = server.server_port
        self.__start_server_event.set()
        server.serve_forever()
