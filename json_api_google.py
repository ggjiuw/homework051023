import json
import requests


url = 'https://script.googleusercontent.com/macros/echo?user_content_key=6UqqJlqhXRB3t9I9UbzUryw2FXeLhvQS8_tjbbLQbMRGMoUvZZQ5xtDI_KbcgRwWv4Owoceo8Jd0zjvRLJP7kLiVyOypIFGam5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnOR8jsPZSYeAcj4w9rCMPYZpyQfjxt9FTrhvZE4B-g6ZhOMRYA1Pk_JohCJrhzlHnCusAfKPmohxr9Ljjvp9hyNAZYHaRiIttg&lib=MvOR8-gJfQC4LBGr_gYUOmQSW3VxzywJF'

params = {
    'limit': 30000,
    'skip': 0,
}
response = requests.get(url=url, params=params).json()

with open('google_api.json', mode='w', encoding='utf-8') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)


some_list = [1.0, 2, 3, 4, 5, 6.0001, 7, 8, 255.47, 123.12444, 151, 0.11, 10.02]

result = list(map(str, some_list))
print(result)


def is_int(num):
    return type(num) is int


result = list(filter(is_int, some_list))
print(result)
