from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "Exotel IVR Server Running"

@app.route("/exotel.xml")
def exotel_xml():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="female" language="en-IN">Hi Aditya. This is your test call from Exotel.</Say>
</Response>
"""
    return Response(xml, mimetype="text/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
