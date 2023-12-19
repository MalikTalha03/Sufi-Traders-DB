Create Database Sufi_Traders;

CREATE TABLE Employee (
    employeeID int PRIMARY KEY,
    empFName varchar(25) NOT NULL,
    empLName varchar(25),
    empContact varchar(11) NOT NULL,
    employeeAddress varchar(100) NOT NULL,
    salary decimal(10, 2) NOT NULL,
    employeeType varchar(25) NOT NULL,
    passwords varchar(150)
);

CREATE TABLE Customers (
    customerID int PRIMARY KEY,
    custFName varchar(25) NOT NULL,
    custLName varchar(25),
    customerContact varchar(11) NOT NULL
);

CREATE TABLE Credit_Customers (
    creditCustomerID int PRIMARY KEY,
    customerID int FOREIGN KEY REFERENCES Customers(customerID) NOT NULL UNIQUE,
    totalCredit decimal(10, 2) NOT NULL
);

CREATE TABLE Customer_Order (
    orderID int PRIMARY KEY,
    customerID int FOREIGN KEY REFERENCES Customers(customerID) NOT NULL,
    employeeID int FOREIGN KEY REFERENCES Employee(employeeID) NOT NULL,
    orderDate date NOT NULL,
    orderTime time(7) NOT NULL,
    paymentStatus varchar(15) NOT NULL
    CONSTRAINT paystat CHECK (paymentStatus IN ('Paid', 'Credit','Partially Paid'))
);

CREATE TABLE Categories (
    categoryID int PRIMARY KEY,
    categoryName varchar(25) NOT NULL
);

CREATE TABLE Discounts (
    discountID int PRIMARY KEY,
    orderID int FOREIGN KEY REFERENCES Customer_Order(orderID) NOT NULL,
    amount decimal(10, 2) NOT NULL
);

CREATE TABLE Supplier (
    supplierID int PRIMARY KEY,
    supplierName varchar(25) NOT NULL,
    supplierAddress varchar(50) NOT NULL,
    supplierContact varchar(11) NOT NULL
);

CREATE TABLE Supplier_Order (
    orderID int PRIMARY KEY,
    orderDate date NOT NULL,
    supplierID int FOREIGN KEY REFERENCES Supplier(supplierID) NOT NULL,
    totalAmount decimal(10, 2) NOT NULL,
    paymentStatus varchar(15) NOT NULL
    CONSTRAINT paymentst CHECK (paymentStatus IN ('Paid','Not Paid','Partially Paid'))
);

CREATE TABLE Products (
    productID int PRIMARY KEY,
    productName varchar(50) NOT NULL,
    salePrice decimal(10, 2) NOT NULL,
    categoryID int FOREIGN KEY REFERENCES Categories(categoryID) NOT NULL,
    supplierID int FOREIGN KEY REFERENCES Supplier(supplierID) NOT NULL,
    inventory int NOT NULL
);

CREATE TABLE Supplier_Order_Details (
    orderId int FOREIGN KEY REFERENCES Supplier_Order(orderID) NOT NULL,
    productID int FOREIGN KEY REFERENCES Products(productID) NOT NULL,
    purchasePrice decimal(10, 2) NOT NULL,
    quantity int NOT NULL,
    PRIMARY KEY (orderId, productID)
);

CREATE TABLE Customer_Order_Details (
    orderId int FOREIGN KEY REFERENCES Customer_Order(orderID) NOT NULL,
    productID int FOREIGN KEY REFERENCES Products(productID) NOT NULL,
    quantity int NOT NULL,
    salePrice decimal(10, 2) NOT NULL,
    PRIMARY KEY (orderId, productID)
);

CREATE TABLE Customer_Transactions (
    transactionID int PRIMARY KEY,
    transactionType varchar(15) NOT NULL
    CONSTRAINT chk_transaction CHECK (transactionType IN ('Cash', 'Credit', 'Bank Transfer','Refund')),
    totalAmount decimal(10, 2) NOT NULL,
    orderID int FOREIGN KEY REFERENCES Customer_Order(orderID) NOT NULL,
    transactionDate date NOT NULL,
    transactionTime time(7) NOT NULL
);

CREATE TABLE Supplier_Transactions (
    transactionID int PRIMARY KEY,
    transactionType varchar(15) NOT NULL
    CONSTRAINT chksupp_transaction CHECK (transactionType IN ('Cash', 'Bank Transfer')),
    totalAmount decimal(10, 2) NOT NULL,
    orderID int FOREIGN KEY REFERENCES Supplier_Order(orderID) NOT NULL,
    transactionDate date NOT NULL
);
