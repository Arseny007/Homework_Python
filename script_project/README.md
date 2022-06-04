##### IT-колледж Сириус
+
+
+
+
+
# Проектное задание
#### выполнил Боровой А.М.,
#### направление 09.02.06
#### группа 6.1
#### Проверил Тенигин А.А.
+
+
+
+
+
+
#### Сириус, 2022
+
+
+ Проектное задание
+ + Придумать скрипт, который будет полезен для системного администратора. Требования: минимум 30-40 строк осмысленного кода на баше 
(перенос одной скобочки или точки с запятой за строку не считается). Задание: написать придуманный скрипт, сделав две реализации: python и bash.  
Проектное задание должно состоять из: титульного листа; краткой теоретической справки по питону и башу, их сходству и различиям, 
целесообразности применения обоих; постановка задачи вашего скрипта; текст вашего скрипта на питоне; текст вашего скрипта на баше; 
выводы о проделанной работе, какие места было сложнее и легче писать на питоне, а какие - на баше. Общие выводы также приветствуются.
----------------------------------------
#### Краткая справка по выбранным языкам.
+ Python - очень универсальный язык. На нем можно писать bachend, автотесты, приложения. Python - один из самых популярных языков, что влечет за собой большую
поддержку develop соmmunity и много различных модулей.

+ Bash - язык поддерживающийся почти на всех unix системах, почти везде выполняется, что дает ему какую-никакую мультиплатформенность. На них разумно писать вредоносное ПО. с этим языком легче работать с файлами, консольными командами, взаимодействием с сетевыми устройствами и  другими более системными настройками

-----------------------------------------

+ Что делает мой скрипт?
+ Он облегчает работу с ip адресами. У него несколько функций:
+ **1)** Расчет полной записи маски в формате x.x.x.x из сокращенной записи в формате числа от 0 до 32
+ **2)** Вывод ip адреса интерфейса, маски подсети и адреса сети
+ **3)** Вывод внешнего ip
+ **4)** Расчет адреса подсети, бродкастного адреса, минимального и максимального адресов по данному ip адресу и маске подсети
------------------------------------------
+ [скрипт на Python](https://github.com/Arseny007/Homework_Python/blob/classwork/projipt/scrIPt.py) 
+
+ [скрипт на Bash](https://github.com/Arseny007/Homework_Python/blob/classwork/projipt/scrIPt.sh)
------------------------------------------
### Выводы
+ Я не столкнулся с проблемами на реализации этого скрипта на любом из этих языков, однако могу сказать, что на Python писать было легче, благодаря библиотеке [ipaddress](https://docs.python.org/3/library/ipaddress.html) 
Но так как Bash самый великий язык программирования, то на нем писать было гораздо приятнее и душевнее. Рад, что у меня в репертуаре появился такой замечательнй язык как Bash