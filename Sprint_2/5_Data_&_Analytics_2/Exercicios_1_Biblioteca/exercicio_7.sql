-- Exercício 7
-- Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

SELECT
    au.nome 
FROM autor AS au
LEFT JOIN livro AS li 
    ON li.autor = au.codautor
where li.publicacao IS NULL
GROUP BY au.nome
ORDER BY au.nome
