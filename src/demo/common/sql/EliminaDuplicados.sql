-- ELIMINAMOS LOS PROCEDIMIENTOS ALMACENADOS EXACTAMENTES DUPLICADOS POR NOMBRE

WITH C AS
(
	SELECT O.object_id AS ID, O.name AS Nombre, S.name AS Esquema, case O.type when 'P' then 'Stored Procedure' else ' ' end 'Tipo de Objeto', 
	ROW_NUMBER() OVER	(PARTITION BY
						O.name
						ORDER BY object_id) AS ExactamenteDuplicado
	FROM 
		sys.objects O
			LEFT JOIN SYS.SCHEMAS S ON O.schema_id = S.schema_id
	WHERE 
		TYPE = 'P' 
)
DELETE FROM C
WHERE ExactamenteDuplicado > 1