# Проект по тестированию главной страницы сайта *[nexign.com](https://nexign.com/)*
![This is an image](design/main_page.png)
## Список проверок
 - Проверка перехода на страницу *Контакты*;
 - Проверка перехода на домашнюю страницу через логотип;
 - Проверка сменяемости языка;
 - Проверка наличия пунктов меню;
 - Проверка функции поиска статей.

## Технoлoгии и инструмeнты
<p align="center">
<a href="https://www.python.org/"><img src="design/icons/python.svg" width="50" height="50"  alt="Python" title="Python"/></a>
<a href="https://docs.pytest.org/"><img src="design/icons/pytest.svg" width="50" height="50"  alt="PyTest" title="PyTest"/></a>
<a href="https://www.selenium.dev//"><img src="design/icons/selenium.svg" width="50" height="50"  alt="Selenium" title="Selenium"/></a>
<a href="https://aerokube.com/selenoid/"><img src="design/icons/selenoid.png" width="50" height="50"  alt="Selenoid" title="Selenoid"/></a>
<a href="https://www.jenkins.io/"><img src="design/icons/jenkins.svg" width="50" height="50"  alt="Jenkins" title="Jenkins"/></a>
<a href="https://qameta.io/allure-report/"><img src="design/icons/allure.png" width="50" height="50"  alt="allure-report" title="allure-report"/></a>
<a href="https://qameta.io/allure-report/"><img src="design/icons/allure_testops.png" width="50" height="50"  alt="allure-report" title="allure-report"/></a>
<a href="https://github.com/"><img src="design/icons/github.png" width="50" height="50"  alt="Github" title="Github"/></a>
<a href="https://web.telegram.org/"><img src="design/icons/telegram.png" width="50" height="50"  alt="Telegram" title="Telegram"></a>
</p>

## Запуск автотестов в Jenkins
#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C07-elena_ching-python_unit15/">проект</a>
#### 2. Нажать **Build Now**
![This is an image](design/jenkins_build.png)
#### 3. Результат запуска сборки можно посмотреть в отчёте Allure
![This is an image](design/allure_results.png)


### Пример видеозаписи прохождения теста

![This is an image](design/UI.gif)

# Интеграция с Allure TestOps и Telegram
### Результаты прохождения тестов, а также сами тест-кейсы будут отправлены в Allure TestOps
![This is an image](design/testopts.png)
### Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram
![This is an image](design/telegram.png) 