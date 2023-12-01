Select customerID from Customers where custFName='Malik' and custLName='Talha'
And customerID =  (select * from Customer_Order where customerID= '1');
select * from Customer_Order where customerID= '1'
Select * from Customers where customerID= '1'
SELECT SUM(quantity * salePrice) FROM Customer_Order_Details where orderID='1'
Select * from Credit_Customers where customerID='1'