SQL - Introduction



# SQL Commands and Purposes

## 1. CREATE DATABASE
```sql
CREATE DATABASE IF NOT EXISTS database_name;
```
- **Purpose**: To create a new database for storing related data tables.
- **When and Why**: Use when setting up a new project or system. The `IF NOT EXISTS` clause prevents errors if the database already exists.

## 2. USE
```sql
USE database_name;
```
- **Purpose**: Selects a database to make it the current one for executing subsequent commands.
- **When and Why**: Use after creating or selecting a specific database to focus on.

## 3. CREATE TABLE
```sql
CREATE TABLE table_name (
    column1_name datatype constraints,
    column2_name datatype constraints
);
```
- **Purpose**: To create a new table to store data.
- **When and Why**: Use when defining the structure for data storage, including columns and data types. Constraints (like `PRIMARY KEY`) ensure data integrity.

## 4. ALTER TABLE
```sql
ALTER TABLE table_name ADD COLUMN new_column_name datatype;
```
- **Purpose**: Modify an existing table’s structure.
- **When and Why**: Use when you need to add, remove, or modify columns in a table after it’s created.

## 5. DROP DATABASE / DROP TABLE
```sql
DROP DATABASE database_name;
DROP TABLE table_name;
```
- **Purpose**: Deletes an entire database or table, along with all data within it.
- **When and Why**: Use cautiously, typically during cleanup or when deprecating databases/tables.

## 6. INSERT INTO
```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```
- **Purpose**: Add new rows of data into a table.
- **When and Why**: Use when populating tables with data. Ensures data entry aligns with column types and constraints.

## 7. SELECT
```sql
SELECT column1, column2 FROM table_name WHERE condition;
```
- **Purpose**: Retrieve data from a table.
- **When and Why**: Use to fetch specific data based on conditions, for reading, analyzing, or displaying data. It’s one of the most-used SQL commands.

## 8. UPDATE
```sql
UPDATE table_name SET column1 = value1 WHERE condition;
```
- **Purpose**: Modify existing data within a table.
- **When and Why**: Use to make changes to data, such as correcting records or updating outdated information.

## 9. DELETE
```sql
DELETE FROM table_name WHERE condition;
```
- **Purpose**: Remove rows from a table based on specific conditions.
- **When and Why**: Use when you need to delete records, typically to clear outdated, irrelevant, or incorrect data.

## 10. TRUNCATE TABLE
```sql
TRUNCATE TABLE table_name;
```
- **Purpose**: Quickly removes all rows from a table without deleting the table itself.
- **When and Why**: Use when you need to clear all data in a table but retain the structure for new data.

## 11. JOIN
```sql
SELECT columns FROM table1 JOIN table2 ON table1.column = table2.column;
```
- **Purpose**: Combine rows from two or more tables based on related columns.
- **When and Why**: Use to fetch data across tables, especially when working with relational databases. Types include `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL JOIN`.

## 12. GROUP BY
```sql
SELECT column, COUNT(*) FROM table_name GROUP BY column;
```
- **Purpose**: Group rows based on one or more columns to perform aggregate calculations.
- **When and Why**: Use with aggregate functions (like `COUNT`, `SUM`, `AVG`) for reporting and analytics.

## 13. ORDER BY
```sql
SELECT column FROM table_name ORDER BY column ASC|DESC;
```
- **Purpose**: Sorts the result set based on one or more columns.
- **When and Why**: Use for organizing output to make data easier to analyze, especially when ordering by date, name, or priority.

## 14. HAVING
```sql
SELECT column, COUNT(*) FROM table_name GROUP BY column HAVING COUNT(*) > 1;
```
- **Purpose**: Filters results after a `GROUP BY` operation.
- **When and Why**: Use when you need to filter aggregate results, as `WHERE` cannot be used directly with aggregates.

## 15. Subquery
```sql
SELECT column FROM table_name WHERE column IN (SELECT column FROM another_table);
```
- **Purpose**: Query nested within another query.
- **When and Why**: Use for complex queries where a secondary condition or dataset is needed for filtering.

## 16. MySQL Functions
Examples:
```sql
SELECT UPPER(column) FROM table_name; -- Converts text to uppercase
SELECT COUNT(column) FROM table_name; -- Counts rows in a column
SELECT NOW(); -- Returns the current date and time
```
- **Purpose**: Built-in functions provide specific operations like text manipulation, date and time handling, and aggregation.
- **When and Why**: Use for data processing, analytics, and calculations without needing external tools.

