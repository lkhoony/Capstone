<template>
  <div>
    <div class="">
      <h2 style="color:#39f5c6">예측 전력 사용량 비교</h2>
      <p style="display:inline-block; margin-right : 15px">실제 전력 사용량과 예측 모델로 부터 구한 전력 사용량을 비교하여 모델의 타당성 확인</p>
      <div style="display:inline-block">

        <b-button variant="info" size="sm" v-b-modal.modal-1>XAI 확인</b-button>

        <b-modal id="modal-1" title="설명 가능한 인공지능 eXplainable AI, XAI">
          <p class="my-4">전력 사용량 예측을 수행할 때 사용된 입력 변수들의 영향도를 나타냅니다.</p>
          <div class="">
            <img slot="image" class="card-img-top" src="../assets/xai.png" alt="Card image cap" height="100%"/>
          </div>
        </b-modal>

      </div>
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
              <!-- 요금제 조회 -->
              <b-col cols=6>
                <b-row>
                  <b-col sm="3">요금제 조회</b-col>
                  <b-col sm="7"><b-form-select id="payment" v-model="payment" :options="payments" name="payment" ref="payment" ></b-form-select></b-col>
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

            <!-- 계약전력 입력 -->
            <b-row>
              <b-col cols=6>
                <b-row>
                  <b-col sm="3">계약 전력</b-col>
                  <b-col sm="7">
                    <b-form-input
                      id="contractElec"
                      v-model="contractElec"
                      type="text"
                      placeholder="계약 전력 입력"
                      autocomplete="off"
                      name="contractElec"
                      ref="contractElec"
                    ></b-form-input></b-col>
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
      <div id="compare_plot_box" style="width : 100%"></div>
    </div>

    <div class="row">
      <div id="compare_fee_plot_box" style="width : 100%"></div>
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
        startDate : '',
        endDate : '',

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

        period: 3,
        periods: [
          { value: 3, text: '연간' },
          { value: 2, text: '월간' },
          { value: 1, text: '일간' }
        ],

        contractElec : ''

      }
    },

    methods: {

      // createPlot(){
      //
      //   let path = "http://" + window.location.hostname + ":5000/electric/compare";
      //   // axios.get(path).then((res) => { this.my_data = res.data; }).catch((error) => { console.error(error);});
      //
      //   // var graphs = {{plot | safe}};
      //   // Plotly.plot('bargraph',graphs,{});
      //
      //   $.ajax({
      //     url: path,
      //     type: "GET",
      //     contentType: 'application/json;charset=UTF-8',
      //     dataType:"json",
      //     success: function (data) {
      //       console.log(data);
      //       Plotly.newPlot('compare_plot_box', [data[0],data[1]], data[2]);
      //       Plotly.newPlot('compare_fee_plot_box', [data[3],data[4]], data[5]);
      //     }
      //   });
      // }

      createPlot(){
        let path = "http://" + window.location.hostname + ":5000/electric/compare";
        // console.log(this.startDate);
        // console.log(this.endDate);
        // console.log(this.payment);
        // console.log(this.contractElec);
        // console.log(this.period);
        var startDate = this.startDate;
        var endDate = this.endDate;
        var payment = this.payment;
        var period = this.period;
        var contractElec = this.contractElec;

        axios({
                method:"POST",
                url: path,
                data:{
                    "startDate": startDate,
                    "endDate": endDate,
                    "payment" : payment,
                    "period" : period,
                    "contractElec" : contractElec
                }
            }).then((res)=>{
                Plotly.newPlot('compare_plot_box', [res.data[0], res.data[1]],res.data[2]);
                Plotly.newPlot('compare_fee_plot_box', [res.data[3], res.data[4]], res.data[5]);
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
