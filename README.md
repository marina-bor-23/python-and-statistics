<h1 align="center"> PYTHON AND STATISTICS</h1>

<h3 align="center"> Коды, операции над данными, параметрический анализ данных, построение графиков, использование библиотек pandas, numpy, matplotlib.pyplot, seaborn, plotly, scipy.stats<br> | Codes, data operations, parametric data analysis, plotting, using pandas, numpy, matplotlib.pyplot, seaborn, plotly, scipy.stats libraries </h3> 

Работу я выполняла в Google Colab. Запустить мои проекты можно либо там либо в установленном Python на ПК.<br>

**1. Методы визуализации в Python. методы визуализации; основы pandas, matplotlib, seaborn, plotly.** <br>
<br>
<a href="https://colab.research.google.com/drive/1Hxesy4huzxYqP3ImR_WgcHa1A5AectMz?usp=sharing">Ссылка на 1-ый проект в Google Colab.</a> Либо первый проект можно посмотреть в формате файла .py под названием "1st project".<br>
<br>
Компетенции: <br>
•	Писать код на языке Python для исследовательского и статистического анализа данных; <br>
•	Визуализировать данные;<br>
•	Реализовывать базовые задачи по автоматизации.<br>
<br>
Задачи:<br>
Есть файл с данными по спросу на такси в городе N за несколько недель, данные в формате xlsx под названием «1st database».<br>
Необходимо:<br>
1.	Построить зависимость спроса на такси от дня «Day» за все время. (Спрос = кол-во людей, которые увидели 0 машин+ кол-во людей, которые увидели 1+ машину).<br>
2.	Построить зависимость среднего значения спроса от дня недели.<br>
3.	Построить распределение всех значений по полю «Online (h)».<br>
4.	Проверить, есть ли зависимость между спросом и кол-вом активных водителей «Active drivers».<br>
<br>
<br>
Я использовала pandas для работы с базой данных, для просмотра таблицы и для вычислений средних, совместного спроса.<br>
Я построила plot (линейная), hist (гистограмма) с помощью matplotlib.pyplot чтобы наглядно отразить зависимость спроса и завершенных поездок, зависимость спроса (как раздельного, так и совместного) и дня, зависимость среднего спроса (как раздельного, так и совместного) от дня недели; построила распределение всех значений по полю «Online».<br>
Я построила boxplot, scatterplot с помощью seaborn чтобы наглядно отразить зависимость спроса (как раздельного, так и совместного) и дня, зависимость среднего спроса (как раздельного, так и совместного) от дня недели; построила распределение всех значений по полю «Online». <br>
Я проверила зависимость (наличие связи) между спросом (как раздельным, так и совместным) и количеством активных водителей «Active drivers» с помощью функции корреляции numpy, построила scatterplot, чтобы наглядно отразить эту связь с помощью seaborn. Сделала то же самое для проверки связи между временем, проведенным онлайн и количеством активных водителей «Active drivers». <br>
<br>
<br>
<br>
I did the work in Google Colab. You can run my projects either there or in the installed Python on your PC.<br>
<br>

**1. Visualization methods in Python. visualization methods; fundamentals of pandas, matplotlib, seaborn, plotly.** <br>
<br>
<a href="https://colab.research.google.com/drive/1Hxesy4huzxYqP3ImR_WgcHa1A5AectMz?usp=sharing">Link to 1rd project in Google Colab.</a> Or the first draft can be viewed in a file format .py titled "1st project".<br>
<br>
Competencies:<br>
• Write Python code for research and statistical data analysis;<br>
• Visualize data;<br>
• Implement basic automation tasks.<br>
<br>
Tasks:<br>
There is a file with data on the demand for taxis in the city of N for several weeks, data in xlsx format called "1st database".<br>
Necessary:<br>
1. Build the dependence of taxi demand on the day "Day" for all time. (Demand = number of people who saw 0 cars + number of people who saw 1+ car).<br>
2. Build the dependence of the average demand value on the day of the week.<br>
3. Build a distribution of all values in the "Online (h)" field.<br>
4. Check whether there is a relationship between demand and the number of active drivers.<br>
<br>
<br>
I used pandas to work with the database, to view the table and to calculate averages, joint demand. <br>
I built a plot (linear), hist (histogram) using matplotlib.pyplot to visually reflect the dependence of demand and completed trips, the dependence of demand (both separate and shared) and day, the dependence of average demand (both separate and shared) on the day of the week; I built the distribution of all values across the field "Online". <br>
I built boxplot, scatterplot using seaborn to visually reflect the dependence of demand (both separate and joint) and day, the dependence of average demand (both separate and joint) on the day of the week; I built the distribution of all values in the "Online" field.<br>
I checked the relationship between demand (both separate and joint) and the number of active drivers using the numpy correlation function, built a scatterplot to visually reflect this relationship using seaborn. I did the same to check the relationship between the time spent online and the number of active drivers.<br>

