from .LogProcessor import LogProcessor


class InfoLogProcessor(LogProcessor):
    def __init__(self, nextLogProcessor):
        super().__init__(nextLogProcessor)

    def log(self, logLevel, message):
        if logLevel == "INFO":
            print(f"INFO: {message}")
        else:
            super().log(logLevel, message)

