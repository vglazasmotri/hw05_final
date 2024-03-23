<h1 align=center>🌟Практика применения Unittest в Django🌟</h1>

## 📄 **Описание - Тесты для проекта Yatube**


<div class="Markdown base-markdown base-markdown_with-gallery markdown markdown_size_normal markdown_type_theory full-markdown"><h3>Тестирование Models: <strong>«</strong>Unittest в Django: тестирование моделей<strong>»</strong></h3><div class="paragraph">Протестируйте модели приложения <strong>posts</strong> в <strong>Yatube</strong>.</div><div class="paragraph">Добавьте в классы <strong>Post</strong> и <strong>Group</strong> метод <code class="code-inline code-inline_theme_light"><svg class="code-inline__check-icon" width="16" height="16" viewBox="0 0 16 16" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.6805 3.76721C14.0852 4.14301 14.1086 4.77574 13.7328 5.18046L7.23281 12.1805C7.0401 12.388 6.76842 12.5041 6.48524 12.4999C6.20206 12.4957 5.93393 12.3716 5.74744 12.1585L2.24744 8.15851C1.88375 7.74287 1.92587 7.11111 2.34151 6.74743C2.75715 6.38375 3.38891 6.42586 3.75259 6.8415L6.52208 10.0066L12.2672 3.81955C12.643 3.41484 13.2758 3.39141 13.6805 3.76721Z" fill="currentColor" fill-opacity="0.85"></path></svg><span class="code-inline__content">__str__</span></code> (если его ещё нет):</div><ul><li>для класса <strong>Post</strong> — первые пятнадцать символов поста: <code class="code-inline code-inline_theme_light"><svg class="code-inline__check-icon" width="16" height="16" viewBox="0 0 16 16" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.6805 3.76721C14.0852 4.14301 14.1086 4.77574 13.7328 5.18046L7.23281 12.1805C7.0401 12.388 6.76842 12.5041 6.48524 12.4999C6.20206 12.4957 5.93393 12.3716 5.74744 12.1585L2.24744 8.15851C1.88375 7.74287 1.92587 7.11111 2.34151 6.74743C2.75715 6.38375 3.38891 6.42586 3.75259 6.8415L6.52208 10.0066L12.2672 3.81955C12.643 3.41484 13.2758 3.39141 13.6805 3.76721Z" fill="currentColor" fill-opacity="0.85"></path></svg><span class="code-inline__content">post.text[:15]</span></code>;</li><li>для класса <strong>Group</strong> — название группы.</li></ul><div class="paragraph">Протестируйте, правильно ли отображается значение поля <code class="code-inline code-inline_theme_light"><svg class="code-inline__check-icon" width="16" height="16" viewBox="0 0 16 16" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.6805 3.76721C14.0852 4.14301 14.1086 4.77574 13.7328 5.18046L7.23281 12.1805C7.0401 12.388 6.76842 12.5041 6.48524 12.4999C6.20206 12.4957 5.93393 12.3716 5.74744 12.1585L2.24744 8.15851C1.88375 7.74287 1.92587 7.11111 2.34151 6.74743C2.75715 6.38375 3.38891 6.42586 3.75259 6.8415L6.52208 10.0066L12.2672 3.81955C12.643 3.41484 13.2758 3.39141 13.6805 3.76721Z" fill="currentColor" fill-opacity="0.85"></path></svg><span class="code-inline__content">__str__</span></code> в объектах моделей.  </div><h3>Тестирование URLs: <strong>«</strong>Unittest в Django: тестирование URLs<strong>»</strong></h3><div class="paragraph">Проверьте доступность страниц и названия шаблонов приложения <strong>Posts</strong> проекта <strong>Yatube.</strong> Проверка должна учитывать права доступа. </div><div class="paragraph">Проверьте, что запрос к несуществующей странице вернёт ошибку 404.</div><div class="paragraph"><div class="downloadable-image"><a class="downloadable-image__button" download="Image.png"><svg class="icon icon-arrows-24-download downloadable-image__icon" width="24" height="24" viewBox="0 0 24 24" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3C11.45 3 11 3.45 11 4V10.9219C11 11.6763 11.0854 12.4276 11.254 13.1613L11.0483 13.3684L10.8331 13.0242C10.4323 12.3835 9.96022 11.7902 9.42583 11.2558L8.46 10.29C8.07 9.89999 7.44 9.89999 7.05 10.29C6.66 10.68 6.66 11.32 7.05 11.71L10.9404 15.5926C11.526 16.1769 12.474 16.1769 13.0596 15.5926L16.95 11.71C17.34 11.32 17.34 10.68 16.95 10.29C16.56 9.89999 15.93 9.89999 15.54 10.29L14.5742 11.2558C14.0398 11.7902 13.5677 12.3835 13.1669 13.0242L12.9517 13.3684L12.746 13.1613C12.9146 12.4276 13 11.6763 13 10.9219V4C13 3.45 12.55 3 12 3ZM7 19C6.44772 19 6 19.4477 6 20C6 20.5523 6.44772 21 7 21H17C17.5523 21 18 20.5523 18 20C18 19.4477 17.5523 19 17 19H7Z" fill="currentColor" fill-opacity="0.85"></path></svg></a><img src="https://pictures.s3.yandex.net:443/resources/S05_01_1629250721.png" alt="image" crossorigin="anonymous" class="image image_expandable"></div></div><h3>Проверка namespace:name и шаблонов: <strong>«</strong>Unittest в Django: тестирование Views<strong>»</strong></h3><div class="paragraph">Напишите тесты, проверяющие, что во view-функциях используются правильные html-шаблоны.</div><div class="paragraph"><div class="downloadable-image"><a class="downloadable-image__button" download="Image.png"><svg class="icon icon-arrows-24-download downloadable-image__icon" width="24" height="24" viewBox="0 0 24 24" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3C11.45 3 11 3.45 11 4V10.9219C11 11.6763 11.0854 12.4276 11.254 13.1613L11.0483 13.3684L10.8331 13.0242C10.4323 12.3835 9.96022 11.7902 9.42583 11.2558L8.46 10.29C8.07 9.89999 7.44 9.89999 7.05 10.29C6.66 10.68 6.66 11.32 7.05 11.71L10.9404 15.5926C11.526 16.1769 12.474 16.1769 13.0596 15.5926L16.95 11.71C17.34 11.32 17.34 10.68 16.95 10.29C16.56 9.89999 15.93 9.89999 15.54 10.29L14.5742 11.2558C14.0398 11.7902 13.5677 12.3835 13.1669 13.0242L12.9517 13.3684L12.746 13.1613C12.9146 12.4276 13 11.6763 13 10.9219V4C13 3.45 12.55 3 12 3ZM7 19C6.44772 19 6 19.4477 6 20C6 20.5523 6.44772 21 7 21H17C17.5523 21 18 20.5523 18 20C18 19.4477 17.5523 19 17 19H7Z" fill="currentColor" fill-opacity="0.85"></path></svg></a><img src="https://pictures.s3.yandex.net:443/resources/Untitled_2_1629250743.png" alt="image" crossorigin="anonymous" class="image image_expandable"></div></div><h3>Тестирование контекста: <strong>«</strong>Unittest в Django: тестирование views<strong>»</strong></h3><div class="paragraph">Проверьте, соответствует ли ожиданиям словарь <code class="code-inline code-inline_theme_light"><svg class="code-inline__check-icon" width="16" height="16" viewBox="0 0 16 16" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.6805 3.76721C14.0852 4.14301 14.1086 4.77574 13.7328 5.18046L7.23281 12.1805C7.0401 12.388 6.76842 12.5041 6.48524 12.4999C6.20206 12.4957 5.93393 12.3716 5.74744 12.1585L2.24744 8.15851C1.88375 7.74287 1.92587 7.11111 2.34151 6.74743C2.75715 6.38375 3.38891 6.42586 3.75259 6.8415L6.52208 10.0066L12.2672 3.81955C12.643 3.41484 13.2758 3.39141 13.6805 3.76721Z" fill="currentColor" fill-opacity="0.85"></path></svg><span class="code-inline__content">context</span></code>, передаваемый в шаблон при вызове.</div><div class="paragraph"><div class="downloadable-image"><a class="downloadable-image__button" download="Image.png"><svg class="icon icon-arrows-24-download downloadable-image__icon" width="24" height="24" viewBox="0 0 24 24" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3C11.45 3 11 3.45 11 4V10.9219C11 11.6763 11.0854 12.4276 11.254 13.1613L11.0483 13.3684L10.8331 13.0242C10.4323 12.3835 9.96022 11.7902 9.42583 11.2558L8.46 10.29C8.07 9.89999 7.44 9.89999 7.05 10.29C6.66 10.68 6.66 11.32 7.05 11.71L10.9404 15.5926C11.526 16.1769 12.474 16.1769 13.0596 15.5926L16.95 11.71C17.34 11.32 17.34 10.68 16.95 10.29C16.56 9.89999 15.93 9.89999 15.54 10.29L14.5742 11.2558C14.0398 11.7902 13.5677 12.3835 13.1669 13.0242L12.9517 13.3684L12.746 13.1613C12.9146 12.4276 13 11.6763 13 10.9219V4C13 3.45 12.55 3 12 3ZM7 19C6.44772 19 6 19.4477 6 20C6 20.5523 6.44772 21 7 21H17C17.5523 21 18 20.5523 18 20C18 19.4477 17.5523 19 17 19H7Z" fill="currentColor" fill-opacity="0.85"></path></svg></a><img src="https://pictures.s3.yandex.net:443/resources/Untitled_3_1629250762.png" alt="image" crossorigin="anonymous" class="image image_expandable"></div></div><h3>Дополнительная проверка при создании поста: <strong>«</strong>Unittest в Django: тестирование Views<strong>»</strong></h3><div class="paragraph">Проверьте, что если при создании поста указать группу, то этот пост появляется </div><ul><li>на главной странице сайта,</li><li>на странице выбранной группы,</li><li>в профайле пользователя.</li></ul><div class="paragraph">Проверьте, что этот пост не попал в группу, для которой не был предназначен.</div><h3>Тестирование Forms: <strong>«</strong>Unittest в Django: тестирование Forms<strong>»</strong></h3><div class="paragraph">В проекте <strong>Yatube</strong> напишите тесты, которые проверяют, что</div><ul><li>при отправке валидной формы со страницы создания поста <code class="code-inline code-inline_theme_light"><svg class="code-inline__check-icon" width="16" height="16" viewBox="0 0 16 16" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.6805 3.76721C14.0852 4.14301 14.1086 4.77574 13.7328 5.18046L7.23281 12.1805C7.0401 12.388 6.76842 12.5041 6.48524 12.4999C6.20206 12.4957 5.93393 12.3716 5.74744 12.1585L2.24744 8.15851C1.88375 7.74287 1.92587 7.11111 2.34151 6.74743C2.75715 6.38375 3.38891 6.42586 3.75259 6.8415L6.52208 10.0066L12.2672 3.81955C12.643 3.41484 13.2758 3.39141 13.6805 3.76721Z" fill="currentColor" fill-opacity="0.85"></path></svg><span class="code-inline__content">reverse('posts:create_post')</span></code> создаётся новая запись в базе данных;</li><li>при отправке валидной формы со страницы редактирования поста <code class="code-inline code-inline_theme_light"><svg class="code-inline__check-icon" width="16" height="16" viewBox="0 0 16 16" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.6805 3.76721C14.0852 4.14301 14.1086 4.77574 13.7328 5.18046L7.23281 12.1805C7.0401 12.388 6.76842 12.5041 6.48524 12.4999C6.20206 12.4957 5.93393 12.3716 5.74744 12.1585L2.24744 8.15851C1.88375 7.74287 1.92587 7.11111 2.34151 6.74743C2.75715 6.38375 3.38891 6.42586 3.75259 6.8415L6.52208 10.0066L12.2672 3.81955C12.643 3.41484 13.2758 3.39141 13.6805 3.76721Z" fill="currentColor" fill-opacity="0.85"></path></svg><span class="code-inline__content">reverse('posts:post_edit', args=('post_id',))</span></code> происходит изменение поста с <code class="code-inline code-inline_theme_light"><svg class="code-inline__check-icon" width="16" height="16" viewBox="0 0 16 16" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.6805 3.76721C14.0852 4.14301 14.1086 4.77574 13.7328 5.18046L7.23281 12.1805C7.0401 12.388 6.76842 12.5041 6.48524 12.4999C6.20206 12.4957 5.93393 12.3716 5.74744 12.1585L2.24744 8.15851C1.88375 7.74287 1.92587 7.11111 2.34151 6.74743C2.75715 6.38375 3.38891 6.42586 3.75259 6.8415L6.52208 10.0066L12.2672 3.81955C12.643 3.41484 13.2758 3.39141 13.6805 3.76721Z" fill="currentColor" fill-opacity="0.85"></path></svg><span class="code-inline__content">post_id</span></code> в базе данных.</li></ul></code></div></div>
<br>
<br>

