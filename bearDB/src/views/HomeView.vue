<script >
import TheWelcome from '../components/TheWelcome.vue'
import Auth from '../components/Auth.vue'
import NavBar from './Nav.vue'
import logo from '../assets/logo.png'
export default {
  

methods:{
  showsnackbar(){
    var x = document.getElementById("snackbar");

// Add the "show" class to DIV
x.className = "show";

// After 3 seconds, remove the show class from DIV
setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
  },
  copytoclipboard(){
    navigator.clipboard.writeText('python3 -m pip install Beardb')
    this.showsnackbar()
  }

}
}
</script>

<template>

  <main>
   <nav>
    <div class="logo">
      <img src='../assets/logo.png' alt="BearDB Logo">
      <label for="">Beardb</label>
    </div>

    <div class="nav-items">
      <a href="/">
        Home
      </a>
      <a href="/docs" class="active">
        Docs
      </a>
      <a href="/Contact">
       Contact
      </a>
    </div>
 
   </nav>
<div class="app-container">
  <div class="side-nav">
  <div class="items">
    <div class="item">
      <b>Getting Started</b>
      <ul>
        <a href="#requirements">
          <li>

Requirements
</li>
        </a>
     <a href="#installation">


        <li>
          Installation
        </li>
      </a>
        <a href="#importatation">
        <li>
          Importing Modules
        </li>
      </a>
    </ul>
    </div>
    <div class="item">
      <b>BearDB</b>
      <ul>
        <a href="#newproject">
        <li>
        New Project
        </li>
      </a>
        <a href="#newdatabase">
        <li>
        New Database
        </li>
      </a>
          <a href="#newbucket">
          <li>
          New Bucket
          </li>
        </a>
        <a href="#insertdata">
          <li>
          Insert Data
          </li>
        </a>
        <a href="#updatedata">
          <li>
          Update Data
          </li>
        </a>
       
    </ul>
    </div>
  </div>
  </div>
  <div class="app">
    <div class="requirements" id="requirements">
      <h1>Requirements</h1>
      <p>
        To use BearDB, you need to have the following requirements:
      </p>
      <ul>
        <li>
Python 3.6 or higher
        </li>
        
      </ul>
      <p>
        You can download Python from <a href="https://www.python.org/downloads/">here</a>.
      </p>
   
    </div>
    <div class="installation" id="installation">
      <h1>Installation</h1>
      <p>
        To install BearDB, you need to run the following command in your terminal:
      </p>
 
        <code>
          <div class="top">
            <i @click="copytoclipboard" class='bx bx-copy'></i>
            
          </div>
          <div class="textarea">
            $ python3 -m pip install Beardb
          </div>
     
        </code>
   
       
       
 
  </div>
  <div id="importatation" class="mt-4">
      <h1>Import Required Modules</h1>
      <p>
        To import BearDB, you need to write the following code in your python script:
      </p>

      <code>
        <div class="top">
          <i @click="copytoclipboard" class='bx bx-copy '></i>
        </div>
        <div class="textarea">
          <label for="">
            <span class="import">from</span> <span class="module">Beardb.Beardb</span> <span class="import">import</span> <span class="module">Beardb</span> 
          </label>
          <label for="">
            <span class="import">from</span> <span class="module">Beardb.Bucket</span> <span class="import">import</span> <span class="module">Bucket</span> 
          </label>
        </div>
      </code>
  </div>
  <div id="newproject" class="mt-4">
    <h1>Creating new Project</h1>
    <p>
      To create a new project, you need to write the following code in your python script:
    </p>

    <code>
      <div class="top">
        <i @click="copytoclipboard" class='bx bx-copy
        '></i>
        </div>

        <div class="textarea">
          <label for="">
            project <span class="var">=</span> <span class="module">Beardb</span>(<span class="var">'projectname'</span>)

          </label>

         
    </div>
  </code>      
  </div>
  <div id="newdatabase" class="mt-4">
    <h1>Creating new Database</h1>
    <p>
      To create a new database, you need to write the following code in your python script:
    </p>
    <code>
      <div class="top">
        <i @click="copytoclipboard" class='bx bx-copy
        '></i>
        </div>

        <div class="textarea">
        
          <label for="">
            project.<span class="function">load_database</span>(<span class="var">'database_name'</span>)
            </label>
    </div>
  </code>
  </div>

  <div class="newbucket mt-4" id="newbucket">
    <h1>Create New Bucket </h1>
    <p>
      To create a new bucket, you need to write the following code in your python script:
    </p>
    <code>
      <div class="top">
        <i @click="copytoclipboard" class='bx bx-copy
        '></i>
        </div>

        <div class="textarea">
        
          <label for="">
            users <span class="var">=</span> <span class="function">Bucket</span>(project<span class="var">=</span>project, bucket_name<span class="var">='users'</span>)
           
            </label>
    </div>
  </code>

  </div>
  <div class="insertdata mt-4" id="insertdata">

    <h1>Insert Data</h1>
    <p>
      To insert data, you need to write the following code in your python script:
    </p>
    <code>
      <div class="top">
        <i @click="copytoclipboard" class='bx bx-copy
        '></i>
        </div>

        <div class="textarea">
        
          <label for="">
            users.<span class="function">insert</span>(data<span class="var">={'name':'John Doe', 'age': 20}</span>)
           
            </label>
    </div>
  </code>

  </div>

  <div class="updatedata mt-4" id="updatedata">
    <h1>Update Data </h1>
    <p>
      To update data, you need to write the following code in your python script:
    </p>


    <code>
      <div class="top">
        <i @click="copytoclipboard" class='bx bx-copy
        '></i>
        </div>

        <div class="textarea">
          
            <label for="">
              users.<span class="function">update</span>(data<span class="var">={'name':'John Doe', 'age': 20}</span>, query<span class="var">={'name':'John Doe'}</span>)
            
              </label>

    </div>
              </code>
    
        


