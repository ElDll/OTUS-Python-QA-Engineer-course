import json
import os
import re
import glob
import sys

regex = "^(?P<ip>\S*).*\[(?P<date>.*)\]\s\"(?P<method>\S*)\s(?P<path>\S*)\s(?P<request_version>[^\"].*)\"\s(?P<status_code>\S*)\s(?P<bytes>\S*)\s\"(?P<url>[^\"]*|.*)\"\s\"(?P<user_agent>.*)\"\s(?P<time>[0-9].*)$"


def get_top_3(collection: dict):
    final_dict = {}
    for i in range(3):
        maximum = max(collection, key=collection.get)
        final_dict[maximum] = collection[maximum]
        del collection[maximum]
    return final_dict


for path in glob.glob(sys.argv[1] + '\\*.log'):
    request_count = 0
    methods = {'GET': 0, 'HEAD': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0, 'CONNECT': 0, 'OPTIONS': 0, 'TRACE': 0}
    ip_addresses = {}
    requests_dict = {}
    file_name = '\\'.join(path.split('\\')[-1:])
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            request_count += 1
            matches = re.match(regex, line.strip())
            ip_addresses[matches.group('ip')] = 0
            requests_dict[matches.group('method') + " " +
                          matches.group('url') + " " +
                          matches.group('ip') + " " +
                          matches.group('time') + " " +
                          matches.group('date')] = int(matches.group('time'))

        for line in lines:
            matches = re.match(regex, line.strip())
            ip_addresses[matches.group('ip')] += 1
            for key in methods.keys():
                if key == matches.group('method'):
                    methods[key] += 1
                    break

    report = {"request_count": request_count,
              "http_methods": methods,
              "top_ip_addresses": get_top_3(ip_addresses),
              "top_long_requests": get_top_3(requests_dict)}

    print(file_name + " report\n"
          f"request_count: {request_count}\n"
          f"http_methods: {methods}\n"
          f"top_ip_addresses:\n{report['top_ip_addresses']}\n"
          f"top_long_requests:\n{report['top_long_requests']}\n")

    try:
        dir_name = file_name[:-4] + "_report"
        os.mkdir(dir_name)
    except OSError:
        pass

    with open(dir_name + '\\report.json', 'w') as file:
        file.write(json.dumps(report, indent=4))
