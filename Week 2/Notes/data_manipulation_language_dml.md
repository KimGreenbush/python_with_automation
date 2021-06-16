# DML - Data Manipulation Language

Data Manipulation Language statements are used to perform CRUD operations on the actual data. Operations are normally performed by row in a relational database.

- **INSERT**, to insert a new row into a table.

```sql
INSERT INTO TABLE_NAME VALUES (V1, V2, ..., VN)
INSERT INTO TABLE_NAME (C1, C2, C3) VALUES (V1, V2, V3)
```

- **UPDATE**, to update one or more rows column values of a table that match a specific WHERE clause.

```sql
UPDATE TABLE_NAME SET C1 = V1, ... , CN = VN WHERE X = Y
```

- **DELETE**, to delete one or more rows of a table that match a specific WHERE clause.

```sql
DELETE TABLE_NAME WHERE [condition]
```

- **SELECT**, to obtain one or more rows of a table that match a specific WHERE clause. In ORACLE databases this one is considered DML. This is how we perform queries in a database.

```sql
SELECT C1, ..., CN FROM TABLE_NAME [table] WHERE [condition] GROUP BY [expression]
HAVING [condition] ORDER BY table.field
```