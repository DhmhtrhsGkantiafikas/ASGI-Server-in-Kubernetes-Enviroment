from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app= FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    """
    <!DOCTYPE html>
    <html>
    <head>
        <title>K0s & Kong Gateway</title>
        <style>
            body { background-color: #1e1e2e; color: #cdd6f4; font-family: 'Courier New', Courier, monospace; text-align: center; padding-top: 50px; }
            h1 { color: #a6e3a1; font-size: 2.5em; }
            .box { border: 2px solid #89b4fa; padding: 20px; border-radius: 10px; display: inline-block; background-color: #181825; box-shadow: 0px 0px 15px #89b4fa; }
            a { color: #f38ba8; text-decoration: none; font-weight: bold; font-size: 1.2em; }
            a:hover { color: #f9e2af; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Kubernetes Project Active</h1>
            <p><strong>Infrastructure:</strong> k0s Bare-Metal VMs</p>
            <p><strong>Networking:</strong> Cilium eBPF</p>
            <p><strong>Ingress:</strong> Kong Gateway API</p>
            <br>
            <p>Δες τα ακατέργαστα δεδομένα του API εδώ:</p>
            <a href="/api/status">🔗 /api/status</a>
        </div>
    </body>
    </html>
    """
    return (html_kwdikas)

