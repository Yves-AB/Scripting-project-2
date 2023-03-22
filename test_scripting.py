import requests
import sys
import re


def main():
    #if arguments are <2 then there is no domain
    if len(sys.argv) < 2:
        print("No domain provided")
        sys.exit(1)
    else:
        DOMAIN = sys.argv[1]
        print(DOMAIN)

    try:
        test = requests.get(f"https://{DOMAIN}")
        if (test.status_code >= 404):
            print("Invalid domain entered")
            sys.exit(1)
    except Exception as error:
        print(f"Some exception occurred: {error}")
        return

    #Load directories and subdomains
    dirs, subdomains = loadFiles()

    valid_dirs = []
    for dir in dirs:
        url = f"https://{DOMAIN}/{dir}"
        request = requests.get(url)
        if request.status_code == 200:
            print(f"Found valid url: {url}")
            valid_dirs.append(url)

    #Create new directory
    with open("output_dirs.bat", "w") as f1:
        for i in valid_dirs:
            f1.write(i + "\n")

    valid_subdomains = []
    for subdomain in subdomains:
        url = f"https://{subdomain}.{DOMAIN}"
        request = requests.get(url)
        if request.status_code == 200:
            print(f"Found valid url: {url}")
            valid_subdomains.append(url)
    #Create new subdomain
    with open("output_subdomains", "w") as f2:
        for i in valid_subdomains:
            f2.write(i + "\n")

    #Load method getFiles() that gets the matching 
    valid_files = getFiles(DOMAIN)
    with open("output_files", "w") as f3:
        for i in valid_files:
            f3.write(i + "\n")

def getFiles(DOMAIN):
    files = []
    request = requests.get(f"https://{DOMAIN}")
    html = request.text
    # Use regular expressions to extract all file names from the HTML
    pattern = r'href\s*=\s*["\']?(.*?)[\'"]'  #From regex in class
    files += re.findall(pattern, html)
    return files

#method to load the files that were sent to us
def loadFiles():
    with open("subdomains_dictionary.bat", "r") as f1:
        dirs = f1.read().splitlines()

    with open("dirs_dictionary.bat", "r") as f2:
        subdomains = f2.read().splitlines()

    return dirs, subdomains

if __name__ == '__main__':
    main()