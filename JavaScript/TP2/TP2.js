const elemnt1= document.querySelector("#rectangle1")
const elemnt2= document.querySelector("#rectangle2")
const milieu1= document.querySelector("#droite")
const milieu2= document.querySelector("#gauche")

const tableau=["Mon Premier","Mon Deuxieme","Mon Troisieme","Mon Quatrieme"]

tableau.forEach(function(x){
    const para=document.createElement('p')
    para.textContent=x

    elemnt1.appendChild(para)

    para.addEventListener('mouseover',function(){
      para.classList.add('selected') 
      para.style.backgroundColor="blue" 
      para.style.color="white"
      para.style.fontSize="25px"
    })
})

function active(){
    if(elemnt1.children.length==0){
        milieu1.disabled=true
        milieu1.style.backgroundColor="white"
    }else{
        milieu1.disabled=false
        milieu1.style.backgroundColor="aqua"
    }
    if(elemnt2.children.length==0){
        milieu2.disabled=true
        milieu2.style.backgroundColor="white"
    }else{
        milieu2.disabled=false
        milieu2.style.backgroundColor="aqua" 
        
    }

}
active()

milieu1.addEventListener('click',function(){
    const selection= elemnt1.querySelector('.selected')
    if(selection){
        elemnt2.appendChild(selection)
        active()
    }
})


milieu2.addEventListener('click',function(){
    const selection= elemnt2.querySelector('.selected')
        elemnt1.appendChild(selection)
        active()
})



