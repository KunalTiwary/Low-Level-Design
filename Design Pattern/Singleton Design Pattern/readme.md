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

# Issues in Double Locking -
Issue 1 - 
This way we are putting locks here - 

```python
with cls._lock:
```
Now to be precise when super(DBConnection, cls).__new__(cls) is called, there will be certain instructions that will be executed behind the scenes like - 
1) Allocate memory
2) Initialize the member variables (if any)
3) Return the address of the memory to cls._conObject

But, for better performance CPU changes the order without changing the logic. In our case 1->2->3 can be executed in 1->3->2 order. Then, in the new order cls._conObject will have the object before initialization of member variables. Therefore, some other thread can use it without the member variables which will cause some errors. 

Issue 2 -
In CPU we have different cores and each core has its own cache. The cores uses there own L1 cache and then write it to memory after sometime. Now, let's say thread 1 has already created the object and sitting in L1 cache of some particular core. Then, thread 2 is scheduled to a different core and but the object created by thread 1 is still not in memory so thread 2 will create one more object and store in it's core's L1 cache. 


However, in Java we use the volatile keyword while creating the class itself - 
```java
private static volatile DBconnection conObject;
```

This will help us because - 
- It ensures that nothing is written in L1 cache but everything is written in memory directly (Issue 2 is resolved).
- It will make sure that all the instructions before and after the volatile object creation will execute in the same group. In our case, step 3 is volatile so, step 1 and step 2 can be reordered by CPU but it has to be done before step 3 and written in memory.



## Object pool design pattern

- In a production environment, we often need multiple database connections (say 20–30) rather than a single instance. The Singleton pattern is still useful here because it ensures that there is only one connection pool manager in the application.

- This manager (implemented as a Singleton) is responsible for creating and maintaining a fixed number of connections, and reusing them efficiently.

- So, while the Singleton itself only restricts the pool manager to a single instance, the pool manager internally applies an Object Pool pattern to restrict the total number of DB connections (e.g., 20–30).

Use this diagram with locks :
<img width="979" height="367" alt="image" src="https://github.com/user-attachments/assets/37ffd3f9-20ed-46d8-a525-dde024527877" />

### Advantages -
- Reduces overhead and latency of creating and destroying highly CPU and memory intensive objects.
- Controls the number of objects in a pool

### Dis-Advantages - 
- Resource leak can happen if not handled properly
- Requires more memory for storing objects.
- Adds complecity of managing pool
