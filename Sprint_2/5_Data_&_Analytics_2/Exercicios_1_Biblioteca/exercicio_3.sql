-- Exercício 3
--  Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

select 
	count(*) as quantidade,
	ed.nome, 
	en.estado,
	en.cidade
from livro as li
inner join editora as ed
	on li.editora = ed.codeditora 
inner join endereco as en
	on ed.endereco = en.codendereco 
group by ed.nome
order by quantidade desc
limit 5