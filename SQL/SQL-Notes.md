 # What is SQL
SQL (pronounced S.Q.L. or Sequel, no one really cares) stands for Structured Querying Language and is a language that is used to query, form, and manipulate databases.
# Servers
The computer that contains your database or databases. This is typically your highest level of "container" for databases.
# Databases
A database is a collection of Schemas and Tables that we can interact with.
# Schemas
Schemas are the highest level of organization in many Databases and can contain multiple tables.
# Tables
Tables can be thought of in the same way you think about sheets in Excel. It's a collection of columns and rows that we'll be interacting with.
# Different Database Types
I'll be talking about SQL like it's a standardized language and although it technically is, in practice SQL databases you'll most likely be interacting with are going to created and run by major corporations who will sprinkle their own flavor of SQL on top of or in lieu of standard SQL. The commands we'll be focusing in this course are pretty standard and shouldn't be drastically different from that which you'll be using in most other databases. Some of the biggest databases are listed below: MySQL - Open Source - Current Development by Oracle
SQL Server - Created by Microsoft PostgreSQL - Open Source
Oracle Database - Created by Oracle
# What is field? 
Every table is broken up into smaller entities called fields. The fields in the CUSTOMERS table consist of ID, NAME, AGE, ADDRESS and SALARY. 
A field is a column in a table that is designed to maintain specific information about every record in the table. 
# What is record or row? 
A record, also called a row of data, is each individual entry that exists in a table. For example, there are 7 records in the above CUSTOMERS table. Following is a single row of data or record in the CUSTOMERS table: 
# Basic Querying :-
* SELECT :-
* The most basic query used to pull data from a database.
* select * from databasename;
* select weather,temperature from database;
  - This will only select the weather and temperature columns from the dataset.
  
