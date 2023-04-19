-- v_saida_mensal source

CREATE VIEW v_saida_mensal 
AS
SELECT  l.nome as "localidade",
		c.nome as "classe",
		strftime('%Y',s.dt_saida) as "ano",
		strftime('%m',s.dt_saida) as "mes",
		SUM(s.peso) as peso_mensal,
		SUM(s.custo) as custo_mensal,
		SUM(s.receita) as receita_mensal
FROM saida s
JOIN localidade l 
	ON s.id_localidade = l.id_localidade 
JOIN classe c 
	ON s.id_classe = c.id_classe 
GROUP BY localidade, classe, ano, mes;