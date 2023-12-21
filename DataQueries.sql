SELECT
                                    DATEPART(HOUR, CO.orderTime) AS OrderHour,
                                    SUM(COD.quantity * COD.salePrice) AS HourlySales
                                FROM
                                    Customer_Order CO
                                JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CONVERT(DATE, CO.orderDate) = 'GETDATE()'
                                GROUP BY
                                    DATEPART(HOUR, CO.orderTime)
                                ORDER BY
                                    OrderHour;