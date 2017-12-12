import os
import pymysql
from bottle import route, run, static_file, request, error, template, post

@route('/')
def baeta():
    return "Virkar!"

run(host="0.0.0.0", port=os.environ.get('PORT'))
