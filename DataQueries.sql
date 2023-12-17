SELECT
    P.productID,
    P.productName,
    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
FROM
    Customer_Order CO
JOIN
    Customer_Order_Details COD ON CO.orderID = COD.orderID
JOIN
    Products P ON COD.productID = P.productID
WHERE
    CONVERT(DATE, CO.orderDate) = GETDATE()
GROUP BY
    P.productID,
    P.productName
ORDER BY
    DailySales DESC;
