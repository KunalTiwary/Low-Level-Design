from .LogProcessor import LogProcessor


class ErrorLogProcessor(LogProcessor):
    def __init__(self, nextLogProcessor=None):
        super().__init__(nextLogProcessor)

    def log(self, logLevel, message):
        if logLevel == "ERROR":
            print(f"ERROR: {message}")
        else:
            super().log(logLevel, message)