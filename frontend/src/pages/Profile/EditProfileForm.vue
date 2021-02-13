<template>
  <card>
    <h3 slot="header" class="title">회원가입</h3>
    <div class="row">  
      <div class="col-md-4 pr-md-1" role="group">
        <label for="input-live">ID</label>
          <b-form-input
              id="input-live"
              type="text"
              v-model="id"
              :state="idState"
              aria-describedby="input-live-help input-live-feedback"
              placeholder="Enter your ID"
              trim
          ></b-form-input> 
       <b-input-group-append>
             <!-- <b-button class ="idcheck" size="sm" variant="dark">중복 확인</b-button> -->
          </b-input-group-append>
          <b-form-invalid-feedback id="input-live-feedback">
             6글자 이상 입력하시오
          </b-form-invalid-feedback>
      </div>
     </div> 

      <div class="row"> 
      <div class="col-md-4 pr-md-1" role="group">
        <label for="input-live2">Password</label>
          <b-form-input
              id="input-live2"
              type="password"
              maxlength="13"
              v-model="password"
              :state="passwordState"
              aria-describedby="input-live2-help input-live2-feedback"
              placeholder="Enter your Password"
              trim
          ></b-form-input>
          <b-form-invalid-feedback id="input-live2-feedback">
             8글자 이상 입력하시오
          </b-form-invalid-feedback>
      </div>
    </div>
    <div class="row">
      <div class="col-md-4 pr-md-1">
        <base-input 
                  label="관리자 이름"
                  minlength="2"
                  :state="usernameState"
                  placeholder="Username"
                  v-model="username"
                  >
        </base-input>
      </div>
      <div class="col-md-4 pl-md-1">
        <base-input label="이메일"
                  minlength="10"
                  type="email"
                  :state="emailState"
                  v-model="email"
                  placeholder="name@email.com">
        </base-input>
      </div>
    </div>
    <div class="row">
      <div class="col-md-5 pr-md-1">
        <base-input label="학교"
                  placeholder="School Name"
                  minlength="4"
                  :state="schoolState"
                  v-model="school">
        </base-input>
      </div>
       <div class="col-md-8" id="addresssearch">
         <label for="input-live2">도로명 주소</label>
        <b-form-group id="fieldset1">
          <b-form-input id="address" readonly="readonly" placeholder="Enter the street name address" v-model="userFullAddress"></b-form-input>
           <!-- <b-button variant="dark" size="sm" type=button @click="execDaumPostcode">주소 검색</b-button> -->
           <!-- <b-button id="show-btn" @click="$bvModal.show('adressmodal')">주소 검색</b-button>
           <b-modal id="adressmodal"  size="sm" centered title="도로명 주소">
             <DaumPostcode
               :on-complete=handleAddress width=100%
             /> 
            </b-modal>-->
            <!-- <b-button @click="vue-daum-postcode" size="sm" variant="success">주소 검색</b-button> -->
              <vue-daum-postcode @onsearch="result = $event" style="border: 2px dashed #2f9763" />
              <!-- <div>{{ result }}</div> -->
        </b-form-group>

        <label for="input-live2">상세 주소</label>
        <b-form-group id="fieldset2" >
          <b-form-input id="detailAddress" placeholder="Enter a detailed address" v-model="userDetailAddress"></b-form-input>
        </b-form-group>
       <!-- <daum-post-code-modal @setUserData="setUserData" ref="modal"></daum-post-code-modal> -->
      </div>
    </div>

      <div class="col-md-7 px-md-1">
       
        <label for="input-live">데이터 업로드</label>
        <b-form-file class="mt-3"
            v-model="file1"
            :state="Boolean(file1)"
            placeholder="Data Upload"
            drop-placeholder="Drop file here"
            browse-text ="파일 첨부"
        ></b-form-file>
        <div class="data">첨부된 파일: {{ file1 ? file1.name : '' }}</div>
      </div>

    <div class="row"> 
     <div class="col-md-3 pr-md-1">
        <base-input label="ISmart ID"
                  v-model="ismartid"
                  minlength="2"
                  :state="ismartState1"
                  placeholder="ISmart ID">
        </base-input>
      </div>
      <div class="col-md-3 px-md-1">
        <base-input label="ISmart Password"
                  v-model="ismartpassword"
                  minlength="3"
                  :state="ismartState2"
                  placeholder="ISmart Password">
        </base-input>
      </div>
    </div> 
    <button type="submit" native-type="submit" class="btn btn-fill btn-info btn-wd">가입 완료</button>
    <!-- <b-button slot="footer" type="submit" variant="primary" fill>Save</b-button> -->
  </card>
</template>

