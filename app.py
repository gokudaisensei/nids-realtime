import platform
import subprocess

from flask import Flask, render_template, jsonify
from nids import packet_capture as pk, config, winpcap_install

app = Flask(__name__)


@app.route('/')
def index():
    pk.start_capture(output_filename=config.get_packet_location() + "test.pcap")
    return jsonify({"message": "packets captured"})
    # return render_template("login.html")


if __name__ == '__main__':
    config.get_packet_location()
    winpcap_install.main()
    app.run()
