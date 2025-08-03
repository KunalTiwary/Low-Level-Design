# The main gist —

When multiple child classes of the same parent class share common functionality in an inherited method, it indicates code reusability. However, if you don't want to use hard code repeatedly and want the ability to change the behavior at runtime, it becomes a candidate for the Strategy Design Pattern.

To resolve this, we should extract the shared logic into a separate interface or class (a strategy), which the child classes can use. This promotes composition over inheritance and allows greater flexibility and maintainability.

<img width="1400" height="528" alt="image" src="https://github.com/user-attachments/assets/2e561865-e39a-4c0b-9dbb-792d7c8efc11" />

## Note - 
- Here we are using constructor injection in vehicle class, this will help the child class to change the strategy at runtime.
  
