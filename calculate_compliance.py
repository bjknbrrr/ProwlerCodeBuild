
import json
import sys

def calculate_cis_compliance(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    total_checks = 0
    passed_checks = 0

    for item in data:
        if 'CIS' in item['GROUP_TITLE']:
            total_checks += 1
            if item['RESULT'] == 'PASS':
                passed_checks += 1

    if total_checks > 0:
        return round((passed_checks / total_checks) * 100, 2)
    else:
        return 0

if __name__ == "__main__":
    compliance_percentage = calculate_cis_compliance(sys.argv[1])
    print(compliance_percentage)
