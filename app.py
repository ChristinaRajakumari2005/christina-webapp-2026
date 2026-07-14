from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Christina Rajakumari | Cloud Portfolio</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #FFB6C1, #FF69B4);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                background: white;
                border-radius: 24px;
                padding: 3rem;
                max-width: 700px;
                width: 90%;
                box-shadow: 0 16px 48px rgba(255,77,121,0.3);
                text-align: center;
            }
            h1 {
                color: #FF4D79;
                font-size: 2rem;
                margin-bottom: 0.5rem;
            }
            .tagline {
                color: #9C5B80;
                margin-bottom: 2rem;
                font-size: 1rem;
            }
            .cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 1rem;
                margin-bottom: 2rem;
            }
            .card {
                background: #FFF0F5;
                border-radius: 16px;
                padding: 1.2rem;
                border: 2px solid #FFB3D1;
            }
            .card h3 { color: #FF4D79; margin-bottom: 0.4rem; }
            .card p { color: #9C5B80; font-size: 0.85rem; }
            .badge {
                display: inline-block;
                background: #FF4D79;
                color: white;
                padding: 0.5rem 1.2rem;
                border-radius: 999px;
                font-size: 0.85rem;
                margin: 0.3rem;
            }
            .footer {
                margin-top: 2rem;
                color: #9C5B80;
                font-size: 0.8rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🩷 Christina Rajakumari</h1>
            <p class="tagline">Final Year ECE Student | Cloud Computing Intern @ KrutanicXAdobe</p>

            <div class="cards">
                <div class="card">
                    <h3>☁️ Cloud</h3>
                    <p>AWS S3, Azure App Service, boto3, DevOps</p>
                </div>
                <div class="card">
                    <h3>🤖 IoT</h3>
                    <p>ESP32, AMB82, LoRa, GPS/GSM, Arduino</p>
                </div>
                <div class="card">
                    <h3>🧠 AI</h3>
                    <p>Edge AI, ML models, Seizure Prediction</p>
                </div>
                <div class="card">
                    <h3>💻 Dev</h3>
                    <p>Python, C, Bash, Git, Linux</p>
                </div>
            </div>

            <div>
                <span class="badge">AWS</span>
                <span class="badge">Azure</span>
                <span class="badge">Python</span>
                <span class="badge">IoT</span>
                <span class="badge">Edge AI</span>
                <span class="badge">Linux</span>
                <span class="badge">Git</span>
            </div>

            <div class="footer">
                <p>🚀 Deployed on Microsoft Azure App Service</p>
                <p>LICET Chennai | IEEE Photonics Society Chair | FabLab LICET</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy", "app": "christina-webapp-2026"}

if __name__ == "__main__":
    app.run()