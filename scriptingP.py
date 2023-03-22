import requests
import sys
import re
def main():

    if len(sys.argv) < 2:
        print("No domain provided")
        sys.exit(1)
    else:
        DOMAIN = sys.argv[1]
        print(DOMAIN)

    test=None

    try:
        test = requests.get(f"https://{DOMAIN}")
        if (test.status_code == 404):
            print("Invalid domain entered")
            sys.exit(1)
    except requests.exceptions.RequestException as error:
        print(f"Connection error: {error}")
    except requests.exceptions.HTTPError as error :
        print(f"HTTP Exception occured: {error} of code: ",test.status_code)
    except Exception as error:
        #Do nothing
        print(f"Some other exception occured: {error}")

    if (test.status_code == 404):
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
    with open("output_dirs.bat", "w") as f1:
        for i in valid_dirs:
            f1.write(i, "\n")

    valid_subdomains = []
    for subdomain in subdomains:
        url = f"https://{subdomain}.{DOMAIN}"
        request = requests.get(url)
        if request.status_code == 200:
            print("Found valid url: {url}")
            valid_subdomains.append(url)
    with open("output_subdomains", "w") as f2:
        for i in valid_subdomains:
            f2.write(valid_subdomains, "\n")

    valid_files = getFiles(DOMAIN)
        
def getFiles(DOMAIN):
    files = []
    request = requests.get(f"https://{DOMAIN}")
    html = request.text
    # Use regular expressions to extract all file names from the HTML
    pattern = r'href=["\']?([^"\'>]+)'
    files += re.findall(pattern, html)

    return files

def loadFiles():
    with open("subdomains_dictionary.bat", "r") as f1:
        dirs = f1.read().splitlines()

    with open("dirs_dictionary.bat", "r") as f2:
        subdomains = f2.read().splitlines()

    return dirs, subdomains


def writeFiles(valid_subdomains, valid_dirs, valid_files):
    with open("output_subdomains", "w") as f2:
        f2.write(valid_subdomains, "\n")
    with open("output_files", "w") as f3:
        f3.write(valid_files, "\n")
        

main()
