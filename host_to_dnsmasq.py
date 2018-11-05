import re
import sys

import requests

exclude_domains = ['localhost', 'XiaoQiang', 'broadcasthost']


def main(output_path):
    host_file_url = 'https://raw.githubusercontent.com/vokins/yhosts/master/hosts.txt'

    print("host file url is %s" % host_file_url)
    resp = requests.get(host_file_url)
    lines = resp.text.splitlines()

    with open(output_path, 'w+') as f:
        for line in lines:
            line_content = line.strip()
            match_result = re.search(r"^\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line_content)
            if match_result is None:
                continue
            ip_and_domain = line_content.split()
            domain = ip_and_domain[1]
            if domain in exclude_domains:
                continue

            dnsmasq_str = "address=/{}/{}\n".format(domain, ip_and_domain[0])
            f.writelines(dnsmasq_str)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please specify output file path...")
    main(sys.argv[1])
