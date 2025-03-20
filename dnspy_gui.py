import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import ttk
from query import query_dns as query
import threading
from typing import Dict, List


class DNSpyGUI:
    def __init__(self, master):
        self.master = master
        master.title("DNSpy")

        # Configure grid weights for better responsiveness
        master.grid_columnconfigure(1, weight=1)
        master.grid_rowconfigure(4, weight=1)

        # Create main container frame
        self.main_frame = ttk.Frame(master)
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # Target domain input
        self.target_label = ttk.Label(
            self.main_frame, text="Target Domain:", font="Calibri 12 bold")
        self.target_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.target_entry = ttk.Entry(self.main_frame, width=30)
        self.target_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.target_entry.bind('<Return>', lambda e: self.start_enumeration())

        # Options Frame
        self.options_frame = ttk.LabelFrame(self.main_frame, text="Options")
        self.options_frame.grid(
            row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.options_frame.grid_columnconfigure(1, weight=1)

        # Verbose Output Checkbox
        self.verbose_var = tk.BooleanVar()
        self.verbose_var.set(False)
        self.verbose_checkbox = ttk.Checkbutton(
            self.options_frame, text="Verbose Output", variable=self.verbose_var
        )
        self.verbose_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.create_tooltip(self.verbose_checkbox,
                            "Show detailed query information")

        # Record Types Checkboxes
        self.record_types_label = ttk.Label(
            self.options_frame, text="Record Types:", font="Calibri 10")
        self.record_types_label.grid(
            row=1, column=0, padx=5, pady=5, sticky="w")

        self.record_types = ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SOA"]
        self.record_vars: Dict[str, tk.BooleanVar] = {}

        # Create a frame for record checkboxes
        self.records_frame = ttk.Frame(self.options_frame)
        self.records_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        for i, record in enumerate(self.record_types):
            self.record_vars[record] = tk.BooleanVar()
            self.record_vars[record].set(True)
            checkbox = ttk.Checkbutton(
                self.records_frame,
                text=record,
                variable=self.record_vars[record],
            )
            checkbox.grid(row=i // 4, column=i % 4, padx=5, pady=2, sticky="w")
            self.create_tooltip(checkbox, f"Query {record} records")

        # Buttons Frame
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.grid(row=3, column=0, columnspan=2, pady=5)

        self.enumerate_button = ttk.Button(
            self.buttons_frame, text="Run (F5)", command=self.start_enumeration
        )
        self.enumerate_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = ttk.Button(
            self.buttons_frame, text="Clear", command=self.clear_output
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            self.main_frame, variable=self.progress_var, maximum=100
        )
        self.progress_bar.grid(
            row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Output text area
        self.output_text = scrolledtext.ScrolledText(
            self.main_frame, wrap=tk.WORD, width=60, height=20
        )
        self.output_text.grid(row=5, column=0, columnspan=2,
                              padx=5, pady=5, sticky="nsew")
        self.output_text.config(state=tk.DISABLED)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(
            self.main_frame, textvariable=self.status_var, relief=tk.SUNKEN
        )
        self.status_bar.grid(row=6, column=0, columnspan=2,
                             sticky="ew", padx=5, pady=2)

        # Bind keyboard shortcuts
        self.master.bind('<F5>', lambda e: self.start_enumeration())
        self.master.bind('<Control-l>', lambda e: self.clear_output())

        # Initialize state
        self.is_running = False

    def create_tooltip(self, widget: tk.Widget, text: str) -> None:
        """Create a tooltip for a widget."""
        def show_tooltip(event=None):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")

            label = ttk.Label(
                tooltip, text=text, background="#ffffe0", relief=tk.SOLID, borderwidth=1
            )
            label.pack()

            def hide_tooltip():
                tooltip.destroy()

            tooltip.bind('<Leave>', lambda e: hide_tooltip())
            widget.bind('<Leave>', lambda e: hide_tooltip())

        widget.bind('<Enter>', show_tooltip)

    def clear_output(self) -> None:
        """Clear the output text area."""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.status_var.set("Ready")

    def start_enumeration(self) -> None:
        """Start the DNS enumeration process."""
        if self.is_running:
            return

        target = self.target_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a target domain.")
            return

        self.is_running = True
        self.clear_output()
        self.update_output(f"Starting DNS Enumeration for {target}\n")
        self.enumerate_button.config(state=tk.DISABLED)
        self.progress_var.set(0)
        self.status_var.set("Running queries...")

        # Run enumeration in a separate thread
        threading.Thread(target=self.run_enumeration,
                         args=(target,), daemon=True).start()

    def run_enumeration(self, target: str) -> None:
        """Run the DNS enumeration process."""
        try:
            selected_records = [
                record for record, var in self.record_vars.items() if var.get()
            ]

            if not selected_records:
                self.update_output("No record types selected.")
                return

            total_records = len(selected_records)
            for i, record in enumerate(selected_records, 1):
                if self.verbose_var.get():
                    self.update_output(f"Querying {record} records...")

                try:
                    data = query(target, record)
                    if not data:
                        if self.verbose_var.get():
                            self.update_output(
                                f"No records found for {record}")
                    else:
                        self.update_output(f"\n{record} Records:")
                        for item in data:
                            self.update_output(f"  {item}")
                except Exception as e:
                    self.update_output(
                        f"Error querying {record} records: {str(e)}")

                self.progress_var.set((i / total_records) * 100)
                self.status_var.set(
                    f"Processed {i}/{total_records} record types")

        except Exception as e:
            self.update_output(f"An error occurred: {str(e)}")
        finally:
            self.is_running = False
            self.enumerate_button.config(state=tk.NORMAL)
            self.status_var.set("Ready")
            self.progress_var.set(0)

    def update_output(self, message: str) -> None:
        """Update the output text area with a new message."""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.config(state=tk.DISABLED)
        self.output_text.see(tk.END)


def main():
    root = tk.Tk()
    root.title("DNSpy")
    root.geometry("800x600")
    gui = DNSpyGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
