<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Text slides with image -->
      <b-carousel-slide

        img-src="https://cdn.pixabay.com/photo/2019/04/30/12/34/smart-4168483_960_720.jpg"
      ><h1>지속가능 사회를 위한 대학 운영, 온실가스 감축을 위한 친환경 교정 구축</h1></b-carousel-slide>

      <!-- Slides with custom text -->
      <b-carousel-slide img-src="https://cdn.pixabay.com/photo/2018/05/11/09/07/technology-3389917_960_720.jpg">
        <h1>미래의 친환경 인재 양성을 위한 친환경 교육 및 연구 실시</h1>
      </b-carousel-slide>

      <!-- Slides with image only -->
      <b-carousel-slide img-src="https://cdn.pixabay.com/photo/2016/03/29/16/49/electricity-1288717_960_720.jpg">
      <h1>대학 및 지역사회에 친환경 문화 전파를 위한 참여 확산</h1></b-carousel-slide>

      <!-- Slides with img slot -->
      <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->

      <!--<b-carousel-slide>
        <template #img>
          <img
            class="d-block img-fluid w-100"
            width="1024"
            height="480"
            src="https://cdn.pixabay.com/photo/2018/05/11/09/07/technology-3389917_960_720.jpg"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>-->
    </b-carousel>


    <div class="Cards">
      <b-card-group deck>
       <card style="width: 20rem;">
         <img slot="image" class="card-img-top" src="@/assets/e2.png" alt="Card image cap" height="100%"/>
            <br><h2 class="card-title">삼천리: 자가열병합 도입효과</h2>
              <h4 class="card-text">기존방식에 비해 에너지종합효율을 약 90%까지 향상시켜 에너지사용량과 온실가스를 줄이는 고효율 에너지절약 시스템입니다.</h4><br>
                <template #footer>
                  <a href="http://www.samchully.co.kr/business/gas/cogeneration.do?p=2" class="btn btn-primary">더 보러가기</a>
                </template>
       </card>

       <card style="width: 20rem;">
        <img slot="image" class="card-img-top" src="@/assets/e1.gif" alt="Card image cap" height="100%"/>
          <br><h2 class="card-title">열병합발전소란 - DS파워(주)</h2>
            <h4 class="card-text">열병합발전이란 열효율 향상을 위해 두 종류의 열 사이클을 조합하여 발전을 하고, 남은 열을 지역 냉·난방, 공업용 스팀 등으로 이용하는 발전소를 말합니다.</h4><br>
              <template #footer>
                <a href="https://www.dspower21.co.kr/area_biz/cogen_plant.aspx" class="btn btn-primary">더 보러가기</a>
              </template>
       </card>

       <card style="width: 20rem;">
        <img slot="image" class="card-img-top" src="@/assets/e3.jpg" alt="Card image cap" height="100%"/>
          <br><h2 class="card-title">집단 에너지 | 한국 에너지 공단</h2>
           <h4 class="card-text">집단에너지공급의 확대를 통해 국가에너지절약 및 기후변화협약에 능동적인 대응을 가능하게 하고 국민생활의 편익증진에 이바지 하는 역활이 큽니다.</h4><br>
            <template #footer>
              <a href="http://www.kemco.or.kr/web/kem_home_new/ener_efficiency/industry_08.asp" class="btn btn-primary">더 보러가기</a>
            </template>
       </card>
      </b-card-group>
    </div>


  </div>
</template>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Sunflower:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Nanum+Brush+Script&display=swap');
@font-face {
    font-family: 'BMDOHYEON';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMDOHYEON.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
  font-family: 'Do Hyeon', sans-serif;
  font-size: 18px;
}
h1{
  text-align: center;
  top: 1000px;
  padding: 0 0 250px 0;
  font-family: 'BMDOHYEON';
  font-size: 30px;
}
.Cards{
  margin: 30px 0 30px 0;
  padding: 10px;
}

.card-title {
font-family: 'Jua', sans-serif;
}
.card-text{
 font-family: 'Jua', sans-serif;
}

</style>

<script>
import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
 export default {
    data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
    }
  }
</script>
