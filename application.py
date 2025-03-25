from flask import Flask

application=Flask(__name__)
app=application

@app.route("/",methods=["GET","POST"])
def run():
    return "Hellodgf"

if __name__=="__main__":
    app.run(host="0.0.0.0")