<br>
<br>
<br>
<br>


**2. Статистические гипотезы и уровень значимости. Коэффициент корреляции. уровень значимости, статистические гипотезы; коэффициент корреляции; методы сравнения данных; сравнение номинальных данных; методы сравнения средних.** <br>
<br>
<a href="https://colab.research.google.com/drive/1m9_TebWQAlhG9GX81YMGD9gP2ezV6gD5?usp=sharing">Ссылка на 2-ой проект в Google Colab.</a> Либо второй проект можно посмотреть в формате файла .py под названием "2nd project".<br>
<br>
Компетенции:<br>
•	Формулировать и проверять гипотезы с применением знаний описательной статистики и основ математического анализа.<br>
<br>
Задачи:<br>
Есть файл с данными (датасет) одного из A/B-тестов. Есть id клиента, наличие у него транзакции (целевое действие) пол, возраст и группа в которую клиент попал. Главная задача – определить, является ли действие улучшением для бизнеса или нет. Датасет находится в файле под названием «2nd database».<br>
Необходимо:<br>
1.	Является размер выборки для теста достаточным, если продуктом пользуется 16 миллионов клиентов.<br>
2.	Определить тип распределения.<br>
3.	Описать распределения с точки зрения матстатистики.<br>
4.	Ответить на вопрос при помощи Т-критерия Стьюдента, улучшился ли продукт.<br>
5.	Самостоятельно придумать еще гипотезы и подтвердить/опровергнуть их.<br>
<br>
<br>
Я доказала достаточность выборки для A/B-теста с помощью калькулятора. Высчитала сколько человек совершили транзакцию из всей выборки. Рассчитала среднюю, медиану и моду по возрасту тех, кто совершили транзакцию, определила тип распределения данных с их помощью и также с помощью тестов Шапиро и Колмогорова-Смирнова, используя scipy.stats. Сделала это, используя matplotlib.pyplot, pandas, numpy, построила графики plot (линейный) и hist. Также рассчитала 1, 2, 3 квартили по возрасту.<br>
Проверила, отличается ли среднее количество транзакций в каждой группе с помощью numpy и pandas. Нулевая гипотеза: среднее кол-во транзакций в каждой группе не отличается. Сгруппировала данные только по группе A и группе B, чтобы рассчитать средние и сравнить их статистическим методом, чтобы доказать эффективность проведенного теста. Высчитала среднее арифметическое (матожидание), Среднеквадратичное отклонение (S1), кол-во транзакций и кол-во человек (N), описала таким образом распределение с точки зрения математической статистики. Среднее у группы B больше, чем у группы A. Далее провела ttest с помощью scipy.stats, получила p-значение меньше 0,05 и отвергнула нулевую гипотезу t-критерия, сделав вывод о том,что имеется достаточно доказательств того, что средние у двух выбранных групп - разные. Это говорит о том, что A/B-тест принес эффективный результат и продукт улучшился.<br>
Далее выдвинула свои гипотезы: пол не влияет на совершение/кол-во транзакций. Посчитала коэффициент корреляции между «has_transaction» и «Age» и получила коэффициент, равный 0.02, сила взаимосвязи – отсутствует. Нулевая гипотеза принимается.<br>
Следующая гипотеза: пол влияет на совершение/колво транзакций. Нулевая гипотеза: пол не влияет на кол-во транзакций. Я сгруппировала данные по полу, посчитала сколько каждый пол совершил транзакций и сделала первый вывод о том, что женщины делали транзакции чаще мужчин. Далее я сгруппировала эти данные по A и B группам, в результате в группе A женщины тоже совершали транзакции чаще мужчин, однако, в группе B этот процент был выше (около 4% в группе A и около 7 в группе B). Итого, процент совершивших транзакцию стал в 2 раза больше. Нулевая гипотеза отвергается (то есть пол влияет на кол-во совершённых транзакций), т.к. после проведения A/B теста видно, что средние росли пропорционально и женщины до и после проведения теста покупали больше мужчин.<br>
<br>
<br>
<br>

