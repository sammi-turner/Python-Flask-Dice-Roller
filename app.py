from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/roll<int:num>d<int:dice>", methods=["GET"])
def roll(num, dice):
    count = 0
    result = 0
    while count < num:
        result += random.randint(1, dice)
        count += 1
    score = str(result)
    numString = str(num)
    diceString = str(dice)
    scoreString = str(score)
    f = open("scores.txt", "a")
    f.write(f"\n{numString}d{diceString} => {scoreString}\n")
    f.close()
    return render_template("roll.html", numString=numString, diceString=diceString, scoreString=scoreString)

if __name__ == "__main__":
    app.run(debug=True)
