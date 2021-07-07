import pandas as pd
import numpy as np

dataset = [
	['아메리카노', '카페라떼'],
	['카페라떼', '아메리카노', '카푸치노'],
	['바닐라라떼', '아메리카노'],
	['녹차라떼', '카페라떼', '아메리카노'],
	['카페모카', '아메리카노'],
	['아메리카노', '카페라떼'],
	['초콜릿', '아메리카노'],
	['아메리카노'],
	['카페모카', '카페라떼'],
    ['아메리카노', '카페라떼' ,'초콜릿'],
    ['아메리카노', '바닐라라떼'],
    ['녹차라떼', '카페라떼'],
    ['카페모카', '아메리카노','초콜릿'],
    
]

col= ['녹차라떼', '바닐라라떼' ,'아메리카노' ,'초콜릿', '카페라떼' , '카페모카', '카푸치노']

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

te = TransactionEncoder()
test = te.transform(dataset)
print(test)

te_result = te.fit(dataset).transform(dataset)


#print(te_result)

#df = pd.Dataframe(te_result).add_prefix('col')
df = pd.DataFrame(te_result, columns=col)

print(df)

itemset = apriori(df, use_colnames=True)


itemset = apriori(df, min_support=0.1, use_colnames=True)
itemset
print(itemset)



from mlxtend.frequent_patterns import association_rules
association_rules(itemset, metric="confidence", min_threshold=0.1) 
print(association_rules(itemset, metric="confidence", min_threshold=0.1))
