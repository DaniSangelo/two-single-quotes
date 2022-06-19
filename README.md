## two-single-quotes
A simple script to add two single quotes to a file - specifically .sql files.

💡

I came up with this idea when I needed to create a script to create a database object (stored procedure, function, trigger and tables, etc) in different databases simultaneously. Thats because in the .sql file could be some message come from a raiserror statement - or something like that, for example.

Let's say I created a stored procedure `[master].dbo.my_customized_sp` whose purpose is to execute any sql statement on all databases. To run my sql statement on all databases that I would, I must to run, sometimes, something like that:

```sql
EXEC [master].dbo.my_customized_sp
  @stmt = N'CREATE OR ALTER PROCEDURE dbo.insert_customer
    @strFirstName VARCHAR(20)
  AS
  BEGIN
    IF ISNULL(@strFirstName, '') = ''
    BEGIN
      RAISERROR('First name must be informed', 16, 1);
      RETURN;
    END;
    /*
      statements
    */
  END;'
```

Note that the `@stmt` parameter is of type `NVARCHAR`. So, if inside the `insert_customer` body there is a statement that uses single quotes, as shown above, then we have a problem. The `EXEC [master].dbo.my_customized_sp` won't work.

In order to fix that problem, I made, with an important contribuition from my teammate **Geandreson Costa**, a script to duplicate each single quoted found.
```sql
EXEC [master].dbo.my_customized_sp
  @stmt = N'CREATE OR ALTER PROCEDURE dbo.insert_customer
    @strFirstName VARCHAR(20)
  AS
  BEGIN
    IF ISNULL(@strFirstName, '''') = ''''
    BEGIN
      RAISERROR(''First name must be informed'', 16, 1);
      RETURN;
    END;
    /*
      statements
    */
  END;'
```
