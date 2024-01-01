import random
from application.canvas import Canvas
from application.event import ServerToClient, Instruction, ClientToServer
from application.consolestreamcanvas import ConsoleStreamCanvas
from application.eventtoinput import event_to_input
from consoleui import UiButton, UiChar, UiViewManager, UiView, UiAction

class ButtonAction(UiAction):
    def __init__(self, canvas: Canvas) -> None:
        super().__init__()
        self.canvas = canvas

    def execute(self):
        print('executed')
        self.canvas.fill_style = 'red'
        
class Application:
    """
    Application

    The starting point of the application

    Properties
        session_key: str
            The identifier used to match the client to the application
    """
    def __init__(self, session_key):
        """
        Init

        Creates a new Main object
        """
        self.session_key = session_key
        self._width = 9.6015625 * 80 # Controls width of canvas on client side
        self._height = 16 * 24 # Controls height of canvas on client side
        self._canvas = Canvas()
        self._console_canvas = ConsoleStreamCanvas(self._canvas, 50, 50)
        self._root_view = UiView()
        self._manager = UiViewManager(self._root_view, self._console_canvas)
        self._listeners = [ 
            "click",
            # "keydown",
            # "keyup",
            # "dblclick",
            # "mousedown",
            # "mouseup",
            # "mousemove",
            # "touchstart",
            # "touchmove",
            # "touchend",
            # "touchcancel",
            # "load",
            "beforeunload",
            "resize"
        ] # List of events to get from the client

    def setup(self, setup_info) -> ServerToClient:
        """
        Setup

        Called only once at when the client connects to the sever. Used to set everything
        to its initial state. 

        Parameters:
            setup_info: ??? Going to change
                Data from the client needed to successfully setup the application

        Returns
            ServerToClient: The message to send to the client
        """
        font_height = 16
        font_width = 9.6015625

        rows = setup_info['height'] // font_height
        cols = setup_info['width'] // font_width

        self._height = rows * font_height
        self._width = cols * font_width

        response = ServerToClient()
        response.add_instructions([
            Instruction("command", "setSessionKey", [self.session_key]),
            Instruction("command", "setWidth", [self._width]),
            Instruction("command", "setHeight", [self._height]),
            Instruction("command", "setListeners", [self._listeners])
        ])

        button = UiButton()
        button.action = ButtonAction(self._canvas)
        self._root_view.add_gizmo(button)

        self._canvas.fill_style = "blue"
        self._canvas.font = "16px Monaco"

        response.add_instructions(self._canvas.get_draw_instructions())

        return response
    
    def loop(self, message: ClientToServer) -> ServerToClient:
        """
        Loop

        Called every frame by the client. Sends a message to the client containing instructions.

        Parameters:
            message: Message from the client containing event data

        Returns:
            ServerToClient: The response to send to the client
        """
        events = message.events
        response = ServerToClient()
        
        self._canvas.clear_instructions()
        
        for e in events:
            if e.type == 'click':
                input = event_to_input(e)
                print(input.type)
                self._manager.advance(input)
                
                response.add_instructions(self._canvas.get_draw_instructions())

        return response
    
    def shutdown(self):
        """
        Shutdown

        This is called when the client is refreshed or closed.

        Todo: Needs to be made
        """
        ...

    def error(self, client_error):
        """
        Error

        Errors from the client forwared to the server

        Todo: Needs to be made
        """
        response = {}

        return response