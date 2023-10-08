import time
import socket
from scapy.all import sniff, wrpcap, IFACES
from pcap_handler import pcapHandler


def packet_capture(packet):
    return packet.summary()


def get_wireless_interface():
    try:
        # Get the IPv4 address
        target_ipv4 = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        # Handle the case where hostname cannot be resolved
        return None

    # Get the list of network interfaces
    interfaces = list(IFACES.data.values())

    for iface in interfaces:
        # Check if the IPv4 address of the interface matches the target
        if iface.ip == target_ipv4:
            return iface
    # If no interface matches, return None
    return None


def start_capture(*, output_filename: str):
    # Get the wireless interface
    wireless_iface = get_wireless_interface()
    if wireless_iface is None:
        print("Unable to find wireless interface.")
        return

    # Initialize an empty list to store packets
    packets = sniff(iface=wireless_iface, prn=packet_capture, count=10)

    # Introduce a delay (e.g., 1 second) to ensure the capture is complete
    time.sleep(1)

    # Save captured packets to a PCAP file
    wrpcap(output_filename, packets)

def write_to_csv(*, pcap_filename: str, output_filename: str):
    packets = pcapHandler(file=pcap_filename)
    packets.to_DF().to_csv()
