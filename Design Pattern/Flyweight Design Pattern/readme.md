### Main Gist -

- Used for designing word processor
- This pattern helps us to reduce memory usage by sharing data among multiple objects. This way memory is saved.
  
The Flyweight pattern keeps the shared state (intrinsic) in one central place (the flyweight object), and then lets many lightweight instances reuse that shared state.

When you need something unique for each instance, you supply it as extrinsic state at runtime.

In short:
Shared stuff lives inside the flyweight → unique stuff is passed in when you use it.

# Where to use it ?
- When memory is limited
- When objects share data -
1) Intrinsic Data: shared across objects and remain same once defined one value.
2) Extrinsic Data: changes based on client input and differs from one object to another.
- Creation ob objects.
