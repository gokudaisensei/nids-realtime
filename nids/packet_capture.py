import time

from scapy.all import sniff, wrpcap


def packet_capture(packet):
    return packet.summary()


def start_capture(*, output_filename: str):
    # Initialize an empty list to store packets
    packets = sniff(prn=packet_capture, count=10)

    # Introduce a delay (e.g., 1 second) to ensure the capture is complete
    time.sleep(1)

    # Save captured packets to a PCAP file
    wrpcap(output_filename, packets)
