from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "szupertitkoskulcs"


aliasok = ["valami", "test", "aliasez","ezis","valami", "test", "aliasez","ezis", "valami", "test", "aliasez","ezis", "aliasez","ezis", "valami", "test", "aliasez","ezis"]
tovabbitok = ["valami", "test", "aliasez","ezis","valami", "test", "aliasez","ezis", "valami", "test", "aliasez","ezis", "aliasez","ezis", "valami", "test", "aliasez","ezis"]
emailek = ["valami@test.com", "valami@test1.com", "valami@test2.com", "valami@test3.com", "valami@test4.com", "valami@test5.com", "valami@test3.com", "valami@test4.com", "valami@test5.com"]
domainek = ["google.com", "github.com", "youtube.com", "example.com", "google.com", "github.com", "youtube.com", "example.com"]

"""

Input name tags:
    - aliasok.html > (add alias inp): alias_name

"""


@app.route("/")
def index():
    return render_template("index.html", aliasok=aliasok, tovabbitok=tovabbitok, emailek=emailek, domainek=domainek)


@app.route("/alias")
def alias():
    return render_template("aliasok.html", aliasok=aliasok)





# Funkcionalitás

@app.route("/add_alias", methods=["POST"])
def add_alias():
    alias_name = request.form.get('alias_name')
    if alias_name == "":
        flash("Hiba! Üres a bemeneti mező", "danger")
        return redirect(url_for("alias"))
    aliasok.append(alias_name)
    return redirect(url_for("alias"))



if __name__ == "__main__":
    app.run(debug=True)