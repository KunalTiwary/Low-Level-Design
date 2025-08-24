# Main Gist-
It provides a simplified interface to a set of complex subsystems, making it easier for clients to interact with them without worrying about the details.

Without facade → 
1. Client has to deal with multiple classes and their complex interactions.
2. If any new logic is changed/added/deleted, the client has to change its flow

We can create multiple sub-facades and use it, this is simplify the code even further

## Diff between facade and proxy -
- Proxy can create the object of only one class
- Proxy is an implementation of the same abstract class

## Diff between facade and adapter - 
- Adapter pattern is used when the client and adaptee is incompatible whereas
- facade is used to hide the complexity
