import pymysql
from bottle import route, run, static_file, request, error, template

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2304003260', passwd='mypassword', db='2304003260_todo')
cur = conn.cursor()

@route('/')
def index():


@route('/todo')
def rot():
    cur.execute("SELECT * FROM todo")

    return template('index', cur = cur, conn=conn)

run(host='localhost', port=8080, debug=True)