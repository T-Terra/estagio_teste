\copy operadoras_saude FROM '/downloads/Relatorio_cadop.csv'
WITH (FORMAT CSV, DELIMITER ';', HEADER TRUE, ENCODING 'UTF8');

-- padrão para importação das demonstrações contábeis

-- 2024
\copy contabilidade_2024_tmp FROM '/downloads/2024/1T2024/1T2
024.csv' WITH (FORMAT CSV, DELIMITER ';', HEADER TRUE, ENCODING 'UTF8');

-- 2023
\copy contabilidade_2023_tmp FROM '/downloads/2023/1T2023/1T2
023.csv' WITH (FORMAT CSV, DELIMITER ';', HEADER TRUE, ENCODING 'UTF8');

-- Executar no terminal psql e adicionar o caminho correto do arquivo