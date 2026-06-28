# Python Packet Sniffer

## Overview

This project is a simple packet sniffer developed in Python using the Scapy library. It captures live network packets from the local network interface and extracts key information from each packet for analysis.

The application demonstrates basic network packet inspection by displaying source and destination IP addresses, transport protocols, port numbers, timestamps, and packet payloads (when available).

---

## Features

* Capture live network traffic
* Display source IP address
* Display destination IP address
* Identify packet protocols (TCP, UDP, ICMP)
* Display source and destination port numbers
* Display packet payload (when available)
* Display packet timestamp
* Count captured packets

---

## Technologies Used

* Python 3
* Scapy
* Npcap (Windows)

---

## Installation

### Install Scapy

```bash
pip install scapy
```

### Install Npcap (Windows)

Download and install Npcap, ensuring that **WinPcap API-Compatible Mode** is enabled during installation.

---

## Running the Program

Execute the program using:

```bash
python packet_sniffer.py
```

The program will begin capturing live network packets and display their details in the terminal.

To stop packet capture, press:

```text
CTRL + C
```

---

## Sample Output

```text
==================================================
Packet #15
Time: 2026-06-28 10:45:12

Source IP: 10.217.116.56
Destination IP: 10.217.116.105

Protocol: UDP
Source Port: 50312
Destination Port: 53

Payload:
b'...'
==================================================
```



---

## Author

Derick
