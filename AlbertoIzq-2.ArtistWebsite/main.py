from flask import Flask, render_template 

app = Flask(__name__) # __name__ gets the .py name

# Home page
@app.route('/') # Declarator
def home(): # Content
    return render_template("home.html")

if __name__ == "__main__": # It's True if this script is executed and not imported to another script
    app.run(debug = True)