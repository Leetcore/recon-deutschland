import requests
import json

print("Search term:")
search_term = input()

if search_term.isdigit():
    print("Search for ASN")
    # https://api.bgpview.io/asn/199880/prefixes
    response = requests.get(f"https://api.bgpview.io/asn/{search_term}/prefixes")
    if response.status_code != 200:
        exit()
else:
    # https://api.bgpview.io/search?query_term=digitalocean
    response = requests.get(f"https://api.bgpview.io/search?query_term={search_term}")
    if response.status_code != 200:
        exit()

result = json.loads(response.content)
output: list[dict[str, str]] = []
status = result['status']

if status == 'ok':
    data = result['data']
    if data:
        prefixes = data['ipv4_prefixes']
        for ip_result in prefixes:
            if ip_result['country_code'] == "DE":
                ip = ip_result['ip']
                prefix = ip_result['prefix']
                name = ip_result['name']
                description = ip_result['description']

                item = {}
                item['ip'] = ip
                item['prefix'] = prefix
                item['name'] = name
                item['description'] = description
                output.append(item)
                print(item)
        print("Save results? yes/no")
        save = input()
        if save == "yes":
            print("Filename as CSV:")
            filename = input()
            with open(filename, 'w') as f:
                file_output: list[str] = []
                for output_item in output:
                    output_write: list[str] = []
                    for key, value in output_item.items():
                        output_write.append(str(value))
                    file_output.append(", ".join(output_write) + "\n")
                f.writelines(file_output)