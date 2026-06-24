from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

packet_count = 0

def process_packet(packet):

    global packet_count
    packet_count += 1

    print("\n" + "=" * 50)
    print(f"Packet #{packet_count}")
    print(f"Time: {datetime.now()}")

    if packet.haslayer(IP):

        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")

        if packet.haslayer(TCP):

            print("Protocol: TCP")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif packet.haslayer(UDP):

            print("Protocol: UDP")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        elif packet.haslayer(ICMP):

            print("Protocol: ICMP")




    if packet.haslayer(Raw):

         try:
            payload = packet[Raw].load

            print(f"Payload: {payload[:100]}")

         except:
             print("Unable to decode payload")    

print("Starting packet capture...")
print("Press CTRL+C to stop.\n")

sniff(
    prn=process_packet,
    count=100,
    store=False
)