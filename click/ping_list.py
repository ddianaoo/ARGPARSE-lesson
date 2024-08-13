import click
import subprocess


def ping_ip(ip_address, count):
    """
    Ping IP address and return True/False
    """
    reply = subprocess.run(
        f"ping -c {count} -n {ip_address}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if reply.returncode == 0:
        return True
    else:
        return False


@click.command()
@click.argument("ip_address", nargs=-1, required=True)
@click.option("--count", "-c", default=3)
def main(ip_address, count):
    for ip in ip_address:
        if ping_ip(ip, count=3):
            print(f"IP address {ip:15} is pingable")
        else:
            print(f"IP address {ip:15} is not pingable")


if __name__ == "__main__":
    main()

# python3 ping_list.py 8.8.8.8 10.1.1.1 8.8.4.4 192.168.100.1
# python3 ping_list.py 8.8.8.8 10.1.1.1 8.8.4.4 192.168.100.1 -c 2