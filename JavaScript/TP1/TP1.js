const ajoutbouton= document.querySelector("#ajoutpage")
const edit =`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(255, 255, 255, 1);transform: ;msFilter:;"><path d="m7 17.013 4.413-.015 9.632-9.54c.378-.378.586-.88.586-1.414s-.208-1.036-.586-1.414l-1.586-1.586c-.756-.756-2.075-.752-2.825-.003L7 12.583v4.43zM18.045 4.458l1.589 1.583-1.597 1.582-1.586-1.585 1.594-1.58zM9 13.417l6.03-5.973 1.586 1.586-6.029 5.971L9 15.006v-1.589z"></path><path d="M5 21h14c1.103 0 2-.897 2-2v-8.668l-2 2V19H8.158c-.026 0-.053.01-.079.01-.033 0-.066-.009-.1-.01H5V5h6.847l2-2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2z"></path></svg>`
const poubelle= `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(255, 255, 255, 1);transform: ;msFilter:;"><path d="M5 20a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8h2V6h-4V4a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v2H3v2h2zM9 4h6v2H9zM8 8h9v12H7V8z"></path><path d="M9 10h2v8H9zm4 0h2v8h-2z"></path></svg>`
ajoutbouton.addEventListener('click',function(){
const nouvelement= document.createElement('div')
nouvelement.classList.add('carte');
const header= document.createElement("header")
header.innerHTML= edit+poubelle
    
nouvelement.appendChild(header)
const text= document.createElement("textarea")
nouvelement.appendChild(text)
const container= document.querySelector(".cartes");
container.appendChild(nouvelement)
 });

document.addEventListener('click',function(){
    const cartes = document.querySelectorAll('.carte')

    cartes.forEach(carte => {
        const btns = carte.querySelectorAll("svg")
        btns.forEach((btn,i) => {
            btn.addEventListener('click',function(){
                if(i===0){
                    if(carte.lastChild.disabled){
                        carte.lastChild.disabled=false
                    }else{
                        carte.lastChild.disabled=true
                    }
                }else{
                    carte.remove()
                }
            })
        });
    });

})



//  nouvelement.innerHTML = `
//  <header></header>
//  <textarea name="" id=""></textarea>`