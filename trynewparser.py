from fake_useragent import UserAgent
import requests
import json

ua = UserAgent()

def collect_data():
    cnt = 2
    response = requests.get(
        url='https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=100&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap',
        headers={'user-agent': f'{ua.random}'}
    )

    with open('result.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

    with open('result.json') as file:
        data = json.load(file)

    for token in data['data']['cryptoCurrencyList']:
        print('Name:', token['name'], end='\n')

        if round(token['quotes'][2]['price'], 4) == 0:
            res = '{:.8f}'.format(token['quotes'][2]['price'])
            print('Price:', res, end='')

        elif int(token['quotes'][2]['price']) == 0:
            for i in range(2, 5, 2):
                if round(token['quotes'][2]['price'], i) == 0:
                    continue
                else:
                    print('Price:', round(token['quotes'][2]['price'], i), end='')
                    break
        else:
            print('Price:', round(token['quotes'][2]['price'], 2), end='')
        print('$')
        print('Link:', 'https://coinmarketcap.com/currencies/', end='')
        print(token['slug'])
        print()


def main():
    collect_data()


if __name__ == '__main__':
    main()
