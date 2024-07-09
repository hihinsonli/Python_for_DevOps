import os
import re
import requests

def get_url(fname, regex_pattern):
    result = []
    img_reg_compiled = re.compile(regex_pattern)

    with open(fname) as fobj:
        for line in fobj:
            m = img_reg_compiled.findall(line)
            if m:
                result.extend(m)
    return result

def download_file(url, fname):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(fname, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download file: {response.status_code}")

if __name__ == '__main__':
    path = '/tmp/web_imgs'
    fname = input('Please enter filename to be stored:')
    url = input('Please enter url:')
    if not os.path.exists(path):
        os.mkdir(path)
    file_path = os.path.join(path, fname)
    if not os.path.exists(file_path):
        download_file(url, file_path)
    
    regex_img = r'(http|https:)//[\w.-]+\.(jpg|jpeg|png|gif)'
    img_list = get_url(file_path, regex_img)
    
    for img_url in img_list:
        img_name = os.path.join(path, os.path.basename(img_url))
        download_file(img_url, img_name)
    
    print(f"Downloaded {len(img_list)} images to {path}")
