import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from io import StringIO
from tabulate import tabulate
import csv

data_set = pd.read_csv('data2.csv')
#data_set = pd.read_csv('data2.csv')
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
df = pd.DataFrame(te_result, columns= te.columns_).head(10)
print(tabulate(df.head(5), headers='keys', tablefmt='fancy_grid'))
#print(tabulate(df, headers='keys', tablefmt='fancy_grid'))




itemset = apriori(df, min_support=0.1, use_colnames=True)
itemset
print(itemset,'\n')
print('3-2. 지지도(support)를 구하는 법  \n')
# 데이터프레임을 통해 나온 표를 가지고 구한다. 
#print(df.sum(),'\n')
print('지지도(support)를 구하는 공식 support(X) = count(X) / N =>  지지도 =  아이템X의 거래건수 / 전체 거래건수')
print(df.sum(),' \n support : \n ',df.sum()/8 )

# 총 케이스는 8건이라는 데이터를 사용한다.
# 녹차라뗴, 아메리카노를 예시로 한번 계산해보자 
# 1. 지지도(녹차라떼 -> 아메리카노 ) ? 녹차라떼와 아메리카노를 동시에 구매할 확률 ( 결합 확률 ) supoort
# 총 8건의 케이스 중, 녹차라뗴 + 아메리카노 조합은 2건  => 2/8 => 0.250
# 2. 신뢰도(녹차라떼 -> 아메리카노 ) ? 녹차라뗴를 구매할 때, 아메리카노도 같이 구매할 확률 ( 조건부 확률 ) confidence 
# 총 2건의 케이스 중, 녹차라떼 + 아메리카노 조합은 2건 => 2/2 => 1.0  (녹차라떼가 주가 된다는 생각을 해야함) 
# 3. 향상도(녹차라뗴 -> 아메리카노 ) ? 녹차라떼와 아메리카노로 생성된 규칙이 효용가치가 있는지를 나타내는 척도  lift
# 여기가 겁~나 헷갈린다.  Lift(X,Y) = c( X -> Y) / s(Y) 이므로 분모가 되는 support : Y 즉, 아메리카노에 대한 support를 넣어야 한다.
# Lift(X,Y) =  1 / 아메리카노의 Support (0.875) = 1.14286 


from mlxtend.frequent_patterns import association_rules

# association_rules(itemset, metric="confidence", min_threshold=0.5)
rules = association_rules(itemset, metric="confidence", min_threshold=0.5)
rules["antecedents"] = rules["antecedents"].apply(lambda x: list(x)[0]).astype("unicode")
rules["consequents"] = rules["consequents"].apply(lambda x: list(x)).astype("unicode")

print('4. apriori 알고리즘 사용해서 정리하기  \n')
print(rules)
print(association_rules(itemset, metric="confidence", min_threshold=0.5))
# df = association_rules(itemset, metric="confidence", min_threshold=0.5)
# df.to_csv('soogeunjung.csv', index=False, encoding='cp949')


# test= rules[rules['antecedents'] == frozenset(('702056', '251002'))]
rules = rules[['antecedents', 'consequents', 'support']]  # 컬럼명 추려서 표시하기
# print('data \n', test)
test = rules[rules.antecedents.apply(lambda x: '702037' in x )] # 특정 조건으로만 추출하기
print('data2 \n' ,rules)
print('data3 \n' , test)

test.to_csv('soogeunjung.csv', index=False, encoding='cp949')



# 특정한 컬럼만 뽑는다.
# rules = rules[rules.antecedents.apply(str).str.contains("702051")].sort_values('lift', ascending=True)
#print(tabulate(rules, headers='keys', tablefmt='fancy_grid'))

#
# association_rules_df = association_rules(itemset,
#                                          metric='confidence',
#                                          min_threshold=0.005,
#                                         )
#
# all_confidences = []
# collective_strengths = []
# cosine_similarities = []
# for _,row in association_rules_df.iterrows():
#     all_confidence_if = list(row['consequents'])[0]
#     # print( " all_confidence_if >> " , all_confidence_if)
#     all_confidences.append(all_confidence_if)
#
# data = rules
# data.to_csv('soogeunjung.csv')
#
# # data = all_confidences
# # data.to_csv('tset.csv')
#
# # csv파일로 적기 # newline 설정을 안하면 한줄마다 공백있는 줄이 생긴다.
# with open('listfile.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(all_confidences)

#df = association_rules(itemset, metric="confidence", min_threshold=0.1)
#df.to_csv('soogeunjung.csv', index=False, encoding='cp949')
#print(tabulate(association_rules(itemset, metric="confidence", min_threshold=0.8), headers='keys', tablefmt='fancy_grid'))