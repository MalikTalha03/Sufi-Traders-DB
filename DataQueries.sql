SELECT
    DATEPART(HOUR, CO.orderDate) AS OrderHour,
    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS HourlySales
FROM
    Customer_Order CO
LEFT JOIN
    Customer_Order_Details COD ON CO.orderID = COD.orderID
WHERE
    CO.customerID = 1
    AND CONVERT(DATE, CO.orderDate) = '2023-12-4'
GROUP BY
    DATEPART(HOUR, CO.orderDate)
ORDER BY
    OrderHour;
