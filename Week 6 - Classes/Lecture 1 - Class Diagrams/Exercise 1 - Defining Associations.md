# Exercise 1
You should provide examples for each of the following relationship types:
- Dependency
- Simple Association
- Bidirectional Association
- Aggregation
- Composition

## Dependency
One example of a Dependency Association could be between a Circle and a Shape. A Circle is, itself, a Shape (extending
the Shape class -- meaning any changes to Shape would/could affect the Circle).

## Simple Association
One example of a Simple Association could be between an Order and a Product. The Order would know which
Products are a part of it, but the Product would not know about which Orders it is associated with.

## Bidirectional Association

One example of a Bidirectional Association could be between Employees and a Store. Each Employee
would know what Store they work for/at, and the Store would know which Employees work there.

## Aggregation

One example of an Aggregation Association could be between Students and Classes. A Student can exist
independent of a Class, if a Class is cancelled or stopped the Student would still remain.

## Composition
One example of a Composition Association could be between Customers (Class A) and their Orders (Class B). Orders
will know what Customer they belong to, but cannot exist without the Customer also existing.