<script type="text/JavaScript" src="https://t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js"></script>
<script type="text/javascript">

    function execDaumPostcode() {
        new daum.Postcode({
            oncomplete: function(data) {
                // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

                // 각 주소의 노출 규칙에 따라 주소를 조합한다.
                // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
                var addr = ''; // 주소 변수
                var extraAddr = ''; // 참고항목 변수

                //사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
                if (data.userSelectedType === 'R') { // 사용자가 도로명 주소를 선택했을 경우
                    addr = data.roadAddress;
                } else { // 사용자가 지번 주소를 선택했을 경우(J)
                    addr = data.jibunAddress;
                }

                // 사용자가 선택한 주소가 도로명 타입일때 참고항목을 조합한다.
                if(data.userSelectedType === 'R'){
                    // 법정동명이 있을 경우 추가한다. (법정리는 제외)
                    // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
                    if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                        extraAddr += data.bname;
                    }
                    // 건물명이 있고, 공동주택일 경우 추가한다.
                    if(data.buildingName !== '' && data.apartment === 'Y'){
                        extraAddr += (extraAddr !== '' ? ', ' + data.buildingName : data.buildingName);
                    }
                    // 표시할 참고항목이 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
                    if(extraAddr !== ''){
                        extraAddr = ' (' + extraAddr + ')';
                    }
                    // 조합된 참고항목을 해당 필드에 넣는다.
                    document.getElementById("extraAddress").value = extraAddr;

                } else {
                    document.getElementById("extraAddress").value = '';
                }

                // 우편번호와 주소 정보를 해당 필드에 넣는다.
                // document.getElementById('postcode').value = data.zonecode;
                document.getElementById("address").value = addr;
                // 커서를 상세주소 필드로 이동한다.
                document.getElementById("detailAddress").focus();
            }
        }).open();
    }
</script>
<script>
import { VueDaumPostcode } from "vue-daum-postcode"

  export default {
    components:{
      VueDaumPostcode,
    },
    props: {
      model: {
        type: Object,
        default: () => {
          return {};
        }
      }
    },
     computed: {
      idState() {
        return this.id.length > 5 ? true : false
      },
      passwordState() {
        return this.password.length > 7 ? true : false
      },
      usernameState(){
        return this.username.length > 2 ? true : false
      },
      emailState(){
        return this.email.length > 10 ? true : false
      },
      schoolState(){
        return this.school.length > 3 ? true : false
      },
      ismartState1(){
        return this.ismartid.length > 2 ? true : false
      },
      ismartState2(){
        return this.ismartpassword.length > 3 ? true : false
      }
    },
    data() {
      return {
        id: '',
        password: '',
        email:'',
        username: '',
        school: '',
        ismartid:'',
        ismartpassword:'',
        file1: [],
        userFullAddress: null,
        userDetailAddress: null,

      }
    },
    methods: {
      filesChange(file1) {
        this.file1 = file1
      },
      submit() {
          alert("회원 가입이 완료되었습니다");
      }
      // execDaumPostcode : function() {
      //  new daum.Postcode({
      //       oncomplete: function(data) {
      //           // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

      //           // 각 주소의 노출 규칙에 따라 주소를 조합한다.
      //           // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
      //           var addr = ''; // 주소 변수
      //           var extraAddr = ''; // 참고항목 변수

      //           //사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
      //           if (data.userSelectedType === 'R') { // 사용자가 도로명 주소를 선택했을 경우
      //               addr = data.roadAddress;
      //           } else { // 사용자가 지번 주소를 선택했을 경우(J)
      //               addr = data.jibunAddress;
      //           }

      //           // 사용자가 선택한 주소가 도로명 타입일때 참고항목을 조합한다.
      //           if(data.userSelectedType === 'R'){
      //               // 법정동명이 있을 경우 추가한다. (법정리는 제외)
      //               // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
      //               if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
      //                   extraAddr += data.bname;
      //               }
      //               // 건물명이 있고, 공동주택일 경우 추가한다.
      //               if(data.buildingName !== '' && data.apartment === 'Y'){
      //                   extraAddr += (extraAddr !== '' ? ', ' + data.buildingName : data.buildingName);
      //               }
      //               // 표시할 참고항목이 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
      //               if(extraAddr !== ''){
      //                   extraAddr = ' (' + extraAddr + ')';
      //               }
      //               // 조합된 참고항목을 해당 필드에 넣는다.
      //               document.getElementById("sample6_extraAddress").value = extraAddr;

      //           } else {
      //               document.getElementById("sample6_extraAddress").value = '';
      //           }

      //           // 우편번호와 주소 정보를 해당 필드에 넣는다.
      //           document.getElementById('sample6_postcode').value = data.zonecode;
      //           document.getElementById("sample6_address").value = addr;
      //           // 커서를 상세주소 필드로 이동한다.
      //           document.getElementById("sample6_detailAddress").focus();
      //       }
      //   }).open();
      // }
    },
  }
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

h3{
  font-family: 'Jua', sans-serif;
  letter-spacing: 2.5px;
}
.data{
  font-size: 13px;
  letter-spacing: 1px;
  margin-left: 10px;
  margin-top: 9px;
}
b-form-invalid-feedback{
  letter-spacing: 1px;
}
.idcheck{
    margin-left: 30px;
}
</style>
