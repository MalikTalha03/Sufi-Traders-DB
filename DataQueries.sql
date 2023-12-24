-- Assuming you want to retrieve the username for an active session
SELECT E.empFName + ' ' + ISNULL(E.empLName, '') AS EmployeeUsername
FROM Employee_Session ES
JOIN Employee E ON ES.empID = E.employeeID
WHERE ES.currStatus = 'Active';
