# Document Recommendation system
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
한국어는 영어와 달리 '어근+어미' 형태, '명사+조사' 형태 등 단순 띄어쓰기로는 품사를 구분할 수 없는 경우가 많기에 영어와는 다른 독자적 자연어처리 패키지를 필요로 한다. 이를 위한 패키지 중에서도 꼬꼬마, 한나눔, MeCab-ko 등 국내외에서 개발된 여러 형태소 분석기를 포함하고 있는 한국어 정보처리 패키지인 konlpy를 사용하였다.
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
+ _크롤링할 웹사이트/문서 주제 선택/tokenizer 선택 기능 제공_(미구현)

## Demo
<img src="https://user-images.githubusercontent.com/77797199/119304233-edc80f80-bca1-11eb-9445-bb9d3086cb60.PNG" width="700">

+ 크롤링 데이터가 저장된 DB ; PostgreSQL, paAdmin4


------



<img src="https://user-images.githubusercontent.com/77797199/119304222-e86ac500-bca1-11eb-8d02-89776f22bf88.PNG" width="700">

+ 메인 페이지 ; index, back/next, search<br>
------



<img src="https://user-images.githubusercontent.com/77797199/119304665-8bbbda00-bca2-11eb-9eb5-0dcfb79c62bd.PNG" width="700">
                                                                                                                        
+ Search ERROR: 정상적인 출력 중간에 튀는 값 발생(유사 문서 추천도 동일) 크롤링으로 가져온 값을 PostgreSQL에 저장하는 과정에서 PRIMARY KEY의 값이 (SERIAL 설정에도 불구하고) 중간중간 튀어있는 것이 원인으로 추측됨. SERIAL KEY 오류의 원인은 찾지 못함. CSV 입출력 형식으로 변경할 예정.
                                                                                                                        
------



<img src="https://user-images.githubusercontent.com/77797199/119304241-f02a6980-bca1-11eb-9a9c-4e2e111845c8.PNG" width="350"> <img src="https://user-images.githubusercontent.com/77797199/119304247-f1f42d00-bca1-11eb-87ea-cf8a836dba17.PNG" width="350">

+ 모든 단어에 대한 VOCA 출력 예시
