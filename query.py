import dns.resolver
import logging

# DNS errors are logged in file
logging.basicConfig(filename='dns_query_errors.log', level=logging.ERROR,
                    # timestamp, error level, message
                    format='%(asctime)s - %(levelname)s - %(message)s')


def query_dns(target, record_type, nameservers=None):
    """Performs DNS query using target, record_type, and optional custom nameservers."""
    resolver = dns.resolver.Resolver()
    if nameservers:
        resolver.nameservers = nameservers

    try:
        result = resolver.resolve(target, record_type)
        print(f"{record_type} for {target}:")
        return [str(data) for data in result]

    except dns.resolver.NoAnswer:
        msg = f"No answer for {record_type} record for {target}"
    except dns.resolver.NXDOMAIN:
        msg = f"Domain {target} does not exist"
    except dns.resolver.NoNameservers:
        ns_list = ", ".join(map(str, resolver.nameservers)
                            ) if resolver.nameservers else ""
        msg = f"No name servers found for {target}"
        if ns_list:
            msg += f" among {ns_list}"
    except dns.exception.Timeout:
        ns_list = ", ".join(map(str, resolver.nameservers)
                            ) if resolver.nameservers else ""
        msg = f"Timeout while querying {record_type} record for {target}"
        if ns_list:
            msg += f" from nameservers {ns_list}"
    except Exception as e:
        msg = f"An error occurred while querying {record_type} record for {target}: {e}"

    logging.error(msg)
    print(msg)
    return []
