import platform
import subprocess
import os
from flask import Flask, render_template, jsonify
from nids import packet_capture as pk, config, npcap_install

app = Flask(__name__)


@app.route('/')
def index():
    pk.start_capture(output_filename=os.path.join(config.get_packet_location(), "captured_packets.pcap"))
    return jsonify({"message": "packets captured"})
    # return render_template("login.html")


if __name__ == '__main__':
    config.get_packet_location()
    app.run()
