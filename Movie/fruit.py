import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

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

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_) #위에서 나온걸 보기 좋게 데이터프레임으로 변경

print(df)