-- Exercício 9
-- Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

select 
	vn.cdpro,
	vn.nmpro 
from tbvendas as vn
where dtven between '2014-02-03' and '2018-02-02'
group by vn.status 
order by vn.status DESC 
limit 1