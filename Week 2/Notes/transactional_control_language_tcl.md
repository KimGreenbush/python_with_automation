# TCL - Transaction Control Language

Transaction Control Language statements are utilized to manage transactions within a relational database.

- **COMMIT**, any DML operations that were executed before the statements will be persisted permanently.
- **ROLLBACK**, any DML operations between two COMMIT statements will be completely erased (something like Ctrl + Z that will stop only when it reaches last time you opened the specific file). *Committed transactions cannot be rollbacked.*
- **SAVEPOINT**, utilized to ROLLBACK to a specific point in time.

The general flow of using TCL could be as follows:

```sql
"Many DML Operations"
SAVEPOINT A
"Many DML Operations"
ROLLBACK TO A
```