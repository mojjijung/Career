import pandas as pd
import numpy as np


dataset = [
	['JAVA개발자', 'React개발자'],
	['React개발자', 'JAVA개발자', 'Vue개발자'],
	['AI Dev', 'JAVA개발자'],
	['블록체인', 'React개발자', 'JAVA개발자'],
	['Spring Boot', 'JAVA개발자'],
	['JAVA개발자', 'React개발자'],
	['JPA', 'JAVA개발자'],
	['JAVA개발자'],
	['Spring Boot', 'React개발자'],
    ['JAVA개발자', 'React개발자' ,'JPA'],
    ['JAVA개발자', 'AI Dev'],
    ['블록체인', 'React개발자'],
    ['Spring Boot', 'JAVA개발자','JPA'],
]

col= ['블록체인', 'AI Dev' ,'JAVA개발자' ,'JPA', 'React개발자' , 'Spring Boot', 'Vue개발자']

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

te = TransactionEncoder()
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