**2. Statistical hypotheses and the level of significance. The correlation coefficient. significance level, statistical hypotheses; correlation coefficient; methods of comparing data; comparison of nominal data; methods of comparing averages.** <br>
<br>
<a href="https://colab.research.google.com/drive/1m9_TebWQAlhG9GX81YMGD9gP2ezV6gD5?usp=sharing">Link to 2rd project in Google Colab.</a> Or the second project can be viewed in a file format .py titled "2nd project".<br>
<br>
Competencies:<br>
• Formulate and test hypotheses using knowledge of descriptive statistics and fundamentals of mathematical analysis.<br>
<br>
Tasks:<br>
There is a data file (dataset) of one of the A/B tests. There is a client's ID, whether he has a transaction (target action), gender, age, and the group the client is in. The main task is to determine whether an action is an improvement for the business or not. The dataset is located in a file called "2nd database".<br>
Necessary:<br>
1. Is the sample size for the test sufficient if the product is used by 16 million customers.<br>
2. Determine the type of distribution.<br>
3. Describe the distributions from the point of view of mathematical statistics.<br>
4. Answer the question using the Student's T-test, whether the product has improved.<br>
5. Independently come up with more hypotheses and confirm / refute them.<br>
<br>
<br>
I proved the sufficiency of the sample for the A/B test using a calculator. I calculated how many people made a transaction from the entire sample. I calculated the average, median and age fashion of those who made the transaction, determined the type of data distribution using them and also using the Shapiro and Kolmogorov-Smirnov tests using scipy.stats. I did this using matplotlib.pyplot, pandas, numpy, and built plot (linear) and hist graphs. I also calculated 1, 2, 3 quartiles by age.<br>
I checked whether the average number of transactions in each group differs using numpy and pandas. Null hypothesis: the average number of transactions in each group does not differ. I grouped the data only by group A and group B in order to calculate the averages and compare them statistically to prove the effectiveness of the test. I calculated the arithmetic mean (expectation), the standard deviation (S1), the number of transactions and the number of people (N), thus described the distribution from the point of view of mathematical statistics. The average of group B is higher than that of group A. Next, she conducted a ttest using scipy.stats, obtained a p-value less than 0.05 and rejected the null hypothesis of the t-test, concluding that there is sufficient evidence that the averages of the two selected groups are different. This indicates that the A/B test has produced an effective result and the product has improved.<br>
Then she put forward her hypotheses: gender does not affect the commission / number of transactions. I calculated the correlation coefficient between "has_transaction" and "Age" and got a coefficient equal to 0.02, the strength of the relationship is missing. The null hypothesis is accepted.<br>
The following hypothesis: gender affects the performance /number of transactions. Null hypothesis: gender does not affect the number of transactions. I grouped the data by gender, calculated how many transactions each gender had made, and made the first conclusion that women made transactions more often than men. Next, I grouped these data into groups A and B, as a result, in group A, women also made transactions more often than men, however, in group B this percentage was higher (about 4% in group A and about 7 in group B). In total, the percentage of those who completed the transaction became 2 times more. The null hypothesis is rejected (that is, gender affects the number of transactions made), because after the A/B test, it is clear that the average grew proportionally and women bought more men before and after the test.<br>

<br>
<br>
<br>
<br>

**3. Постановка и проверка гипотез. Валидация результатов. Взаимосвязь данных. постановка и проверка гипотез; валидация результатов; взаимосвязь данных.** <br>
<br>
<a href="https://colab.research.google.com/drive/1ymMrdqEPyN04NqRl0koryZc7kSPDmGwa?usp=sharing">Ссылка на 3-ий проект в Google Colab.</a> Либо третий проект можно посмотреть в формате файла .py под названием "3rd project".<br>
<br>
Компетенции:<br>
•	выявлять и корректно обрабатывать выбросы, пропуски и дубликаты в данных;
•	формулировать и проверять гипотезы с применением знаний описательной статистики и основ математического анализа.<br>
<br>
Задачи:<br>
Есть датасет. Нужно сформулировать как минимум 3 гипотезы и проверить их. Можно самой сформулировать метрики и гипотезы.<br>
<details>
  <summary>Датасет содержит в себе несколько полей:</summary>
