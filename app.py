from flask import Flask
# Import flask

# In order for us to use flask we need to create an instance of our app.
app = Flask(__name__) # This is the standard syntax to create a flask instance

# Syntax for decorators to create a web route
@app.route("/")


# Create a method to display on the home page
def index():
    return "Welcome to MVC with flask project"
# Index method will be called at the end point (where we connect to)
# The Index method will display on our home/default page

# print(index())

# Syntax to run our app
if __name__ == "__main__":
    app.run()
