# Unit Converter

A Python web app project for converting between various units of measurement. This project forces a dual-method style of web app development since the webpages must use target=_self in the forms. The server uses Flask to serve the HTML pages and implements both GET and POST methods to both serve the pages and perform their respective conversion actions. This is part of the [Roadmap.sh Backend Roadmap](https://roadmap.sh/backend) project challenges, specifically the [Unit Converter Challenge](https://roadmap.sh/projects/unit-converter).

## Features

- Convert between length, temperature, and weight units.
- Simple web interface with separate pages for each conversion type.
- Supports both GET and POST requests for conversions.
- Built with Flask for easy deployment and development.

## Usage

1. **Install dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the app**  
    ```bash
    python app.py
    ```

3. **Access the web interface**  
    Open your browser and go to `http://localhost:5000`.

## Pages

- `/length` — Convert between meters, kilometers, miles, and feet.
- `/temp` — Convert between Celsius, Fahrenheit, and Kelvin.
- `/weight` — Convert between grams, kilograms, pounds, and ounces.

## Development

- All HTML pages are in the `pages/` directory.
- The Flask app logic is in `app.py`.
- Use the provided `Dockerfile` for containerized deployment.

## License

This project is open source and available under the MIT License.