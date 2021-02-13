<template>
  <div>
    <div class="">
      <h2 style="color:#39f5c6">교육용 요금제</h2>
      <p>학교인정 교육시설, 도서관, 박물관 등에서 사용되는 전기 요금제</p>
    </div>

    <div>
      <br> <h4 class='payment'>교육용(갑) 요금제</h4>
       <img src="@/assets/1.png" style="max-width: 110%; height: auto;" alt="slide">
    </div>

     <div>
     <br> <br> <h4 class='payment'>교육용(을) 요금제</h4>
       <img src="@/assets/2.png" style="max-width: 110%; height: auto;" alt="slide">
    </div>

     <div>
     <br> <br><h4 class='payment'>계절별 시간대별 구분</h4>
       <img src="@/assets/3.png" style="max-width: 110%; height: auto;" alt="slide">
    </div>

  </div>
</template>

<script>
export default {
}
</script>

<style lang="css" scoped>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Jua&family=Nanum+Brush+Script&family=Sunflower:wght@300&display=swap');
@font-face {
    font-family: 'BMDOHYEON';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMDOHYEON.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
@import url(//fonts.googleapis.com/earlyaccess/hanna.css);
.hanna * {
    font-family: 'Hanna', fantasy;
}

img{
  margin: 30px 30px 0 50px;
  width: 800px;
}
h3{
  margin-left: 30px;
  font-family: 'Hanna', fantasy;
  font-size: 35px;
  letter-spacing: 2.5px;
}
.payment{
  margin-left: 40px;
  /* font-family: 'Noto Sans KR', sans-serif; */
  font-family: 'Hanna', fantasy;
  /* font-family: 'Jua', sans-serif;  */
  /* color: #c4bfbf; */
  font-size: 27px;
  letter-spacing: 1px;
}
</style>
