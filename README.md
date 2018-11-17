# Logs Analysis 

##Introduction

A large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

1. What are the most popular three articles?
2. Who are the most popular article authors?
3. On which days did more than 1% of requests lead to errors?

## Technologies Used

* SQL
* Python
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)

## Setup

1. Ensure that Python, the python package [psycopg2](https://pypi.python.org/pypi/psycopg2), [Vagrant](https://www.vagrantup.com/), and [VirtualBox](https://www.virtualbox.org/) are installed.
2. In the terminal and enter `vagrant up` to bring the server online, followed by `vagrant ssh` to log in.
3. After login `cd /vagrant`
3. Download the [SQL database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip, and save `newsdata.sql` in the vagrant directory.
4. import the downloaded data to the database run `psql -d news -f newsdata.sql` to connect to and run the project database.
5. To execute the program in this repo, run `python logs_analysis.py`.
6. After running the program a message will be shown in the terminal (finished, file has been wrote with name: output.txt) a file has been genenrated.


## Result

Check the output.txt it will be generated after the program execution.

### Query 1: Most popular three articles

| Articles  | Views 
| :------------ |:---------------:
| Candidate is jerk, alleges rival     | 338647 views 
| Bears love berries, alleges bear     | 253801 views     
|  Bad things gone, say good people | 170098 views

### Query 2: Most popular authors

| Authors  | Views 
| :------------ |:---------------:
| Ursula La Multa     | 507594 views 
| Rudolf von Treppenwitz     | 423457 views     
|  Anonymous Contributor | 170098 views
|  Markoff Chaney | 84557 views

### Query 3: Days on which > 1% HTTP requests returned 404 errors

| Day  | Percentage  
| :------------ |:---------------:
| July 17, 2016     | 2.25% errors 


       