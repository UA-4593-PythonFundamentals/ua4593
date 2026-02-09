from flask import Flask, request

app = Flask(__name__)




@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user")
@app.route("/user/<username>", methods=['GET', 'POST'])
def show_user_profile(username=None):
    if username is None:
        return "No user specified"
    
    if request.method == 'POST':
        return f"Posted data for user: {username}"
    return f"get User: {username}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
