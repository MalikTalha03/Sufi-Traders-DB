-- Assuming you want to get hourly sales for the current month

-- Retrieve hourly sales for the current month
SELECT
    DATEPART(HOUR, CO.orderTime) AS OrderHour,
    SUM(COD.quantity * COD.salePrice) AS HourlySales
FROM
    Customer_Order CO
JOIN
    Customer_Order_Details COD ON CO.orderID = COD.orderID
WHERE
    YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
    AND MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
GROUP BY
    DATEPART(HOUR, CO.orderTime)
ORDER BY
    OrderHour;
 