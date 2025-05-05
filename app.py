from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/page1")
def page1():
    return render_template('page1.html', picked_page='Page One')

@app.route("/page2", methods=['GET', 'POST'])
def page2():
    message = None
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        genre = request.form.get('genre')

        print(f"📚 Book Submission - Title: {title}, Author: {author}, Genre: {genre}")

        message = f"✅ Thanks! Now I know what kind of genre you like! Hmu so it can be mailed to you"
    
    return render_template('page2.html', message=message)



@app.route("/page3")
def page3():
    user_ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log.txt", "a") as f:
        f.write(f"[{timestamp}] Page 3 clicked from IP: {user_ip}\n")

    return render_template("page3.html")

@app.route("/page4", methods=["GET", "POST"])
def page4():
    message = None
    if request.method == "POST":
        response = request.form.get("response")
        if response == "yes":
            message = "🎉 Yayyyyyyy"
        elif response == "no":
            message = "Ouch. Anyways we move 😂"
    return render_template("page4.html", message=message)

@app.route("/page5")
def page5():
    return render_template("page5.html")  

if __name__ == "__main__":
    app.run(debug=True)
