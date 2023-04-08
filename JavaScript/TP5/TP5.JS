const Quiz= [
    {
        question:"Quel est le meilleur langage de programmation en 2022",
        a:"Java",
        b:"C",
        c:"Python",
        d:"JavaScript",

        correct:"d"
    },

    {
        question: "Que signifie CSS?",
        a: "Central Style Sheets",
        b: "Cascading Style Sheets",
        c: "Cascading Simple Sheets",
        d: "Cars SUVs Sailboats",
        
        correct: "b",
      },

      {
        question: "Que signifie HTML",
        a: "Hypertext Markup Language",
        b: "Hypertext Markdown Language",
        c: "Hyperloop Machine Language",
        d: "Helicopters Terminals Motorboats Lamborginis",
        
        correct: "a",
      },


    {
        question:"En quelle année a été crée HTML?",
        a:"1990",
        b:"2000",
        c:"1995",
        d:"2015",

        correct:"a"
    },

    {
        question:"En quelle année a été crée JavaScript?",
        a:"1988",
        b:"2002",
        c:"1990",
        d:"1995",

        correct:"d"
    },
]

const questionnaire=document.querySelector('h3')
const soumettre=document.getElementById('soumettre')
soumettre.disabled=true
const resultats=document.getElementById('resultats')
let numeroquestion=0
const q=document.querySelector("#questionnaire")
const r=document.querySelector('p')
const inputs=document.querySelectorAll('input')
let compteur=0
let reponse
r.style.display='none'
ajoutelement(numeroquestion)
function ajoutelement(x){
    questionnaire.textContent=Quiz[x].question
    const labela=document.getElementById('a').nextElementSibling
    const labelb=document.getElementById('b').nextElementSibling
    const labelc=document.getElementById('c').nextElementSibling
    const labeld=document.getElementById('d').nextElementSibling
    labela.textContent=Quiz[x].a
    labelb.textContent=Quiz[x].b
    labelc.textContent=Quiz[x].c
    labeld.textContent=Quiz[x].d    
}
soumettre.addEventListener('click',function(){
    if(reponse==Quiz[numeroquestion]?.correct){
        compteur++
    }
    inputs.forEach(function(input){
        input.checked=false
    })
    soumettre.disabled=true
    numeroquestion++
    if (numeroquestion<Quiz.length){
        ajoutelement(numeroquestion)
    }
    else if(numeroquestion==Quiz.length){
        r.textContent=`Vous avez trouvé ${compteur} / ${Quiz.length} Questions.`
        r.style.backgroundColor="white"
        r.style.fontSize="30px"
        soumettre.textContent='Rejouer'
        q.style.display='none'
        r.style.display='block'
        soumettre.disabled=false
    }
    else{
        
        numeroquestion=0
        compteur =0
        ajoutelement(numeroquestion)
        soumettre.textContent="Soumettre"
        q.style.display='block'
        r.style.display='none'
    }

})


inputs.forEach(function( input){
    input.addEventListener('change',function(e){
        if(e.target.checked){
          reponse = e.target.value
          soumettre.disabled=false
        }else {
            reponse = ""
        }
    })
})


