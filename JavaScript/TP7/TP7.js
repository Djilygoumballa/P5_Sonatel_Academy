const APIURL ="https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1  ";
const IMGPATH = "https://image.tmdb.org/t/p/w1280";
const SEARCHAPI ="https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query=";

const contenants=document.getElementById("contenants")

fetch(APIURL)
.then(reponse=>reponse.json())
.then(donnee=>{
    donnee.results.forEach(film => {
        console.log(film)
        affichage(film)       
    })}) 
function affichage(film){
     // creation d'image pour contenir l'image de chaque film
     const image=document.createElement('img')
     image.classList.add('image')

 
     
     // creation d'un div pour l'overview de chaque film
     const para=document.createElement('div')
     para.classList.add('text')

    
     // ensemble contenant l'overview et l'image de chaque film
     const ensemble=document.createElement('div')
     ensemble.appendChild(image)
     ensemble.appendChild(para)


     // creation de l'ensemble contenant toutes les informations des films
     const contenant=document.createElement('div')
     contenant.classList.add('film')


     // creation d'un titre de niveau h3 pour le titre de chaque film 
     const titre=document.createElement('h3')
     titre.classList.add('info')
     
     
     // recuperation des notes des films
     const note=document.createElement('p')
     note.classList.add('not')
     if(film.vote_average>=8){
         note.style.color="lightgreen"
     }
     if(film.vote_average<8){
         note.style.color="orange"
     } 
     
     
     // ensemble contenan le titre et la note pour chaque film
     const infos=document.createElement('div')
     infos.appendChild(titre)
     infos.appendChild(note)
     infos.classList.add('description')
 
     
     // recuperation des informations des films
     image.src=IMGPATH+film.poster_path
     titre.textContent=film.title
     note.textContent=film.vote_average
     para.textContent=film.overview
     
     
     // le contenant d'un film
     contenant.appendChild(ensemble)
     contenant.appendChild(infos)


     // afficher la description
    
     contenant.addEventListener('mouseover',function(){
         para.style.display='block'
         image.style.opacity='.5'
     })
     contenant.addEventListener('mouseout',function(){
         para.style.display='none'
         image.style.opacity='1'
     })
     
     // le contenant de l'ensemble des films
     contenants.appendChild(contenant)
}





const recherche=document.querySelector("#recherche input")
recherche.addEventListener("input",() =>{
    cherche(recherche.value.toLowerCase())
})

function cherche(x){
    fetch(APIURL)
    .then(reponse=>reponse.json())
    .then(donnee=> {
        contenants.innerHTML=""
        donnee.results.forEach(film => {
            if(film.title.toLowerCase().includes(x)){
                affichage(film)
            }
            
        })})
}

