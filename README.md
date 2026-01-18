This is a simple URL Shortener mini project.
Test it here: https://url-shortener-mag8.onrender.com/
Running locally, it will also create a database in your directory called `url_shortener.db`. Your shortened url `http://127.0.0.1:5000/{shortened-url}` will be stored here.

Note: Since it used free instance of Render Web Service, expect it to have have 60 seconds delay when accessing it after long period of inactivity.

Test it locally by following these steps:

1. Clone the repository

```bash
git clone https://github.com/tamama01/url-shortener.git
cd url-shortener
```

2. Create and activate a virtual environment  

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python app.py
```

5. Open your browser and go to `http://127.0.0.1:5000` to test locally.
