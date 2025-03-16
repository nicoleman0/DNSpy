import dns.resolver

# Pick target domain and record type
target = "example.com" # example domain
record_types = ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SOA"]

resolver = dns.resolver.Resolver()

def query_dns(target, record_type):
    try:
        result = resolver.resolve(target, record_type)
        print(f"{record_type} for {target}:")
        for data in result:
            print(data)
    except dns.resolver.NoAnswer:
        print(f"No answer for {record_type} record for {target}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {target} does not exist")
    except dns.resolver.NoNameservers:
        print(f"No name servers found for {target}")
    except dns.exception.Timeout:
        print(f"Timeout while querying {record_type} record for {target}")

for record in record_types:
    query_dns(target, record)
