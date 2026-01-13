from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder="templates")  # Make sure Flask knows where templates are

# Function to retrieve interaction data from the database
def get_interaction_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email, timestamp FROM interactions")
    data = cursor.fetchall()
    conn.close()
    return data

# Route to display the analytics dashboard
@app.route('/')
def dashboard():
    data = get_interaction_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    print("🚀 Starting Flask app...")
    app.run(debug=True)
