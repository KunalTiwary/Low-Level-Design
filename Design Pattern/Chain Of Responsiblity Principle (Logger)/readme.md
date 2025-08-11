## Here why we are not using Factory Design pattern to create the correct logger object?

Ans - Because, We are not deciding "which logger to create" at runtime for each message. Instead, we always use the same chain, and the chain itself decides whether to process or pass the request along.

In Factory:

Selection happens at creation time (choose one object).

In Chain of Responsibilty:

Selection happens at request handling time (handlers pass request until one processes it).

## In an ATM’s note dispensing system - 
Each type of note can contribute to serving the total amount, and multiple dispensers are involved in a single transaction. The Factory pattern is not suitable here because it creates only one type of object for a given request, whereas the Chain of Responsibility pattern allows multiple handlers to process the same request sequentially.
- If you withdraw ₹3800:
- The ₹2000 dispenser tries first, gives 1 note, passes remaining ₹1800 to the next
- The ₹500 dispenser gives 3 notes, passes remaining ₹300 to the next.
- The ₹100 dispenser gives 3 notes, done.
