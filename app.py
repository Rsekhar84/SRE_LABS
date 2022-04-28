from flask import Flask


app=Flask(__name__)

@app.route("/")
def hello():
    return"hello world"


@app.route("/number")
def randomnum():
    import random
    from random import randint

    n=random.randint(1,100)
    return str(n)






    










if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")