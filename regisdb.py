#!d:\Python34\python.exe
import cgi
import mysql.connector
con=mysql.connector.connect(user='root',password='root',host='localhost',database='pydemo')
cursor=con.cursor()
form=cgi.FieldStorage()
fname=form.getvalue('t1')
sname=form.getvalue('t2')
email=form.getvalue('t3')
bran=form.getvalue('t4')
st=form.getvalue('t7')
yr=int(form.getvalue('t5'))
ach=form.getvalue('t6')
print("Content.Type: text/html")
print("""
     <html>
     <head>
     <title>DEMO</title>
     </head>
     </html>
"""
)
sql="insert into regisa values('%s','%s','%s','%s','%s','%d','%s')"%(fname,sname,email,bran,st,yr,ach)
try:
    cursor.execute(sql)
    print("User Register Successfully");
    con.commit()
except Exception as e:
    print(e)

    
