-- Apenas a diferença entre o mês passado e o atual.
SELECT
	tv2.nestab AS Loja,
	tv2.npdv AS PDV,
	MAX(tv2.datahora) AS Data_Ultima_Venda,
	COALESCE(SUBSTRING(MAX(chavecfe) FROM 26 FOR 9), 'NÃO ENCONTRADO') AS "Nº de Série SAT"
FROM
	t_venda_{particao_passada} tv2
	JOIN (
		SELECT
			DISTINCT
			tv1.npdv,
			tv1.nestab
		FROM
			t_venda_{particao_passada} tv1
		EXCEPT (
			SELECT
				DISTINCT
				tv0.npdv,
				tv0.nestab
			FROM
				t_venda_{particao_atual} tv0
		)
	ORDER BY
		2,
		1
	) AS sqry ON tv2.npdv = sqry.npdv AND tv2.nestab = sqry.nestab
GROUP BY 1, 2;

-- Todos os meses.
-- SELECT
-- 	tv2.nestab AS Loja,
-- 	tv2.npdv AS PDV,
-- 	MAX(tv2.datahora) AS Data_Ultima_Venda,
-- 	COALESCE(SUBSTRING(MAX(chavecfe) FROM 26 FOR 9), 'NÃO ENCONTRADO') AS "Nº de Série SAT"
-- FROM
-- 	t_venda tv2
-- 	JOIN (
-- 		SELECT
-- 			DISTINCT
-- 			tv1.npdv,
-- 			tv1.nestab
-- 		FROM
-- 			t_venda tv1
-- 		EXCEPT (
-- 			SELECT
-- 				DISTINCT
-- 				tv0.npdv,
-- 				tv0.nestab
-- 			FROM
-- 				t_venda_202312 tv0
-- 		)
-- 	ORDER BY
-- 		2,
-- 		1
-- 	) AS sqry ON tv2.npdv = sqry.npdv AND tv2.nestab = sqry.nestab
-- GROUP BY 1, 2;
