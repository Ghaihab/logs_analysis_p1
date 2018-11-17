# Logs Analysis with SQL
Questions: 
1. What are the most popular three articles?
2. Who are the most popular article authors?
3. On which days did more than 1% of requests lead to errors?

## Technologies Used

* SQL
* Python
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)

## Setup

1. Ensure that Python, the python package [psycopg2](https://pypi.python.org/pypi/psycopg2), [Vagrant](https://www.vagrantup.com/), and [VirtualBox](https://www.virtualbox.org/) are installed. (The vagrantfile I used is [here](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile).)
2. Download or clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
3. Download the [SQL database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip, and save `newsdata.sql` in the vagrant directory.
4. Navigate to the vagrant folder in the terminal and enter `vagrant up` to bring the server online, followed by `vagrant ssh` to log in.
5. To run the SQL queries directly, navigate to the vagrant directory with `cd /vagrant`, then enter `psql -d news -f newsdata.sql` to connect to and run the project database.
6. To execute the program in this repo, run `python logs_analysis.py`.
7. After running the program a message will be shown in the terminal (finished, file has been wrote with name: output.txt) a file has been genenrated.

## Database

The SQL script to create the data (downloadable [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)) results in a database called 'news' with three tables:

* The `articles` table includes information about news articles and their contents.
* The `authors` table includes information about the authors of articles.
* The `log` table includes one entry for each time a user has accessed the news site.
