Render as:

### Concept - 
General Flow of Object Creation - 

- In Python, the lifecycle of object creation follows these steps:

- Class Initialization – When a class is instantiated, Python internally calls the __new__() method first.

- __new__() Execution – By default, this method is inherited from the base object class. Its job is to:

- Allocate memory for the new object

- Create the instance

- Pass it to the __init__() method for initialization

- __init__() Execution – Initializes the newly created instance. This is why the first parameter is self, which represents the object returned by __new__().

Customizing __new__() for Singleton -

- In our implementation, we override the __new__() method to enforce the Singleton pattern (ensuring only one instance of the class exists). The logic is:

- Acquire a threading lock to make object creation thread-safe.

- Check if an instance already exists.

- If not, call the parent class’s __new__() (from object) to allocate memory and create the instance.

- Store the instance and always return the same reference for subsequent calls. 


```python
cls._conObject = super(DBConnection, cls).__new__(cls)
```

## Actual Usage

- In a production environment, we often need multiple database connections (say 20–30) rather than a single instance. The Singleton pattern is still useful here because it ensures that there is only one connection pool manager in the application.

- This manager (implemented as a Singleton) is responsible for creating and maintaining a fixed number of connections, and reusing them efficiently.

- So, while the Singleton itself only restricts the pool manager to a single instance, the pool manager internally applies an Object Pool pattern to restrict the total number of DB connections (e.g., 20–30).



