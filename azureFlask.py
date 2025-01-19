from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    output = '''
<h1>Hello World! This is Bharathwaj</h1>
<h2>Welcome to Azure DevOps</h2>
<h3>If you want to make changes in web app, update and commit the code on github to trigger the pipelines</h3>
<h4>Changes made in Github or co-workers can be applied in local using git pull command</h4>
'''
    return output
    #return "<h1>Hello World! This is Bharathwaj</h1>"

if __name__=="__main__":
    app.run(debug=True,host="localhost")
