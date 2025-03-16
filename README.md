# DNS Enumeration Tool

This tool provides a flexible way to perform DNS enumeration on a target domain. It queries for various DNS record types and displays the results in a clear and concise format.

## Features

*   **Multiple Record Types:** Queries for common DNS record types, including A, AAAA, CNAME, MX, NS, TXT, and SOA.
*   **Customizable Queries:** Specify the target domain and the desired record types directly from the command line.
*   **Error Handling:** Robustly handles a variety of common DNS errors, such as:
    *   `NoAnswer`: No records found for the specified type.
    *   `NXDOMAIN`: The domain does not exist.
    *   `NoNameservers`: No name servers found for the domain.
    *   `Timeout`: Query timed out.
    *   Other exceptions.
*   **Clear Output:** Presents the results in a readable format, clearly indicating the record type and the corresponding data.
*   **Verbose Mode:** Option to enable verbose output for more detailed information.

## Files

*   **`enumeration.py`:** The main script that drives the DNS enumeration process.
*   **`query.py`:** Contains the `query_dns` function responsible for querying the DNS server and handling responses.

## Usage

1.  **Prerequisites:**
    *   Python 3.x
    *   `dnspython` library: Install with `pip install dnspython` (this is necessary)

2.  **Running the Script:**

    *   Navigate to the directory containing `enumeration.py` and `query.py`.
    *   Run the script from your terminal with the target domain as an argument:

        ```bash
        python3 enumeration.py example.com
        ```
    * Optional arguments
        * `--type`: Allows you to specify the record types you are interested in.
        ```bash
        python3 enumeration.py example.com --type A --type MX --type TXT
        ```
        * `-v`: Activate verbose mode
        ```bash
        python3 enumeration.py example.com -v
        ```
3.  **Customization:**
    * **Target Domain:** No longer requires manual changes in the script. Instead, the first command-line argument specifies the target.
    *   **Record Types:** Using the `--type` argument, you can specify which DNS record types are you querying for. If no record types are given, all are queried by default.
    * **Verbose mode**: Using the `-v` argument will activate verbose mode.

## Code Description

### `query.py`

*   **`query_dns(target, record_type)`:**
    *   Takes the `target` domain and the `record_type` as input.
    *   Uses `dns.resolver.Resolver()` to create a DNS resolver object.
    *   Attempts to resolve the `target` for the given `record_type`.
    *   Prints the results if successful.
    *   Handles various exceptions (e.g., `NoAnswer`, `NXDOMAIN`, `NoNameservers`, `Timeout`) and prints appropriate error messages.

### `enumeration.py`

*   **Command-Line Argument Parsing:** Uses a library such as `argparse` to parse command line arguments, including the `target` domain, record types, and potentially a verbose flag.
* **Record Types**: If not specified, it will default to all common record types.
*   **Loop:** Iterates through the specified `record_types` (or all default types) and calls the `query_dns` function for each record type.
* **Verbose Mode**: If enabled, provides extra information about each query.

## Examples
```bash
python3 enumeration.py google.com
python3 enumeration.py microsoft.com --type A --type AAAA --type MX
python3 enumeration.py example.net -v
