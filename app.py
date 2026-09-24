from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        return f"Your name is {first_name} {last_name}"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)