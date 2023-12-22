SELECT
                                        DATEPART(HOUR, CO.orderTime) AS OrderHour,
                                        ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS HourlySales
                                    FROM
                                        Customer_Order CO
                                    LEFT JOIN
                                        Customer_Order_Details COD ON CO.orderID = COD.orderID
                                    WHERE
                                        COD.productID = 1 AND CONVERT(DATE, CO.orderDate) = GETDATE()
                                    GROUP BY
                                        DATEPART(HOUR, CO.orderTime)
                                    ORDER BY
                                        OrderHour;