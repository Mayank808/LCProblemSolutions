# We want to do a left join excluding inner join in this case 
    # I.e we want to join all customers that have no rows in the orders table
SELECT name AS Customers # Select column to display as Customers
FROM Customers AS T1 # Choosing left table as Customers
LEFT JOIN ORDERS AS T2 # Left join orders
ON T1.id = T2.customerId # Left join on the forgin key relationship 
WHERE T2.customerId IS NULL # Exclude the inner join using this logic
