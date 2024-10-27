import psutil


def block_conn(ip, port):
    connections = psutil.net_connections()

    for conn in connections:
        if conn.laddr.ip == ip and conn.laddr.port == port:
            try:
                proc = psutil.Process(conn.pid)
                proc.kill()
                print(f"Connection with {ip}:{port} blocked.")
            except Exception as e:
                print(f"Failed to block the connection: {e}")


def main():
    ip = input("Enter IP-address to block: ")
    port = int(input("Enter port to block: "))
    block_conn(ip, port)


if __name__ == '__main__':
    main()
