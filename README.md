Note: any step that is just `command here` is juest a line to run in terminal
1. `git clone https://github.com/NJIT-CS490/project2-m1-mt393`
2. `cd project2-m1-mt393`
3. `npm ci`
4. `pip install flask-socketio`
5. `pip install eventlet`
6. `npm install -g webpack`
7. `pip install finnhub-python`
8. `pip install requests`
9. `npm install --save-dev webpack`
10. `npm install socket.io-client --save`
11. If you already have psql set up then go to the next step, otherwise skip to "psql setup with python"
12. Copy your sql.env file into this new directoy
13. Go to finnhub.io and click "Get free API key", then create a username, password and email and submit
14. add this value to a new line of your sql.env file in the format
 REPLACE THE [VALUES] IN THIS COMMAND WITH YOUR RESPECIVE FINNHUB API KEY
`export STOCK_KEY = '[YOUR API KEY HERE]'`
15. `sudo service postgresql start`
16. `psql`
17. go to your database with command `\c`
18.
`CREATE TABLE IF NOT EXISTS Trebchat (
id SERIAL PRIMARY KEY,
message VARCHAR,
names VARCHAR);`
19. 
`CREATE TABLE IF NOT EXISTS activeusers (
sid VARCHAR PRIMARY KEY,
username VARCHAR);`
# psql setup with python
`sudo yum update`

`sudo /usr/local/bin/pip install --upgrade pip`

`sudo /usr/local/bin/pip install psycopg2-binary`

`sudo /usr/local/bin/pip install Flask-SQLAlchemy==2.1`

# setup psql
`sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docsgit clone https://github.com/NJIT-CS490/project2-m1-mt393`
    (answer yes to everything)
    
`sudo service postgresql initdb`
    (this will fail if you already have a db initialized, thats fine)
    
`sudo service postgresql start`
`sudo -u postgres createuser --superuser $USER`
    Error "could not change directory" is fine, it still worked
    
`sudo -u postgres createdb $USER`
    Error "could not change directory" is fine, it still worked
    
`psql`

`\du`
    look for ec2-user as a user
    
`\u`
    look for ec2-user as a database
 REPLACE THE [VALUES] IN THIS COMMAND WITH A RESPECIVE SHORT USERNAME AND PASSWORD
`create user [some_username_here] superuser password '[some_unique_new_password_here]';`
make a new file called sql.env

 REPLACE THE {VALUES} IN THIS COMMAND WITH A RESPECIVE SHORT USERNAME AND PASSWORD
`export DATABASE_URL = postgresql://{USERNAME}:{PASSWORD}@localhost/postgres`

# Enabling read/write from SQLAlchemy 
1. Open the file in vim: `sudo vim /var/lib/pgsql9/data/pg_hba.conf`
If that doesn't work: `sudo vim $(psql -c "show hba_file;" | grep pg_hba.conf)`  
2. Replace all values of `ident` with `md5` in Vim: `:%s/ident/md5/g`  
3. After changing those lines, run `sudo service postgresql restart`  
4. Ensure that `sql.env` has the username/password of the superuser you created! 
5. Go to finnhub.io and click "Get free API key", then create a username, password and email and submit
6. add this value to a new line of your sql.env file in the format
## REPLACE THE [VALUES] IN THIS COMMAND WITH YOUR RESPECIVE FINNHUB API KEY
`export STOCK_KEY = '[YOUR API KEY HERE]'`
8. `psql`
9. go to your database with command `\c`
10.
`CREATE TABLE IF NOT EXISTS Trebchat (
id SERIAL PRIMARY KEY,
message VARCHAR,
names VARCHAR);`
11. 
`CREATE TABLE IF NOT EXISTS activeusers (
sid VARCHAR PRIMARY KEY,
username VARCHAR);`
12. Run your code!    
13. `npm run watch`. If prompted to install webpack-cli, type "yes"   
14. In a new terminal, `python app.py`    
15. Preview Running Application (might have to clear your cache by doing a hard refresh)

# known issues
- the chat does not occupy 50% of the width of the screen by default.
potential solution: learn better css. i dont know the commands too well, most that I try to implement fall flat I know I need to set the width somewhere to 50%, but I'm not sure where.
- the sql server frequently gets too many connections and breaks the app until i restart it in the terminal
potential solution: heroku has dyno connection pools or something to handle this on its own so id look into that
- i want to give the bot AI in the future
potential solution: have it use the messages sent over the app as input for the neural network

# solved issues
- I've had db problems with setting up the db on heroku's end and using the flask commands like db.create_all() doesnt work for some reason
Solution: its a bit of a band-aid solution but I'm able to manually alter or create whatever tables I need with `psql` and `heroku pg:psql`
- I didnt know how to send multiple columns of a row together to my content.jsx and map them together
Solution: I made 2 separate arrays, sent them both through the socket with individual names, used an individual use.state for each and when it came to looping through the messages with each index, i also used that index to choose a respective item in the array of names. theres a way to send multiple pieces of data in that loop and I could have done message.message and message.name for each index but I couldnt figure out how to set that up.
- when trying to delete from my activeusers it wouldnt commit appropriately, i would not see it in my db afterwards
solution: i was trying to use the models.activeusers.query function but my commands should all be going through db.session and have my table in the parameter such as db.session.query(models.activeusers())


# credits
i used the https://github.com/Sresht/lect11-starter code as a starter both for my code and readme
i followed the corresponding youtube series as well https://www.youtube.com/playlist?list=PLejYYoWvB7A1lGuvAWTRKnrxzC-5Th5ru
this is a helpful official website about how to use flask and sqlalchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
