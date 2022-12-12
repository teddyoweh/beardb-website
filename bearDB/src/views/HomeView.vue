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
      <label for="">BearDB </label>
    </div>

    <div class="nav-items">
      <a href="/">
        Home
      </a>
      <a href="/docs" class="active">
        Docs
      </a>
      <a href="/contact">
       Contact
      </a>
      <a href="/donate">
       Donate
      </a>
    </div>
 
   </nav>
<div class="app-container">
  <div class="side-nav">
  <div class="items">
    <div class="item">
      <b>Getting Started</b>
      <ul>
        <a href="#introduction">
          <li>

Introduction
</li>
        </a>
        <a href="#sourcecode">
          <li>

Source Code
</li>
        </a>
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
          Update Data with Query
          </li>
        </a>
        <a href="#updatedataid">
          <li>
          Update Data with ID
          </li>
        </a>
        <a href="#fetchdata">
          <li>
          Fetch Data with Query
          </li>
        </a>
        <a href="#fetchdataid">
          <li>
          Fetch Data with ID
          </li>
        </a>
        <a href="#deletedata">
          <li>
          Delete Data with Query
          </li>
        </a>
        <a href="#deletedataid">
          <li>
          Delete Data with ID
          </li>
        </a>
    </ul>
    </div>
  </div>
  </div>
  <div class="app">
    <div id="introduction">
      <h1>Introduction</h1>
  

      <p>BearDB  is a database system that implements encrypted versions of JSON data, making it easy to access, manage, and deploy remotely. With Beardb, you can securely store and manage your data without worrying about unauthorized access. The system is designed to be user-friendly and easy to set up, even for users with limited technical experience.


</p><p>        To deploy Beardb on a remote server, you will need to have access to a server that meets the system's requirements. These requirements include a Linux-based operating system, a minimum of 4GB of RAM, and at least 10GB of free storage space. Once you have a suitable server, you can download and install the Beardb software and follow the provided instructions to set up the database.

 </p> <p> Once Beardb is up and running on your remote server, you can easily manage your data using the system's intuitive interface. You can create, read, update, and delete records as needed, and access your data from any device with an internet connection. The system's encryption features ensure that your data remains secure, even when accessed remotely.

 </p> <p> Overall, Beardb is a powerful and flexible database system that makes it easy to manage and access your data, even when working remotely. Whether you're a small business owner, a developer, or just someone looking for a secure and easy-to-use database solution, Beardb has you covered.

 </p> <p>Database system implementing encrypted versions JSON of data. Easy to access, manage and deploy remotely.
      </p>
      

    </div>
  <div id="sourcecode">
<h1>Source Code</h1>
<div class="sourcelinks">

  <a target="_blank" href="https://pypi.org/project/Beardb/">

    <i class='bx bxs-package'></i>
<label for="" class="ml-3"> BearDB Python Package</label>
</a>
  <a target="_blank" href="https://github.com/teddyoweh/beardb">

  <i class='bx bxl-github'></i>
  <label for="" class="ml-3"> BearDB Source Code</label>
  </a>
  <a  target="_blank" href="https://github.com/teddyoweh/beardb-api">

<i class='bx bxl-github'></i>
<label for="" class="ml-3"> BearDB  API Source Code</label>
</a>
</div>

  </div>

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

<div class="updatedataid mt-4" id="updatedataid">

<h1>Update Data With ID</h1>
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

<div id="fetchdata" class="mt-4">
  
  <h1>Fetch Data With Query</h1>
  <p>
    To fetch data with query, you need to write the following code in your python script:
  </p>

  <code>
  <div class="top">
    <i @click="copytoclipboard" class='bx bx-copy
    '></i>
    </div>

    <div class="textarea">
      
        <label for="">
          users.<span class="function">fetchData</span>(query<span class="var">={'name':'John Doe'}</span>)
        
          </label>
         

  
     
          </div>
</code>
  
</div>
<div id="fetchdataid" class="mt-4">

  <h1>Fetch Data With ID</h1>
  <p>
    To fetch data with ID you need to write the following code in your python script:
  </p>
  <code>
  <div class="top">
    <i @click="copytoclipboard" class='bx bx-copy
    '></i>
    </div>

    <div class="textarea">
        
          <label for="">
            users.<span class="function">fetchbyID</span>(id<span class="var">='ae0ca44e-5301-11ed-8d24-a6bd5a94b3a6'</span>)
          
            </label>
          
  
    
      
            </div>
  </code>

  </div>
<div id="deletedata" class="mt-4">
  <h1>Delete Data With Query</h1>
  <p>
    To delete the data with Query you need to write the following code in your python script:
  </p>
  <code>
  <div class="top">
    <i @click="copytoclipboard" class='bx bx-copy
    '></i>
    </div>

    <div class="textarea">
        
          <label for="">
            users.<span class="function">delete</span>(query<span class="var">={'name':'John Doe'}</span>)
          
            </label>
          
  
    
      
            </div>
  </code>
  </div>
<div id="deletedataid" class="mt-4">
  <h1>Delete Data With ID</h1>
  <p>
    To delete the data with ID you need to write the following code in your python script:
  </p>
  <code>
  <div class="top">
    <i @click="copytoclipboard" class='bx bx-copy
    '></i>
    </div>

    <div class="textarea">

      <label for="">
        users.<span class="function">deletebyId</span>(id<span class="var">='ae0ca44e-5301-11ed-8d24-a6bd5a94b3a6'</span>)
      
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
.sourcelinks{
padding: 10px;
  display: flex;
  flex-direction: column;
  a{margin-bottom: 3%;
    font-size: 17px;
    display: flex;
    flex-direction: row;
    align-items: center;
    cursor: pointer;
    color: #049464;
    &:hover{
      color: #03bd7e;
    }
  }
  label{
    cursor: pointer;
    margin-left: 10px;
  }
}
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
    overflow-y: scroll;
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