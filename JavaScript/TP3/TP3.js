const suces=document.querySelector("#Success")
const dang=document.querySelector("#Danger")
const warn=document.querySelector("#Warning")
const inf=document.querySelector("#Info")
const lapille=document.querySelector("#lapille")

suces.addEventListener('click',function(){
    const pile= document.createElement('div')
    pile.innerHTML=`ATTENTION`
    pile.classList.add('pille','Success')
    lapille.appendChild(pile)
    setTimeout(function(){
        lapille.removeChild(pile)
    },2000)
})


dang.addEventListener('click',function(){
    const pile= document.createElement('div')
    pile.innerHTML=`DANGER`
    pile.classList.add('pille','Danger')
    lapille.appendChild(pile)
    setTimeout(function(){
        lapille.removeChild(pile)
    },2000)
})

warn.addEventListener('click',function(){
    const pile= document.createElement('div')
    pile.innerHTML=`WARNING`
    pile.classList.add('pille','Warning')
    lapille.appendChild(pile)
    setTimeout(function(){
        lapille.removeChild(pile)
    },2000)
})

inf.addEventListener('click',function(){
    const pile= document.createElement('div')
    pile.innerHTML=`INFORMATION`
    pile.classList.add('pille','Info')
    lapille.appendChild(pile)
    setTimeout(function(){
        lapille.removeChild(pile)
    },2000)
})