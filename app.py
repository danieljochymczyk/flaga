from flask import Flask, render_template
import os
import requests


app=Flask(__name__)

@app.route('/')
def index():
    
    text = open("spiderman_xd.py").read()
    
    return render_template("index.html", text=text)
    
if __name__=="__main__":
    app.run()
