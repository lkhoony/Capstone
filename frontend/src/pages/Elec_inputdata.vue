<template>
  <div>
    <div class="">
      <h2 style="color:#39f5c6">입력 변수 데이터 통계</h2>
      <p>전력 사용량과 입력 변수로 사용된 데이터들의 상관성 확인</p>
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
                  <b-col sm="3">시작 일자</b-col>
                  <b-col sm="7"><b-form-input id="startDate" type="date" name="startDate" ref="startDate" v-model="startDate"></b-form-input></b-col>
                </b-row>
              </b-col>
              <!-- 단위 선택 -->
              <b-col cols=6>
                <b-row>
                  <b-col sm="3">단위 선택</b-col>
                  <b-col sm="7">
                    <b-form-radio-group
                      id="period"
                      v-model="period"
                      :options="periods"
                      name="period"
                      ref="period"
                    ></b-form-radio-group>
                  </b-col>
                </b-row>
              </b-col>
            </b-row>

            <!-- 종료일자, 단위 선택 -->
            <b-row>
              <!-- 종료일자 -->
              <b-col cols=6>
                <b-row>
                  <b-col sm="3">종료 일자</b-col>
                  <b-col sm="7"><b-form-input id="endDate" draggable=""type="date" name="endDate" ref="endDate" v-model="endDate"></b-form-input></b-col>
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
        startDate : '',
        endDate : '',
        period: 3,
        periods: [
          { value: 3, text: '연간' },
          { value: 2, text: '월간' },
          { value: 1, text: '일간' }
        ],

      }
    },
    methods: {

      createPlot(){
        let path = "http://" + window.location.hostname + ":5000/electric/input";
        // console.log(this.startDate);
        // console.log(this.endDate);
        // console.log(this.payment);
        // console.log(this.contractElec);
        // console.log(this.period);
        var startDate = this.startDate;
        var endDate = this.endDate;
        var period = this.period;

        axios({
                method:"POST",
                url: path,
                data:{
                    "startDate": startDate,
                    "endDate": endDate,
                    "period" : period,
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
