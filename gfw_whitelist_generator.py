import sys
import requests
import base64

default_whitelist_url = 'https://raw.githubusercontent.com/neko-dev/gfw_whitelist/master/gfw_whitelist.txt'

private_address = [
    '/127\.0\.0\.1/',
    'localhost',
    '/192\.168\.\d+\.\d+/',
    '/10\.0\.0\.\d+/'
]

if __name__ == '__main__':
    whitelist_url = default_whitelist_url
    if len(sys.argv) > 2:
        whitelist_url = sys.argv[1]
    out_path = sys.argv[-1]

    print("Using white list url %s" % whitelist_url)
    resp = requests.get(whitelist_url)
    content = '\n'.join(private_address).encode('utf-8') + resp.content
    base64_content = base64.encodebytes(content).decode('utf-8')
    with open(out_path, 'w+') as f:
        f.writelines(base64_content)
    print('Write to file %s update success!' % out_path)
