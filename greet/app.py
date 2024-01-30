from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home(): 
    html = f"""
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1> This is the home page </h1> 
            <h2> Connect to the other pages </h2> 
             <a href="/welcome">Welcome</a> 
             <br> 
             <a href="/welcome/home">Welcome Home</a>
             <br> 
             <a href="/welcome/back">Welcome Back</a>
        </body>
        </html>
    """
    return html

@app.route("/welcome")
def welcome(): 
    return "Welcome"

@app.route("/welcome/home")
def welcome_home(): 
    return "Welcome home"

@app.route("/welcome/back")
def welcome_back(): 
    return "Welcome back"