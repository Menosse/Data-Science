/****** Script do comando SelectTopNRows de SSMS  ******/
SELECT TOP 10 *
  FROM [DSTRAINING].[dbo].[RAW_FAKENAMES_UK_20200610]
  where [Centimeters] = ''
  or [Kilograms] = ''
  or [BloodType] = ''