from flask import Flask, request, jsonify, render_template
import util  # Interpreter is Anaconda as it comes with Flask by default..
# This is our main server file
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("app.html")

@app.route('/get_location_names', methods=['GET']) # Exposing HTTP endpoints
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names() # locations are returned via util file which is imported in this file
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    }) # this is done to call get_estimated_price function and record the estimated price function value in variable response
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    # app.debug = Truekill
    app.run()
