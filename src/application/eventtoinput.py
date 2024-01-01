from consoleui import UiInput, InputType
from application.event import Event

def event_to_input(event: Event) -> UiInput:
    input = None
    if event.type == 'click':
        print('clock')
        input = UiInput()
        input.type = InputType.CLICK
        input.x = event.x // 10
        input.y = event.y // 20

    return input