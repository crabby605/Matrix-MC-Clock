import requests
import time
import board
import displayio
import framebufferio
import rgbmatrix

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=19.2411&longitude=73.1304&current_weather=true"

def fetch_current_time():
    """Fetch current time from Open-Meteo API."""
    try:
        print(f"Fetching time data from {API_URL}...")
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        # Extract the current time (UTC format)
        current_time = data["current_weather"]["time"]
        print(f"Current time (UTC): {current_time}")
        return current_time
    except Exception as e:
        print(f"Error fetching time data: {e}")
        return None

# Set up the matrix display
matrix = rgbmatrix.RGBMatrix(
    width=32, height=32, bit_depth=4,
    rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
    addr_pins=[board.A5, board.A4, board.A3, board.A2],
    clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1
)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

splash = displayio.Group()
display.root_group = splash

morning_bitmap = displayio.OnDiskBitmap("dawn.bmp")
afternoon_bitmap = displayio.OnDiskBitmap("noon.bmp")
evening_bitmap = displayio.OnDiskBitmap("dusk.bmp")
night_bitmap = displayio.OnDiskBitmap("midnight.bmp")

image = displayio.TileGrid(morning_bitmap, pixel_shader=morning_bitmap.pixel_shader)
splash.append(image)

while True:
    current_time = fetch_current_time()
    if current_time:
        hour = int(current_time.split("T")[1].split(":")[0])

        splash.pop()
        if 6 <= hour < 12:  # Morning
            image = displayio.TileGrid(morning_bitmap, pixel_shader=morning_bitmap.pixel_shader)
        elif 12 <= hour < 18:  # Afternoon
            image = displayio.TileGrid(afternoon_bitmap, pixel_shader=afternoon_bitmap.pixel_shader)
        elif 18 <= hour < 21:  # Evening
            image = displayio.TileGrid(evening_bitmap, pixel_shader=evening_bitmap.pixel_shader)
        else:  # Night
            image = displayio.TileGrid(night_bitmap, pixel_shader=night_bitmap.pixel_shader)
        
        splash.append(image)
    
    display.refresh()
    time.sleep(300)
