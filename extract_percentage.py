import re
import sys

def extract_passed_percentage():
    try:
        with open('prowler_output.txt', 'r') as file:
            content = file.read()
        match = re.search(r'(\d+\.\d+)% \(.*\) Passed', content)
        if match:
            print(match.group(1))
        else:
            print("0")  # Print 0 if no match is found
    except Exception as e:
        print("0")  # Print 0 in case of an error reading the file or running regex
        sys.exit(1)  # Exit with status 1 to indicate failure

if __name__ == "__main__":
    extract_passed_percentage()
