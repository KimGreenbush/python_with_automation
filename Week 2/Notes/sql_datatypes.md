# Data types

When defining the properties of an entity in the database (i.e. the columns), you must specify the data type to store. Common SQL datatypes include:

Numeric
- BIT
- TINYINT
- BIGINT
- DECIMAL
- NUMERIC
- FLOAT
- REAL

Date/Time
- DATE
- TIMESTAMP
- DATETIME
- TIME
- YEAR

Character/String
- CHAR
- NCHAR
- VARCHAR
- NVARCHAR
- NTEXT

Binary
- BINARY
- VARBINARY
- IMAGE
- Miscellaneous
- CLOB
- BLOB
- XML
- JSON

Each database vendor may support their own data types, or not support some of the ones listed above. Refer to the specific vendor documentation for more information.

### Conventions
SQL is a *case-insensitive language*, but the **convention is to use UPPERCASE to refer to SQL keywords and lowercase for non-SQL specific entities** (like table or column names). This helps distinguish between SQL keywords and other words. Also, for readability purposes we should **split long commands or queries into multiple lines**.

For example, this:

```sql
SELECT * FROM table1
LEFT JOIN table2 ON table1.a = table2.b
WHERE table1.x < 5
AND table2.y > 8
ORDER BY table1.a DESC;
```
is much more readable than:

```sql
SELECT * FROM table1 LEFT JOIN table2 ON table1.a = table2.b WHERE table1.x < 5 AND table2.y > 8 ORDER BY table1.a DESC;
```