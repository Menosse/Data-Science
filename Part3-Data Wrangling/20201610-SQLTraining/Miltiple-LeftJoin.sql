/****** Script do comando SelectTopNRows de SSMS  ******/
USE DSTRAINING
GO

SELECT *
FROM [P12-ListOfOrders] AS A
LEFT JOIN [P12-OrderBreakdown] AS B
ON A.[ORDER ID] = B.[ORDER ID]

