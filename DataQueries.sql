SELECT DISTINCT
                            Employee.employeeID,
                            Employee.empFName,
                            Employee.empLName
                        FROM
                            Customer_Order CO
                        JOIN
                            Employee ON CO.employeeID = Employee.employeeID
                        WHERE
                            MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE());