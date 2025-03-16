# DNS Enumeration Tool

This tool provides a simple way to perform DNS enumeration on a target domain. It queries for various DNS record types and displays the results in a simple, and concise format.

## Features

*   **Multiple Record Types:** Queries for common DNS record types, including A, AAAA, CNAME, MX, NS, TXT, and SOA.
*   **Error Handling:** Handles a variety of common DNS errors such as:
    *   `NoAnswer`: No records found for the specified type.
    *   `NXDOMAIN`: The domain does not exist.
    *   `NoNameservers`: No name servers found for the domain.
    *   `Timeout`: Query timed out.
    * Other exceptions.
*   **Clear Output:** Presents the results in a readable format, indicating the record type and the corresponding data.

## Files

*   **`enumeration.py`:** The main script that drives the DNS enumeration process.
*   **`query.py`:** Contains the `query_dns` function responsible for querying the DNS server and handling responses.

## Usage

1.  **Prerequisites:**
    *   Python 3.x
    *   `dnspython` library: Install with `pip install dnspython` (this is necessary)

2.  **Running the Script:**

    *   Navigate to the directory containing `enumeration.py` and `query.py`.
    *   Run the script from your terminal: `python3 enumeration.py`

3.  **Customization:**

    *   **Target Domain:** Modify the `target` variable in `enumeration.py` to change the domain being queried.
    ```python
    target = "example.com"  # Change this to your desired domain
    ```
    *   **Record Types:** Adjust the `record_types` list in `enumeration.py` to include or exclude specific record types.
    ```python
    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SOA"] # Add or remove record types
    ```

## Code Description

### `query.py`

*   **`query_dns(target, record_type)`:**
    *   Takes the `target` domain and the `record_type` as input.
    *   Uses `dns.resolver.Resolver()` to create a DNS resolver object.
    *   Attempts to resolve the `target` for the given `record_type`.
    *   Prints the results if successful.
    *   Handles various exceptions (e.g., `NoAnswer`, `NXDOMAIN`, `NoNameservers`, `Timeout`) and prints appropriate error messages.

### `enumeration.py`

*   **`target`:** A variable to store the target domain.
*   **`record_types`:** A list of DNS record types to query.
*   **Loop:** Iterates through the `record_types` list and calls the `query_dns` function for each record type.


