### Main Gist -

- Used for designing word processor
- This pattern helps us to reduce memory usage by sharing data among multiple objects. This way memory is saved.
  
The Flyweight pattern keeps the shared state (intrinsic) in one central place (the flyweight object), and then lets many lightweight instances reuse that shared state.

When you need something unique for each instance, you supply it as extrinsic state at runtime.

In short:
Shared stuff lives inside the flyweight → unique stuff is passed in when you use it.
