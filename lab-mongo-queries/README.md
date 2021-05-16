![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# MongoDB | Compass CRUD

## Introduction

We are back with our queries! :wink:

We have learned some super useful query operators, that will helps us to make much better queries to retrieve the data we need. We will continue using the **Crunchbase** collection we used on the last exercise.

## Submission

- Upon completion, create Pull Request so your TAs can check up your work.

## Deliverables

In the `your_code/main.ipynb` file, you will find the instructions about the queries you need to do. Complete the code with your queries using `pymongo`. Remember not to print all results as there may be quite a lot for some queries. Printing the first element is enough. :wink:  
(Windows, Mac) You may test your queries on Mongo Compass, but you will need to write it on a format compatible with `pymongo` python library. 

## Instructions

### Iteration 1

First, we need to import the Crunchbase data into a mongo collection, inside `ironhack` database. Crunchbase is the premier destination for discovering industry trends, investments, and news about hundreds of thousands of companies globally. From startups to Fortune 500s, Crunchbase is recognized as the primary source of company intelligence by millions of users globally.

The collection contains more than 18k documents, and each of them has a lot of information about each of the companies. A document looks like the following:

![image](https://user-images.githubusercontent.com/23629340/36494916-d6db1770-1733-11e8-903e-5119b3c1b688.png)

1. You will find the `.zip` file with the data on the **lab** folder.
2. Unzip the file
3. Make sure a mongo instance is running.
4. Depending on your operating system:  
    4a. (Windows, Mac) Using MongoDB Compass, import the data into a collection called `companies` inside `ironhack` database.  
    4b.(Linux) On the terminal locate yourself in the folder where `companies.json` file is. Then run
    ```bash
    $ mongoimport --db ironhack --collection companies --file companies.json
    ```

### Iteration 2

You already know how this goes, so let's start working:

1. All the companies whose name match 'Babelgum'. Retrieve only their `name` field.
2. All the companies that have more than 5000 employees. Limit the search to 20 companies and sort them by **number of employees**.
3. All the companies founded between 2000 and 2005, both years included. Retrieve only the `name` and `founded_year` fields.
4. All the companies that had a Valuation Amount of more than 100.000.000 and have been founded before 2010. Retrieve only the `name` and `ipo` fields.
5. All the companies that have less than 1000 employees and have been founded before 2005. Order them by the number of employees and limit the search to 10 companies.
6. All the companies that don't include the `partners` field.
7. All the companies whose name contains the substring "hola".
8. All the companies that have at least 100 employees but less than 1000. Retrieve only the `name` and `number of employees` fields.
9. Give a dictionary similar to `{"CocaCola": 1000, "Pepsi": 900}` with the top 10 companies regarding IPO price.
10. Give a list with the names of the 10 companies with more employees.
11. All the companies founded on the second semester of the year. Limit your search to 1000 companies.
12. All the companies founded before 2000 that have an acquisition amount of more than 10.000.000
13. All the companies that have been acquired after 2010, order by the acquisition amount, and retrieve only their `name` and `acquisition` field.
14. Order the companies by their `founded year`, retrieving only their `name` and `founded year`.
15. All the companies that have been founded on the first seven days of the month, including the seventh. Sort them by their `acquisition price` in a descending order. Limit the search to 10 documents.
16. All the companies on the 'web' `category` that have more than 4000 employees. Sort them by the amount of employees in ascending order.
17. All the companies whose currency is 'EUR'.
18. All the companies that have been acquired on the first trimester of the year. Limit the search to 10 companies, and retrieve only their `name` and `acquisition` fields.
19. All the companies that have been founded between 2000 and 2010, but have not been acquired before 2011.

Happy Coding! :heart: :rocket:
