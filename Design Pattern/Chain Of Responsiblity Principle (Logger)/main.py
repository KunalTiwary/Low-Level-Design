from .LogProcessor import LogProcessor
from .DebugLogProcessor import DebugLogProcessor
from .ErrorLogProcessor import ErrorLogProcessor
from .InfoLogProcessor import InfoLogProcessor


if __name__ == "__main__":
    logger = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor()))
    logger.log("INFO", "HELLO")
    logger.log("ERROR", "HELLO2")
    logger.log("DEBUG", "HELLO3")


# you can run this by - python -m "{main File Name}.main", This makes Python treat the script as part of a
# package, resolving the imports correctly.