import requests
import re
print('lấy mã r thì chờ tầm 80s r nhập')
clk = input('enter your clk: ')

response = requests.post(f'https://traffic-user.net/GET_MA.php?codexn=taodeptrai&url=https://bet88ec.com/cach-danh-bai-sam-loc&loai_traffic=https://bet88ec.com/&clk={clk}')

html = response.text

match = re.search(r'<span id="layma_me_vuatraffic"[^>]*>\s*(\d+)\s*</span>', html)
if match:
    code = match.group(1)
    print(f"code: {code}")
else:
    print("ko tìm thấy mã")
