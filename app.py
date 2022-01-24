from flask import Flask, render_template
import os
import requests


app=Flask(__name__)

@app.route('/')
def index():
    
    
    text = "Siema tutaj Kasia, co tam u was? "
    
    
    return render_template("index.html", text=text)
    
if __name__=="__main__":
    app.run()
