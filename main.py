import pandas as pd
import requests

def download():
    # 指定文件夹地址
    file_dir = str(input('请输入文件路径，如xxx/xxx/:'))
    save_dir = './runtime'
    # 读取excel文件
    v = pd.read_excel(file_dir,index_col=0)
    # 转化数据为列表
    l = v.values.tolist()
    # 循环下载
    for v in l:
        # 下载文件
        file_url = v[8]
        file_name = v[1]
        print(file_name + ':下载开始')
        file = requests.get(file_url,allow_redirects=True)
        # 保持文件流
        open(f'{save_dir}/{file_name}.pdf','wb').write(file.content)
        print('下载成功')

download()