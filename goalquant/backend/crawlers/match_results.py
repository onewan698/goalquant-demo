import requests
from bs4 import BeautifulSoup

def fetch_results():
    url = "https://example.com/results"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # 解析比赛结果
    return [{"team1": "A", "team2": "B", "score": "2-1"}]
