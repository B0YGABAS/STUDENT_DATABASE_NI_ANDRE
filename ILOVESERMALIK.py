from flask import Flask,redirect,url_for,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
import sqlite3
import json
#import WHARDASHIT

conn = sqlite3.connect('data.db')
'''
c = conn.cursor()

def READALL():
    c.execute("SELECT * FROM data")
    return c.fetchall()

GEEOHEM=READALL()
'''

class OML():
    def __init__(self):
        self.GEEOHEM=[]#GEEOHEM

OHEMGEE=OML()

app = Flask(__name__)

class FOARM(FlaskForm):
    username=""

@app.route('/home')
def hello():
    return 'Hello, World!'
'''
@app.route('/<name>')
def WHAT(name):
    return f"HI {name}"
'''
@app.route('/admin')
def admin():
    return redirect(url_for("hello"))

@app.route('/aaaaa')
#@app.route('/login')
#, students=["ANDRE","ANDREY","ANDREI"]
def login():
    return render_template("OML.html")

@app.route('/')
@app.route('/ditabis')
def ditabis(filter=""):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    OHEMGEE.GEEOHEM=c.fetchall()
    if filter!="":
        filterer=[]
        for student in OHEMGEE.GEEOHEM:
            for field in student:
                field=field.upper()
                digitletter=[]
                for letterdigit in field:
                    #print(" - - "+letterdigit)
                    digitletter.append(letterdigit)
                    #print(" - - - "+"".join(digitletter))
                    if "".join(digitletter)==filter:
                        compare=0
                        for comparer in filterer:
                            if comparer==student:
                                compare=1
                                break
                        if compare==0:
                            filterer.append(student)
                        break
        OHEMGEE.GEEOHEM=filterer

    """
    if filter!="":
        filterer=[]
        for student in OHEMGEE.GEEOHEM:
            for field in student:
                if field==filter:
                    filterer.append(student)
                    break
        OHEMGEE.GEEOHEM=filterer
        """
    '''
    print(OHEMGEE.GEEOHEM)
    filterer=[]
    for i in OHEMGEE.GEEOHEM:
        OHMAY=[]
        OHMAY.append(''.join(i[0]))
        OHMAY.append(''.join(i[1]))
        OHMAY.append(''.join(i[2]))
        OHMAY.append(''.join(i[3]))
        filterer.append(OHMAY)
    print(filterer)
    OHEMGEE.GEEOHEM=filterer
    '''
    for i in OHEMGEE.GEEOHEM:
        break
    return render_template("FORMS.html", students=OHEMGEE.GEEOHEM)
    '''
    if request.method=="POST":
        
        aydi=request.form.get("ID")
        nim=request.form.get("NIM")
        kors=request.form.get("KORS")
        yir=request.form.get("YIR")
        print(aydi)
        
        FILTER=[]
        for checkbox in OHEMGEE.GEEOHEM:
            tsikbox=checkbox[0]#print(checkbox[0])
            x=request.form.get(tsikbox)
            print(x)
            #print(request.form[checkbox[0]])
            #if request.form(checkbox[0])==1:
            if x=="1":
                FILTER.append(checkbox)
        return render_template("FORMS.html", students=FILTER)
        #return render_template("FORMS.html", students=OHEMGEE.GEEOHEM)
    else:
        return render_template("FORMS.html", students=OHEMGEE.GEEOHEM)
    '''

@app.route('/hadukick')
def hadukick():
    return render_template("hadukick.html")

@app.route('/WTF')
def WTF():
    return render_template("waow.html", kaow=["HIGH","LOW","MID"])

@app.route('/create',methods=["POST"])
def create():
    if request.method=="POST":
        #aydi=request.form.get("ID")
        nim=request.form.get("NIM")
        kors=request.form.get("KORS")
        yir=request.form.get("YIR")
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT id from data")
        aydi=c.fetchall()
        if len(aydi)!=0:
            aydi="0"+str(int("".join(aydi[-1]))+1)
        else:
            aydi="00"
        c.execute("insert into data(id,name,course,yearlevel) VALUES (?,?,?,?)", (aydi,nim,kors,yir))
        conn.commit()
        #OHEMGEE.CREATE(aydi,nim,kors,yir)
    return ditabis()

@app.route('/search', methods=["POST"])
def SEARCH():
    if request.method=="POST":
        
        serts=request.form.get("SERTS").upper()
        return ditabis(serts)

@app.route('/update',methods=["POST"])
def update():
    if request.method=="POST":
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        AYDEE=request.form.get("EAYDI")
        NEEM=request.form.get("ENIM")
        KURS=request.form.get("EKORS")
        YEER=int(request.form.get("EYIR"))
        c.execute("UPDATE data SET name=:name,course=:course,yearlevel=:yearlevel WHERE id=:identity",{"name":NEEM,"course":KURS,"yearlevel":YEER,"identity":AYDEE})
        conn.commit()
    return ditabis()
@app.route('/delete',methods=["GET","POST"])
def delete():
    if request.method=="POST":     
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        #c.execute("DELETE FROM data WHERE id=:identity",{"identity":identity})
        FILTER=[]
        for checkbox in OHEMGEE.GEEOHEM:
            #print(checkbox[0])
            tsikbox=checkbox[0]
            x=request.form.get(tsikbox)
            #print(x)
            if x=="1":
                c.execute("DELETE FROM data WHERE id=:identity",{"identity":tsikbox})
                #FILTER.append(checkbox)
        conn.commit()
    return ditabis()
    #print("Hey ",id)
    #return ditabis()
    #form=FOARM()
    #if form.validate_on_submit():
    #OHEMGEE.DELETE(id)

if __name__ == "__main__":
    app.run()# debug=True)
