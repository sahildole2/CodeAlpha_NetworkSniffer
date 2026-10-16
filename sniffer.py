"""
CodeAlpha Task 1 - Basic Network Sniffer
Author: Sahil Dole

Ye program network ke packets pakadta hai aur dikhata hai:
source IP, destination IP, protocol (TCP/UDP/ICMP) aur payload.

Run (admin/root zaroori hai):
    Linux/Mac : sudo python3 sniffer.py
    Windows   : Npcap install karo, phir Admin terminal me: python sniffer.py

Sirf apne network par use karo. Doosre ke network par bina permission sniff karna illegal hai.
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw, wrpcap

captured = []          # saare packets yahan save honge (baad me .pcap bana sakte hain)
PACKET_LIMIT = 30      # kitne packets pakadne hain


def show_packet(packet):
    """Har packet ke liye ye function chalta hai."""
    # Hume sirf IP wale packets chahiye
    if IP not in packet:
        return

    captured.append(packet)
    src = packet[IP].src
    dst = packet[IP].dst

    # Protocol pehchano
    if TCP in packet:
        proto = "TCP"
        ports = f"{packet[TCP].sport} -> {packet[TCP].dport}"
    elif UDP in packet:
        proto = "UDP"
        ports = f"{packet[UDP].sport} -> {packet[UDP].dport}"
    elif ICMP in packet:
        proto = "ICMP (ping)"
        ports = "-"
    else:
        proto = f"Other (number {packet[IP].proto})"
        ports = "-"

    print("-" * 60)
    print(f"Packet #{len(captured)}")
    print(f"Source IP      : {src}")
    print(f"Destination IP : {dst}")
    print(f"Protocol       : {proto}")
    print(f"Ports          : {ports}")

    # Payload (data) agar hai to thoda sa dikhao
    if Raw in packet:
        data = bytes(packet[Raw].load)[:50]   # sirf pehle 50 bytes
        print(f"Payload (50B)  : {data}")
    else:
        print("Payload        : (empty)")


def main():
    print(f"Sniffing shuru... {PACKET_LIMIT} packets pakdenge. Rokne ke liye Ctrl+C.\n")
    try:
        sniff(prn=show_packet, count=PACKET_LIMIT, store=False)
    except PermissionError:
        print("Permission error: admin/root se run karo.")
        return
    except KeyboardInterrupt:
        print("\nBand kar diya.")

    # Summary
    print("\n===== SUMMARY =====")
    print(f"Total IP packets captured: {len(captured)}")
    if captured:
        wrpcap("capture.pcap", captured)
        print("Saved as capture.pcap (Wireshark me khol sakte ho)")


if __name__ == "__main__":
    main()
