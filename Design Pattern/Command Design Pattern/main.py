from .AC import AC
from .TurnOnCommand import TurnOnCommand
from .TurnOffCommand import TurnOffCommand
from .SetTemperatureCommand import SetTemperatureCommand
from .RemoteControl import RemoteControl


if __name__ == "__main__":
    ac = AC()

    turn_on_command = TurnOnCommand(ac)
    turn_off_command = TurnOffCommand(ac)
    set_temp_command = SetTemperatureCommand(ac, 24)

    remote = RemoteControl()

    remote.set_command(turn_on_command)
    remote.press_button()

    remote.set_command(set_temp_command)
    remote.press_button()

    remote.press_undo(1)

    remote.set_command(turn_off_command)
    remote.press_button()

    remote.press_undo(1)
