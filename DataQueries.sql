SELECT
    CONVERT(DATE, CO.orderDate) AS OrderDate,
    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
FROM
    Customer_Order CO
LEFT JOIN
    Customer_Order_Details COD ON CO.orderID = COD.orderID
WHERE
    CO.customerID = 1
    AND MONTH(CO.orderDate) = MONTH(GETDATE())
    AND YEAR(CO.orderDate) = YEAR(GETDATE())
GROUP BY
    CONVERT(DATE, CO.orderDate)
ORDER BY
    OrderDate;
