import argparse
import sys

from collections import Counter
from pathlib import Path
from rich import box
from rich.console import Console
from rich.table import Table
from typing import Dict, List, Tuple

console = Console()

def arg_parser() -> Dict[str, str]:
        parser = argparse.ArgumentParser(description="Parse AJAX logs")
        parser.add_argument("-f", "--file", dest="ajax_file", help="Path to the AJAX log file")
        parser.add_argument("-n", action='store_true', help="Retrieves the next line after 'action'")
        if len(sys.argv) == 1:
                parser.print_help(sys.stderr)
                sys.exit(1)
        return vars(parser.parse_args())

class AjaxLogParser:

        def __init__(self, ajax_file: str):
                self.ajax_file = str(self.get_ajax_file_location(ajax_file))
        
        def get_ajax_file_location(self, ajax_file: str) -> Path:
                """Returns the path to the AJAX file.
                
                Parameters:
                        ajax_file : str
                        The file name of the AJAX file, passed in by the user as an argument during class instantiation.
                        E.g. 'ajax.log'
                Returns:
                        Path: Uses pathlib.Path to return a Path of where the file is located.
                """
                project_directory = Path().cwd()
                return project_directory.joinpath(ajax_file)

        def read_ajax_file(self):
                """Reads the AJAX file and returns a list of the text.

                Returns:
                List of strings
                """
                with open(self.ajax_file, 'r') as f:
                        return f.read().splitlines()

        def filter_results(self, ajax_data) -> List[Tuple[str, str]]:
                """Filters lines containing '[action]' and extracts specific parts of each line.

                Parameters:
                ajax_data (list of str): List of strings representing lines of AJAX data.

                Returns:
                list of tuples: Each tuple contains the first and third parts of the filtered lines.
                """
                return [self.extract_parts(line) for line in ajax_data if '[action]' in line]

        def extract_parts(self, line) -> Tuple[str, str]:
                """Extracts specific parts of a line after stripping whitespace.

                Parameters:
                line (str): A single line of text.

                Returns:
                Tuple: A tuple containing the first and third parts of the line.
                """
                stripped_line = line.strip()
                parts = stripped_line.split(' => ', 1)
                if len(parts) == 2:
                        return parts[0], parts[1]
                return stripped_line, ""

        def count_data(self) -> Counter:
                ajax_data = self.read_ajax_file()
                filtered_results = self.filter_results(ajax_data)
                return Counter(filtered_results)

        def get_most_common(self) -> List[Tuple[Tuple[str, str], int]]:
                """Returns the 10 most common AJAX calls.
                
                Returns:
                List[Tuple[Tuple[str, str], int]] a list of tuples, where each tuple contains a tuple of the action name and the count.
                
                For example: [(('[action]', 'heartbeat'), 100)]
                """
                return self.count_data().most_common(n=10)

        def build_table(self) -> Table:
                # Print the results
                ajax_table = Table(title="Admin-AJAX Calls", box=box.ROUNDED)
                ajax_table.add_column("Count", justify="left")
                ajax_table.add_column("Action Name", justify="left")
                return ajax_table

        def display_results(self, top_results: List[Tuple[str, str]]) -> Table:
                ajax_table = self.build_table()
                for line, count in top_results:
                        ajax_table.add_row(f"{count}", line[1])
                return ajax_table

def main():
        args = arg_parser()
        ajax_file = args['ajax_file']
        ajax_parser = AjaxLogParser(ajax_file)
        top_results = ajax_parser.get_most_common()
        ajax_table = ajax_parser.display_results(top_results=top_results)
        print()
        console.print(ajax_table)

if __name__ == "__main__":
        main()
