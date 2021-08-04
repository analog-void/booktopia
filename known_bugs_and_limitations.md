# Known Limitations and bugs
* Authors(model)  - една книга може да има повече от 1 автор, посоката на РЕЛ в ДБ трябва да се обърне /// не става ...
- save() от темплейт не създава рк директория. Да се помисли за post_save signal
  	- EMAIL AS FOLDER (SLUGIFY)
  	- REMOVE TEMPORARY
  	- 
- owner >>> to user
- TAGS - без реална употреба на този етап





# TODO:
***
## DESIGN / FRONTEND
- [ ] A CHANGER LE HEADER IMAGE AVEC UN TRUC DE BIBLIO
- [x] IS_OWNER IN BOOKS = ДА СЕ СЛОЖИ ПРЕДИ БУТОНИТЕ
- [ ] REVIEWS - A LES FINIR
    - [ ] VOIR COMMENT ÇA SE PASSE DANS LE MODELE EN RELATION AVEC

- [ ] A FUSIONNER COMMENTS AND REVIEWS TOUT SIMPLEMENT
LE REVIEW EST FAIT PAR ÉDITEUR

- [ ] METTRE UN BOUTON QUI AFFICHE UNE BOULE D'AIDE A COTE DES CHAMPS - UN POPUP?
- [ ] 
- [ ] PAGINATION SUR TOUTES LES PAGES (TABLES)
	- [ ] BOOKS
	- [ ] AUTEURS
	- [ ] PRES DE MOI
	- [ ] RESERVATIONS
	- [ ] PAST ...
	- [ ] MOUVEMENTS
	- [ ] COMMENTS

***
- [ ] RECHERCHE INTERNE
- [ ] DES STARS POUR LES BOUQUINS / COMMENTAIRES
- [ ] THUMBNAIL CREATION / IMAGE RESIZE / FORMAT CHANGE to PNG > PIP / OTHER

- [ ] VOIR LE JUMBOTRON
- [ ] a faire la page interne quant tu te log - les dermers bouquins, news etc
- [ ] A FIXER LE FOOTER
- [ ] 
- [ ] 
- [ ] 

да има селери/крон, който всеки ден проверява началната дата на заеманията (или три дни преди това) и ако има 
започваща или завършваща да се предлага в бонтитата като възмойност за взимане (да се посочи мястото за взимане в 
този случай)





***


## CRITICAL / BACKEND
- [ ] A FAIRE LE SYSTEME DE LOGIN
	- [ ] LOGIN FORM
	- [ ] REGISTER FORM
	- [ ] EDIT PROFILE FORM
	- [ ] EMAIL SEND ON CREATION
		- [ ] EMAIL CONFIRMATION OF THE ACCOUNT CREATION
	
- [x] DELETE BOOK
	- [ ] CHECK FOR PENDING RESERVATIONS, IF SO - MESSAGE THE USER, GIVE TOONS OF MESSAGES
	- [ ] CONFIRMATION POPUP (EN MODAL)


## VRAC
	# TODO: a ajouter plusieurs auteurs par livre,
	# agrandir le synopsis
	# Стойност на гаранцията (лв.): - Add value
	# Release year - DATE type
	# Con avec un API? > ISBN ET AUTRE
	# VOIR COMMENT LES CHOSES SONT FAITES A CHITANKA

	

# DONE
- [x] TAGS - ne marchent pas comme il faudrai
- DELETE - нещо не става потвърждението



