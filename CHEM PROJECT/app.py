from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

districts = sorted([
    "Mumbai City","Mumbai Suburban","Thane","Palghar","Raigad","Ratnagiri","Sindhudurg",
    "Ahmednagar","Dhule","Jalgaon","Nandurbar","Nashik",
    "Kolhapur","Sangli","Satara","Solapur","Pune",
    "Aurangabad","Beed","Hingoli","Jalna","Latur","Nanded","Osmanabad","Parbhani","Chhatrapati Sambhajinagar",
    "Nagpur","Wardha","Bhandara","Chandrapur","Gadchiroli","Gondia",
    "Amravati","Akola","Washim","Yavatmal","Buldhana"
])


district_coords = {
    "Ahmednagar": {"lat": 19.0934, "lon": 74.7469},
    "Akola": {"lat": 20.7106, "lon": 77.0037},
    "Amravati": {"lat": 20.9375, "lon": 77.7792},
    "Aurangabad": {"lat": 19.8806, "lon": 75.3431},
    "Beed": {"lat": 18.9772, "lon": 75.7131},
    "Bhandara": {"lat": 21.1603, "lon": 79.5289},
    "Buldhana": {"lat": 20.5325, "lon": 76.1389},
    "Chandrapur": {"lat": 19.9719, "lon": 79.2953},
    "Dhule": {"lat": 20.9897, "lon": 74.7735},
    "Gadchiroli": {"lat": 19.5783, "lon": 80.0194},
    "Gondia": {"lat": 21.4597, "lon": 80.1956},
    "Hingoli": {"lat": 19.7964, "lon": 77.1842},
    "Jalgaon": {"lat": 21.0056, "lon": 75.5667},
    "Jalna": {"lat": 19.8583, "lon": 75.8833},
    "Kolhapur": {"lat": 16.7050, "lon": 74.2433},
    "Latur": {"lat": 18.4094, "lon": 76.5872},
    "Mumbai City": {"lat": 18.9750, "lon": 72.8258},
    "Mumbai Suburban": {"lat": 19.0760, "lon": 72.8777},
    "Nagpur": {"lat": 21.1458, "lon": 79.0882},
    "Nanded": {"lat": 19.1833, "lon": 77.3167},
    "Nandurbar": {"lat": 21.3833, "lon": 74.2500},
    "Nashik": {"lat": 20.0113, "lon": 73.7908},
    "Osmanabad": {"lat": 18.1811, "lon": 76.0422},
    "Palghar": {"lat": 19.9181, "lon": 72.7460},
    "Parbhani": {"lat": 19.2678, "lon": 77.0172},
    "Pune": {"lat": 18.5204, "lon": 73.8567},
    "Raigad": {"lat": 18.2047, "lon": 73.4095},
    "Ratnagiri": {"lat": 16.9890, "lon": 73.3115},
    "Sangli": {"lat": 16.8600, "lon": 74.5611},
    "Satara": {"lat": 17.6903, "lon": 73.8567},
    "Sindhudurg": {"lat": 16.0185, "lon": 73.7524},
    "Solapur": {"lat": 17.6890, "lon": 75.9064},
    "Thane": {"lat": 19.2183, "lon": 72.9780},
    "Wardha": {"lat": 20.7464, "lon": 78.5972},
    "Washim": {"lat": 20.1172, "lon": 77.1492},
    "Yavatmal": {"lat": 20.3944, "lon": 78.1306}
}

OPENWEATHER_API_KEY = "c5b481bfba2be2031ef9e3b55a6278d2"

def load_district_data():
    with open("data/district_data.json") as f:
        return json.load(f)

def get_weather(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return {
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["main"],
            "forecast": data["weather"][0]["description"]
        }
    return None

@app.route("/", methods=["GET","POST"])
def index():
    selected_district = None
    info = None
    if request.method == "POST":
        selected_district = request.form.get("district")
        district_data = load_district_data()
        info = district_data.get(selected_district, {})

        if selected_district in district_coords:
            coords = district_coords[selected_district]
            weather_info = get_weather(coords["lat"], coords["lon"])
            if weather_info:
                info["weather"] = weather_info

    return render_template("index.html",
                           districts=districts,
                           selected_district=selected_district,
                           info=info)

if __name__ == "__main__":
    app.run(debug=True)