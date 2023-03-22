import requests
import sys

def main():

    if len(sys.argv) < 2:
        print("No domain provided")
    else:
        DOMAIN = sys.argv[1]

    test = requests.get("https://{DOMAIN}")
    if test.status_code == 404:
        print("Invalid domain entered")
        sys.exit(1)
    
    dirs, subdomains = loadFiles()

    valid_dirs = []
    for dir in dirs:
        url = f"https://{DOMAIN}/{dir}"
        request = requests.get(url)
        if request.status_code == 200:
            print(f"Found valid url: {url}")
            valid_dirs.append(url)

    valid_subdomains = []
    for subdomain in subdomains:
        url = f"https://{subdomain}.{DOMAIN}"
        request = requests.get(url)
        if request.status_code == 200:
            print("Found valid url: {url}")
            valid_subdomains.append(url)

    valid_files = getFiles(DOMAIN)

    
        
        
def getFiles(DOMAIN):
    files = []
    request = requests.get(f"https://{DOMAIN}")
    html = request.text
    # REGEX
    
    return files

def loadFiles():

    with open("subdomains_dictionary.bat", "r") as f1:
        dirs = f1.read().splitlines()

    with open("dirs_dictionary.bat", "r") as f2:
        subdomains = f2.read().splitlines()

    return dirs, subdomains


def writeFiles(valid_subdomains, valid_dirs, valid_files):
    with open("output_dirs.bat", "w") as f1:
        f1.write(valid_dirs, "\n")
    with open("output_subdomains", "w") as f2:
        f2.write(valid_subdomains, "\n")
    with open("output_files", "w") as f3:
        f3.write(valid_files, "\n")