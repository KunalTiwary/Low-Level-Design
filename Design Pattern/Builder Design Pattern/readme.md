### The main gist is - 

- Useful when an object has many optional or mandatory fields.
- Instead of a large, messy constructor with many optional parameters, the Builder pattern lets you build an object gradually through method chaining.
- At the end, you call a build() (or similar) method to get the final object.

### Differnce between Decorator and Builder

- Decorator can handle dynamic creations of objects but Builder has to work on the predefined builder classes. Example, using decorator we can create a lot of combinations of pizza's and its decorators but for builder we need to define builder class for each of the types of pizza's (example - paneer pizza builder, mushroom pizza builder, panner mushroom pizza builder)
