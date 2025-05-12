from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Covenant Marques Mapuranga | Portfolio</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #f9f9f9;
                color: #333;
            }
            header {
                background-color: #1abc9c;
                color: white;
                padding: 40px 0 20px;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            header h1 {
                margin: 0;
                font-size: 2.5em;
            }
            header p {
                margin: 5px 0;
            }
            .contact-info {
                margin-top: 10px;
                font-size: 0.95em;
            }
            .container {
                max-width: 1000px;
                margin: 40px auto;
                padding: 0 20px;
            }
            section {
                margin-bottom: 40px;
            }
            h2 {
                border-bottom: 2px solid #1abc9c;
                padding-bottom: 10px;
                color: #2c3e50;
            }
            ul {
                padding-left: 20px;
            }
            footer {
                text-align: center;
                padding: 20px;
                background-color: #eee;
                color: #555;
                font-size: 0.9em;
            }
            .project {
                background: #fff;
                padding: 15px;
                margin-bottom: 10px;
                border-left: 5px solid #1abc9c;
                box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Covenant Marques Mapuranga</h1>
            <p>Aspiring Web Developer | Python & Front-End Specialist</p>
            <div class="contact-info">
                <p>📞 +263 716 859 706 | ✉️ mapurangacovenant1@gmail.com</p>
            </div>
        </header>
        <div class="container">
            <section>
                <h2>About Me</h2>
                <p>Hello! I’m Covenant, passionate about technology, web design, and building clean, functional websites using HTML, CSS, JavaScript, and Python.</p>
            </section>
            <section>
                <h2>Skills</h2>
                <ul>
                    <li>HTML5, CSS3, JavaScript</li>
                    <li>Python (Flask, pandas, requests)</li>
                    <li>Git & GitHub</li>
                    <li>Responsive Web Design</li>
                </ul>
            </section>
            <section>
                <h2>Projects</h2>
                <div class="project">
                    <strong>Job Scraper</strong>
                    <p>A Python script that scrapes job listings and exports them to CSV using `requests` and `BeautifulSoup`.</p>
                </div>
                <div class="project">
                    <strong>Payslip Generator</strong>
                    <p>A Flask app that reads Excel data and generates personalised PDF payslips for employees.</p>
                </div>
            </section>
        </div>
        <footer>
            &copy; 2025 Covenant Marques Mapuranga | 📞 +263 716 859 706 | ✉️ mapurangacovenant1@gmail.com
        </footer>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
