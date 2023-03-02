-- Exercício 5
-- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

select DISTINCT 
	au.nome 
from autor as au
left join livro as li
	on au.codautor = li.autor
left join editora as ed
	on li.editora = ed.codeditora 
left join endereco as en
	on ed.endereco = en.codendereco 
where en.estado <> 'RIO GRANDE DO SUL' and en.estado <> 'PARANÁ'
order by au.nome