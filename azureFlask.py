from flask import Flask, render_template

app = Flask(__name__,template_folder="template")

@app.route("/")
def home():
    return render_template("index.html")

if __name__=="__main__":
<<<<<<< HEAD
    app.run()
=======
    app.run(debug=True, host='0.0.0.0')
>>>>>>> ca42ceb0e390b1673ffd880acd00b557db32a4ce
