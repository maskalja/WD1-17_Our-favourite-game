from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        if not request.cookies.get("secret_number"):
            secret_number = random.randint(1, 30)
        else:
            secret_number = request.cookies.get("secret_number")

        response = make_response(render_template("index.html"))
        response.set_cookie("secret_number", str(secret_number))

        return response

    elif request.method == "POST":

        player_number = int(request.form.get("player_number"))
        secret_number = int(request.cookies.get("secret_number"))

        if player_number == secret_number:
            feedback = f"Congrats, secret number really was {secret_number}!"
            response = make_response(render_template("result.html", feedback=feedback, player_number=player_number))
            response.set_cookie("secret_number", expires=0)
            return response
        elif player_number < secret_number:
            feedback = "Your number is too low! Try something bigger."
            return render_template("result.html", feedback=feedback, player_number=player_number)
        elif player_number > secret_number:
            feedback = "Your number is too high! Try something smaller."
            return render_template("result.html", feedback = feedback, player_number=player_number)


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)

