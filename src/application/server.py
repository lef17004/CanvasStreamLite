from application.application import Application
from consoleui import UiChar

class Server:
    """
    Server

    Manages all the running applications. 

    Properties:
        applications
        available_keys

    """
    def __init__(self):
        self.applications = {}
        self.available_keys = list(range(10))

    def start_application(self) -> Application:
        session_key = str(self.available_keys.pop())
        self.applications[session_key] = Application(session_key)
        return self.get_session(session_key)

    def get_session(self, session_key):
        return self.applications.get(session_key)
    