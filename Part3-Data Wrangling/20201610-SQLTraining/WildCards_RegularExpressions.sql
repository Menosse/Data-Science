use DSTRAINING

GO

Select * from [P12-ListOfOrders]

/* 
	The goal is to get only the orderID that have ES in the begining
	Using regular expressions (LIKE OPERATOR)
 */

SELECT * FROM [P12-ListOfOrders]
	WHERE [ORDER ID] LIKE 'ES%'

/* 
	The goal is to get only the orderID that have IT in the begining
	Using regular expressions (LIKE OPERATOR)
 */

SELECT * FROM [P12-ListOfOrders]
	WHERE [ORDER ID] LIKE 'IT%'

/* 
	The goal is to get only the Countries with the letter E on their names
	Using regular expressions (LIKE OPERATOR)
 */

SELECT * FROM [P12-ListOfOrders]
	WHERE [Country] LIKE '%E%'