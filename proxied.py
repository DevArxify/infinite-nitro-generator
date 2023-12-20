import requests

url = 'https://api.discord.gx.games/v1/direct-fulfillment'
data = '{"partnerUserId":"bc385c68-be5f-43c2-9713-cb2051fef65b"}'  # Raw JSON data

headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
}

with open('proxies.txt', 'r') as file:
    proxies = [line.strip() for line in file if line.strip()]

while True:
    for proxy in proxies:
        try:
            response = requests.post(url, headers=headers, proxies={'http': proxy, 'https': proxy}, data=data, timeout=5)
            response_json = response.json()
            
            token = response_json.get('token')
            
            if token:
                link_with_token = f'https://discord.com/billing/partner-promotions/1180231712274387115/{token}'
                print(f"new code saved to output.txt")
                with open('output.txt', 'a') as output_file:
                    output_file.write(f'{link_with_token}\n')
        except Exception as e:
            print(f"Proxy {proxy} - Error: {e}")
