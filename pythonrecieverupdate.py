import argparse
import time
from pythonosc import dispatcher
from pythonosc import osc_server

last_emotion = None  # Global variable to store the last emotion value
last_processed_time = 0  # Global variable to store the time of the last processed message
debounce_interval = 0.1  # Interval in seconds (e.g., 0.5 seconds)

def handler(address, *args):
    global last_emotion, last_processed_time  # Declare the global variables
    current_time = time.time()

    # Only process if enough time has passed since the last processed message
    if current_time - last_processed_time > debounce_interval:
        emotion = args[0]  # Expecting args to be a tuple with the emotion as the first element

        if emotion != last_emotion:
            if emotion == 1:
                print("You're angry!")
            elif emotion == 2:
                print("You're sad???")
            elif emotion == 3:
                print("You're happy!")
            elif emotion == 4:
                print("You're scared!")

            last_emotion = emotion  # Update the last emotion value
            last_processed_time = current_time  # Update the last processed time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1", help="The IP to listen on")
    parser.add_argument("--port",
                        type=int, default=12000, help="The port to listen on")  # port 12000 set in wekinator
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/wek/outputs", handler)  # OSC messages are formatted like URLs

    try:
        server = osc_server.ThreadingOSCUDPServer(
            (args.ip, args.port), dispatcher)
        print("Serving on {}".format(server.server_address))
        server.serve_forever()
    except Exception as e:
        print(f"An error occurred: {e}")
