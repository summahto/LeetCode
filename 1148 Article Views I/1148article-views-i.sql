# Write your MySQL query statement below

SELECT distinct(author_id) as id
FROM VIEWS
WHERE viewer_id = author_id
ORDER BY id;