id: просто ID уникальный для слота дата-время<br>
year: год<br>
hour: час (0 - 23)<br>
season: 1 = зима, 2 = весна, 3 = лето, 4 = осень<br>
holiday: является ли день праздником<br>
workingday: является ли день рабочим (не выходной и не праздник)<br>
weather: 1 - отличная 4 - ужасная погода<br>
temp: температура в градусах Цельсия<br>
atemp: ощущаемая температура<br>
humidity: Влажность<br>
windspeed: скорость ветра<br>
count количество аренд велосипедов в этот слот.<br>
   </p>
</details>

Датасет находится в файле «3rd database» в формате csv.<br>
<br>
<br>
Для начала я посмотрела общую информацию по корреляции между всеми столбцами в датасете с помощью функции data.corr(). Далее определила те столбцы, которые имеют корреляцию больше 0,25 с основным столбцом «count», и выдвинула свои гипотезы и метрики.<br>
<br>
Гипотезы:<br>
•	season,<br>
•	holiday,<br>
•	year,<br>
•	hour,<br>
•	humidity,<br>
•	temp,<br>
•	atemp,<br>
•	workingday<br>
не влияют на count.<br>
<br>
Метрики:<br>
•	среднее кол-во count во время праздников (avg count per holiday);<br>
•	средний count (avg count);<br>
•	наиболее популярный час для взятия в аренду велосипеда (the most popular hour for count);<br>
•	среднее кол-во арендованных велосипедов в рабочие и нерабочие дни (avg count per workingday and not);<br>
•	наиболее популярные погодные условия, при которых берут велосипеды в аренду чаще всего (the most popular weather for count).<br>
<br>
<br>
Я сгруппировала данные по сезонам через pandas и построила barplot через seaborn, после чего проверила нормальность распределения через Критерий согласия Пирсона (st.normaltest). Далее сгруппировала данные по сезонам, посчитала сколько было заявок и арендованных велосипедов за каждый сезон, посчитала долю каждого сезона и на основе этих данных пришла к выводу, что лето и весна – самые популярные сезоны для аренды велосипеда. Далее начала это доказывать через выборки: при точности в 95%, погрешности в 5% и генеральной совокупности в 1901 чел., требуемый размер выборки составил 320 чел. для зимнего, осеннего и весеннего сезонов и 321 для летнего. Посчитав средние для каждого сезона, с помощью цикла while и numpy я сделала рандомную выборку по 31 разу для летнего и весеннего сезонов, после чего соединила две таблицы и построила распределение через sns.barplot, которое выровнялось благодаря проделанным шагам. Далее я проверила ttest, средние для весеннего и летнего сезона теперь отличаются от тех, что я посчитала до выборки. Полученная вероятность равна 0.0008616351 значит, нулевая гипотеза отклоняется, и средние у двух сезонов (весна и лето) РАЗЛИЧАЮТСЯ.<br>
Далее рассмотрела аренды велосипедов по дням. 17, 18 и 8 часов – самые популярные, рассчитала среднее кол-во арендованных велосипедов за день для весеннего и летнего сезонов, также посчитала моды и медианы, вывела эти данные в формате таблицы pandas, построила распределения.<br>
Следующая нулевая гипотеза: year не влияет на count. Я сгруппировала данные и посчитала коэффициент корреляции между годами и кол-вом арендованных велосипедов, он равен 0.2619 , а сила взаимосвязи – слабая, Нулевая гипотеза: year не влияет на count отвергается. Хоть и сила взаимосвязи слабая, year всё равно влияет на count. Также я посчитала и проанализировала метрику «среднее кол-во арендованных велосипедов» (avg count), сгруппировала данные по годам, проанализировала динамику из года в год и пришла к выводу, что т.к. кол-во арендованных велосипедов растет из года в год, бизнес улучшается.<br>
Следующая нулевая гипотеза: holiday не влияет на count. Коэффициент корреляции между праздниками и кол-вом арендованных велосипедов равен -0.0099 , а сила взаимосвязи - обратная связь. Нулевая гипотеза: holiday не влияет на count - принимается. Корреляция имеет обратную связь и это не holiday влияет на count, а count на holiday. Далее посчитала и проанализировала еще одну выдвинутую мною метрику: среднее кол-во арендованных велосипедов во время праздников. Я сгруппировала данные только по праздникам и посчитала среднюю, сделала то же самое для каждого года, в итоге среднее кол-в аренд велосипедов во время праздников из года в год растет, поэтому можно сделать вывод о том, что бизнес улучшился. <br>
Следующая нулевая гипотеза: hour не влияет на count. Я посчитала коэффициент корреляции между часом и кол-вом арендованных велосипедов, он равен 0.4 , а сила взаимосвязи - умеренная, средняя. Нулевая гипотеза: hour не влияет на count - принимается. Однако, сила влияния не является высокой, лишь умеренной и средней, то есть, hour немного влияет на count, но нельзя сказать, что не влияет вовсе. Кроме того, я посчитала еще одну метрику: наиболее популярные для аренды велосипедов часы. Я распределила данные по группам (00 – 03 часа ночи и 21 – 23 часов ночи – относятся к группе «ночь»; с 4 часов утра до 11 – «утро»; с 12 часов дня до 16 – «день»; и с 17 часов вечера до 20 – «вечер»), посчитала кол-во арендованных велосипедов в эти временные промежутки, создала и вывела таблицу pandas DataFrame с этими данными, показала график barplot с помощью seaborn и пришла к выводу, что несмотря на то, что в часть суток "вечер" входят всего 4 часа, аренд велосипедов там наибольшее кол-во. Далее идёт дневное время (5 часов). Утреннее отстаёт, но не сильно, однако к утру отнесено довольно большое кол-во часов (8 часов). Наконец, наименее популярные часы приходятся на ночь (7 часов) и это логично. Возможно, стоит давать скидку или применять акции 1=1 = 3 в ночные часы для привлечения бОльшего кол-ва клиенток и клиентов.<br>
Следующая нулевая гипотеза: weather не влияет на count. Коэффициент корреляции между погодными условиями и кол-вом арендованных велосипедов равен -0.13 , а сила взаимосвязи - обратная связь. Нулевая гипотеза: weather не влияет на count - принимается. Корреляция имеет обратную связь и это не weather влияет на count, а count на weather. Кроме того, я посчитала еще одну метрику: в какие погодные условия чаще всего берут велосипеды (the most popular weather for count). Я сгруппировала данные по погодным условиям, вывела график barplot с помощью seaborn и пришла к выводу, что наиболее популярная для аренд велосипедов погода - лёгкая, умеренная, хорошая.<br>
Следующая нулевая гипотеза: workingday не влияет на count. Коэффициент корреляции между рабочими днями и кол-вом арендованных велосипедов равен 0.02 , а сила взаимосвязи – отсутствует. Нулевая гипотеза: workingday не влияет на count - принимается. Связь отсутствует. Еще одна метрика: среднее кол-во арендованных велосипедов во время рабочего дня и не во время рабочего дня(avg count per workingday and not), которую я посчитала путем группировки данных по рабочим/нерабочим дням, и пришла к выводу, что в рабочие дни (их 5/7 на неделе) больше всего арендуют велосипеды, что логично. Далее посчитала кол-во заявок и средние. Таким образом, несмотря на то, что в рабочие дни обычно намного больше заявок (5208 и 2481 шт. в нерабочие) среднее кол-во арендованных велосипедов примерно одинаково (193.88 и 186.25 шт.). Это говорит о том, что на выходных берут больше велосипедов при меньшем кол-ве заявок. Здесь можно придумать различные акции, чтобы и в рабочие дни брали много велосипедов за раз.<br>
Следующая нулевая гипотеза: temp не влияет на count. Коэффициент корреляции между температурой и кол-вом арендованных велосипедов равен 0.4 , а сила взаимосвязи - умеренная, средняя. Нулевая гипотеза: temp не влияет на count -отклоняется. Связь умеренная, temp влияет на count.<br>
Следующая нулевая гипотеза: atemp не влияет на count. Коэффициент корреляции между ощущаемой температурой и кол-вом арендованных велосипедов равен 0.39 , а сила взаимосвязи - умеренная, средняя. Нулевая гипотеза: atemp не влияет на count - отклоняется. Связь умеренная, atemp влияет на count.<br>
Следующая нулевая гипотеза: humidity не влияет на count. Коэффициент корреляции между влажностью и кол-вом арендованных велосипедов равен -0.32 , а сила взаимосвязи - обратная связь. Нулевая гипотеза: humidity не влияет на count - принимается. Связь обратная.<br>
<br>
В итоге я придумала 9 гипотез, из которых отклонила 4, на них необходимо сделать акцент и придумать акционные предложения по повышению аренд велосипедов и, соответственно, прибыли. Все гипотезы вывела в формате таблицы с информацией о том, была она принята или нет.<br>
Вывод: положение дел в бизнесе улучшилось. Арендовать стали больше и чаще. Очевидные, как казалось, составляющие не влияют на кол-во арендованных велосипедов. При этом влияющих составляющих достаточно в таблице.
<br>
<br>
<br>

