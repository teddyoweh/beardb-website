<script>
import { useState } from '../composables/state';
import axios from 'axios';
export default {
    setup() {
    
          
          
        return {
           
        };
    },
    methods:{
        createaccount(){
        const body={
        
        email:'this.email',
        secret:'this.password'
        }
        axios({
  method: 'post',
  url: 'http://127.0.0.1:3000/newuser',
  data: {
    email:this.email,
    password:this.password,
    fullname:this.fullname,
  },
  headers: {
    'Content-Type': 'application/json',
    'Accept':"*/*",
    'Access-Control-Allow-Origin': '*',
  }
})
              .then((res)=>{
              this.regscuccess=true
              this.info=res.data
              }
              )
        },
        loginaccount(){
        
        axios({
  method: 'post',
  url: 'http://127.0.0.1:3000/login',
  data: {
    email:this.loginid,
   secret:this.secret,
    
  },
  headers: {
    'Content-Type': 'application/json',
    'Accept':"*/*",
    'Access-Control-Allow-Origin': '*',
  }
})
              .then((res)=>{
              this.logininfo=res.data
              }
              )
              .catch((err)=>{
              if(err.response.status==401){
                this.logininfo ='invalid email'
                this.loginiderror=true
                this.secreterror=false
              }else if(err.response.status==402){
                this.logininfo ='invalid password'
                this.loginiderror=false
                this.secreterror=true
              }else{
                this.logininfo ='invalid email and password'
              }
              
           
              
            //   =stuff
              }
              )
        }
    
    },


    data(){
    
        return {
            authview:'login',
            passview:false,
            passview1:false,
            password:'',
            email:'',
            loginid:'',
            loginiderror:false,
            fullname:'',
            secret:'',
            regscuccess:false,
            secreterror:false,
            info:null,
            logininfo:null,
        }
    }
};
</script>
<template>
    <div class="auth">
    
        <div class="auth-form">
         
            <div class="auth-header">
                <label v-if="authview=='login'" @click="authview='login'"  class="active" for="">
                   Login
                </label>
                <label v-else @click="authview='login'"   for="">
                   Login
                </label>
                <label v-if="authview=='create'"  class="active"  @click="authview='create'" for="">
                    Create Account
                </label>
                <label v-else @click="authview='create'" for="">
                    Create Account
                </label>
            </div>
            
            <div v-if="authview=='login'" class="auth-body">
                <form action="">
              <div v-if="loginiderror==true" class='alert alert-danger' role="alert">

            <i class="bx bxs-error-circle"></i> <label> Email not found  </label>

            </div>
            <div v-if="secreterror==true" class='alert alert-danger' role="alert">

            <i class="bx bxs-error-circle"></i> <label> Incorrect Password</label>

                </div>
                    <div class="auth-sec">
                        <label for="">Login ID</label>
                        <input  type="text"
                        :value="loginid"
                        @input="event => loginid = event.target.value"
                        >
                        
                    </div>
                    <div class="auth-sec">
                        <label for="">Secret</label>
                        <div class="pass-box" v-if="passview==false">
                            <input    
                            :value="secret"
                            @input="event => secret = event.target.value"
                            type='password'>
                            <i  @click="passview =true" class='bx bxs-hide'></i>
                             
                          
                        </div>
                        
                        <div class="pass-box" v-else-if="passview==true">
                            <input   
                            :value="secret"
                            @input="event => secret = event.target.value"
                            type='text'>
                            <i  @click="passview =false" class='bx bxs-show'></i>
                           
                        </div>
           
                    </div>
                    <div class="auth-sec">
                       <submitbtn @click="loginaccount">Login</submitbtn>
                    </div>
                </form>
            </div>
            
             <!-- Create Account -->
            <div v-else-if="authview=='create'" class="auth-body">
                <form action="">
                    <div v-if="regscuccess==true" class='alert alert-success' role="alert">

<i class="bx bxs-check-circle"></i> <label>Account Registered, Details Sent to <b> {{email}}</b> </label>

</div>
              
                <div class="auth-sec">
                        <label for="">Fullname</label>
                        <input type="text"
                        :value="fullname" 
                        @input="event => fullname = event.target.value"
                        >
                    </div>
                    <div class="auth-sec">
                        <label for="">Email</label>
                        <input type="text"
                        :value="email"
                        @input="event => email = event.target.value"
                        >
                    </div>
                    <div class="auth-sec">
                        <label for="">Password</label>
                        <div class="pass-box" v-if="passview1==false">
                            <input 
                            :value="password"
                            @input="event => password = event.target.value"
                            type="password"><i  @click="passview1=true" class='bx bxs-hide'></i>
                        </div>
                        <div class="pass-box" v-else-if="passview1==true">
                            <input  
                            :value="password"
                            @input="event => password = event.target.value"
                            type='text'>
                            <i  @click="passview1 =false" class='bx bxs-show'></i>
                        </div>
                    </div>
                    <div class="auth-sec">
                       <submitbtn @click="createaccount">Get Started</submitbtn>
                    </div>
                </form>
            </div>
        
        </div>
    
    </div>
</template>
  
<style lang="scss">
  .auth{
    width: 100%;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    .auth-form{
    width: 40%;
        .auth-header{
        display: flex;
        flex-direction: row;
     
            label{
            color: white;
            padding: 10px;
            font-size: 20px;
            font-family: poppins;
            font-weight: 700;
            border-width: 0px 0px 3px;
            border-color: transparent;
            cursor: pointer;
            border-style: solid;
            transition: 0.3s;
            margin-right: 2%;
            &:hover{
                color: rgb(6, 114, 78);
         
                transition: 0.3s;
            }
            &.active{
            border-color: hsla(160, 100%, 37%, 1); ;
                color: hsla(160, 100%, 37%, 1);
            }
            }
        }
        .auth-body{padding: 20px 0 ;
            form{
                .auth-sec{
                padding: 10px 0;
                display: flex;
                flex-direction: column;
                submitbtn{
                    background-color: hsla(160, 100%, 37%, 1);
                    color: white;
                    text-align: center;
                    font-family: poppins;
                    font-weight: 500;
                    font-size: 15px;
                    border: none;
                    margin-top: 4%;
                    width: 40%;
                    padding: 8px 10px;
                    border-radius: 10px;
                    cursor: pointer;
                
                }
                    .pass-box{
                    
                   
                    display: flex;
                    align-items: center;
                    flex-direction: row;
                    width: 100%;
                    border-color:  hsla(160, 100%, 37%, 1);
                        border-style: solid;
                        border-width: 0px 0px 1px;
                        input{
                        border: none;
                        }
                    i{
                        color: hsla(160, 100%, 37%, 1);
                        font-size: 18px;
                        cursor: pointer;
                    
                    }
                    }
                    label{
                        font-weight: 500;
                        font-family: poppins;
                        font-size: 17px;
                        color: hsla(160, 100%, 37%, 1);
                        
                    }
                    
                    input{
                        border-color:  hsla(160, 100%, 37%, 1);
                        border-style: solid;
                        border-width: 0px 0px 1px;
                        outline: none;
                        color: white;
                        padding: 8px 0px;
                        font-size: 16px;
                        width: 100%;
                        background-color: transparent;
                        &.error{
                            border-color: #cc1a0f;
                        }
                    }
                    small{
                        color: #cc1a0f;
                        font-size: 12px;
                        font-family: poppins;
                        font-weight: 500;
                    }
                }
            }
        }
    }
  }
  
  
  
</style>
  