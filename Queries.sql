Create Database Sufi_Traders;

Create Table Employee (
employeeID int Primary Key,
empFName varchar(25) Not Null,
empLName varchar(25),
empContact varchar(11) Not Null,
employeeAddress varchar(100) Not Null,
salary decimal(10, 2) Not Null,
employeeType varchar(25) Not Null
);

Create Table Customers (
customerID int Primary Key,
custFName varchar(25) Not Null,
custLName varchar(25),
customerContact varchar(11) Not Null
);

Create Table Credit_Customers(
creditCustomerID int Primary Key,
customerID int Foreign Key References Customers(customerID) Not Null,
totalCredit decimal(10, 2) Not Null
);

Create Table Customer_Order(
orderID int Primary Key,
orderTime timestamp Not Null,
customerID int Foreign Key References Customers(customerID) Not Null,
employeeID int Foreign Key References Employee(employeeID) Not Null
);

Create Table Categories(
categoryID int Primary Key,
categoryName varchar(25) Not Null
);

Create Table Discounts(
discountID int Primary Key,
orderID int Foreign Key References Customer_Order(orderID) Not Null,
amount decimal(10, 2) Not Null
);

Create Table Supplier (
supplierID int Primary Key ,
supplierName varchar(25) Not Null,
supplierAddress varchar(50) Not Null,
supplierContact varchar(11) Not Null
);

Create Table Supplier_Order(
orderID int Primary Key,
orderDate date Not Null,
supplierID int Foreign Key References Supplier(supplierID) Not Null,
totalAmount decimal(10, 2) Not Null
);

Create Table Products (
productID int Primary Key,
productName varchar(50) Not Null,
salePrice decimal(10, 2) Not Null,
categoryID int Foreign Key References Categories(categoryID) Not Null,
supplierID int Foreign Key References Supplier(supplierID) Not Null,
inventory int Not Null
);

Create Table Supplier_Order_Details (
orderId int Foreign Key References Supplier_Order(orderID) Not Null,
productID int Foreign Key References Products(productID) Not Null,
purchasePrice decimal(10, 2) Not Null,
quantity int Not Null
Primary Key (orderID, productID)
);

Create Table Customer_Order_Details (
orderId int Foreign Key References Customer_Order(orderID) Not Null,
productID int Foreign Key References Products(productID) Not Null,
quantity int Not Null,
Primary Key (orderID, productID)
);

Create Table Customer_Transactions(
transactionID int Primary Key,
transactionType varchar(15) Not Null
CONSTRAINT chk_transaction CHECK (transactionType IN ('Cash', 'Credit', 'Bank Transfer')),
totalAmount decimal(10, 2) Not Null,
orderID int Foreign Key References Customer_Order(orderID) Not Null,
transactionTime timestamp Not Null

);

Create Table Supplier_Transactions(
transactionID int Primary Key,
transactionType varchar(15) Not Null
CONSTRAINT chksupp_transaction CHECK (transactionType IN ('Cash', 'Bank Transfer')),
totalAmount decimal(10, 2) Not Null,
orderID int Foreign Key References Supplier_Order(orderID) Not Null,
transactionDate date Not Null
);

