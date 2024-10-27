from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP


def packet_callback(packet):
    print("----- The package -----")
    print(f"Type of package: {packet.summary()}")

    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source: {ip_layer.src}")
        print(f"Destination: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"Source port: {tcp_layer.sport}")
            print(f"Destination port: {tcp_layer.dport}")
            print(f"TCP flags: {tcp_layer.flags}")

        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"Source port: {udp_layer.sport}")
            print(f"Destination port: {udp_layer.dport}")

        elif ICMP in packet:
            icmp_layer = packet[ICMP]
            print(f"ICMP type: {icmp_layer.type}")
            print(f"ICMP code: {icmp_layer.code}")

    print("--------------------------\n")


def start_sniffer(interface):
    print(f"Starting sniffer on the interface: {interface}")
    sniff(iface=interface, prn=packet_callback, store=0)


def main():
    interface = input("Enter Ethernet adapter name: ")
    start_sniffer(interface)


if __name__ == "__main__":
    main()
