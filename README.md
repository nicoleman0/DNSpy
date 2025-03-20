# DNSpy

A simple GUI tool for performing DNS queries and enumeration.

## Features
- Query multiple DNS record types (A, AAAA, CNAME, MX, NS, TXT, SOA)
- Customizable query options
- Verbose output mode
- Error logging
- Multi-threaded queries for better performance

## Installation

1. Ensure you have Python 3.x installed on your system.

2. Install the required dependency using pip:
```python
pip install dnspython
```

3. Clone this repository or download the source code:
```bash
git clone <your-repository-url>
cd <repository-name>
```

4. You are now ready to use DNSpy.

## Usage Example

```python
from query import query_dns

# Query A record
results = query_dns("example.com", "A")

# Query with custom nameservers
results = query_dns("example.com", "MX", nameservers=["8.8.8.8", "8.8.4.4"])
```

Note: The program will log any DNS query errors to `dns_query_errors.log` in the same directory.

Be cautious with your activities.
