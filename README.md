# Capstone Design

🥇 소프트웨어 융합대학 창의설계경진대회 최우수상
🥉 교내 창의설계경진대회 동상

[![GitHub license](https://img.shields.io/github/license/lkhoony/EV-obseoye?style=plastic)](https://github.com/lkhoony/Capstone)

세종대학교 교내 전력 사용량 예측을 통한 경제성 분석 및 삼중 열 병합 발전(CCHP) 스케줄링 웹 어플리케이션  

  - 전력 사용량 패턴 및 전력 사용 요금 분석
  - 예측 모델을 활용한 전력 사용량 예측 및 CCHP 발전 스케줄링
  - CCHP 발전으로 발생하는 경제적 이득 분석
  - 
![image](https://user-images.githubusercontent.com/66773320/107849755-c068fb80-6e40-11eb-8475-4122243225ef.png)

![image](https://user-images.githubusercontent.com/66773320/107849774-daa2d980-6e40-11eb-9459-2650928c52c7.png)

### Tech

* Vue.js - 사용자의 요청 및 데이터를 API 서버에 전송 및 그래프 시각화
* Flask - Front End에서의 요청을 받아 그래프를 전송하는 API 구현
* MySQL - 전력 사용량 데이터 저장을 위한 DBMS
* Sklearn - 전력 사용량 예측 모델 개발을 위한 라이브러리
* Plotly - 데이터 시각화 라이브러리
* Docker - 개발 환경 구축 및 배포

### Development
Open your favorite Terminal and run these commands.

First Tab:
```sh
cd frontend
npm run serve
```

Second Tab:
```sh
cd backend
python "app.py"
```

### Docker

또한 아래의 명령어를 실행하여 docker-compose.yml 파일을 읽어 개발환경을 구축하고 웹 앱과 API 서버 컨테이너를 실행할 수 있다.

```sh
cd capstone
docker-compose up -d
```

### Todos

 - 회원 가입 시 전력 사용량 데이터 입력받아 예측 모델 생성

License
----

MIT


**Free Software, Hell Yeah!**
