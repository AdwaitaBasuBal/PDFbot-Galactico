import json
import requests

chat_url = "http://127.0.0.1:8000/response"
summary_url = "http://127.0.0.1:8000/summary"

query = input('Query: ')

while query != 'q':
    if query == 'summary':
        response = requests.get(summary_url)
        print(response.text)

    else:
        params = {"query": f"{query}"}
        response = requests.get(chat_url, params=params)

        try:
            [answer, page_no] = json.loads(response.text)

            print(f'Bot: {answer} ')
            if page_no != 'none':
                print(f'Page: {page_no}')

        except:
            print(json.loads(response.text))
        finally:
            pass

        query = input('Query: ')
