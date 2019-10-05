import pymysql
import pandas as pd 

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', port=3306, user='test', password='test',
                       db='testdb', charset='utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor )
 
# Connection 으로부터 Cursor 생성
cursor = conn.cursor(pymysql.cursors.DictCursor)
 
# SQL문 실행
sql = "select * from users"
cursor.execute(sql)
 
# 데이타 Fetch
result = pd.DataFrame(cursor.fetchall())

print(result['Userid'].head())     # 전체 rows
 
# Connection 닫기
conn.close()