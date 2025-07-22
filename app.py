from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project', methods=["POST", "GET"])
def predict():
    result = None

    brand_dict = {
        'TVS': 1,
        'Royal Enfield': 2,
        'Triumph': 3,
        'Yamaha': 4,
        'Honda': 5,
        'Hero': 6,
        'Bajaj': 7,
        'Suzuki': 8,
        'Benelli': 9,
        'KTM': 10,
        'Mahindra': 11,
        'Kawasaki': 12,
        'Ducati': 13,
        'Hyosung': 14,
        'Harley-Davidson': 15,
        'Jawa': 16,
        'BMW': 17,
        'Indian': 18,
        'Rajdoot': 19,
        'LML': 20,
        'Yezdi': 21,
        'MV': 22,
        'Ideal': 23
    }

    if request.method == 'POST':
        brand_name = request.form['brand_name']
        owner = request.form['owner']
        age = request.form['age']
        power = request.form['power']
        kms_driven = request.form['kms_driven']

        # Convert brand name to code
        brand_code = brand_dict.get(brand_name)
        if brand_code is None:
            return "Invalid brand name", 400

        # Data for model input (example, replace with real model if needed)
        data = [[brand_code, owner, age, power, kms_driven]]

        # You can load and use your ML model here to get a result
        result = f"Received data: {data}"

    return render_template('project.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
