#BookTopia
(ЛОГО)
VictorP, analogvoid@protonmail.com

Онлаин проект, представляващ виртуална библиотека за каталогиране, продажба и заемане на книги. Проектът е част от 
модула на Softuni - Python Web Framework - юли 2021 (https://softuni.bg/trainings/3356/python-web-framework-july-2021)

Проектът, в неговият начален замисъл, по големина и времеемкост надмина възможностите на неговия автор. По време на 
защитата му ще бъде направен опит за обяснение на основният му замиисъл. 


## Обобщение
- Голяма часто от съдържанието е написано на Български език.
- Проектът ше бъде достъпен с демонтрационна цел на адрес: http://booktopia.analogvoid.com след 12.8.2021.
- Файлът known_bugs_and_limitations.md съдържа описание на текущите задачи и описание на познати бъгове (на които до 
  този момент не е намерено решение).
- Файлът used_resources.md показва използваните външни източниици на информация при изработката на настоящия проект.

## Функционалности

## Покрити Изисквания
**Mandatory requirements/Must haves**
- [x] The application must be implemented using Django Framework
- [x] The application must have at least 10 endpoints
- [x] The application must have login/register functionality
- [x] The application must have public part (A part of the website, which is accessible by everyone – 
  un/authenticated users and admins)
- [x] The application must have private part (accessible only by authenticated user and admins)
- [x] The application must have admin part (accessible only to admins)
- [x] Unauthenticated users (public part) have only 'get' permissions e.g., landing page, details, about page
- [x] Authenticated users (private part) have full CRUD for all their created content
- [x] Admins have full CRUD functionalities
- [ ] Form validations
- [ ] To avoid crashes, implement Error Handling and Data Validations
- [x] Use PostgreSQL as a database.
- [ ] Write tests for at least 60% coverage on your business logic
- [x] Templates (your controllers/views must return HTML files) – one and the same template could be re-used/used 
  multiple times (with the according adjustments, if such needed)
- [x] Use a source control system by choice – Github or Gitlab. You must have at least 5 commits + README

**Optional/Bonuses**
- [x] Responsive web design 
- [x] Class-based views (<30%)
- [x] Extended Django user
- [ ] Documentation/ Swagger (>50%)
- [ ] Use a file storage cloud API e.g., Cloudinary, Dropbox, Google Drive or other for storing the files
- [ ] Implement Microservice architecture in your application.
- [ ] Additional functionality, not explicitly described in this section, will be counted as a bonus if it has practical usage.


**Добавени и имплементирани външни библиотеки**
- django-grappelli - Редизайн на панела за администрация
- django-import-export - въвеждане/извеждане на реални външни данни
- django-taggit - Вътрешна тагова йерархия
- django-widget-tweaks - Туикове на генерирани форми 
- egn - Дейности с ЕГН
- qrcode - Библиотека за генериране на QR код


**Специфични функции и/или функционалнности**
- regex проверка за валиден БГ мобилен телефонен номер
- ЕГН - извличане на пол, рожденна дата, административна област на раждане, зодиакален знак
- Вътрешна система за класиране, според броя на добавени книги и коментари
- Генериране на уникален код за всяка книга, както и код за генериране на QR изображение
- Процент на завършеност на регистрацията на нов потребител
- 

