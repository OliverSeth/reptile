import pymysql


def write_comments(comments):
    conn = pymysql.connect(host='localhost', user='root', password='123456', database='comments_db', charset='utf8')
    cursor = conn.cursor()
    for com in comments:
        sql = 'INSERT INTO COMMENTS(username,comment) VALUES (%s, %s);'
        username = str(com['user']['nickname'])
        comment = str(com['content'])
        try:
            cursor.execute(sql, [username, comment])
        except Exception as e:
            print(repr(e))
    conn.commit()
    cursor.close()
    conn.close()
