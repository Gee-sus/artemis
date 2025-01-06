from flask import Flask, flash, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
from os import environ
from flask_wtf.csrf import CSRFProtect

load_dotenv()

app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')
csrf = CSRFProtect(app)  # Add CSRF protection

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


@app.route("/products/trucking-solutions")
def trucking_solutions():
    return render_template("products/trucking_solutions.html")


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


@app.route("/products/software-solutions")
def software_solutions():
    return render_template("products/software_solutions.html")

@app.route("/services/3pl-services")
def three_pl_services():
    return render_template("services/3pl_services.html")


@app.route("/our-philosophy")
def our_philosophy():
    return render_template("our_philosophy.html")


@app.route("/thank-you")
def thank_you():
    print("Rendering thank you page")  # Add debug print
    return render_template("thank_you.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your login logic here
        # For example:
        # if check_credentials(username, password):
        #     session['logged_in'] = True
        #     return redirect(url_for('dashboard'))
        # else:
        #     flash('Invalid credentials')
    return render_template("login.html")

@app.route("/lets-begin", methods=['GET', 'POST'])
def lets_begin():
    if request.method == 'POST':
        try:
            print("Form submitted!")
            
            # Get form data
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            business_phone = request.form['business_phone']
            services = request.form.getlist('services')
            message = request.form['message']

            # Use context manager for database connection
            with sqlite3.connect('database.db') as conn:
                c = conn.cursor()
                c.execute('''
                    INSERT INTO inquiries 
                    (first_name, last_name, email, business_phone, services, message)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (first_name, last_name, email, business_phone, ','.join(services), message))
                conn.commit()

            flash("Thank you for reaching out!", "success")
            return redirect(url_for('thank_you'))

        except Exception as e:
            print("ERROR:", str(e))
            flash(f"An error occurred: {str(e)}", "error")
            return redirect(url_for('lets_begin'))

    return render_template("lets_begin.html")

@app.route("/debug-db")
def debug_db():
    try:
        # Connect to database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        # Get table info
        c.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='inquiries';")
        table_info = c.fetchone()
        
        # Get all data
        c.execute("SELECT * FROM inquiries")
        data = c.fetchall()
        
        conn.close()
        
        return {
            "table_structure": table_info[0] if table_info else "No table found",
            "data": data
        }
        
    except Exception as e:
        return {"error": str(e)}

@app.route("/init-check")
def init_check():
    import os
    
    try:
        # Check if database file exists
        db_exists = os.path.exists('database.db')
        
        if not db_exists:
            return "Database file not found! Running init_db()..."
            init_db()
        
        # Connect and check table
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='inquiries';")
        table_exists = c.fetchone() is not None
        
        if not table_exists:
            return "Table not found! Running init_db()..."
            init_db()
            
        return "Database and table exist!"
        
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/find-db")
def find_db():
    import os
    
    # Get current working directory
    current_dir = os.getcwd()
    
    # Look for database file
    db_path = os.path.join(current_dir, 'database.db')
    
    if os.path.exists(db_path):
        return f"""
        Database found!
        Location: {db_path}
        Size: {os.path.getsize(db_path)} bytes
        """
    else:
        return f"""
        Database not found!
        Looked in: {db_path}
        Current directory: {current_dir}
        """

@app.route("/delete-all")
def delete_all():
    try:
        # Open the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Delete all data from the table
        cursor.execute('DELETE FROM inquiries')
        
        # Save changes
        conn.commit()
        conn.close()
        
        return "✅ All data deleted! Your table is now empty."
        
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/view-entries")
def view_entries():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM inquiries')
        entries = cursor.fetchall()
        conn.close()
        
        # Format the entries for display
        formatted_entries = []
        for entry in entries:
            formatted_entries.append({
                'id': entry[0],
                'first_name': entry[1],
                'last_name': entry[2],
                'email': entry[3],
                'business_phone': entry[4],
                'services': entry[5],
                'message': entry[6],
                'created_at': entry[7]
            })
            
        return {'entries': formatted_entries}
        
    except Exception as e:
        return f"Error: {str(e)}"







if __name__ == '__main__':
    app.run(debug=True)
    