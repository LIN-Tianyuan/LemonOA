
SECRET_KEY = "123456789gjksjksjkjskjk"

# Configuration information of the database
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'lemon_oa'
USERNAME = 'root'
PASSWORD = ''
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# Mailbox Configuration
MAIL_SERVER = "smtp.gmail.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "sgsgkxkx@gmail.com"
MAIL_PASSWORD = "nqluqymgrrqwufdg"
MAIL_DEFAULT_SENDER = "sgsgkxkx@gmail.com"

