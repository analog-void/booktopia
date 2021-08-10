#BookTopia
(ЛОГО)

Онлаин проект, представляващ виртуална библиотека за каталогитане, описване и размяна на книги. Проектът е част от 
модула на Softuni - Python Web Framework - юли 2021 (https://softuni.bg/trainings/3356/python-web-framework-july-2021#lesson-30207)



## Обобщение


- Голяма часто от съдържанието е написано на Български език
- Проектът ше бъде достъпен с демонтрационна цел на адрес: http://booktopia.analogvoid.org след 12.8.2021
- Файлът known_bugs_and_limitations.md съдържа описание на текущите задачи и описание на познати бъгове (на които до 
  този момент не е намерено решение)


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
- [x] Class-based views (50%)
- [x] Extended Django user
- [ ] Documentation/ Swagger
- [ ] Use a file storage cloud API e.g., Cloudinary, Dropbox, Google Drive or other for storing the files
- [ ] Implement Microservice architecture in your application.
- [ ] Additional functionality, not explicitly described in this section, will be counted as a bonus if it has practical usage.
