import dns.resolver
import logging

# DNS errors are logged in file
logging.basicConfig(filename='dns_query_errors.log', level=logging.ERROR,
                    # timestamp, error level, message
                    format='%(asctime)s - %(levelname)s - %(message)s')


def query_dns(target, record_type, nameservers=None):
    """Performs DNS query using target, record_type, and optional custom nameservers."""
    resolver = dns.resolver.Resolver()  # Creates a DNS resolver object
    if nameservers:
        resolver.nameservers = nameservers
    try:
        result = resolver.resolve(target, record_type)  # DNS query
        print(f"{record_type} for {target}:")
        data_list = []
        for data in result:  # adds each record found to a list
            print(data)
            data_list.append(str(data))
        return data_list
    except dns.resolver.NoAnswer:
        logging.error(f"No answer for {record_type} record for {target}")
        print(f"No answer for {record_type} record for {target}")
        return []
    except dns.resolver.NXDOMAIN:
        logging.error(f"Domain {target} does not exist")
        print(f"Domain {target} does not exist")
        return []
    except dns.resolver.NoNameservers:
        if resolver.nameservers:
            nameservers = ", ".join(map(str, resolver.nameservers))
            logging.error(
                f"No name servers found for {target} among {nameservers}")
            print(f"No name servers found for {target} among {nameservers}")
        else:
            logging.error(f"No name servers found for {target}")
            print(f"No name servers found for {target}")
        return []
    except dns.exception.Timeout:
        if resolver.nameservers:
            nameservers = ", ".join(map(str, resolver.nameservers))
            logging.error(
                f"Timeout while querying {record_type} record for {target} from nameservers {nameservers}")
            print(
                f"Timeout while querying {record_type} record for {target} from nameservers {nameservers}")
        else:
            logging.error(
                f"Timeout while querying {record_type} record for {target}")
            print(f"Timeout while querying {record_type} record for {target}")

        return []
    except Exception as e:
        logging.error(
            f"An error occurred while querying {record_type} record for {target}: {e}")
        print(
            f"An error occurred while querying {record_type} record for {target}: {e}")
        return []
