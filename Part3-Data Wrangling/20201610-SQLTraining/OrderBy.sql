USE DSTRAINING
GO

SELECT *
	FROM [P12-OrderBreakdown]
	ORDER BY CONVERT(FLOAT,[SALES]) ASC

SELECT *
	FROM [P12-OrderBreakdown]
	ORDER BY CAST([SALES] AS FLOAT) ASC

SELECT *
	FROM [P12-OrderBreakdown]
	ORDER BY [CATEGORY] DESC