from flask import Flask, flash, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
from os import environ

load_dotenv()

app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS inquiries
    (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT NOT NULL, business_phone TEXT NOT NULL, services TEXT NOT NULL, message TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

    conn.commit()
    conn.close()

init_db()


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

@app.route("/services/sea-freight")
def sea_freight():
    return render_template("services/sea_freight.html")


@app.route("/services/trucking-solutions")
def trucking_solutions():
    return render_template("services/trucking_solutions.html")


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


@app.route("/services/project-cargo")
def project_cargo():
    return render_template("services/project_cargo.html")

@app.route("/services/3pl-services")
def three_pl_services():
    return render_template("services/3pl_services.html")


@app.route("/our-philosophy")
def our_philosophy():
    return render_template("our_philosophy.html")


@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")

@app.route("/lets-begin", methods=['GET', 'POST'])
def lets_begin():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        business_phone = request.form['business_phone']
        services = request.form['services']
        message = request.form['message']

        try:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute('''INSERT INTO inquiries (first_name, last_name, email, business_phone, services, message) 
                        VALUES (?, ?, ?, ?, ?, ?)''', 
                     (first_name, last_name, email, business_phone, services, message))
            conn.commit()
            conn.close()

            flash("Thank you for reaching out! We have received your inquiry and will contact you soon.", "success")
            return redirect(url_for('thank_you'))
        except Exception as e:
            flash("An error occurred while submitting your inquiry. Please try again.", "error")
            print(f"Database error: {e}")
            return redirect(url_for('lets_begin'))

    return render_template("lets_begin.html")







if __name__ == '__main__':
    app.run(debug=True)
    