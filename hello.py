from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file

                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
def hello_world():
  return render_template('index.html') # Return the string 'Hello World!' as a response.

@app.route("/success")
def onSuccess():
  return render_template('success.html')

app.run(debug=True)      # Run the app in debug mode.

