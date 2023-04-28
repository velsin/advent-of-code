# import re
from typing import Any, Dict, Iterable, List

filepath = "./data/day07.txt"


# Read the input from file
def read_input(path: str) -> List[str]:
    with open(path) as f:
        input_lines = f.read().split("\n")
    return input_lines


# Parse the input list into a nested dict data structure
def parse_input(input_lines: List[str]) -> Dict[str, Any]:
    # Create the root folder and keep track of current path
    file_system = {}
    current_path = []

    for line in input_lines:
        if line.startswith("$"):
            # since args can be 0 or more we catch all
            command, *args = line[2:].split()
            # We don't need to do anything when the command is 'ls' since the infor needed is going
            # to appear on the next lines.
            if command == "cd":
                target_dir = args[0]

                match target_dir:
                    case "/":
                        current_path = []
                    case "..":
                        current_path.pop()
                    case _:
                        current_path.append(target_dir)

        elif line.startswith("dir"):
            # We need to create a subdictionary at our current location for the directory
            folder_name = line[4:]

            # set a pointer at root and traverse location
            ptr = file_system
            for folder in current_path:
                ptr = ptr[folder]

            ptr[folder_name] = {}

        else:
            # If it's not a command or a directory, then create a file at current location
            file_size, file_name = line.split()

            # set a pointer at root and traverse location
            ptr = file_system
            for folder in current_path:
                ptr = ptr[folder]

            ptr[file_name] = int(file_size)

    return file_system


def get_size(ptr: Any, path: List[str], results: Dict[str, int]) -> int:
    if existing_size := results.get("/".join(path)):
        return existing_size

    if isinstance(ptr, dict):
        results["/".join(path)] = sum(
            [get_size(ptr[key], path + [key], results) for key in ptr.keys()]
        )
        return results["/".join(path)]

    else:
        return ptr


def directory_sum(file_system: Dict[str, Any], size_limit: int) -> Dict[str, int]:
    # Travel recursively down the file system and get the sizes of every directory, return those
    # within limit

    folder_sizes = {}
    path = []

    # get the file sizes recursively, unpleasant function since it primarily mutates the dict to
    # get result
    get_size(file_system, path, folder_sizes)

    # iterate through the saved folder sizes and get the result

    res = sum([value for value in folder_sizes.values() if value <= size_limit])
    return res


print(directory_sum(file_system=parse_input(read_input(filepath)), size_limit=100000))
