from query import query_dns as query

# Pick target domain and record type
target = "example.com" # example domain
record_types = ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SOA"]

for record in record_types:
    query(target, record)
