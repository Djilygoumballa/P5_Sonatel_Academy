function compte(){
let jour=document.querySelector("#jour")
let heure=document.querySelector("#heure")
let minute=document.querySelector("#minute")
let seconde=document.querySelector("#seconde")
var datearrivee=new Date("Jan 01, 2024 00:00:00").getTime()
var datedepart=new Date().getTime()

var difference=datearrivee-datedepart

var nb_jours = Math.floor(difference / (1000 * 60 * 60 * 24));
var nb_hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
var nb_minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
var nb_seconds = Math.floor((difference % (1000 * 60)) / 1000);

jour.textContent=nb_jours
heure.textContent=nb_hours
minute.textContent=nb_minutes
seconde.textContent=nb_seconds

setTimeout(compte,1000)
}
compte()