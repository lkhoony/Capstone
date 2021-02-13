<template>
  <div>
    <div class="">
      <h2 style="color:#39f5c6">CCHP 스케줄링 운영 시간표</h2>
      <p>예측된 전력 사용량을 이용하여 가장 높은 경제적 이득을 기대할 수 있는 CCHP 발전 스케줄링 시간표</p>
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
              <b-col cols=6>
                <b-row>
                  <b-col sm="3">요금제 조회</b-col>
                  <b-col sm="7"><b-form-select id="payment" v-model="payment" :options="payments" name="payment"></b-form-select></b-col>
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
        <div id="cchp_scheduling_plot_box" style="width : 100%"></div>
    </div>

    <div class="row">
        <div id="cchp_scheduling_fee_plot_box" style="width : 100%"></div>
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

  export default {
    components: {
      LineChart,
      BarChart,
      TaskList,
      UserTable
    },

    data() {
      return {
        payment: null,
        payments: [
          { value: null, text: '요금제 선택'  },
          { value: 1, text: '교육용(갑) 저압전력' },
          { value: 2, text: '교육용(갑) 고압A 선택I' },
          { value: 3, text: '교육용(갑) 고압A 선택II' },
          { value: 4, text: '교육용(갑) 고압B 선택I' },
          { value: 5, text: '교육용(갑) 고압B 선택II' },
          { value: 6, text: '교육용(을) 고압A 선택I' },
          { value: 7, text: '교육용(을) 고압A 선택II' },
          { value: 8, text: '교육용(을) 고압B 선택I' },
          { value: 9, text: '교육용(을) 고압B 선택II' }
        ],
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
        let path = "http://" + window.location.hostname + ":5000/scheduling/cchpsch";
        var predictDate = this.predictDate;
        var payment = this.payment;
        var contractElec = this.contractElec;
        axios({
                method:"POST",
                url: path,
                data:{
                    "predictDate": predictDate,
                    "payment" : payment,
                    "contractElec" : contractElec
                }
            }).then((res)=>{
              console.log(res);
                Plotly.newPlot('cchp_scheduling_plot_box', [res.data[0],res.data[1]], res.data[2]);
                Plotly.newPlot('cchp_scheduling_fee_plot_box', [res.data[3],res.data[4]], res.data[5]);
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
