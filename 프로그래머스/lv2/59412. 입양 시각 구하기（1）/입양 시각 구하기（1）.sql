-- 코드를 입력하세요
SELECT HOUR(DATETIME) H, COUNT(*) FROM ANIMAL_OUTS GROUP BY H HAVING H >= 9 AND H <= 19 ORDER BY H;