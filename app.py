from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "szupertitkoskulcs"


aliasok = ["valami", "test", "aliasez","ezis","valami", "test", "aliasez","ezis", "valami", "test", "aliasez","ezis", "aliasez","ezis", "valami", "test", "aliasez","ezis"]
tovabbitok = ["valami", "test", "aliasez","ezis","valami", "test", "aliasez","ezis", "valami", "test", "aliasez","ezis", "aliasez","ezis", "valami", "test", "aliasez","ezis"]
emailek = ["valami@test.com", "valami@test1.com", "valami@test2.com", "valami@test3.com", "valami@test4.com", "valami@test5.com", "valami@test3.com", "valami@test4.com", "valami@test5.com"]
domainek = ["google.com", "github.com", "youtube.com", "example.com", "google.com", "github.com", "youtube.com", "example.com"]




@app.route("/")
def index():
    return render_template("index.html", aliasok=aliasok, tovabbitok=tovabbitok, emailek=emailek, domainek=domainek)

if __name__ == "__main__":
    app.run(debug=True)