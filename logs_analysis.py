#! /usr/bin/env python2.7
import psycopg2


def get_query_results(query):
    db = psycopg2.connect(database='news')
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


def popular_articles():
    query = ("""
    SELECT title,number_of_access
    FROM  (SELECT substr(path,10) AS slugInLog, count(*) AS number_of_access
    FROM log
    WHERE path LIKE '%/article/%' GROUP BY path)
    AS hits, articles WHERE slugInLog = slug
    ORDER BY number_of_access DESC LIMIT 3;
        """)

    result = get_query_results(query)

    file = open("output.txt", "w")
    file.write('\n Query 1: Most popular three articles')
    for title, num in result:
        file.write('\n    {}  --  {} views'.format(title, num))
    pass
    file.write('\n')


def popular_authors():
    query = ("""
        SELECT name, sum(number_of_access) AS views FROM
            (SELECT name, author, title, number_of_access FROM
                 (
                 SELECT substr(path,10) AS slugInLog, count(*)
                 AS number_of_access
                 FROM log
                 WHERE path LIKE '%/article/%' GROUP BY path
                 ) AS hits, articles, authors
                 WHERE slugInLog = slug AND author = authors.id
                 ORDER BY number_of_access DESC
                 ) AS table_alis GROUP BY name ORDER BY views DESC;
        """)
    result = get_query_results(query)

    file = open("output.txt", "a")
    file.write('\n Query 2: Most popular authors')
    for name, total_views in result:
        file.write('\n    {}  --  {} views'.format(name, total_views))
    pass
    file.write('\n')


def error_percent():
    query = ("""
              SELECT error_date,
              num_of_http_requests,
              num_of_not_found_404_reqs,
              100.0 * num_of_not_found_404_reqs / num_of_http_requests
              AS err_percent
              FROM (SELECT date_trunc('day', time) AS request_date, count(*)
                 AS num_of_http_requests
              FROM log
              GROUP BY request_date)
                 AS requests,
             (SELECT date_trunc('day', time)
             AS error_date, count(*) AS num_of_not_found_404_reqs
              FROM log
              WHERE status = '404 NOT FOUND'
              GROUP BY error_date)
                 AS errors
              WHERE request_date = error_date
              AND errors.num_of_not_found_404_reqs
               > 0.01 * requests.num_of_http_requests
              ORDER BY error_date DESC;
        """)
    result = get_query_results(query)

    file = open("output.txt", 'a')
    file.write(
        '\n Query 3: Days on which >1% HTTP requests returned 404 errors'
    )
    for errdate, http_requests, http_404, errpct in result:
        file.write(
            "\n {:%B %d, %Y}  --  {:.2f}% errors".format(errdate, errpct)
        )
    pass


if __name__ == "__main__":
    popular_articles()
    popular_authors()
    error_percent()
    print('\033[94m finished, file has been wrote with name: output.txt')
