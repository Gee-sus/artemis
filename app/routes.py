from app import app, db
from app.models import User
from flask import render_template, request, redirect, url_for, flash

# Add this at the top to see all registered routes
print("Available Routes:")
print(app.url_map)

# Keep all your existing routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/products/artemis-booking")
def artemis_booking():
    return render_template("products/artemis_booking.html")

@app.route("/products/customs-streamlined")
def customs_streamlined():
    return render_template("products/customs_streamlined.html")

@app.route("/products/real-time-tracking")
def real_time_tracking():
    return render_template("products/real_time_tracking.html")

@app.route("/products/software-solutions")
def software_solutions():
    return render_template("products/software_solutions.html")

@app.route("/products/trucking-solutions")
def trucking_solutions():
    return render_template("products/trucking_solutions.html")

@app.route("/services/sea-freight")
def sea_freight():
    return render_template("services/sea_freight.html")

@app.route("/services/air-freight")
def air_freight():
    return render_template("services/air_freight.html")

@app.route("/services/import-clearance")
def import_clearance():
    return render_template("services/import_clearance.html")

@app.route("/services/export-clearance")
def export_clearance():
    return render_template("services/export_clearance.html")

@app.route("/services/dangerous-goods")
def dangerous_goods():
    return render_template("services/dangerous_goods.html")

@app.route("/services/3pl-services")
def three_pl_services():
    return render_template("services/three_pl_services.html")

@app.route("/our-philosophy")
def our_philosophy():
    return render_template("our_philosophy.html")

@app.route("/lets-begin")
def lets_begin():
    return render_template("lets_begin.html")

# ... (all your other existing routes) ...

# Make sure this is at the bottom of routes.py
if __name__ == '__main__':
    app.run(debug=True) 