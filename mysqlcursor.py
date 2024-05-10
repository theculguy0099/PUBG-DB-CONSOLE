import pymysql
import subprocess as sp
import pymysql.cursors

con = pymysql.connect(host='localhost',
                            #   port=30306,
                              user="root",
                              password="2005",
                              db='pubg',
                              cursorclass=pymysql.cursors.DictCursor)

cur = con.cursor()