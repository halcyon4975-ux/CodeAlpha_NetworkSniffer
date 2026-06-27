# Python Packet Sniffer

A simple packet sniffer developed using **Python** and **Scapy** to capture and analyze live network traffic. The application listens for packets on the network interface and displays essential packet information such as IP addresses, protocols, ports, and payload data.

## Features

- Capture live network packets
- Display source and destination IP addresses
- Identify network protocols (TCP, UDP, ICMP)
- Display source and destination port numbers
- Display packet payload (when available)
- Timestamp each captured packet
- Count captured packets

## Technologies Used

- Python 3.x
- Scapy
- Npcap (Windows)

## Project Structure

```
packet-sniffer/
│
├── packet_sniffer.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd packet-sniffer
```

### 2. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Npcap

For Windows, install **Npcap** and enable **WinPcap API-Compatible Mode** during installation.

## Running the Program

Run the packet sniffer with:

```bash
python packet_sniffer.py
```

The application will begin capturing live network traffic until it is stopped manually (Ctrl + C) or reaches the specified packet count if configured.

## Sample Output

```
==================================================
Packet #1
Time: 2026-06-23 10:15:42

Source IP: 192.168.1.10
Destination IP: 8.8.8.8

Protocol: UDP
Source Port: 54321
Destination Port: 53

Payload:
b'...'
==================================================
```

## Learning Outcomes

This project demonstrates practical understanding of:

- Network packet capture
- IP addressing
- TCP/IP protocols
- Packet analysis
- Python programming for cybersecurity
- Basic network traffic monitoring

## Author

**Derick**

