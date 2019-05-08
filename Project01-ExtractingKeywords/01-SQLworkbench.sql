USE news_chinese;
/*USE database_name */

SELECT 
    table_schema 'sqlResult_1558435',
    SUM(data_length + index_length) 'Size in Bytes',
    ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) 'Size in MiB'
FROM information_schema.tables 
GROUP BY table_schema;
/* Check the size of the database.*/

SELECT * FROM sqlResult_1558435;
/*Select all columns*/


SELECT id,author,source, content,title, url  FROM sqlResult_1558435;


