const MP=document.getElementById('MP')
const number=document.getElementById('number')
const Maj=document.getElementById('Maj')
const Min=document.getElementById('Min')
const Nomb=document.getElementById('Nomb')
const CS=document.getElementById('CS')
const generer=document.getElementById('generer')

const lettre_maj="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
const lettre_min="abcdefghijklmnopqrstuvwxyz"
const nombre="0123456789"
const carspe="@&#()-)$^*ù!:;,<>?./§%µ£+°]^`|[{{~~´"

function Gmp(){
    let password=''
    let vd=''

    if(Maj.checked){
        vd+=lettre_maj
    }

    if(Min.checked){
        vd+=lettre_min
    }

    if(Nomb.checked){
        vd+=nombre
    }

    if(CS.checked){
        vd+=carspe
    }

    for(let i=0; i<number.value; i++){
        var saa=Math.floor(Math.random()*vd.length)
        password+=vd[saa]
    }
    MP.value=password
}


function actbut(){
    if(Maj.checked || Min.checked || Nomb.checke || CS.checked) {
        generer.disabled=false
    } else{
        generer.disabled=true
    }
}

Maj.addEventListener('change',actbut)
Min.addEventListener('change',actbut)
Nomb.addEventListener('change',actbut)
CS.addEventListener('change',actbut)
generer.addEventListener('click',Gmp)
