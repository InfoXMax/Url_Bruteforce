# Directory and File URL Brute-Forcing Tool


## Description

This Python script is a simple directory and file brute-forcing tool designed to discover hidden directories and files on a web server during penetration testing and web application security assessments. It allows you to provide a target URL and a wordlist of possible directory and file names to scan. The tool sends requests to the target server and reports any discovered directories or files.

## Features

- Fast and efficient directory and file enumeration.
- Customizable wordlists for scanning.
- Option to save only the "Found 200 OK" results to a text file.
- Display of a banner upon execution.
- Easy-to-use command-line interface.

## Requirements

- Python 3.x
- requests library (install it using `pip`)
     ```bash
  pip install requests

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/directory-bruteforce.git
   cd directory-bruteforce
   python brute.py   
   

Follow the on-screen prompts to input the target URL, wordlist file, and choose whether to save the results.

Example
   ```bash

$ python brute.py

Enter the target URL: https://example.com
Enter the path to the wordlist text file: wordlist.txt

[+] Found 200 OK: https://example.com/admin
[+] Found 200 OK: https://example.com/login
[+] Not Found: https://example.com/backup

Do you want to save the 'Found 200 OK' results to a text file? (yes/no): yes
Results saved to 'results.txt'.

```
## License

This project is licensed under the [MIT License](LICENSE).
