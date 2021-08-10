https://github.com/analog-void/booktopia/
***
# Known Limitations and bugs
* Authors(model)  - една книга може да има повече от 1 автор, посоката на РЕЛ в ДБ трябва да се обърне /// не става ...
- save() от темплейт не създава рк директория. Да се помисли за post_save signal
  	- EMAIL AS FOLDER (SLUGIFY)
  	- REMOVE TEMPORARY
  	- 
- owner >>> to user
- TAGS - без реална употреба на този етап
- Автори - държавата за раждане не се появява в изгледа. да се направи querryset()
- ЕГН - веднъж въведено, да не може повече да се достъпва до линка за въвеждане



# TODO:

## DESIGN / FRONTEND
- [ ] SCORING - ЕВОЛЮЦИЯ НА ПОТРЕБИТЕЛИТЕ И ГЕНЕРИРАНЕ НА РЕЙТИНГ СПОРЕД КОМЕНТАРИ И КНИГИ
- [ ] REGEX ВАЛИДАТОР НА ТЕЛЕФОНЕН НОМЕР БГ
- [ ] СМЯНА НА ХЕДЪРА С РАЗЛИЧЕН СТОКФОТО (JUMBOTRON)
- [ ] ДА СЕ ПОКАЗВА ИМЕТО НА ПОТРЕБИТЕЛЯ В ТАБЛИЦАТА С КНИГИТЕ
  - [ ] ДА СЕ ДОБАВИ КОГА Е ДОБАВЕНА КНИГАТА
  
- [x] IS_OWNER IN BOOKS = ДА СЕ СЛОЖИ ПРЕДИ БУТОНИТЕ
- [ ] REVIEWS / COMMENTS - ДА СЕ НАПРАВИ ФОРМА, ДА СЕ МЪРДЖНАТ
	- [ ] ДА НЕ МОЖЕ СОБСТВЕНИКА ДА КОМЕНТИРА СОБСТВЕНАТА СИ КНИГА
    - [ ] ДА СЕ ВИДИ КАК ТОЧНО СЕ СЛУЧВАТ НЕЩАТА В АДММИН

- [ ] ДА СЕ ОПИШЕ ТЕКСТ ЗА РЕВЮТО - ЧЕ Е ЗАДЪЛЖИТЕЛНО
- [ ] ДА НЕ НАПРАВЯТ БУТОНИ ЗА ИЗБОР НА РОЛЯ ПО ВРЕМЕ НА РЕГИСТРТАЦИЯТА

- [ ] METTRE UN BOUTON QUI AFFICHE UNE BOULE D'AIDE A COTE DES CHAMPS - UN POPUP?
- [ ] PAGINATION НА СТРАНИЦИТЕ (TABLES)
	- [ ] BOOKS
	- [ ] AUTEURS
	- [ ] PRES DE MOI
	- [ ] RESERVATIONS
	- [ ] PAST ...
	- [ ] MOUVEMENTS
	- [ ] COMMENTS

***
- [ ] ВЪТРЕШНА ТЪРСАЧКА
- [ ] ДА СЕ ПРОВЕРЯТ ТЪРСЕНИЯТА В АДМИН   
- [ ] THUMBS UP / DOWN ЗА КОМЕНТАРИТЕ
- [ ] ЗВЕЗДИЧКИ ЗА ЕВАЛ НА КНИГАТА 
- [ ] THUMBNAIL CREATION / IMAGE RESIZE / FORMAT CHANGE to PNG > PIP / OTHER

- [ ] a faire la page interne quant tu te log - les dermers bouquins, news etc
- [ ] ДА СЕ ОПРАВЯТ ЛИНКОВЕТЕ ВЪВ ФУТЪРА

да има селери/крон, който всеки ден проверява началната дата на заеманията (или три дни преди това) и ако има 
започваща или завършваща да се предлага в бонтитата като възмойност за взимане (да се посочи мястото за взимане в 
този случай)




## CRITICAL / BACKEND
- [ ] FAIRE UN AUTRE MENU, AQUAND LES GENS ONT PAS ENCORE DE PROFIL (MENU)

- [ ] A VIRER LES OWNERS
  STATUS HISTORY
  

- [ ] FAIRE LA BIZLOGIC LORS DE LA CONNEXION 
- [X] A FAIRE LE SYSTEME DE LOGIN
	- [X] LOGIN FORM
	- [X] REGISTER FORM
	- [X] EDIT PROFILE FORM
	- [X] EGN CHECKER
	  
	- [ ] EMAIL SEND ON CREATION
		- [ ] EMAIL CONFIRMATION OF THE ACCOUNT CREATION
	
- [x] DELETE BOOK
	- [ ] CHECK FOR PENDING RESERVATIONS, IF SO - MESSAGE THE USER, GIVE TOONS OF MESSAGES
	- [ ] CONFIRMATION POPUP (EN MODAL)




## ADMIN
REFAIRE LES VIEWS POUR:
- Потребителски Акаунти
- Автори
- Издателства
- История на заеманията
- Коментари


## VRAC
	# TODO: a ajouter plusieurs auteurs par livre,
	# agrandir le synopsis
	# Стойност на гаранцията (лв.): - Add value
	# Release year - DATE type
	# Con avec un API? > ISBN ET AUTRE
	# VOIR COMMENT LES CHOSES SONT FAITES A CHITANKA


# DONE
- DELETE - нещо не става потвърждението

