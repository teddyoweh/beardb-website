<script>
import axios from 'axios'


export default{
    
data() {
    console.log('dsds',this.$router.currentRoute.value.path)
    return{
    loc:this.$router.currentRoute.value.path
    
    
}
}
}
</script>

<template>

 

    <nav>

    <div class="logo">
        <router-link to="/">
           

      <img src='../assets/logo.png' alt="BearDB Logo">
      <label for="">BearDB </label>
    </router-link>
    </div>

    <div class="nav-items">
        <router-link to="/">
        <a href="/" v-if="loc=='/'" class="active">
        Docs
      </a>
 
      <a v-else href="/" >
        Docs
      </a>
    </router-link>
    <router-link to="/support">
      <a   v-if="loc=='/support'" class="active">
   Support
      </a>
 
      <a v-else   >
        Support
      </a>
    </router-link>
    <router-link to="/">
      <a href="/credits">
       Credits
      </a>
    </router-link>

    </div>
 
   </nav>
 
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
        &:focus{
          transition: 0.3s;
          color: #03bd7e;}
      }
    }
    .logo{
      display: flex;
      flex-direction: row;
      align-items: center;
      cursor: pointer;
      label{
        color: #03bd7e;
        font-size: 600;
        cursor: pointer;
      }
      img{
        height: 40px;
    width: 40px;
    cursor: pointer;
    object-fit: cover;
      }
    }
}
</style>
