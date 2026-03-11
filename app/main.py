from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app= FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    html_kwdikas="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Home</title>
    </head>
    <body>
      
          <h2>ManosPaok1999</h2>
    </body>
    </html>


    """
    return (html_kwdikas)

