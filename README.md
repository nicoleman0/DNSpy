# DNSpy

DNSpy provides a user-friendly graphical interface for performing DNS enumeration on a target domain. It queries for various DNS record types and displays the results for you in a readable format. Be weary in enumerating domains that forbid it in their ToS. It is also advisable to not enumerate any domains associated with governments, militaries, intelligence agencies, etc. Just stay careful out there.

## Features

*   **Multiple Record Types:** Queries for common DNS record types, including A, AAAA, CNAME, MX, NS, TXT, and SOA.
*   **GUI Interface:**  A graphical user interface makes the tool simple and easy to use.
*   **Customizable Queries:** Choose the record types you wish to query, along with an optional verbose mode for more detailed output.
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

*   **`query.py`:** Contains the `query_dns` function responsible for querying the DNS server and handling responses.
*   **`dnspy_gui.py`:** Responsible for the graphical user interface and event handling.

## Usage

1.  **Prerequisites:**

*   **Python 3.x:** DNSpy is written in Python 3 and requires a Python 3 interpreter to be installed on your system. You can check if you have it installed by running `python3 --version` in your terminal. If not, then you can go and visit the official Python website.
*   **`dnspython` Library:** DNSpy utilizes the `dnspython` library for DNS resolution. You can install it using pip:
    ```bash
    pip3 install dnspython
    ```
*   **Tkinter (or another GUI library):** DNSpy uses a graphical user interface (GUI). The current implementation uses Tkinter, which is usually included with Python. If you don't have it, or if you want to use a different GUI library (like PyQt), you'll need to install it.
    *   **Tkinter (Recommended):**  If you don't have it, it may be installed with:
        ```bash
        # On Debian/Ubuntu:
        sudo apt-get install python3-tk

        # On macOS (using Homebrew):
        brew install python-tk

        # On Windows, it's usually included with Python.
        ```
    *   **PyQt (Alternative):** If you prefer PyQt, you can install it with:
        ```bash
        pip3 install PyQt6  # Or PyQt5, depending on your preference
        ```
        **Note:** If you choose PyQt, you'll need to modify the `dnspy_gui.py` file to use PyQt instead of Tkinter.

2.  **Running the Application:**

    *   Navigate to the directory containing `dnspy_gui.py` and `query.py`.
    *   Run the script from your terminal:

        ```bash
        python3 dnspy_gui.py
        ```
    *   The GUI window will open.
    * **Inputs**: In the GUI, enter the target domain in the designated field. 
    * **Record Types Selection**: Check the boxes next to the record types you wish to query (or leave them all checked for default).
    * **Verbose**: If you want verbose output, check the verbose box.
    * **Run**: Click the "Run" button to start the enumeration.
    *   The results will be displayed in the output area within the GUI.
    *   Repeat as many times as you wish.


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

### ``

*   **GUI Creation:**  Uses a GUI library (e.g. `tkinter`, `PyQt`) to create the main application window.
* **User Interface**: The interface includes input fields, checkboxes, a "Run" button, and an output area.
*   **Event Handling:** Handles user interactions, such as button clicks and input changes.
* **Record Types**: If not specified, it will default to all common record types.
* **Verbose Mode**: If enabled, provides extra information about each query.
*   **Query Execution:** When the "Run" button is clicked, retrieves the target domain and selected record types from the GUI.
*   **Calls `query_dns`:** Calls the `query_dns` function from `query.py` to perform the DNS queries.
*   **Result Display:** Formats the results or error messages and displays them in the output area of the GUI.

## Examples

1. Run `python3 dnspy_gui.py`.
2. A GUI will appear.
3. Type `google.com` in the text box.
4. Click on the A, AAAA and MX check box.
5. Click the Run button.
6. Wait for the results.
7. Repeat with `microsoft.com`.
8. Check the verbose box.
9. Run.
