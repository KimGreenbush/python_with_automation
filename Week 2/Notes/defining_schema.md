# Defining Schema
## SQL Schema
This module covers schemas, constraints, multiplicity, and normalization in RDBMS systems.

### Helpful References
- [Oracle Docs - Constraints](https://docs.oracle.com/cd/B19306_01/server.102/b14200/clauses002.htm#:~:text=Use%20a%20constraint%20to%20define,declare%20them%20in%20two%20ways.)

### Defining 'Schema'
A [database schema](https://en.wikipedia.org/wiki/Database_schema) refers to the formal **structure** of data defined in a relational database. This includes the various tables in the database as well as their columns, data types, and the relationship between tables. Schemas are enforced using **constraints** when defining tables, and we can visualize the schema of relational databases through **entity-relationship diagrams, or ERDs**.

*NOTE: In Oracle databases, schema can also refer to a logical data storage structure. Oracle systems create a separate "schema" for each database user. However, we will refer to the original definition above from now on when we mention schema. Don't let this confuse you.*