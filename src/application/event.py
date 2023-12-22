from typing import Union

class Event:
    """
    Event

    Converts the Event JSON sent by the client into a class 
    """
    def __init__(self, event_dict: dict[str:str]):
        """
        Init

        Sets up the Event object. 

        Parameters:
            event_dict: JSON sent from the client containing the data for an event
        """
        # Default Values
        self.type = ''
        self.ctrl_key = False
        self.shift_key = False
        self.meta_key = False
        self.key = ''
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.orientation = ''

        # The event_dict will only have values relevent to that event
        if type := event_dict.get('type'):
            self.type = type
        if ctrl := event_dict.get('ctrlKey'):
            self.ctrl_key = bool(ctrl)
        if shift := event_dict.get('shiftKey'):
            self.shift_key = bool(shift)
        if meta := event_dict.get('metaKey'):
            self.meta_key = bool(meta)
        if key := event_dict.get('key'):
            self.key = key
        if x := event_dict.get('x'):
            self.x = x
        if y := event_dict.get('y'):
            self.y = y
        if width := event_dict.get('width'):
            self.width = float(width)
        if height := event_dict.get("height"):
            self.height = float(height)
        if orientation := event_dict.get('orientation'):
            self.orientation = orientation

class Instruction:
    """
    Instruction

    A class reprenting the Instruction JSON that will be sent to the client. 
    """
    def __init__(self, type: str, name: str, parameters: list[str]):
        """
        Init

        Builds an Instruction object

        Parameters:
            type: Type of instruction (func, var, or command)
            name: Name of the instruction
            parameters: List of values needed to execute instruction
        """
        self.type = type
        self.name = name
        self.parameters = parameters

    def to_dict(self) -> dict[str:Union[str, list[str]]]:
        """
        To Dict

        Converts the Instruction object into a dictionary

        Returns
            dict[str: Union[str, list[str]]] Dictionary representing an Instruction
        """
        return {
            "type": self.type,
            "name": self.name,
            "parameters": self.parameters
        }
        

class ClientToServer:
    """
    Client To Server

    The message sent from the Client to the Server

    Properties
        time: int
            The time the application has been running. 1 for each frame
        events: list[Event]
            A list of the events the client recieved 
    """
    def __init__(self, dictionary: dict[str: Union[str, int, float, bool]]):
        """
        Init

        Creates a new ClientToServer message

        Parameters:
            dictionary: JSON sent from the client
        """
        self.time = 0
        self.events = []

        if time := dictionary.get('time'):
            self.time = time
        if events := dictionary.get("events"):
            for e in events:
                self.events.append(Event(e))
        
class ServerToClient: 
    """
    Server To Client

    The message the server sends to the client

    Properties
        instructions: list[dict]
            A list of instructions stored as dictionaries for the client to execute
    """
    def __init__(self):
        """
        Init

        Creates a new ServerToClient message
        """
        self.instructions = []

    def add_instruction(self, instruction: Instruction):
        """
        Add Instruction

        Adds an instruction to the list of instructions

        Parameters
            instruction: The instruction to add
        """
        self.instructions.append(instruction.to_dict())

    def add_instructions(self, instructions: list[Instruction]):
        """
        Add Instructions

        Adds a list of instructions to the list of instructions

        Parameters:
            instructions: The list of instructions to add
        """
        for instruction in instructions:
            self.add_instruction(instruction)
