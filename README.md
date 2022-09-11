# TQL 
**v0.5.0**

Table Query Language.

SQL like query language for csv files.


## Getting started
You will need the latest version of python installed in your computer. Clone the github repo and then run
`python main.py`

To exit the client use `Ctrl + C`

## Commands
###  load
**Syntax:**

`load [filename]`

**Parameters:**

1. _filename_ : The name of the csv file to load without the `.csv` extension. Rember this file should exist in the same directory as that of `main.py` file.
----
### save
**Syntax**

`save [filename]`

**Parameters**

1. _filename_ : Filename to save as. 
----

### In
**Syntax**

`in [columns] [operation] [conditions]`

**Parameters**

1. _columns_ : Column names separated by **,**
2. _operation_: See **Supported operations** for a list of operations and their function.
3. _conditions_: See **Supported conditions** for a list of conditions.

## Supported operations
### select
Displays the result data in a neat table.
### count
Outputs the count of records in result data.

## Supported conditions
### * operator
Selects all the records
### < operator
Selects all records greater than the given integer value in the given column.

Example:

`in Rank,Country select Rank<25`

### > operator
Selects all records less than the given integer value in the given column

Example

`in Rank,Country select Rank>36`

### = operator
Selects all records equals to the given integer value.
### # operator 
Selects records not equal to a given value. Works like `!=`.
### % operator
Selects records that starts with given string.

Example:

`in Rank,Country select %B`

Selects all country names that starts with **B**
### _ operator
Selects records that ends with given string.

Example:

`in Rank,Country select _a`

Selects all country names that ends with **a**
