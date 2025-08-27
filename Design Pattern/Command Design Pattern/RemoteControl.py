from .Command import Command


class RemoteControl:
    def __init__(self):
        self.command = None
        self.stack = []

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.stack.append(self.command)
            self.command.execute()

    def press_undo(self, times):
        if self.stack and times:
            lastCommand = self.stack.pop()
            lastCommand.undo()
            times -= 1
