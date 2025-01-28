# LED Matrix Clock with Open-Meteo Integration

This project uses a 32x32 RGB LED matrix to display different images based on the current time fetched from the Open-Meteo API. The project is implemented in Python and works in a simulated environment with the `requests` library for HTTP requests.

## Features
- Fetches current time for Kalyan (UTC) from the Open-Meteo API.
- Displays different images for morning, afternoon, evening, and night on the LED matrix.
- Updates the display every 5 minutes.

## Requirements
- Python 3.7 or later
- Libraries:
  - `requests`
- 32x32 RGB LED matrix
- Four 32x32 pixel `.bmp` images:
  - `morning.bmp`
  - `afternoon.bmp`
  - `evening.bmp`
  - `night.bmp`

## Setup

1. Clone this repository or copy the source code into your environment.
2. Place the following `.bmp` images in the working directory:
   - `morning.bmp`
   - `afternoon.bmp`
   - `evening.bmp`
   - `night.bmp`
3. Install the required Python libraries using pip:
   ```bash
   pip install requests
   ```
4. Replace the LED matrix pin configuration in the source code if needed to match your hardware setup.

## How It Works
1. The program fetches the current time for Kalyan from the Open-Meteo API.
2. Depending on the current hour:
   - **6 AM to 12 PM**: Displays `morning.bmp`.
   - **12 PM to 6 PM**: Displays `afternoon.bmp`.
   - **6 PM to 9 PM**: Displays `evening.bmp`.
   - **9 PM to 6 AM**: Displays `night.bmp`.
3. The display refreshes every 5 minutes.

## Usage
Run the program using Python:
```bash
python led_matrix_clock.py
```

## API Details
The project uses the Open-Meteo API to fetch weather and time data. The API URL is pre-configured for Kalyan:
```
https://api.open-meteo.com/v1/forecast?latitude=19.2411&longitude=74&current_weather=true
```

## Troubleshooting
- Ensure your `.bmp` images are exactly 32x32 pixels.
- Verify your internet connection for the API request.
- Check the LED matrix pin configuration if the display is not working.

## Future Enhancements (TODO)
- Add support for dynamic weather-based icons.
- Integrate a real-time clock module for offline functionality.

---

Feel free to reach out if you encounter any issues or have suggestions for improvement!

