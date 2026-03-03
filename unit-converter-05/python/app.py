import os
from flask import Flask, redirect, request, send_from_directory

app = Flask(__name__)


@app.route("/")
def serve_index():
    return redirect("/length.html")


@app.route("/<path:filename>", methods=["GET", "POST"])
def serve_file(filename):
    if request.method == "POST":
        value = request.form.get("inputValue")
        from_unit = request.form.get("fromUnit")
        to_unit = request.form.get("toUnit")

        match filename:
            case "length.html":
                try:
                    value = float(value)
                    converted_value = convert_length(value, from_unit, to_unit)
                    return_path = "length.html"
                except ValueError as e:
                    return str(e), 400
            case "weight.html":
                try:
                    value = float(value)
                    converted_value = convert_weight(value, from_unit, to_unit)
                    return_path = "weight.html"
                except ValueError as e:
                    return str(e), 400
            case "temp.html":
                try:
                    value = float(value)
                    converted_value = convert_temperature(value, from_unit, to_unit)
                    return_path = "temp.html"
                except ValueError as e:
                    return str(e), 400
            case _:
                return "Unsupported conversion type", 400

        return "<div>Converted Value: {:.4f} {}</div><a href='{}'>Back</a>".format(
            converted_value, to_unit, return_path
        )
    elif request.method == "GET":
        return send_from_directory("pages", filename)


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert input to Celsius
    if from_unit == "C":
        value_in_celsius = value
    elif from_unit == "F":
        value_in_celsius = (value - 32) * 5.0 / 9.0
    elif from_unit == "K":
        value_in_celsius = value - 273.15
    else:
        raise ValueError("Unsupported unit")

    # Convert Celsius to target unit
    if to_unit == "C":
        return value_in_celsius
    elif to_unit == "F":
        return (value_in_celsius * 9.0 / 5.0) + 32
    elif to_unit == "K":
        return value_in_celsius + 273.15
    else:
        raise ValueError("Unsupported unit")


def convert_weight(value, from_unit, to_unit):
    units = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "oz": 28.3495,
        "lb": 453.592,
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported unit")

    value_in_grams = value * units[from_unit]
    converted_value = value_in_grams / units[to_unit]

    return converted_value


def convert_length(value, from_unit, to_unit):
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34,
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported unit")

    value_in_meters = value * units[from_unit]
    converted_value = value_in_meters / units[to_unit]

    return converted_value


port = 3000
if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode, port=port, host="0.0.0.0")
