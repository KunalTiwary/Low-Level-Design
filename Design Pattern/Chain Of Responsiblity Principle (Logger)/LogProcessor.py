from abc import ABC


class LogProcessor(ABC):
    def __init__(self, nextLogProcessor):
        self.INFO = 1
        self.DEBUG = 2
        self.ERROR = 3
        self.nextLogProcessor = nextLogProcessor

    def log(self, logLevel, message):
        if self.nextLogProcessor:
            self.nextLogProcessor.log(logLevel, message)
