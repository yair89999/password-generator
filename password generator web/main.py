from flask import Flask, render_template,redirect,url_for,flash,session,request
import os
from generate_password import generate_password

if os.getcwd().split("\\")[-1] != "password generator web": # os.getcwd() gets the folder the file runs on
    try:
        os.chdir("password generator web") # change the diractory it works on to discord bot(now it start it from the "games and projects" directory)
    except: # can cause a error if it starts it from the folder
        pass

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        with_letters = request.form["letters"]
        with_big_letters = request.form["big letters"]
        with_numbers = request.form["numbers"]
        with_signs = request.form["signs"]
        yes_no = [with_letters, with_big_letters, with_numbers, with_signs]
        index = 0
        for i in yes_no:
            if i == "yes":
                yes_no[index] = True
            else:
                yes_no[index] = False
            index += 1
        
        password = None
        long1 = 0
        try:
            yes_no.append(int(request.form["long"]))
            with_letters, with_big_letters, with_numbers, with_signs, long = yes_no
            try:
                password = generate_password(with_letters, with_big_letters, with_numbers, with_signs, long)
            except:
                password = "I am sorry but we couldn't generate a password"
            if password == "cant":
                password = "I am sorry but we couldn't generate a password"
            else: # eerything went good
                long1 = long
        except:
            return render_template("home.html", password = "I am sorry but we couldn't generate a password", long=long)
        return render_template("home.html", password = password, long=long1)
    else:
        return render_template("home.html")


app.run(debug=True)