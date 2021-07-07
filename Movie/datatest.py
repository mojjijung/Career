import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from io import StringIO
from tabulate import tabulate

data_set = pd.read_csv('data2.csv')
print('0. CSV에서 제대로 데이터를 불러오는지 테스트','\n')
print(data_set,'\n')

data_frames = pd.DataFrame(data_set)


data_frames['test'] = data_frames.ProductName.str.split('|')
print('1. CSV에서 받아온 데이터 중, 붙여논 컬럼을 다차원배열로 변경 \n')
print(data_frames.test,'\n')

te = TransactionEncoder()
te_result = te.fit(data_frames.test).transform(data_frames.test)
print('2. 다차원배열로 변경한 데이터를 데이터프레임으로 변경  \n')
print(te_result,'\n')

print('3. 데이터프레임으로 변경한 내역을 보기쉽게 정리  \n')
df = pd.DataFrame(te_result, columns= te.columns_)
print(tabulate(df.head(5), headers='keys', tablefmt='fancy_grid'))

itemset = apriori(df, min_support=0.1, use_colnames=True)
itemset
#print(itemset,'\n')

from mlxtend.frequent_patterns import association_rules
association_rules(itemset, metric="confidence", min_threshold=0.1) 

print('4. apriori 알고리즘 사용해서 정리하기  \n')
#print(association_rules(itemset, metric="confidence", min_threshold=0.1) )
print(tabulate(association_rules(itemset, metric="confidence", min_threshold=0.8), headers='keys', tablefmt='fancy_grid'))