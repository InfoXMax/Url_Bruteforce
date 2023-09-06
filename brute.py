import requests
# Function to display the banner
def display_banner():
    banner = """
     _____        __    __   ____  __            
    |_   _|      / _|   \ \ / /  \/  |           
      | |  _ __ | |_ ___ \ V /| \  / | __ ___  __
      | | | '_ \|  _/ _ \ > < | |\/| |/ _` \ \/ /
     _| |_| | | | || (_) / . \| |  | | (_| |>  < 
    |_____|_| |_|_| \___/_/ \_\_|  |_|\__,_/_/\_\
                                                 
                                                 """
    print(banner)
# Function to check if a directory or file exists
def check_existence(base_url, directory):
    url = f"{base_url}/{directory}"
    response = requests.get(url)
    if response.status_code == 200:
        return f"Found 200 OK: {url}"
    else:
        return f"Not Found: {url}"

# Function to perform directory and file enumeration
def enumerate_directories(base_url, wordlist):
    results = []
    with open(wordlist, 'r') as f:
        for line in f:
            directory = line.strip()
            result = check_existence(base_url, directory)
            results.append(result)
            print(result)
    return results

# Function to save only the "Found 200 OK" results to a text file
def save_results_to_file(results):
    found_results = [result for result in results if "Found 200 OK" in result]
    if found_results:
        with open("results.txt", 'w') as f:
            for result in found_results:
                f.write(result + '\n')
        print("Results saved to 'results.txt'.")
    else:
        print("No 'Found 200 OK' results to save.")

# Main function
def main():
    display_banner()

    url = input("Enter the target URL: ")
    wordlist = input("Enter the path to the wordlist text file: ")
    
    results = enumerate_directories(url, wordlist)
    
    save = input("Do you want to save the 'Found 200 OK' results to a text file? (yes/no): ")
    if save.lower() == "yes":
        save_results_to_file(results)

if __name__ == "__main__":
    main()
