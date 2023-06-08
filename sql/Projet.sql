-- alias
select C.nom,C.adr from contribuable as C,declaration as D
    where C.ncont=D.ncont
    and D.libelle='publicité';

-- sous-requete
 select tel,nom,date from contribuable,payer_amende
    where contribuable.ncont=payer_amende.ncont
    and date<= all(select date from payer_amende)

-- o Fonctions d'agrégation
-- - SUM

select C.tel,C.nom,A.libelle,sum(A.montant) from contribuable as C,payer_amende as PM,amende as A
    where C.ncont=PM.ncont and A.namende=PM.namende
    group by C.tel,C.nom,A.libelle;

-- AVG

select C.nom,C.tel,avg(T.montant) 
    from contribuable as C,taxes as T,payer_taxe as PT
    where C.ncont=PT.ncont
    and T.ntaxe=PT.ntaxe
    group by C.nom,C.tel

-- MIN

select C.tel,C.nom,A.libelle,A.montant
    from contribuable as C,payer_amende as PM,amende as A
    where C.ncont=PM.ncont and A.namende=PM.namende
    and A.montant=(select min(montant) from amende);

-- MAX
select C.tel,C.nom,T.type,T.montant
    from contribuable as C,payer_taxe as PT,taxes as T
    where C.ncont=PT.ncont
    and T.ntaxe=PT.ntaxe
    and T.montant=(select max(montant) from taxes);

-- ORDER BY
select C.tel,C.nom,T.type,T.montant
    from contribuable as C,payer_taxe as PT,taxes as T
    where C.ncont=PT.ncont
    and T.ntaxe=PT.ntaxe
    and T.montant=(select max(montant) from taxes)
    order by PT.date
    limit 5;

-- GROUP BY
select C.nom,T.type,sum(T.montant)
    from contribuable as C,payer_taxe as PT,taxes as T
    where C.ncont=PT.ncont
    and T.ntaxe=PT.ntaxe
    and PT.date='2020-06-05'
    group by C.nom,T.type;

-- HAVING

select C.nom,C.tel
    from contribuable as C,declaration as D,payer_amende as PM,amende as A
    where C.ncont=PM.ncont
    and D.ncont=C.ncont
    and A.namende=PM.namende
    and D.libelle='spectacle'
    group by C.nom,C.tel
    having round(sum(A.montant))>500000;

-- union
select type,sum(T.montant) as totaux
    from declaration as D,payer_taxe as PT,taxes as T
    where D.ncont=PT.ncont
    and T.ntaxe=PT.ntaxe
    and T.type='spectacle'
    union
    select type,sum(T.montant) as totaux
    from declaration as D,payer_taxe as PT,taxes as T
    where D.ncont=PT.ncont
    and T.ntaxe=PT.ntaxe
    and T.type='publicite'
    ;

-- round
select C.nom,C.tel,round(sum(A.montant))
    from contribuable as C,declaration as D,payer_amende as PM,amende as A
    where C.ncont=PM.ncont
    and D.ncont=C.ncont
    and A.namende=PM.namende
    and D.libelle='spectacle'
    group by C.nom,C.tel
    having round(sum(A.montant))>500000;

-- DISTINCT
select C.nom,C.tel
    from contribuable C
    where C.ncont not in(select distinct ncont from payer_amende);


-- LIMIT
select C.nom,C.tel,sum(T.montant)
    from contribuable as C,taxes as T,payer_taxe as PT
    where C.ncont=PT.ncont
    and T.ntaxe=PT.ntaxe
    group by C.nom,C.tel
    order by sum(T.montant) DESC
    limit 1;

-- LIKE %% (B%A)
select * 
    from contribuable
    where adr like '%Paris%';

-- IN not in
select C.nom,C.tel
        from contribuable C
        where C.ncont not in(select ncont from payer_amende);

-- between
select C.tel,C.nom
    from contribuable as C,declaration as D
    where C.ncont=D.ncont
    and ((D.date between '2020-04-04' and '2020-04-15') or (D.date between '2020-05-19' and '2020-05-25'))



select C.nom,C.tel,month(P.date) as mois,sum(T.montant) as total
    from contribuable as C,payer_taxe as P,taxes as T
    where C.ncont=P.ncont
    and P.ntaxe=T.ntaxe
    group by C.nom,C.tel,mois
    order by C.nom;


select *
    from contribuable
    where length(nom) between 4 and 6;
l      from contribuable as C,declaration as D,payer_amende as PM,amende as A      where C.ncont=PM.ncont      and D.ncont=C.ncont      and A.namende=PM.namende      and D.libelle='spectacle'      group by C.nom,C.^C    having round(sum(A.montant))>500000;



SELECT nom, tel 
FROM contribuable c, declaration d
WHERE c.ncont = d.ncont 
AND date BETWEEN '2020-04-04'AND '2020-04-15'
UNION SELECT nom, tel 
FROM contribuable c, declaration d
WHERE c.ncont = d.ncont 
AND date BETWEEN '2020-05-19'AND '2020-05-25'

select * from taxes;