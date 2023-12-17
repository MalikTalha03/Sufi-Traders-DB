SELECT
    YEAR(CO.orderDate) AS OrderYear,
    MONTH(CO.orderDate) AS OrderMonth,
    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS MonthlySales
FROM
    Customer_Order CO
LEFT JOIN
    Customer_Order_Details COD ON CO.orderID = COD.orderID
WHERE
    CO.customerID = 1
    AND YEAR(CO.orderDate) = YEAR(GETDATE())
GROUP BY
    YEAR(CO.orderDate),
    MONTH(CO.orderDate)
ORDER BY
    OrderYear,
    OrderMonth;
