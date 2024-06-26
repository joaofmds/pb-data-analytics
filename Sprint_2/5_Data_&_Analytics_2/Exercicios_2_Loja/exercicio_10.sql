-- Exercício 10
-- A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 
-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.
-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

SELECT 
    vdd.nmvdd AS vendedor,
    SUM(vn.qtd * vn.vrunt) AS valor_total_vendas,
    ROUND(SUM(vn.qtd * vn.vrunt * vdd.perccomissao) / 100, 2) AS comissao
FROM tbvendedor AS vdd
    INNER JOIN tbvendas AS vn 
        ON vdd.cdvdd = vn.cdvdd 
WHERE vn.status = 'Concluído'
GROUP BY vdd.nmvdd, vdd.perccomissao
ORDER BY comissao DESC