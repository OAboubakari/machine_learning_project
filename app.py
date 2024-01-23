from flask import Flask


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "<h1><marquee>Starting Machine Learning Project</h1>"


if __name__=="__main__":

    app.run(debug=True)
