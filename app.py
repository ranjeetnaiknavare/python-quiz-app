from flask import Flask, render_template
from routes.auth import auth_bp  # Import authentication routes

app = Flask(__name__)
app.config.from_object('config')  # Load configuration

# Register Blueprints (Route Modules)
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