**3. Formulation and verification of hypotheses. Validation of the results. The relationship of the data. formulation and verification of hypotheses; validation of results; interrelation of data.** <br>
<br>
<a href="https://colab.research.google.com/drive/1ymMrdqEPyN04NqRl0koryZc7kSPDmGwa?usp=sharing">Link to 3rd project in Google Colab.</a> Or the third project can be viewed in a file format .py titled "3rd project".<br>
<br>
Competencies:<br>
• Identify and correctly handle outliers, omissions and duplicates in the data;<br>
• Formulate and test hypotheses using knowledge of descriptive statistics and the basics of mathematical analysis.<br>
<br>
Tasks:<br>
There is a dataset. It is necessary to formulate at least 3 hypotheses and test them. You can formulate metrics and hypotheses yourself.<br>
<details>
  <summary>The dataset contains several fields:</summary>
id: just an ID unique to the date-time slot<br>
year: year<br>
hour: hour (0 - 23)<br>
season: 1 = winter, 2 = spring, 3 = summer, 4 = autumn<br>
holiday: Is the day a holiday<br>
workingday: is the day a work day (not a day off or a holiday)<br>
weather: 1 - excellent 4 - terrible weather<br>
temp: temperature in degrees Celsius<br>
atemp: perceived temperature<br>
humidity: Humidity<br>
windspeed: Wind speed<br>
count the number of bike rentals in this slot. <br>
    </p>
