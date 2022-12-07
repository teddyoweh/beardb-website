<script>
import axios from 'axios';
export default{
setup(){

 

}
,
data(){
    
    axios({
  method: 'post',
  url: 'http://127.0.0.1:9000/me',
  data: {
    email:'teddyoweh@gmail.com',
    secret:'a5ab78cec047b0a9a3348011360c7e11ad9361bbc7f45e066ffae3b3adde685a'
    
  },
  headers: {
    'Content-Type': 'application/json',
    'Accept':"*/*",
    'Access-Control-Allow-Origin': '*',
  }
})
              .then((res)=>{
                console.log(res.data.data)
                this.projectlist = res.data.data.projects
            
              }
              )
              
              
    return {
        projectinput:'',
        projectlist:null,
        
        
    
    }
              
},
methods:{
    newproject(){
    this.projectlist=[...this.projectlist,this.projectinput]
    axios({
  method: 'post',
  url: 'http://127.0.0.1:9000/newproject',
  data: {
  project:this.projectinput,
    email:'teddyoweh@gmail.com',
    secret:'a5ab78cec047b0a9a3348011360c7e11ad9361bbc7f45e066ffae3b3adde685a'
    
  },
  headers: {
    'Content-Type': 'application/json',
    'Accept':"*/*",
    'Access-Control-Allow-Origin': '*',
  }
})
              .then((res)=>{
                console.log(res.data)
            
              }
              )
   
   } 
}
}

</script>

<template>

<nav></nav>

<div class="dash">
    <div class="dash-content">
        <div class="project-sec">
            <div class="project-sec-header">
                <label for="">
                    Project
                </label>
                
                <newprbtn>
                <form @submit="newproject"  >
                <input type="text"
               
                
                :value="projectinput"
                @input="event => projectinput = event.target.value"
                >
                
                <span @click="newproject">
                    <i class='bx bx-plus'></i>
                New Project
                </span>
            </form>
                
                </newprbtn>
            </div>
            <div class="project-sec-body">
                <small class="hwm">10 Projects</small>
                <div class="project-body">
                
                  
                    <div class="project-item" v-for="section in projectlist" >
                         <div class="icon">
                            <i class='bx bxs-folder'></i>
                         </div>
                         <div class="project-content">
                                <h3>{{section}}</h3>
                                <small>10 Buckets</small>
                         </div>
                    </div>
                 
                
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<style lang="scss">
.dash{
    padding: 10px 20px;
    width: 100%;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    .dash-content{
        width: 100%;
        .project-sec{
            width: 100%;
            .project-sec-header{

                width: 100%;
                display: flex;
                align-items: center;
                flex-direction: row;
                justify-content: space-between;
                border-style: solid;
                border-width: 0px 0px 1px;
                newprbtn{
                    background: white;
    color: #059c69;
    padding: 6px 10px;
    border-radius: 8px;
    font-weight: 700;
    font-family: "Poppins";
    display: flex;
    flex-direction: row;
    margin-bottom: 11px;
                    input{
                    
                        outline: none;
    border-style: solid;
    border-width: 0px 0px 1px;
    border-color: #0aaf74;
}
    span{
        background: #03bd7e;
    color: white;
    padding: 5px 10px;
    margin-left: 15px;
    width: 100%;
    border-radius: 7px;
    box-shadow: 0px 0px 10px #3e3c3cb3;
    font-weight: 600;
    
    }
                   
                }
                  label{
                  font-size: 30px;
                  font-weight: 700;
                  font-family: poppins;
                    color: hsla(160, 100%, 37%, 1);
                  }
              
            }.project-sec-body{
                padding: 30px 20px;
                small.hwm{
                    font-size: 16px;
                    font-weight: 900;
                    font-family: quicksand;
                }
                .project-body{
                padding: 10px 0;
                display: flex;
                flex-direction: row;
                flex-wrap: wrap;
                .project-item{
                margin-right: 2%;
                margin-bottom: 1.5%;
                
                    width: 30%;
    display: flex;
    align-items: center;
    flex-direction: row;
    padding: 10px 20px;
    background: #53c9950d;
    padding-right: 40px;
    border-radius: 9px;
                 
                    .icon{
                        width: 50px;
                        height: 50px;
                        border-radius: 50%;
                        background: hsla(160, 100%, 37%, 1);
                        display: flex;
                        align-items: center;
                        flex-direction: row;
                        justify-content: center;
                        i{
                            color: white;
                            font-size: 20px;
                        }
                    }
                
                    .project-content{
                    padding: 10px;
                        h3{
                        color:  hsla(160, 100%, 37%, 1);;
                            font-size: 23px;
                            font-weight: 700;
                            font-family: quicksand;
                        }
                        small{
                            font-size: 15px;
                            font-weight: 700;
                            font-family: quicksand;
                        }
                    }
                }
                }
            }
        }
    }
 
}
</style>