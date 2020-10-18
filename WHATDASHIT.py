import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
    c.execute('''create table data
            (id text primary key,name text,course text,yearlevel text)''')

def CREATE(id,name,course,yearlevel):
    '''
    id = input('Enter your ID:')
    name = input('Enter your name:')
    course = input('Enter your course name:')
    yearlevel = input('Enter your year level:')
    '''

    c.execute("insert into data(id,name,course,yearlevel) VALUES (?,?,?,?)", (id,name,course,yearlevel))
    conn.commit()

def READ(identity):
    '''
    identity = input("Enter your ID:")
    '''
    c.execute("SELECT * FROM data WHERE id=:identity",{"identity":identity})
    ak=c.fetchall()
    print(ak)

def UPDATE(identity,id,name,course,yearlevel):
    '''
    identity = input("Enter your ID:")
    name = input('EDIT your name:')
    course = input('EDIT your course name:')
    yearlevel = input('EDIT your year level:')
    '''
    c.execute("UPDATE data SET id=:id,name=:name,course=:course,yearlevel=:course WHERE id=:identity",{"id":id,"name":name,"course":course,"yearlevel":yearlevel,"identity":identity})
    #c.execute("UPDATE data SET name=?,course=?,yearlevel=? WHERE id=?",(name,course,yearlevel,identity))
    conn.commit()


    #c.execute('''SELECT * FROM data ''')
    #data = c.fetchall()
    
    #for i in data: 
    #    if i[0]==identity:
    #        print(i)

def DELETE(identity):
    '''
    identity = input("Enter your ID:")
    '''
    #print(identity)
    c.execute("DELETE FROM data WHERE id=:identity",{"identity":identity})
    conn.commit()

def READALL():
    c.execute("SELECT * FROM data")
    return c.fetchall()

#create_table()
#CREATE()    
#READ()
#UPDATE()
#DELETE()
#print(READALL())
SHITDAWHAT=READALL()
#c.close()