## 🛠️ Инструкция по установке
___
### Установка на локальный компьютер.

Клонируйте репозиторий:

```
git clone git@github.com:vglazasmotri/проект.git
```

```
cd проект
```

Устанавливаем виртуальное окружение:

```
python -m venv venv
```

Активируем виртуальное окружение:
```
source venv/Scripts/activate
```

Обновляем Pip:
```
python -m pip install --upgrade pip
```
Устанавливаем зависимости:
```
pip install -r requirements.txt
```

Запускаем:
```
python manage.py test
```

Готово!


<br>
<br>

## 🎞️ Примеры



Запустит все тесты проекта
```
python3 manage.py test
```

Запустит только тесты в приложении posts
```
python3 manage.py test posts
```

Запустит только тесты из файла test_urls.py в приложении posts
```
python3 manage.py test posts.tests.test_urls
```

Запустит только тесты из класса StaticURLTests для test_urls.py в приложении posts  
```
python3 manage.py test posts.tests.test_urls.StaticURLTests
```

Запустит только тест test_homepage()
из класса StaticURLTests для test_urls.py в приложении posts 
```
python3 manage.py test posts.tests.test_urls.StaticURLTests.test_homepage
```

## 🛠️ Применяемые технологии:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
- Python 3.7
- Django 3.2


## 💪 Автор:

- Сергей Сыч Python-разработчик (https://github.com/vglazasmotri)
