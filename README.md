# DNSpy

DNSpy provides a user-friendly graphical interface for performing DNS enumeration on a target domain. It queries for various DNS record types and displays the results for you in a readable format.

## Features

*   **Multiple Record Types:** Queries for common DNS record types, including A, AAAA, CNAME, MX, NS, TXT, and SOA.
*   **GUI Interface:**  A graphical user interface makes the tool simple to use, especially for those less comfortable with the terminal.
*   **Customizable Queries:** Specify the target domain and the desired record types directly within the application's interface using input field.
*   **Error Handling:** Robustly handles a variety of common DNS errors, such as:
    *   `NoAnswer`: No records found for the specified type.
    *   `NXDOMAIN`: The domain does not exist.
    *   `NoNameservers`: No name servers found for the domain.
    *   `Timeout`: Query timed out.
    *   Other exceptions.
*   **Clear Output:** Presents the results in a readable format within the GUI, indicating the record type and corresponding data.
*   **Verbose Mode:** Option to enable verbose output, showing more detailed information about each query.
* **User-Friendly**: Easy to use for users with or without experience with CLI.

## Files

*   **`enumeration.py`:** The main script that drives the DNS enumeration process and manages the GUI.
*   **`query.py`:** Contains the `query_dns` function responsible for querying the DNS server and handling responses.

## Usage

1.  **Prerequisites:**
    *   Python 3.x
    *   `dnspython` library: Install with `pip install dnspython` (this is necessary).
    *   GUI library (e.g., Tkinter, PyQt): If you use a specific one, make sure to write down the installation procedure.
    *   Owner's permission to target their domain. 

2.  **Running the Application:**

    *   Navigate to the directory containing `enumeration.py` and `query.py`.
    *   Run the script from your terminal:

        ```bash
        python3 enumeration.py
        ```
    *   The GUI window will open.
    * **Inputs**: In the GUI, enter the target domain in the designated field.
    * **Record Types Selection**: Check the boxes next to the record types you wish to query (or leave them all checked for default).
    * **Verbose**: If you want verbose output, check the verbose box.
    * **Run**: Click the "Run" or "Query" button to start the enumeration.
    *   The results will be displayed in the output area within the GUI.
    * **Repeat**: You can repeat the procedure as many times as necessary.

3.  **Customization:**

    *   **Target Domain:** Input field in the GUI.
    *   **Record Types:** Checkboxes or similar controls in the GUI allow selecting which record types are to be queried. If none are selected, all types will be queried by default.
    * **Verbose mode**: Checkbox to activate the verbose mode.

## Code Description

### `query.py`

*   **`query_dns(target, record_type)`:**
    *   Takes the `target` domain and the `record_type` as input.
    *   Uses `dns.resolver.Resolver()` to create a DNS resolver object.
    *   Attempts to resolve the `target` for the given `record_type`.
    *   Returns the results if successful.
    *   Handles various exceptions (e.g., `NoAnswer`, `NXDOMAIN`, `NoNameservers`, `Timeout`) and returns appropriate error messages.

### `enumeration.py`

*   **GUI Creation:**  Uses a GUI library (e.g. `tkinter`, `PyQt`) to create the main application window.
* **User Interface**: The interface includes input fields, checkboxes, a "Run" button, and an output area.
*   **Event Handling:** Handles user interactions, such as button clicks and input changes.
* **Record Types**: If not specified, it will default to all common record types.
* **Verbose Mode**: If enabled, provides extra information about each query.
*   **Query Execution:** When the "Run" button is clicked, retrieves the target domain and selected record types from the GUI.
*   **Calls `query_dns`:** Calls the `query_dns` function from `query.py` to perform the DNS queries.
*   **Result Display:** Formats the results or error messages and displays them in the output area of the GUI.

## Examples

No longer command line examples but an explanation:
1. Run `python3 enumeration.py`.
2. A GUI will appear.
3. Type `google.com` in the text box.
4. Click on the A, AAAA and MX check box.
5. Click the Run button.
6. Wait for the results.
7. Repeat with `microsoft.com`.
8. Check the verbose box.
9. Run.
