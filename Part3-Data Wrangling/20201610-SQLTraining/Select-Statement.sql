/****** Script do comando SelectTopNRows de SSMS  ******/

USE DSTRAINING
SELECT TOP 1000 [Order ID]
      ,[Product Name]
      ,[Discount]
      ,[Sales]
      ,[Quantity]
      ,[Category]
  FROM [P12-OrderBreakdown]

/*

select count(*) FROM [P12-OrderBreakdown] WHERE [Category] = 'Furniture'

*/

select * FROM [P12-OrderBreakdown]
	WHERE [Category] = 'Furniture'
	and CONVERT(FLOAT,[Sales]) > 100

select * FROM [P12-OrderBreakdown]
	WHERE ([Category] = 'Furniture'
	AND CONVERT(FLOAT,[Sales]) > 100)
	OR ([Category] = 'Technology')