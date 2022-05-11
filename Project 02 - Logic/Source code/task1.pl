/*FACT*/
/*gender*/
female(elizabethii).

female(diana).
female(camillia).
female(sarah).
female(anne).
female(sophie).

female(kate).
female(meghan).
female(eugenie).
female(beatrice).
female(autumn).
female(zara).
female(lady).

female(charlotte).
/*----------------------------*/
male(philip).

male(charles).
male(andrew).
male(mark).
male(timothy).
male(edward).

male(william).
male(harry).
male(peter).
male(mike).
male(james).

male(george).
male(louis).
male(archie).
/*relationship*/
married(elizabethii,philip).

married(charles,camillia).
married(andrew,sarah).
married(timothy,anne).
married(edward,sophie).

married(william,kate).
married(harry,meghan).
married(peter,autumn).
married(zara,mike).
/*----------------------------*/
divorced(charles,diana).
divorced(mark, anne).
/*----------------------------*/
parent(philip,charles).
parent(elizabethii,charles).
parent(philip,andrew).
parent(elizabethii,andrew).
parent(philip, anne).
parent(elizabethii,anne).
parent(philip,edward).
parent(elizabethii,edward).

parent(charles,william).
parent(diana,william).
parent(charles,harry).
parent(diana,harry).
parent(andrew,eugenie).
parent(sarah,eugenie).
parent(andrew,beatrice).
parent(sarah,beatrice).
parent(mark,peter).
parent(anne,peter).
parent(mark,zara).
parent(anne,zara).
parent(edward,lady).
parent(sophie,lady).
parent(edward,james).
parent(sophie,james).

parent(william,george).
parent(kate,george).
parent(william,charlotte).
parent(kate,charlotte).
parent(william,louis).
parent(kate,louis).
parent(harry,archie).
parent(meghan,archie).
/*RULES*/
father(X,Y) :- parent(X,Y), male(X).
mother(X,Y) :- parent(X,Y), female(X).
child(X,Y) :- parent(Y,X).
son(X,Y) :- parent(Y,X), male(X).
daughter(X,Y) :- parent(Y,X), female(X).
grandparent(X,Y) :- parent(X,Z), parent(Z,Y).
grandmother(X,Y) :- parent(X,Z), parent(Z,Y), female(X).
grandfather(X,Y) :- parent(X,Z), parent(Z,Y), male(X).
grandchild(X,Y) :- parent(Y,Z), parent(Z,X).
granddaughter(X,Y) :- parent(Y,Z), parent(Z,X), female(X).
grandson(X,Y) :- parent(Y,Z), parent(Z,X), male(X).
spouce(X,Y) :- married(X,Y); married(Y,X).
husband(X,Y) :- male(X), spouce(X,Y).
wife(X,Y) :- female(X), spouce(Y,X).
sibling(X,Y) :- child(X,Z), child(Y,Z).
brother(X,Y) :- child(X,Z), child(Y,Z), male(X), dif(X,Y).
sister(X,Y) :- child(X,Z), child(Y,Z), female(X).
uncle(X,Y) :-  parent(Z,Y), (brother(X,Z) ; (sibling(Z,H), married(X,H), male(X))). 
aunt(X,Y) :- parent(Z,Y), (sister(X,Z); (sibling(Z,H), married(H,X), female(X))).
nephew(X,Y) :- sibling(Z,Y), child(X,Z), male(X).
niece(X,Y) :- sibling(Z,Y), child(X,Z), female(X).
firstcousin(X,Y) :- sibling(Z,H), child(X,Z), child(Y,H), dif(Y,X).