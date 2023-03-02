-- Exercício 4
-- Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

SELECT
    au.nome,
    au.codautor,
    au.nascimento,
    COALESCE(COUNT(li.cod), 0) AS quantidade
FROM autor AS au
LEFT JOIN livro AS li 
ON li.autor = au.codautor
GROUP BY au.codautor, au.nome, au.nascimento
ORDER BY au.nome