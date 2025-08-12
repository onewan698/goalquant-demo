def fetch_odds():
    url = "https://example.com/odds"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # 解析赔率数据
    return [{"match": "A vs B", "odds": [1.8, 2.0, 1.9]}]
