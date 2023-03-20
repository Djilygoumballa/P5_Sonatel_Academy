library(stringr)
options(max.print = 1000000)
lect<- read.csv("Donnees_Projet_Python_DataC5.csv",sep=',',dec='.')
lect
View(lect)
lect[lect==""]<-NA
View(lect)
which(is.na(lect),arr.ind = T)
colnum<- lect[,2]
colnum
lect<- na.omit(lect$Numero)
View(lect)
# lect
# dim(lect)
# names(lect)
# str(lect)
# class(lect)
# View(lect)
# summary(lect)
# lect$CODE
validnum<- function(numero){
  
  if ((nchar(numero)==7) && (grepl("[[:upper:]][[:digit:]]",numero))){
    return(T)
  } else{
    return(F)
  }
}
validnum("A1111A1")


isvalidnom<- function(nom){
  
  if(substring(nom,1,1) %in% c(LETTERS,letters)){
    for (i in 2:nchar(nom)){
      if (substring(nom,i,i) %in% c(LETTERS,letters)){
        return(T)
      }else{
        return(F)
      }
    }
  }else{
  return(F)
  }
}
isvalidnom("aA111")
isvalidprenom<- function(prenom){
  if(substring(prenom,1,1) %in% c(LETTERS,letters)){
    s=1
    for (i in 2:nchar(prenom)){
      if (substring(prenom,i,i) %in% c(LETTERS,letters)){
        s=s+1
      }
    }
    if (s >=3){
      return(T)
    }else{
      return(F)
    }
  }else{
    return(F)
  }
}
isvalidprenom("A11AA")  

isvalidclass<- function(classe){
  for(i in(1:nchar(classe))){
    classe<-trimws(classe)
    #gsub(" ","",classe)
    if(substring(classe,1,1) %in% c(3:6) && substring(classe,nchar(classe),nchar(classe)) %in% c("A","B")){
      q<-paste(substring(classe,1,1),substring(classe,nchar(classe),nchar(classe)),sep="em")
      return(q)
    }else{
      return(F)
    }
  }
}
isvalidclass("     3 rB    ")

validdate<- function(date){
  #,"-"="/","_"="/",","="/","\\|"="/",":"="/","."="/"
  date<- trimws(date)
  date<- str_replace_all(date,c("fev"="02","mars"="03","decembre"="12"))
  date<- str_replace_all(date,c(" "="/","-"="/",","="/","_"="/","\\|"="/",":"="/","\\."="/"))
  if(!is.na(as.Date(date,format("%d/%m/%Y")))){
    return(date)
  }else{
    return(F)
  }
 
}
validdate("          01.mars.2004")
validnote<- function(note){
   note<- str_split(note,"#")
   print(length(note[[1]]))
   print(note[[1]][1])
   # for(i in note){
   #   note<- str_replace_all(i,c("\\["=":","\\|"=":","]"=":",";"=":",","="."))
   #   note<- str_split(note,":")
     
     return(note)
   
   # note<- str_replace_all(note,c("["=":","\\|"=":","]"=":",";"=":",","="."))
   # note<- str_split(note,":")
   
    # c=nott[1][1]
    # # d=c[[1]]
    # # 
   
}
a<-"Math[11|13:06]#Francais[08|17:12] #Anglais[13|13:12] #PC[09|18:07] #SVT[15|10:10] #HG[14|19:17]"
b<-validnote(a)
lb
for(n in b){
  print((n[1]))
  print(length(n[[1]]))
  
}

# (b[[1]])
# b
# [[2]]
# b[1][1]
# kl<- "rdes"
# substring(kl,1)
