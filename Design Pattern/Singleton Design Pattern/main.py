import threading

class DBConnection:
    _conObject = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._conObject is None:
            with cls._lock:
                if cls._conObject is None:
                    cls._conObject = super(DBConnection, cls).__new__(cls) # we are calling the base object class
                    # Initialization code can go here if needed
        return cls._conObject

    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        return DBConnection()

# Usage
if __name__ == "__main__":
    connection1 = DBConnection.getInstance()
    connection2 = DBConnection.getInstance()

    print(f"Are both connections the same instance? {'Yes' if connection1 is connection2 else 'No'}")
