from scapy.all import sniff, IP, TCP, UDP, Raw

def analyze_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = "Unknown"

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"

        print(f"\n[+] Packet Captured:")
        print(f"    Source IP      : {src_ip}")
        print(f"    Destination IP : {dst_ip}")
        print(f"    Protocol       : {protocol}")

        if Raw in packet:
            payload = packet[Raw].load
            try:
                print(f"    Payload        : {payload.decode('utf-8', 'ignore')}")
            except:
                print(f"    Payload        : [Non-textual data]")

# Sniff packets
print("🔍 Starting Packet Sniffer... (Press Ctrl+C to stop)\n")
sniff(prn=analyze_packet, count=10)  # captures 10 packets
