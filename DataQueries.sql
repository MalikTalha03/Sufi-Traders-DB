SELECT
                                            DAY(CO.orderDate) AS OrderDay,
                                            ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
                                        FROM
                                            Customer_Order CO
                                        LEFT JOIN
                                            Customer_Order_Details COD ON CO.orderID = COD.orderID
                                        WHERE
                                            COD.productID = 1 AND MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                                AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                        GROUP BY
                                            DAY(CO.orderDate)
                                        ORDER BY
                                            OrderDay;