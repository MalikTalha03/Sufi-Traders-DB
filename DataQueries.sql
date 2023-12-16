-- Assuming you want total sales between two date ranges
DECLARE @StartDate DATE = '2023-8-06'; -- Change to your desired start date
DECLARE @EndDate DATE = '2023-12-09';   -- Change to your desired end date

-- Retrieve total sales between two date ranges
IF DATEDIFF(MONTH, @StartDate, @EndDate) > 1
BEGIN
    SELECT
        Calendar.Year,
        Calendar.MonthNumber,
        ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS MonthlySales
    FROM (
        SELECT
            YEAR(DATEADD(MONTH, number, @StartDate)) AS Year,
            MONTH(DATEADD(MONTH, number, @StartDate)) AS MonthNumber
        FROM master.dbo.spt_values
        WHERE type = 'P'
            AND number BETWEEN 0 AND DATEDIFF(MONTH, @StartDate, @EndDate)
    ) Calendar
    LEFT JOIN
        Customer_Order CO ON Calendar.MonthNumber = MONTH(CONVERT(DATE, CO.orderDate))
    LEFT JOIN
        Customer_Order_Details COD ON CO.orderID = COD.orderID
    GROUP BY
        Calendar.Year,
        Calendar.MonthNumber
    ORDER BY
        Year, MonthNumber;
END
ELSE
BEGIN
    SELECT
        CONVERT(DATE, CO.orderDate) AS OrderDate,
        ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
    FROM
        Customer_Order CO
    LEFT JOIN
        Customer_Order_Details COD ON CO.orderID = COD.orderID
    WHERE
        CONVERT(DATE, CO.orderDate) BETWEEN @StartDate AND @EndDate
    GROUP BY
        CONVERT(DATE, CO.orderDate)
    ORDER BY
        OrderDate;
END
