<script>

import axios from 'axios'
export default{


    setup(){
    

},

data(){
return{
databaseinput:'',
project:''

}
},

methods:{
    newdatabase(){
    // this.bucketlist=[...this.projectlist,this.projectinput]
    axios({
  method: 'post',
  url: 'http://127.0.0.1:9000/newdatabase',
  data: {
  project:this.project,
  database:this.databaseinput,
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


<div class="app-view">
    <div class="app-content">
        <div class="app-header">
          <div> <b>Project:</b> {{$route.params.project}}</div>
          <newprbtn>
                <form @submit="newdatabase"  >
                <input type="text"
               
                
                :value="databaseinput"
                @input="event =>{ databaseinput = event.target.value;
                project=$route.params.project
                }"
                >
                
                <span @click="newdatabase">
                    <i class='bx bx-plus'></i>
                New Bucket
                </span>
            </form>
                
                </newprbtn>
        </div>
        <div class="project-sec-body">
                <small class="hwm">10 Projects</small>
                <div class="project-body">
                
                  
                    <div class="project-item" v-for="section in [1,2,3]" >
                         <div class="icon">
                            <i class='bx bxs-data'></i>
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


</template>


<style lang="scss">

.app-view{
    padding: 10px 20px;
    .app-content{
        .app-header{
            width: 100%;
                display: flex;
                align-items: center;
                flex-direction: row;
                justify-content: space-between;
                border-style: solid;
                
                border-width: 0px 0px 1px;
                
    color: #059c69;
    padding: 6px 10px;
    border-radius: 8px;
 
    font-size: 30px;
    font-family: "Poppins";
    display: flex;
    flex-direction: row;
 
    newprbtn{
                    background: white;
    color: #059c69;
    padding: 6px 10px;
    border-radius: 8px;
    font-weight: 700;
    font-family: "Poppins";
    display: flex;
    font-size: 20px;
    flex-direction: row;
    margin-bottom: 11px;
                    input{
                    
                        outline: none;
    border-style: solid;
    border-width: 0px 0px 1px;
    border-color: #0aaf74;
    font-size: 20px;
}
    span{
        background: #03bd7e;
    color: white;
    padding: 5px 10px;
    margin-left: 15px;
    width: 100%;
    font-size: 20px;
    border-radius: 7px;
    box-shadow: 0px 0px 10px #3e3c3cb3;
    font-weight: 600;
    
    }
                   
                }
    b{
    margin-right: 6px;
    }
        
        }
    }
    .table{
    color: #059c69;
    thead{
    tr{
    th{
    font-weight: 700;
    }
    }
    }
    tbody{
    border: none;
    th{
        border: none;
    }
    tr{
    td{
        border: none;
    color: white;
    }
    }
    }
    }
    
    

}

.project-sec-body{
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


</style>