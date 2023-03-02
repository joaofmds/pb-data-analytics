-- Exercício 6
-- Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

SELECT 
	au.codautor,
	au.nome,
	count(li.publicacao) as "quantidade_publicacoes"

from autor as au
left join livro as li
	on au.codautor = li.autor 
group by au.nome 
order by "quantidade_publicacoes" DESC 
limit 1