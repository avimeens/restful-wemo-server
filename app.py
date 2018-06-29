from flask import Flask
import pywemo, json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/discover")
def discover():
    try:
        devices = pywemo.discover_devices()
        if len(devices) < 1:
            return "There are no wemo devices"
        else:
            temp = []
            for device in devices:
                print "Discovered a We Mo %s called %s" % (device.model_name, device.name)
                temp.append(device)
                print temp 
                return json.dumps(temp)
    except Exception as e:
        feedback = "Error occurred while discovering wemo devices: " + e
        return feedback


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
