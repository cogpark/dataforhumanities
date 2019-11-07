
Let's start with a skeleton of the basic syntax, and then we'll fill in the details:

````
SELECT 
  table1.column_one, 
  table1.column_two, 
  table2.column_three
FROM
  table1
JOIN 
  table 2 
  ON table1.column_one = table2.column_one;
  ````
 
There are 3 major pieces to this query:
* The select clause, which includes columns from multiple tables
