#抓取網頁原始碼
import urllib.request as req
url = "https://bds.oia.ntnu.edu.tw/istudent/OE/exchange-programs"
request = req.Reqest(url, headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response :
    data = response.read().decode("utf-8")
print(data)