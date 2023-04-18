import requests
import pandas as pd

# 发送请求
response = requests.get(
    'http://data.stats.gov.cn/english/easyquery.htm',
    params={
        'cn': 'A01',
        'zb': 'A010703',
        'm': 'getOtherWds',
        'dbcode': 'fsnd',
        'wdcode': 'zb',
        'dfwds': '[{"wdcode":"reg","valuecode":"110000"}]',
        'k1': '1618759343038',
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }, verify=False)

# 解析数据为 DataFrame
import pdb; pdb.set_trace()
json_data = response.json()
df = pd.DataFrame(json_data['returndata']['datanodes'])

# 处理 DataFrame
df[['data_year', 'data_month']] = pd.DataFrame(
    df['code'].str.split('.').tolist(),
    index=df.index)
df['data_year'] = df['data_year'].astype(int)
df['data_month'] = df['data_month'].astype(int)
df['data'] = df['data'].astype(float)

# 查看 DataFrame
print(df.head())

