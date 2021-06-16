# DQL - Data Query Language

Data Query Language, (not really a sub-language within Oracle databases) is the sub language where only the SELECT statement exists. Remember, in Oracle the SELECT statement is considered as DML, but DQL could be an interview question.

## DQL Clauses
### GROUP BY & HAVING
The **GROUP BY** clause will combine all rows by a column specified in a query and perform any aggregate functions which are stated.

```sql
SELECT NAME, COUNT(NAME) FROM STUDENT GROUP BY (NAME)
```

The **HAVING** clause will pass another filter similar to the WHERE clause after everything has been filtered and grouped.

```sql
SELECT NAME, COUNT(NAME) FROM STUDENT GROUP BY (NAME) HAVING COUNT(NAME) > 5;
```

If you try to perform this HAVING clause in a WHERE clause, a SQL error will be thrown, and it makes sense - the RDBMS doesn't want you to perform an aggregate function combining all rows, per each row. It's a performance safety measure.

## Scalar Functions
Scalar functions operate on **individual values** and will perform some operation per row, and can be used in the SELECT or WHERE clause.

- `TO_CHAR(DATE,'DATE_FORMAT')`
- `TO_DATE(DATE,'DATE_FORMAT')`
- `UPPER('VALUE')`
- `LOWER('VALUE')`

To write them in a query:

```sql
SELECT UPPER(NAME) FROM STUDENT;
SELECT NAME FROM STUDENT WHERE UPPER(NAME) LIKE 'P%'.
```

## Aggregate Functions
Aggregate functions operate on **multiple values (multiple rows)**. These functions are used to combine (aggregate) the values existing in one column.
- MAX(COLUMN), which returns the max value on a column.
- MIN(COLUMN), which returns the minimum value on a column.
- AVG(COLUMN), which returns the average value of the column.
- SUM(COLUMN), which returns the sum of the column.
- COUNT(COLUMN), which returns the count of elements in a column.
- And many others.

**These functions are used in the SELECT clause. They can't be used in the WHERE clause.**

If there is more than one column being selected in the SELECT column section of a query which is not aggregating, a GROUP BY clause is required.

In order to perform similar WHERE clause Boolean operations with aggregate functions, the HAVING clause can be used.