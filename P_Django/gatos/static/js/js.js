function inicia(){

    let user=document.getElementById('user').value;
    let pass=document.getElementById('pass').value;

    if(user== 'Alan' & pass== '1234'){

    window.location="../html/index.html";

    }
    else{

        alert("Datos Incorrectos")
        document.getElementById('user').value=''; 
        document.getElementById('pass').value='';
    }

}