from flask import *
import sqlite3

app = Flask('__name__')


@app.route('/')
def home():
    return render_template("Adminlogin.html")


@app.route('/login1', methods=["POST"])
def homepage():
    user = request.form["uname"]
    passw = request.form["pass"]
    if user == "Admin" and passw == "12345":
        return render_template("navigation.html")
    else:
        return "YOU are not authorized.Don't try to login "


@app.route('/register')
def reg():
    return render_template("Register.html")


@app.route('/dashboard', methods=["POST"])
def dash():
    msg = "msg"
    if request.method == "POST":
        try:
            name1 = request.form["pname"]
            mobile = request.form["mno"]
            Age1 = request.form["age1"]
            address1 = request.form["add"]

            date = request.form["pdob"]

            place1 = request.form["ples"]
            pincode1 = request.form["pin"]

            t1 = (name1, mobile, Age1, address1, date, place1, pincode1)
            with sqlite3.connect("hospital1.db") as con:
                cur = con.cursor()

                q = """INSERT INTO hospital_table('name','mobile_no','age','address','DOB','place','pincode')VALUES(?,?,?,?,?,?,?);"""
                cur.execute(q, t1)
                con.commit()
                msg = "Patient Successfully Registered"

        except:
            con.rollback()
            msg = "Cannot add the Patient,Try after some time"
        finally:
            con.close()
            return render_template("success.html", msg=msg)


@app.route('/Psearch', methods=["GET"])
def search():
    return render_template("search.html")


@app.route('/search', methods=["POST"])
def ser():
    m_no = request.form["m_no"]
    con = sqlite3.connect("hospital1.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from hospital_table where mobile_no=?", (m_no,))
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)


@app.route('/Pdel', methods=["GET"])
def delete_1():
    return render_template("delete.html")


@app.route('/delete', methods=["POST"])
def del_1():
    mob1 = request.form["m_nos"]
    with sqlite3.connect("hospital1.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from hospital_table where mobile_no=?", (mob1,))


        except:
            con.rollback()

        finally:
            return "Record Deleted"


@app.route("/viewall")
def view():
    con = sqlite3.connect("hospital1.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("Select * from hospital_table")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)


@app.route('/Pupdate', methods=["GET"])
def update_1():
    return render_template("update.html")


@app.route('/Pup', methods=["POST"])
def updating():
    mno = request.form["mo_nos"]
    k = mno

    con = sqlite3.connect("hospital1.db")
    cur = con.cursor()
    q = "select * from hospital_table where mobile_no=?"
    cur.execute(q, (k,))

    result = cur.fetchall()
    print(result)
    if (result[0][1])!=None:
        return render_template("updateentry.html")


@app.route('/update', methods=["POST"])
def up_1():
    name1 = request.form["user_name"]
    mob1 = request.form["moo_nos"]
    age1 = request.form["ages"]
    prev_no=request.form["moo_1nos"]
    t=(name1,mob1,age1,prev_no)
    e=sqlite3.connect("hospital1.db")
    with e as con:
        try:
            cur = con.cursor()
            cur.execute("update hospital_table set name=?,mobile_no=?,age=?  where mobile_no=?",t)
            con.commit()
            return "Record updated successfully!"
        except:
            con.rollback()




if __name__ == '__main__':
    app.run(debug=True)
