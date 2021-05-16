## CHALLENGE 1 ##

USE Publications;

SELECT authors.au_id, au_lname, au_fname, title, pub_name
	FROM authors
		JOIN titleauthor
			ON titleauthor.au_id = authors.au_id
		JOIN titles
			ON titles.title_id = titleauthor.title_id
		JOIN publishers
			ON publishers.pub_id = titles.pub_id;
	
	
    ## CHALLENGE 2 ##

SELECT titleauthor.au_id , au_lname ,au_fname, COUNT(pub_name)
	FROM authors 
		JOIN titleauthor 
			ON authors.au_id = titleauthor.au_id
		JOIN titles 
			ON titleauthor.title_id = titles.title_id
		JOIN publishers 
			ON titles.pub_id = publishers.pub_id
	GROUP BY pub_name, titleauthor.au_id
	order by COUNT(pub_name) desc;
    
    ## CHALLENGE 3 ##
    SELECT titleauthor.au_id as AUTHOR_ID, au_lname as LAST_NAME ,au_fname as FIRST_NAME, SUM(authors.contract) as TOTAL
	FROM authors 
		JOIN titleauthor 
			ON authors.au_id = titleauthor.au_id
		JOIN titles 
			ON titleauthor.title_id = titles.title_id
		JOIN publishers 
			ON titles.pub_id = publishers.pub_id
	GROUP BY titleauthor.au_id
    order by SUM(authors.contract) desc
    LIMIT 3;
	
    
   ## CHALLENGE 4 ##
	SELECT titleauthor.au_id as AUTHOR_ID, au_lname as LAST_NAME ,au_fname as FIRST_NAME, COALESCE(SUM(sales.qty), 0) as TOTAL
	FROM authors 
		JOIN titleauthor 
			ON authors.au_id = titleauthor.au_id
		JOIN titles 
			ON titleauthor.title_id = titles.title_id
		JOIN sales 
			ON titles.title_id = sales.title_id
	GROUP BY titleauthor.au_id
    order by SUM(sales.qty) desc
    LIMIT 24;
    
    
        ## BONUS CHALLENGE ##
    
SELECT titleauthor.au_id as AUTHOR_ID, au_lname as LAST_NAME ,au_fname as FIRST_NAME, COALESCE(SUM(sales.qty), 0) + COALESCE(SUM(titles.royalty), 0) as PROFIT
FROM authors 
	JOIN titleauthor 
		ON authors.au_id = titleauthor.au_id
	JOIN titles 
		ON titleauthor.title_id = titles.title_id
	JOIN sales 
			ON titles.title_id = sales.title_id
GROUP BY titleauthor.au_id
order by COALESCE(SUM(sales.qty), 0) + COALESCE(SUM(titles.royalty), 0) desc
LIMIT 3;
    
