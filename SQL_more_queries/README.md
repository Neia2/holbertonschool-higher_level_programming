
# MySQL Commands and Concepts

This document provides an overview of essential MySQL commands and concepts, along with explanations on when and why to use them.

---

## 1. Creating a New MySQL User

To create a new user in MySQL, use the following command:

```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```
- **Purpose**: Creates a new user with a specified username and password.
- **When and Why**: Use to add a new user to MySQL for accessing databases. The `host` parameter defines where the user can connect from (`localhost` for local access, `%` for any host).

Example:

```sql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'userpassword';
```

---

## 2. Managing Privileges for a User

To grant privileges:

```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'host';
```
- **Purpose**: Grants specific privileges (e.g., `SELECT`, `INSERT`, `UPDATE`) to a user on a database or table.
- **When and Why**: Use to control what users can do within a database, ensuring data security by limiting permissions.

Example of granting all privileges on a database:

```sql
GRANT ALL PRIVILEGES ON my_database.* TO 'newuser'@'localhost';
```

To revoke privileges:

```sql
REVOKE privilege_type ON database_name.* FROM 'username'@'host';
```

---

## 3. PRIMARY KEY

A **PRIMARY KEY** is a column or set of columns that uniquely identifies each row in a table.

- **Purpose**: Ensures each record is unique and is often used as a reference in relationships between tables.
- **When and Why**: Use when designing tables to uniquely identify each row.

Example:

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);
```

---

## 4. FOREIGN KEY

A **FOREIGN KEY** is a column (or set of columns) that establishes a link between data in two tables, referencing a primary key in another table.

- **Purpose**: Enforces a relationship between two tables, ensuring referential integrity.
- **When and Why**: Use when you want to relate two tables, such as linking an `orders` table to a `customers` table by customer ID.

Example:

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

---

## 5. Using NOT NULL and UNIQUE Constraints

- **`NOT NULL`**: Ensures that a column cannot have a `NULL` value.
- **`UNIQUE`**: Ensures all values in a column are unique.

- **Purpose**: `NOT NULL` guarantees mandatory fields, while `UNIQUE` prevents duplicate values in a column.
- **When and Why**: Use `NOT NULL` for essential fields like email addresses and `UNIQUE` to avoid duplicate records.

Example:

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100) NOT NULL UNIQUE
);
```

---

## 6. Retrieving Data from Multiple Tables

To retrieve data from multiple tables, use **JOIN** statements or **subqueries**.

- **Purpose**: Fetch related data across multiple tables in a single query.
- **When and Why**: Use when you need data that’s spread across different tables.

Example using `INNER JOIN`:

```sql
SELECT customers.name, orders.amount
FROM customers
JOIN orders ON customers.id = orders.customer_id;
```

---

## 7. Subqueries

A **subquery** is a query nested within another query, often used for filtering or complex conditions.

- **Purpose**: Allows more flexible querying based on dynamic conditions.
- **When and Why**: Use for more complex filtering.

Example:

```sql
SELECT name FROM customers WHERE id IN (SELECT customer_id FROM orders WHERE amount > 100);
```

---

## 8. JOIN and UNION

- **JOIN**: Combines rows from two or more tables based on a related column.
    - **INNER JOIN**: Returns only matching records between tables.
    - **LEFT JOIN**: Returns all records from the left table and matching records from the right.
    - **RIGHT JOIN**: Returns all records from the right table and matching records from the left.

   Example of an `INNER JOIN`:

   ```sql
   SELECT users.name, orders.order_date
   FROM users
   INNER JOIN orders ON users.id = orders.user_id;
   ```

- **UNION**: Combines the results of two or more `SELECT` statements, removing duplicates.
   Example:

   ```sql
   SELECT name FROM customers
   UNION
   SELECT name FROM suppliers;
   ```

---

# JOIN Types with Examples

This section provides specific examples for different types of JOIN operations.

### Sample Tables

Assume we have two tables: `customers` and `orders`.

#### `customers` Table
| id | name    |
|----|---------|
| 1  | Alice   |
| 2  | Bob     |
| 3  | Charlie |
| 4  | David   |

#### `orders` Table
| order_id | customer_id | amount |
|----------|-------------|--------|
| 1        | 1           | 100    |
| 2        | 2           | 200    |
| 3        | 2           | 150    |
| 4        | 4           | 250    |

---

## INNER JOIN

An **INNER JOIN** returns only rows where there is a match in both tables.

```sql
SELECT customers.name, orders.amount
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id;
```

#### Result:
| name   | amount |
|--------|--------|
| Alice  | 100    |
| Bob    | 200    |
| Bob    | 150    |
| David  | 250    |

- **Explanation**: Only rows with matching `customer_id` in both tables are returned. `Charlie` is not included.

---

## LEFT JOIN

A **LEFT JOIN** returns all rows from the left table (in this case, `customers`), and matching rows from the right table (`orders`).

```sql
SELECT customers.name, orders.amount
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id;
```

#### Result:
| name    | amount |
|---------|--------|
| Alice   | 100    |
| Bob     | 200    |
| Bob     | 150    |
| Charlie | NULL   |
| David   | 250    |

- **Explanation**: All rows from `customers` are shown. `Charlie` has no matching order, so `amount` is `NULL`.

---

## RIGHT JOIN

A **RIGHT JOIN** returns all rows from the right table (`orders`), and matching rows from the left table (`customers`).

```sql
SELECT customers.name, orders.amount
FROM customers
RIGHT JOIN orders ON customers.id = orders.customer_id;
```

#### Result:
| name   | amount |
|--------|--------|
| Alice  | 100    |
| Bob    | 200    |
| Bob    | 150    |
| David  | 250    |

- **Explanation**: All rows from `orders` are included. Since every `order` has a matching `customer`, all names are shown.

---

### Summary

These examples illustrate:
- **INNER JOIN**: Only matches between both tables.
- **LEFT JOIN**: All from the left table, with `NULL` where no match in the right.
- **RIGHT JOIN**: All from the right table, with `NULL` where no match in the left.
