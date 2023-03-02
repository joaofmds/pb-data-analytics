-- Exercício 12
-- Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
-- Observação: Apenas vendas com status concluído.

select 
	cddep, 
	nmdep, 
	dtnasc,
	sum(vn.qtd * vn.vrunt) AS valor_total_vendas
from tbdependente as dep
inner join tbvendas as vn 
	on dep.cdvdd = vn.cdvdd 
where status = 'Concluído'
group by vn.cdvdd 
order by valor_total_vendas 
limit 1