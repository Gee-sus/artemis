import sqlite3

def view_inquiries():
    try:
        conn  = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM inquiries')
        records = cursor.fetchall()

        columns =[description[0] for description in cursor.description]
        print("\nColumns:", columns)

        print("\nRecords:")
        for record in records:
            print(record)

    except sqlite3.Error as e:
        print(f"Database error; {e}")
    finally:
        conn.close()

__name__== "__main__"
view_inquiries()