</div>  

<div class="updatedatawithid mt-4" id="updatedatawithid">

<h1>Update Data With</h1>
<p>
  To update data with id, you need to write the following code in your python script:
</p>


<code>
  <div class="top">
    <i @click="copytoclipboard" class='bx bx-copy
    '></i>
    </div>

    <div class="textarea">
      
        <label for="">
          users.<span class="function">updatebyId</span>(data<span class="var">={'name':'John Doe', 'age': 20}</span>, id<span class="var">='ae0ca44e-5301-11ed-8d24-a6bd5a94b3a6'</span>)
        
          </label>
         

  
     
          </div>
        </code>

        
</div>
    </div>
</div>
<div id="snackbar">
  <div class="alert alert-success" role="alert">
    <i class='bx bx-check-circle'></i> <label for="">  Copied to clipboard!</label>
</div>
</div>
  </main>
</template>

<style lang="scss">
nav{
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  background: #181818;
    width: 100%;
    z-index: 2;
    padding: 10px;
    border-style: solid;
    border-width: 0px 0px 1px;
    border-color: #2e2e2e;
    top: 0;
    position: sticky;
    .nav-items{
      width: 24%;
    display: flex;
    justify-content: space-evenly;
      a{
        transition: 0.3s;
        margin-right: 4%;
        color: #fff;
        &.active{
          color: #03bd7e;
        }
        &:hover{
          transition: 0.3s;
          color: #03bd7e;
        }
      }
    }
    .logo{
      display: flex;
      flex-direction: row;
      align-items: center;
      label{
        color: #03bd7e;
        font-size: 600;
      }
      img{
        height: 40px;
    width: 40px;
    object-fit: cover;
      }
    }
}
code{
  .top{
  
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-end;
 
    i{
      cursor: pointer;
      transition: 0.3s;
      &:hover{
        transition: 0.3s;
        color:#03bd7e;
      }
    }
 
    
  
  }
  .textarea{
    display: flex;
    flex-direction: column
  }
  .module{
      color: #ffa657;
   }
    .import{
      color: #ff7b72;
    }
    .var{
      color:#79c0ff;
    }
    .function{
      color: #d2a8ff;
    }
  background-color: #1e1e1e;
  color: #fff;
  padding: 15px;
  border-radius: 5px;
  width: 100%;
  display: flex;
  flex-direction: column;

}
.app-container{
width: 100%;
display: flex;
flex-direction: row;
  .side-nav{
    padding: 20px;
    height: 100vh;
    width: 20%;
    background-color: #1e1e1e;
    position: fixed;
    .items{
      .item{
margin-bottom: 4%;
        ul{
          margin: 10px !important;
    list-style: none;
    padding-left: 10px;
    margin: 0;
    border-style: solid;
    border-left-width: 1px !important;
    border-width: 0px;
    border-color: #2e2e2e;
          li{
            padding: 7px;
            color: #fff;
            cursor: pointer;
            transition: 0.3s;
            border-radius: 5px;
            &:hover{
              transition: 0.3s;
              background-color: #2e2e2e;
            }
          }
        }
      }
    }
  }
  .app{
    margin-left: 20%;
    width: 80%;
    padding: 10px 36px;


  }
}
@media screen and (max-width:768px) {
  .side-nav{
    display: none;
  }
  .app{
    margin-left: 0!important;
    width: 100% !important;
  }
}
#snackbar {
  visibility: hidden; /* Hidden by default. Visible on click */
  min-width: 250px; /* Set a default minimum width */
  margin-left: -125px; /* Divide value of min-width by 2 */
 /* Black background color */
 /* White text color */
  text-align: center; /* Centered text */
  border-radius: 2px; /* Rounded borders */
 /* Padding */
  position: fixed; /* Sit on top of the screen */
  // z-index: 1; /* Add a z-index if needed */
  // left: 50%; /* Center the snackbar */
  right:30px;
  top: 30px; /* 30px from the bottom */
}

/* Show the snackbar when clicking on a button (class added with JavaScript) */
#snackbar.show {
  visibility: visible; /* Show the snackbar */
  /* Add animation: Take 0.5 seconds to fade in and out the snackbar.
  However, delay the fade out process for 2.5 seconds */
  -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s;
  animation: fadein 0.5s, fadeout 0.5s 2.5s;
}

/* Animations to fade the snackbar in and out */
@-webkit-keyframes fadein {
  from {right: 0; opacity: 0;}
  to {right: 30px; opacity: 1;}
}

@keyframes fadein {
  from {rightm: 0; opacity: 0;}
  to {right: 30px; opacity: 1;}
}

@-webkit-keyframes fadeout {
  from {right: 30px; opacity: 1;}
  to {right: 0; opacity: 0;}
}

@keyframes fadeout {
  from {right: 30px; opacity: 1;}
  to {right: 0; opacity: 0;}
}
</style>