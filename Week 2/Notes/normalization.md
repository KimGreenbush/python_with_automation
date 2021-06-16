# Normalization

[**Normalization**](https://en.wikipedia.org/wiki/Database_normalization) refers to an optimization process of structuring a relational database in a way that *reduces redundancy* of data and improves data integrity and consistency. There are many different normal forms, which relate to the degree to which a database has been normalized. We will look at the first three normal forms, each of which build upon the previous:

- 1NF - must have a primary key, no repeating groups, and atomic columns
- 2NF - must already be in 1NF, plus have no partial dependencies
- 3NF - must already be in 2NF, plus have no transitive dependencies

The first normal form enforces that a table must:
- Have a primary key
- Each column should be as granular as possible (e.g. "Name" column should be broken up into: "First Name", "Last Name", "Middle Name", etc..)

To be in second normal form, a table must also:
- Not have columns that are dependent on only one part of the key
- If there are no composite primary keys, you are automatically in 2NF

Finally, to get to third normal form, a table must also:
- Not have transitive dependencies
    - This means that if column C relates to column B which relates to column A which is the primary key, this is not in 3NF because C is related to the primary key but indirectly (it is a transitive dependency)

To advance into higher normal forms, we typically "break up" tables into multiple tables and relate them to each other via foreign keys.

A good way of remembering these normal forms in order is to remember the legal proceeding of swearing to tell the truth, the whole truth, and nothing but the truth. In relational databases, we *must have the key (1NF), the whole key (2NF), and nothing but the key (3NF)*.