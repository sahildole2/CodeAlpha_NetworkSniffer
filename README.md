# CodeAlpha Task 1 - Basic Network Sniffer

A beginner-friendly Python packet sniffer built with `scapy`.

## What it does
- Captures live network packets
- Shows source IP, destination IP, protocol (TCP / UDP / ICMP), ports
- Shows the first 50 bytes of payload when available
- Saves everything to `capture.pcap` (open in Wireshark)

## Setup
```bash
pip install scapy
sudo python3 sniffer.py        # Linux/Mac
python sniffer.py              # Windows (Admin terminal + Npcap installed)
```

## How networks work (quick notes)
- Data travels in small **packets**. Each has a header (who sent it, who gets it, which protocol) and a payload (actual data).
- **TCP**: reliable, used by web (HTTP/HTTPS), email. **UDP**: fast, used by DNS, video calls. **ICMP**: used by `ping`.
- HTTPS payloads look like random bytes because they are encrypted. Plain HTTP payloads are readable, which is why HTTP is unsafe.

## Try it
1. Run the script.
2. In another terminal run `ping google.com` and see ICMP packets.
3. Open a website and see TCP/UDP packets.

## Disclaimer
For learning on your own network only.
