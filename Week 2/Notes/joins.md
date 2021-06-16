# Joins
Used to combine two or more tables, joins are a database technique used in SELECT statements. Joins are normally performed comparing primary keys to foreign keys, however, they can be performed with any type of column, as long as the types match. Joins are a way of denormalizing a set of tables in order to aggregate or process some query.

They can be performed in many ways:

### INNER JOIN
The most commonly used type of join, **returns rows only if the columns specified** in the join clause match.

### OUTER JOIN
The OUTER keyword can be used with LEFT, RIGHT or FULL keywords to obtain rows which **some of the join columns are NULL**.
However, in Oracle, this word is optional. LEFT, RIGHT or FULL will be automatically OUTER.

### LEFT [OUTER] JOIN.
Returns the matching rows plus the ones that where **null in the first** table.

### RIGHT [OUTER] JOIN.
Returns the matching rows plus the ones that where **null in the second** table.

### FULL [OUTER] JOIN.
Returns all rows from both tables specified including the ones which had **null values on either side**.

### CROSS JOIN.
Returns the [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product) two or more tables.

### SELF JOIN.
An INNER JOIN performed matching two columns existing in the same table.
They represent hierarchies.

### NATURAL JOIN
Used as a shortcut so that the join predicate is not needed to be specified
The tables are joined on matching column names
As you can see, all JOINS are INNER unless otherwise specified with keywords.

To write a join:
```sql
SELECT A.FIRSTNAME, C.NAME FROM STUDENT S INNER JOIN COURSE C  ON S.COURSEID = C.ID;
SELECT A.FIRSTNAME, C.NAME FROM STUDENT S, COURSE C  WHERE S.COURSEID = C.ID;
SELECT A.FIRSTNAME, C.NAME FROM STUDENT S, COURSE C  WHERE S.COURSEID = C.ID(+);
```
To optimize joins, put the tables to join from more data to less data, and then perform the joins in order.