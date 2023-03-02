-- Exercício 8
-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

select 
	vdd.cdvdd,
	vdd.nmvdd
from tbvendedor as vdd
left join tbvendas as vd
	on vdd.cdvdd = vd.cdvdd 
where vd.status = 'Concluído'
group by vd.status 
order by vd.status desc