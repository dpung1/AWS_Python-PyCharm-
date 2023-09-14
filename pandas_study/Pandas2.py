import pandas as pd
import numpy as np

##########[ CSV 파일 불러오기(Pandas) ]##########
data = pd.read_csv("books_data.csv", encoding="euc-kr")
print("\n---------------[ 전체 데이터 ]---------------")
print(data)

print("\n---------------[ 컬럼명 검색 ]---------------")
print(data.columns)

print("\n---------------[ 도서명만 검색 ]---------------")
print(data["도서명"])

print("\n---------------[ 일치하는 도서명 검색 ]---------------")
print(data.loc[data["도서명"] == "퇴사 후 독립출판 책만들기"])

##########[ CSV 파일 불러오기(CSV 라이브러리) ]##########
import csv
print("\n---------------[ 상세 정보 확인 ]---------------")
f = open("books_data.csv", "r", encoding="euc-kr")
print(f)

print("\n---------------[ 객체 확인 ]---------------")
csvData = csv.reader(f)
print(csvData)

print("\n---------------[ 데이터 원하는 수량만 가져오기 ]---------------")
i = 0
for data in csvData:
    if i < 10:
        print(data)
    else:
        break
    i += 1

