from app import app, db
from app.models import User

# Add the test_db route directly in app.py
@app.route('/test_db')
def test_db():
    try:
        # First check if user exists
        existing_user = User.query.filter_by(email='test@example.com').first()
        
        if existing_user:
            return 'Database connection successful! (User already exists)'
        
        # If user doesn't exist, create new one
        test_user = User(name='Test User', email='test@example.com')
        db.session.add(test_user)
        db.session.commit()
        return 'Database connection successful! (New user created)'
    
    except Exception as e:
        return f'Database error: {str(e)}'

if __name__ == '__main__':
    # Print all registered routes
    print("Available Routes:")
    print(app.url_map)
    
    app.run(debug=True)