</details>
The dataset is located in the "3rd database" file in csv format.<br>

<br>
<br>
To begin with, I looked at the general information on the correlation between all columns in the dataset using the data.corr() function. Next, she identified those columns that have a correlation greater than 0.25 with the main column "count", and put forward her hypotheses and metrics:<br>
<br>
Hypotheses:<br>
•	season,<br>
•	holiday,<br>
•	year,<br>
•	hour,<br>
•	humidity,<br>
•	temp,<br>
•	atemp,<br>
• workingday<br>
do not affect count.<br>
<br>
Metrics:<br>
• average count during the holidays (avg count per holiday);<br>
• average count (avg count);<br>
• the most popular hour for renting a bike (the most popular hour for count);<br>
• average number of rented bicycles on working and non-working days (avg count per workingday and not);<br>
• the most popular weather conditions under which bicycles are rented most often (the most popular weather for count).<br>
<br>
<br>
I grouped the data by season through pandas and built a barplot through seaborn, after which I checked the normality of the distribution using the Pearson Consensus Criterion (St.normaltest). Next, I grouped the data by season, calculated how many applications and rented bicycles there were for each season, calculated the share of each season and based on these data came to the conclusion that summer and spring are the most popular seasons for renting a bicycle. Then she began to prove this through samples: with an accuracy of 95%, an error of 5% and a total population of 1901 people, the required sample size was 320 people. for the winter, autumn and spring seasons and 321 for the summer. After calculating the averages for each season, using the while and numpy loop, I made a random selection 31 times for the summer and spring seasons, after which I connected two tables and built a distribution through sns.barplot, which leveled off due to the steps taken. Next, I checked the ttest, the averages for the spring and summer season are now different from those that I counted before the sample. The resulting probability is 0.0008616351, which means that the null hypothesis is rejected, and the averages of the two seasons (spring and summer) DIFFER.<br>
Next, I considered renting bicycles by day. 17, 18 and 8 o'clock are the most popular, calculated the average number of rented bicycles per day for the spring and summer seasons, also calculated the modes and medians, displayed these data in the pandas table format, and built distributions.<br>
The following null hypothesis: year does not affect count. I grouped the data and calculated the correlation coefficient between years and the number of rented bicycles, it is 0.2619, and the strength of the relationship is weak, the Null hypothesis: year does not affect count is rejected. Although the strength of the relationship is weak, year still affects count. I also calculated and analyzed the metric "average number of rented bicycles" (avg count), grouped the data by year, analyzed the dynamics from year to year and came to the conclusion that since the number of rented bicycles is growing from year to year, business is improving.<br>
The following null hypothesis: holiday does not affect count. The correlation coefficient between holidays and the number of rented bicycles is -0.0099, and the strength of the relationship is feedback. Null hypothesis: holiday does not affect count - accepted. Correlation has an inverse relationship and it is not holiday that affects count, but count on holiday. Next, I calculated and analyzed another metric I put forward: the average number of rented bicycles during the holidays. I grouped the data only by holidays and calculated the average, did the same for each year, as a result, the average number of bike rentals during the holidays is growing from year to year, so we can conclude that the business has improved. <br>
The following null hypothesis: hour does not affect count. I calculated the correlation coefficient between the hour and the number of rented bicycles, it is 0.4, and the strength of the relationship is moderate, average. Null hypothesis: hour does not affect count - accepted. However, the power of influence is not high, only moderate and average, that is, hour has a slight effect on count, but it cannot be said that it does not affect at all. In addition, I counted another metric: the most popular watches for bike rental. I have distributed the data into groups (00 – 03 a.m. and 21 – 23 a.m. – belong to the "night" group; from 4 a.m. to 11 a.m. – "morning"; from 12 p.m. to 16 p.m. – "day"; and from 5 p.m. to 20 p.m. – "evening"), counted the number of rented bicycles in these time intervals, created and displayed a pandas DataFrame table with this data, showed a barplot graph with with the help of seaborn, I came to the conclusion that despite the fact that the "evening" part of the day includes only 4 hours, there are the largest number of bike rentals there. Next comes the daytime (5 hours). Morning lags behind, but not much, however, a fairly large number of hours (8 hours) are attributed to the morning. Finally, the least popular hours are at night (7 o'clock) and this is logical. It may be worth giving a discount or using 1=1 = 3 promotions at night to attract more clients and clients.<br>
The following null hypothesis: weather does not affect count. The correlation coefficient between weather conditions and the number of rented bicycles is -0.13 , and the strength of the relationship is feedback. Null hypothesis: weather does not affect count - accepted. Correlation has an inverse relationship and it is not weather that affects count, but count on weather. In addition, I calculated another metric: in which weather conditions bicycles are most often taken (the most popular weather for count). I grouped the data by weather conditions, plotted the barplot graph using seaborn and came to the conclusion that the most popular weather for bike rentals is light, moderate, and good.<br>
The following null hypothesis: workingday does not affect count. The correlation coefficient between working days and the number of rented bicycles is 0.02, and the strength of the relationship is absent. Null hypothesis: workingday has no effect on count - accepted. There is no connection. Another metric: the average number of rented bicycles during the working day and not during the working day (avg count per workingday and not), which I calculated by grouping data by working/non-working days, and came to the conclusion that on working days (there are 5/7 of them per week) bicycles are rented the most which is logical. Next, I counted the number of applications and the average. Thus, despite the fact that there are usually much more applications on working days (5,208 and 2,481 pcs. on non-working days), the average number of rented bicycles is about the same (193.88 and 186.25 pcs.). This suggests that more bicycles are taken on weekends with fewer applications. Here you can come up with various promotions so that on working days you can take a lot of bicycles at a time.<br>
The following null hypothesis: temp does not affect count. The correlation coefficient between temperature and the number of rented bicycles is 0.4, and the strength of the relationship is moderate, average. Null hypothesis: temp does not affect count -it is rejected. The connection is moderate, temp affects count.<br>
The following null hypothesis: atemp does not affect count. The correlation coefficient between the perceived temperature and the number of rented bicycles is 0.39, and the strength of the relationship is moderate, average. Null hypothesis: atemp does not affect count - it is rejected. The connection is moderate, atemp affects count.<br>
The following null hypothesis: humidity does not affect count. The correlation coefficient between humidity and the number of rented bicycles is -0.32, and the strength of the relationship is the feedback. Null hypothesis: humidity does not affect count - accepted. The connection is reversed.<br>
<br>
As a result, I came up with 9 hypotheses, of which I rejected 4, they need to be emphasized and come up with promotional offers to increase bike rentals and, accordingly, profits. All hypotheses were displayed in the format of a table with information about whether it was accepted or not.
<br>
Conclusion: the business situation has improved. They began to rent more and more often. The obvious components, as it seemed, do not affect the number of rented bicycles. At the same time, there are enough influencing components in the table.<br>



