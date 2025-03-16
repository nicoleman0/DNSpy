import dns.resolver

def query_dns(target, record_type):
    resolver = dns.resolver.Resolver()
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
    except Exception as e:
        print(f"An error occurred while querying {record_type} record for {target}: {e}")
