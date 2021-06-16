# DDL - Data Definition Language

Data Definition Language statements are utilized to define the database schema or skeleton. It is how we implement the design structure of it. Some of the keywords in this sublanguage are:

- **CREATE**, to create new objects or tables.

```sql
CREATE TABLE TABLE_NAME (C_NAME C_TYPE C_SYZE [NULL | NOT NULL], [CONSTRAINT])
```

- **ALTER**, to modify existing objects or tables.

```sql
ALTER TABLE TABLE_NAME [ADD | MODIFY | DROP] C_NAME
ALTER USER IDENTIFIED BY PASSWORD
```

- **DROP**, to delete existing objects or tables.

```sql
DROP TABLE TABLE_NAME [CASCADE]
```

- **TRUNCATE**, to delete all the data existing within a table leaving the skeleton of the table only.

```sql
TRUNCATE TABLE_NAME
```

This is similar to performing DELETE TABLE with no where clause, the key difference is that TRUNCATE commits at the end of the operation.

All DDL operations cannot be rolled back, which means that any **change made by these are permanent**.