WITH despesas AS (
    SELECT 
        registro_ans,
        razao_social,
        nome_fantasia,
        modalidade,
        SUM(CASE 
            WHEN TRIM(descricao) ILIKE '%AVISADOS DE ASSISTÊNCIA%' AND TRIM(descricao) ILIKE '%SINISTRO%' 
            THEN vl_saldo_final 
            ELSE 0 
        END) AS total_despesas
    FROM 
        (SELECT * FROM contabilidade_2024 WHERE data >= '2024-01-01' AND data <= '2024-12-31' 
        ) c
    JOIN 
        operadoras_saude cs ON reg_ans = registro_ans
    GROUP BY 
        registro_ans, razao_social, nome_fantasia, modalidade
)
SELECT 
    registro_ans,
    razao_social,
    nome_fantasia,
    modalidade,
    total_despesas
FROM 
    despesas
ORDER BY 
    total_despesas DESC
LIMIT 10;
