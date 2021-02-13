<template>
  <div>
    <div class="">
      <h2 style="color:#39f5c6">입력 변수 데이터 통계</h2>
      <p>예측 전력 사용량과 예측에 사용 된 입력 변수와의 상관성 확인</p>
    </div>

    <!-- form  -->
    <b-form>
      <b-row algin-v="stretch">

          <!-- 시작 일자, 요금제 조회, 종료일자, 단위 선택 -->
          <b-col cols="12" md="10">
            <!-- 시작일자, 요금제 조회 -->
            <b-row>
              <!-- 시작일자 -->
              <b-col cols=6>
                <b-row>
                  <b-col sm="3">예측 일자</b-col>
                  <b-col sm="7">
                    <b-form-input
                      id="predictDate"
                      type="date"
                      name="predictDate"
                      v-model="predictDate"
                      v-bind:max="max"
                      v-bind:min="min"></b-form-input>
                  </b-col>
                </b-row>
              </b-col>
            </b-row>
          </b-col>

          <!-- 전송 버튼  -->
          <b-col cols="12" md="2">
              <b-button size="lg" variant="primary" v-on:click = "createPlot">조회</b-button>
          </b-col>

      </b-row>
    </b-form>

    <div class="row">
        <div id="consumption_data_plot_box" style="width : 100%"></div>
    </div>

    <div class="row">
        <div id="temperature_data_plot_box" style="width : 100%"></div>
    </div>

    <div class="row">
        <div id="humidity_data_plot_box" style="width : 100%"></div>
    </div>

    <div class="row">
        <div id="windSpeed_data_plot_box" style="width : 100%"></div>
    </div>

  </div>
</template>
<script>
  import LineChart from '@/components/Charts/LineChart';
  import BarChart from '@/components/Charts/BarChart';
  import * as chartConfigs from '@/components/Charts/config';
  import TaskList from './Dashboard/TaskList';
  import UserTable from './Dashboard/UserTable';
  import config from '@/config';
  import { FormSelectPlugin } from 'bootstrap-vue';
  import axios from 'axios';

 // import {Select, Option} from 'element-ui';
  export default {
    components: {
      LineChart,
      BarChart,
      TaskList,
      UserTable
      //[Select.name]: Select,
      //[Option.name]: Option
    },
    data() {
      return {
        max : '',
        min : '',
        predictDate : ''
      }
    },

    created() {
      var today = new Date();
      // let year = today.getFullYear();
      // let month = today.getMonth()+1;
      // let date = today.getDate();
      // let hours = today.getHours();
      // let minutes = today.getMinutes();

      console.log(today.getHours());
      console.log(today.getMinutes());
      if(today.getHours()<20){

        this.min = today.getFullYear() +'-'+ (today.getMonth()+1).toString().padStart(2,0) +'-'+today.getDate().toString().padStart(2,0);

        today.setDate(today.getDate()+1);

        this.max = today.getFullYear() + '-' + (today.getMonth()+1).toString().padStart(2,0) + '-' + today.getDate().toString().padStart(2,0);

      }else{

        if(today.getHours()==20 && today.getMinutes()<10){

          this.min = today.getFullYear() +'-'+ (today.getMonth()+1).toString().padStart(2,0) +'-'+today.getDate().toString().padStart(2,0);

          today.setDate(today.getDate()+1);

          this.max = today.getFullYear() + '-' + (today.getMonth()+1).toString().padStart(2,0) + '-' + today.getDate().toString().padStart(2,0);

        }else{

          today.setDate(today.getDate()+1);

          this.min = today.getFullYear() +'-'+ (today.getMonth()+1).toString().padStart(2,0) + '-'+ today.getDate().toString().padStart(2,0);

          today.setDate(today.getDate()+1);

          this.max = today.getFullYear() + '-' + (today.getMonth()+1).toString().padStart(2,0) + '-' + today.getDate().toString().padStart(2,0);
        }
      }
      console.log(this.min);
      console.log(this.max);

    },
    methods: {

      createPlot(){
        let path = "http://" + window.location.hostname + ":5000/scheduling/input";
        // console.log(this.startDate);
        // console.log(this.endDate);
        // console.log(this.payment);
        // console.log(this.contractElec);
        // console.log(this.period);
        var predictDate = this.predictDate;

        axios({
                method:"POST",
                url: path,
                data:{
                    "predictDate": predictDate
                }
            }).then((res)=>{
                Plotly.newPlot('consumption_data_plot_box', [res.data[0]], res.data[1]);
                Plotly.newPlot('temperature_data_plot_box', [res.data[2]], res.data[3]);
                Plotly.newPlot('humidity_data_plot_box', [res.data[4]], res.data[5]);
                Plotly.newPlot('windSpeed_data_plot_box', [res.data[6]], res.data[7]);

            }).catch(error=>{
                console.log(error);
                throw new Error(error);
            });
      }
    }
  };
</script>
<style>

</style>
