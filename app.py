from flask import Flask, render_template, request, redirect
import string, random, sqlite3, os

app = Flask(__name__)

# database setup
DATABASE = 'url_shortener.db'

def init_db():
    """Create database table if it doesn't exist"""
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''CREATE TABLE urls
                     (short_code TEXT PRIMARY KEY, original_url TEXT)''')
        conn.commit()
        conn.close()

# initialize database on startup
init_db()

def save_url(short_code, original_url):
    """Save URL mapping to database"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO urls VALUES (?, ?)', (short_code, original_url))
    conn.commit()
    conn.close()

def get_url(short_code):
    """Get original URL from database"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT original_url FROM urls WHERE short_code = ?', (short_code,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

# mainpage or index
@app.route("/", methods=["GET", "POST"])
def home():
    shortened_url = None
    if request.method == "POST":
        url = request.form.get("url_input") # from home.html input field

        # generate 6 random characters
        characters = string.ascii_letters + string.digits
        while True:
            short_code = ''.join(random.choice(characters) for _ in range(6))
            # check if short_code already exists
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            c.execute('SELECT short_code FROM urls WHERE short_code = ?', (short_code,))
            existing = c.fetchone()
            conn.close()
            if not existing:
                break
        
        # save to database
        save_url(short_code, url)
        
        # create full shortened URL with host
        shortened_url = f"{request.host}/{short_code}"
    
    return render_template("home.html", shortened_url=shortened_url)

# route to handle shortened links
@app.route("/<short_code>")
def redirect_url(short_code):
    original_url = get_url(short_code)
    if original_url:
        return redirect(original_url)
    return "Link not found", 404

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host="0.0.0.0", port=port)