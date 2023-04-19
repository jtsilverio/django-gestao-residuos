CREATE VIEW v_entrada_mensal 
AS
SELECT  l.nome as "localidade",
		c.nome as "classe",
		strftime('%Y',e.dt_entrada) as "ano",
		strftime('%m',e.dt_entrada) as "mes",
		SUM(e.peso) as peso_mensal
FROM entrada e 
JOIN localidade l 
	ON e.id_localidade = l.id_localidade 
JOIN classe c 
	ON e.id_classe = c.id_classe 
GROUP BY localidade, classe, ano, mes;