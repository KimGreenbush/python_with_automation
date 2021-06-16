# Set Operations
## Set Operators
Set operators are different from joins. Instead of combining columns of two tables, **set operators combine the rows of different result sets**. Essentially, set operators perform some kind of (set) operation on two different queries.

Some set operators are:

### UNION [ALL]
UNION does not keep duplicates, but UNION ALL will

### INTERSECT
Only returns records in common between the queries

### MINUS
Removes from the first result set any rows that appear in the second result set and returns what remains

### EXCEPT
Same as MINUS, but for SQLServer instead of Oracle