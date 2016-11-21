from flask import *


# Create flask app and global pi 'thing' object.
app = Flask(__name__)


# Define app routes.
# Index route renders the main HTML page.
@app.route("/")
def index():

    return render_template('index.html')



# Start the flask debug server listening on the pi port 5000 by default.
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
