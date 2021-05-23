# Document Recommendaion system
<br>

## Prerequisites
* python 3.8+
* sklearn
* selenium, bs4
* pandas, numpy
* django
* PostgreSQL
* konlpy

## 개요
* NLP(konlpy), 코사인 유사도를 기반으로 한 문서 유사도 검색 프로그램
* 단어 수준의 방법론 이용<br><br>

## TF-IDF (Term Frequency-Inverse Document Frequency)
<img src="https://user-images.githubusercontent.com/77797199/119271052-c4c06400-bc3a-11eb-9f1d-1f630571ac45.PNG" width="700">
단어의 빈도와 역 문서 빈도(문서의 빈도에 특정 식을 취함)를 사용하여 DTM 내의 각 단어들마다 중요한 정도를 가중치 배정. 주로 문서의 유사도를 구하는 작업, 검색 시스템에서 검색 결과의 중요도를 정하는 작업, 문서 내에서 특정 단어의 중요도를 구하는 작업 등에 사용됨.<br><br>

## Cosine Similarity
<img width="350" alt="다운로드" src="https://user-images.githubusercontent.com/77797199/119271283-deae7680-bc3b-11eb-8bf7-e284d9c61af4.png">
어떤 차원 공간내에 분포된 데이터에 대하여 인근에 위치한 데이터들끼리의 군집화(Clustering)를 시행할 때 이용되는 방법 중 하나.  

## konlpy
<br><br>

## References
> https://wikidocs.net/92961<br>
> https://wikidocs.net/31698<br>
> https://wikidocs.net/21698<br>
> https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/04/20/docsim/<br>

## Work
![캡처](https://user-images.githubusercontent.com/77797199/119270255-c12ade00-bc36-11eb-8a2d-6610eadb5c91.PNG)

+ 웹에서 데이터를 받아와 DB에 저장(default: daum news, 1000 documents)
+ Django 서버 실행
+ Document Recommendation, Search, Top Ranking Word 기능 제공
+ Document Recommendation 기능 최초 실행시, 크롤링한 모든 데이터의 단어(okt.nouns)를 담은 json 파일 생성
+ _크롤링할 웹사이트/문서 주제 선택/tokenizer 선택 기능 제공_(구현예정)
