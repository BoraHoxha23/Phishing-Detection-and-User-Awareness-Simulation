from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder="templates")  # Ensure Flask knows where templates are

# Function to log user clicks
def log_interaction(user_email):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO interactions (email) VALUES (?)", (user_email,))
    conn.commit()
    conn.close()
    print(f"✅ Interaction logged for: {user_email}")  # Debugging message

# Route triggered when a phishing link is clicked
@app.route('/phish/<email>')
def phishing_page(email):
    print(f"🔹 Received click from: {email}")  # Debugging message
    log_interaction(email)
    return render_template("report.html")  # This should now work

if __name__ == '__main__':
    print("🚀 Starting Flask app...")
    app.run(debug=True)
