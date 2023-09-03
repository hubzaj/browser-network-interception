import os
import threading
from http.server import HTTPServer, CGIHTTPRequestHandler
from logging import Logger, getLogger
from pathlib import Path
from threading import Event
from types import TracebackType

LOGGER: Logger = getLogger(__name__)


class WebServer:
    __SERVER_START_TIMEOUT: int = 30

    def __init__(self, directory: Path) -> None:
        self.__directory: Path = directory
        self.__port: int = 0
        self.__start_server_event: Event = Event()

    def __enter__(self) -> 'WebServer':
        LOGGER.info('Start web server')
        thread = threading.Thread(name='tmp_server', target=self.__start_server)
        thread.daemon = True
        thread.start()
        self.__start_server_event.wait(self.__SERVER_START_TIMEOUT)
        return self

    def __exit__(self, exc_type: BaseException, exc_val: BaseException, exc_tb: TracebackType) -> None:
        LOGGER.info('Shutdown web server')
        # TODO: kill server?
        pass

    def get_url(self) -> str:
        return f"http://localhost:{self.__port}/{os.path.basename(self.__directory)}"

    def __start_server(self) -> None:
        server_directory = os.path.dirname(self.__directory)
        os.chdir(server_directory)
        server = HTTPServer(('', self.__port), CGIHTTPRequestHandler)
        self.__port = server.server_port
        self.__start_server_event.set()
        server.serve_forever()
