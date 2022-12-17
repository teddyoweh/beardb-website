<script>
 
</script>
<template>
  <div class="support">
 
       
    <div class="credit-who">
        <img src="../assets/teddy.jpeg" alt="">
        <div class="info">

       <a href=""> <h1>Teddy Oweh</h1></a>
        <h5>Software Engineer (ML), Network & DevOps Engineer </h5>
        <p> After successfully implementing a facial recognition and fingerprint door control system for my dorm, I realized that there was a need for a local server and database system(in case of the remote server fails) and a remote server and database system to store the facial landmarks, which is sent back and forth from the Raspberry PI4 micro-controller and monitor access to the server infrastructure. This conclusion highlights the technical process and motivation leading to the development of  <a href="https://beardb.net">BearDB</a> . </p>
        <div class="socials">
        <a href="https://github.com/teddyoweh"><i class="bx bxl-github"></i> </a>
        <a href=""><i class="bx bxl-linkedin"></i> </a>
        <a href=""><i class="bx bxl-twitter"></i> </a>
        <a href=""><i class="bx bx-globe"></i> </a>
        <a href=""><i class="bx bx-envelope"></i> </a>


        </div>
                    
    </div>
    </div>
  </div>


</template>


<style lang="scss">
.credit-who{
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    width: 100%;
    img{
        width: 390px;
    height: 400px;
    object-fit: cover;
    border-radius: 6px;
    }
    .info{
        padding: 10px 50px;
    display: flex;
    flex-direction: column;

    }
    .socials{
        display: flex;
        flex-direction: row;
        align-items: center;
        padding-top: 4px;
        a{
            padding-right: 5px ;
            font-size: 18px;
            display: flex;
        }
    }

}
.support{
    display: flex;
    flex-direction: column;
    align-items: center;

    padding: 4% 8%;
  h1{
    color: #fff;
  }
}
p{
    font-size: 16px;
}
a{
    cursor: pointer;
    color: #049464;
    &:hover{
      color: #03bd7e;
    }
}
.contactsection{
    padding-top: 4%;width: 100%;
    p{
        display: flex;
        align-items: center;
        a{
            padding: 0 5px ;
            display: flex;
        align-items: center;
        i{
            padding: 0 5px;
        
        }
        }
    }

}
.chat-section{
    padding-top: 4%;width: 100%;
    .chat-section-header{
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        .searchbox{

        border-radius: 10px;
        border-style: solid;
        display: flex;
        flex-direction: row;
        border-width: 1px;
        align-items: center;
        justify-content: space-between;
        padding: 10px;
        width: 60%;
        input{
            width: 80%;
          color: white;
            border-radius: 5px;
            border: none;
            background-color: transparent;
            outline: none;
        }  }
    }
    .chat-main-section{
        padding-top: 3%;
        display: flex;
        flex-direction: row;
        width: 100%;
        .make-your-post{
            background-color: red;
            width: 60%;
            .questionbox{
                width: 100%;
                textarea{
                    width: 100%;
                    height: 100px;
                    border-radius: 10px;
                    border: none;
                    outline: none;
                    padding: 10px;
                    background-color: #fff;
                    color: white;
                }
            }
        }
        .chat-lists{
            width: 40%;
        }
    }
}
</style>