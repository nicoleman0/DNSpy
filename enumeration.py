import argparse
from query import query_dns as query


def main():
    parser = argparse.ArgumentParser(
        description="Perform DNS enumeration on a target domain.")
    parser.add_argument(
        "target", help="The target domain to enumerate (e.g., example.com).")
    parser.add_argument("-r", "--record_types", nargs="+", default=["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SOA"],
                        help="Specify the record types to query (e.g., A MX TXT). Default: A, AAAA, CNAME, MX, NS, TXT, SOA")
    parser.add_argument("-s", "--nameservers", nargs="+",
                        help="Specify custom name servers (e.g., 8.8.8.8 8.8.4.4)")
    args = parser.parse_args()  # parses command line args
    print(f"Starting DNS Enumeration for {args.target}\n")
    for record in args.record_types:
        print(f"Querying {record} records")
        data = query(args.target, record, args.nameservers)
        if not data:
            print(f"No records found for {record}")
        print("\n")


if __name__ == "__main__":
    main()
