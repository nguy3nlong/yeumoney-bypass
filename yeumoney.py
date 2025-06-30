import requests
import re
print('lấy mã r thì chờ tầm 80s r nhập')
clk = input('enter your clk: ')
type = input('enter quest type: ')

if type == 'm88':
    response = requests.post(f'https://traffic-user.net/GET_MA.php?codexn=taodeptrai&url=https://bet88ec.com/cach-danh-bai-sam-loc&loai_traffic=https://bet88ec.com/&clk={clk}')
    html = response.text
    match = re.search(r'<span id="layma_me_vuatraffic"[^>]*>\s*(\d+)\s*</span>', html)
    if match:
        code = match.group(1)
        print(f"code: {code}")
    else:
        print("ko tìm thấy mã")

elif type == 'fb88':
    response = requests.post(f'https://traffic-user.net/GET_MA.php?codexn=taodeptrai&url=https://fb88mg.com/ty-le-cuoc-hong-kong-la-gi&loai_traffic=https://fb88mg.com/&clk={clk}')
    html = response.text
    match = re.search(r'<span id="layma_me_vuatraffic"[^>]*>\s*(\d+)\s*</span>', html)
    if match:
        code = match.group(1)
        print(f"code: {code}")
    else:
        print("ko tìm thấy mã")

elif type == '188bet':
    response = requests.post(f'https://traffic-user.net/GET_MA.php?codexn=taodeptrailamnhe&url=https://88betag.com/cach-choi-game-bai-pok-deng&loai_traffic=https://88betag.com/&clk={clk}')
    html = response.text
    match = re.search(r'<span id="layma_me_vuatraffic"[^>]*>\s*(\d+)\s*</span>', html)
    if match:
        code = match.group(1)
        print(f"code: {code}")
    else:
        print("ko tìm thấy mã")

elif type == 'w88':
    response = requests.post(f'https://traffic-user.net/GET_MA.php?codexn=taodeptrai&url=https://188.166.185.213/tim-hieu-khai-niem-3-bet-trong-poker-la-gi&loai_traffic=https://188.166.185.213/&clk={clk}')
    html = response.text
    match = re.search(r'<span id="layma_me_vuatraffic"[^>]*>\s*(\d+)\s*</span>', html)
    if match:
        code = match.group(1)
        print(f"code: {code}")
    else:
        print("ko tìm thấy mã")

