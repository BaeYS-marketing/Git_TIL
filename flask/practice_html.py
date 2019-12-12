import random
from flask import Flask
from flask import render_template
from flask import request


@app.route('/pr_input')
def commit():
    return render_template("pr_input.html") 


@app.route('/pr_intance')
def pr_printance():
    name=request.args.get('user')
    atr = ["미모","기럭지",'성격','돈','광채','신앙']
    attribute = random.sample(atr,2)
    one = attribute[0]
    two = attribute[1]
    return render_template('/pr_instance.html',name=you, one=thing1, two=thing2)

