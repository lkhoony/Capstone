<template lang="html">
  <div class="">
   <h3>CCHP의 개념</h3>
   <h4>열병합발전 시스템에서는 연료를 투입하여 가스터빈을 통해 1차로 전력을 생산하고, 배열회수보일러(HRSG)로 폐열을</h4><h4>회수하여 증기터빈으로 보내면,
    증기터빈에서는 회수된 폐열(증기)을 활용하여 전력과 열을 2차로 생산합니다.</h4><h4> 이렇게, 일반 발전 시스템은 전력만을 생산하는 반면,
    열병합발전 시스템은 폐열을 회수하여 재사용하는 단계를 거쳐</h4><h4> 전력과 열을 동시에 생산하기 때문에 에너지 이용 효율을 높이는데 도움을 주는 친환경 시스템입니다.</h4>

   <img src="@/assets/4.png" style="max-width: 100%; height: auto;" alt="slide">
   <img src="@/assets/5.png" style="max-width: 100%; height: auto;" alt="slide">
   <img src="@/assets/6.png" style="max-width: 100%; height: auto;" alt="slide">
   <img src="@/assets/7.png" style="max-width: 100%; height: auto;" alt="slide">
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
h4{
  margin-left: 30px;
  /* font-family: 'Noto Sans KR', sans-serif; */
  font-family: 'Jua', sans-serif;
  font-size: 20px;
  letter-spacing: 1px;
}
</style>
