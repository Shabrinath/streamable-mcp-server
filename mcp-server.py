from fastmcp import FastMCP

app = FastMCP("utility-server", host="0.0.0.0", port=8000)
 

@app.tool()
def get_weather(city: str):
    """Fetch current weather for a city."""
    return {"city": city, "weather": f"Sample weather for {city}: sunny 25°C"}

@app.tool()
def convert_units(value: float, from_unit: str, to_unit: str):
    """Convert between common units (miles<->km, c<->f, kg<->lbs)."""
    conversions = {
        ("miles", "km"): lambda x: x * 1.60934,
        ("km", "miles"): lambda x: x / 1.60934,
        ("c", "f"): lambda x: (x * 9/5) + 32,
        ("f", "c"): lambda x: (x - 32) * 5/9,
        ("kg", "lbs"): lambda x: x * 2.20462,
        ("lbs", "kg"): lambda x: x / 2.20462,
    }
    key = (from_unit.lower(), to_unit.lower())
    if key not in conversions:
        return {"error": f"Conversion {from_unit}->{to_unit} not supported"}
    return {
        "input": f"{value} {from_unit}",
        "output": f"{conversions[key](value):.2f} {to_unit}"
    }

@app.resource("resource://sample-weather")
def sample_weather():
    """Static resource with example weather data."""
    return {"city": "London", "weather": "London: partly cloudy, +18°C"}

@app.prompt()
def weather_prompt():
    return "Ask me about the weather like: get_weather(city='Paris')"

@app.prompt()
def convert_prompt():
    return "Ask me to convert units like: convert_units(value=10, from_unit='miles', to_unit='km')"

if __name__ == "__main__":
    app.run(transport="streamable-http")
