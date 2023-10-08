import platform
import subprocess
import os
from flask import Flask, render_template, jsonify
from nids import packet_capture as pk, config, npcap_install

app = Flask(__name__)
PCAP_FILE_LOCATION = os.path.join(config.get_packet_location(), "captured_packets.pcap")
CSV_FILE_LOCATION = os.path.join(config.get_packet_location(), "captured_packets.csv")

@app.route('/')
def index():
    pk.start_capture(output_filename=PCAP_FILE_LOCATION)
    pk.write_to_csv(pcap_filename=PCAP_FILE_LOCATION, output_filename=CSV_FILE_LOCATION)
    return jsonify({"message": "packets captured"})
    # return render_template("login.html")


if __name__ == '__main__':
    config.get_packet_location()
    app.run()
