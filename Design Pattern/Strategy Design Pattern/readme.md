# The main gist —

When multiple child classes of the same parent class share common functionality in an inherited method, it indicates code reusability. However, if you don't want to use hard code repeatedly and want the ability to change the behavior at runtime, it becomes a candidate for the Strategy Design Pattern.

To resolve this, we should extract the shared logic into a separate interface or class (a strategy), which the child classes can use. This promotes composition over inheritance and allows greater flexibility and maintainability.


<img width="1400" height="528" alt="image" src="https://github.com/user-attachments/assets/be2b5948-86d2-4aca-989a-d7e89f7fb234" />
