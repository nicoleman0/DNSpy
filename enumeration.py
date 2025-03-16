import dns.resolver

# Pick target domain and record type
target = "x.com" # example domain
record_types = ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SOA"]

resolver = dns.resolver.Resolver()

for record in record_types:
    try:
        result = resolver.resolve(target, record)
    except dns.resolver.NoAnswer:
        continue
    except dns.resolver.NXDOMAIN:
        continue
    except dns.resolver.NoNameservers:
        continue

print(f"{record} for {target}:")
for data in result:
    print(data)
