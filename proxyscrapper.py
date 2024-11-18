import requests
import time

def fetch_and_save_proxies():
    """Fetches proxies from the API and saves them to 'proxies.txt'."""
    api_url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=text"
    
    try:
        # Fetch proxies from the API
        response = requests.get(api_url, stream=True)

        # Check if the response is successful
        if response.status_code == 200:
            proxies = response.text.strip().splitlines()

            # Save proxies to proxies.txt
            if proxies:
                with open('proxies.txt', 'w') as f:
                    f.writelines([proxy + '\n' for proxy in proxies])
                print(f"Fetched and saved {len(proxies)} proxies to 'proxies.txt'.")
            else:
                print("No proxies found from the API.")
        else:
            print(f"Failed to fetch proxies. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error fetching proxies: {e}")

def main():
    print("The script will now run every  8 hours.")

    while True:
        # Run the function to fetch and save proxies
        fetch_and_save_proxies()

        # Wait for 3 hours before restarting
        print("Restarting the script in 8 hours...")
        time.sleep(28800)  # Wait for 8 hours

if __name__ == "__main__":
    main()

__import__('sys').exit()
