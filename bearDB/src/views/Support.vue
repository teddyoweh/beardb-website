<script>

</script>
<template>
  <div class="support">
    <h1>Support</h1>
    <p>
        If you are having trouble using Beardb, our support page is here to help. On this page, you can contact us to ask questions regarding issues related to beardb, find troubleshooting tips to help you get the most out of your Beardb experience.


    </p> <p> Contact our support team if you need additional assistance. Our team is here to help you get the most out of your Beardb experience, and we are happy to answer any questions you may have.

</p> <p> Whether you are a first-time user or an experienced developer, we hope that our support page will provide you with the information you need to get the most out of Beardb. Thank you for choosing Beardb as your database solution.

<div class="contactsection">
        <div class="contactsection-header">
            <h1>Contact Us</h1>

        </div>
        <div class="contactsection-content">
            <p>For any questions, enquires or concerns, please email us at <b><a href="mailto:info@beardb.net">info@beardb.net</a></b></p>
            <p>Any issues or bug reports regarding <a target="_blank" href="https://github.com/teddyoweh/beardb">Beardb</a> submit here  <a href="https://github.com/teddyoweh/Beardb/issues"  target="_blank"><i class="bx bxl-github"></i> GitHub Issuess</a> </p>
            <p>Any issues or bug reports regarding <a   target="_blank" href="https://github.com/teddyoweh/beardb-api">BeardbAPI</a> submit here  <a href="https://github.com/teddyoweh/beardb-api/issues"  target="_blank"><i class="bx bxl-github"></i> GitHub Issuess</a> </p>
            </div>
            

</div>
  

      
    </p>
  </div>


</template>


<style lang="scss">
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