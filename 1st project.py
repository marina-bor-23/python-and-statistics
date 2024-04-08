# -*- coding: utf-8 -*-
"""дз20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hxesy4huzxYqP3ImR_WgcHa1A5AectMz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('/content/database 1.xlsx')

data.head()

"""#1. Построить зависимость спроса на такси от дня Day за все время. (Спрос = кол-во людей, которые увидели 0 машин+ кол-во людей, которые увидели 1+ машину).(спрос совместный и раздельный)

Группируем Finished Rides по Day
"""

finished_rides = data.groupby(['Day'])['Finished Rides'].sum().reset_index()

finished_rides.head()

"""Суммируем столбцы "People saw 0 cars (unique)" и "People saw +1 cars (unique)"
"""

data['Joint Demand Sum'] = data[['People saw 0 cars (unique)','People saw +1 cars (unique)']].sum(axis=1)
joint_demand = data.groupby(['Day'])['Joint Demand Sum'].sum().reset_index()

joint_demand.head()

"""Показываем зависимость спроса и завершённых поездок"""

plt.plot(finished_rides['Day'], finished_rides['Finished Rides'], label = 'n rides', color='blue')
plt.plot(joint_demand ['Day'], joint_demand ['Joint Demand Sum'], label = 'n demand', color='orange')
plt.xticks(rotation=90)
plt.grid()
plt.legend()
plt.show()

"""Зависимость спроса (совместного) от дня"""

plt.plot(joint_demand ['Day'], joint_demand ['Joint Demand Sum'], label = 'n joint demand', color='orange')
plt.xticks(rotation=90)
plt.grid()
plt.legend()
plt.show()

"""Зависимость спроса (0 увидевших; +1 увидевших) от дня"""

saw_0_cars_sum = data.groupby(['Day'])['People saw 0 cars (unique)'].sum().reset_index()
saw_1_plus_cars_sum = data.groupby(['Day'])['People saw +1 cars (unique)'].sum().reset_index()

plt.plot(saw_0_cars_sum['Day'], saw_0_cars_sum['People saw 0 cars (unique)'], label = 'n 0 cars', color='black')
plt.plot(saw_1_plus_cars_sum['Day'], saw_1_plus_cars_sum['People saw +1 cars (unique)'], label = 'n +1 cars', color='blue')
plt.xticks(rotation=90)
plt.grid()
plt.legend()
plt.show()

sns.scatterplot(data=data, x="Day", y="People saw 0 cars (unique)")
plt.xticks(rotation=90)
plt.show()

sns.scatterplot(data=data, x="Day", y="People saw +1 cars (unique)")
plt.xticks(rotation=90)
plt.show()

sns.scatterplot(data=data, x="Day", y="Joint Demand Sum")
plt.xticks(rotation=90)
plt.show()

sns.boxplot(data=data, x="Day", y="Joint Demand Sum")
plt.xticks(rotation=90)
plt.show()

"""#2. Построить зависимость среднего значения спроса от дня недели.

Зависимость среднего спроса (совместного) от дня недели
"""

data.head()

saw_0_cars_avg = data['People saw 0 cars (unique)'].agg(['mean'])

saw_0_cars_avg = saw_0_cars_avg.mean().round(1)
saw_0_cars_avg #среднее по 0 увидевших машин в общем

saw_1_plus_cars_avg = data['People saw +1 cars (unique)'].agg(['mean'])

saw_1_plus_cars_avg = saw_1_plus_cars_avg.mean().round(1)
saw_1_plus_cars_avg #среднее по +1 увидевших машин в общем

"""https://uchet-jkh.ru/i/kak-naiti-srednee-cislo-v-pandas/"""

saw_0_cars_avg = data.groupby(sort = False, by='DoW')['People saw 0 cars (unique)'].mean().round(1).reset_index()
saw_1_plus_cars_avg = data.groupby(sort = False, by='DoW')['People saw +1 cars (unique)'].mean().round(1).reset_index()
saw_0_cars_avg.head()

saw_1_plus_cars_avg.head()

data['Joint Demand Avg'] = data[['People saw 0 cars (unique)','People saw +1 cars (unique)']].mean(axis=1)
joint_demand_avg = data.groupby(sort = False, by='DoW')['Joint Demand Avg'].mean().reset_index()
joint_demand_avg.mean().round(1)

plt.plot(joint_demand_avg ['DoW'], joint_demand_avg ['Joint Demand Avg'], label = 'n joint demand avg', color='orange')
plt.grid()
plt.legend()
plt.show()

sns.scatterplot(data=data, x="DoW", y="Joint Demand Avg")
plt.xticks(rotation=90)
plt.show()

sns.boxplot(data=data, x="DoW", y="Joint Demand Avg")
plt.xticks(rotation=90)
plt.show()

"""Зависимость среднего спроса (0 увидевших; +1 увидевших) от дня недели"""

saw_0_cars_avg = data.groupby(sort = False, by='DoW')['People saw 0 cars (unique)'].mean().round(1).reset_index()
saw_1_plus_cars_avg = data.groupby(sort = False, by='DoW')['People saw +1 cars (unique)'].mean().round(1).reset_index()
saw_0_cars_avg.head()

saw_1_plus_cars_avg.head()

plt.plot(saw_0_cars_avg['DoW'], saw_0_cars_avg['People saw 0 cars (unique)'], label = 'n 0 cars', color='black')
plt.plot(saw_1_plus_cars_avg ['DoW'], saw_1_plus_cars_avg ['People saw +1 cars (unique)'], label = 'n +1 cars', color='blue')
plt.grid()
plt.legend()
plt.show()

"""#3. Построить распределение всех значений по полю Online (h)."""

data.head()

plt.hist(data['Online (h)'], bins = 20, color='green')
plt.show()

plt.boxplot(data['Online (h)'])
plt.show()

"""#4. Проверить, есть ли зависимость между временем и кол-вом активных водителей Active drivers."""

data.info()

#главная функция подсчёта корреляции
def calculating_of_corr(a, b):
    corrcoeff = np.corrcoef(a, b)
    return corrcoeff

corrcoeff_active_drivers_online = calculating_of_corr(data['Active drivers'], data['Online (h)']) [0, 1]
corrcoeff_active_drivers_online = corrcoeff_active_drivers_online.round(2)
corrcoeff_active_drivers_online

coeff_corr_1 = corrcoeff_active_drivers_online

#главная функция определния силы взаимосвязи для коэф корреляции
def power_of_connection(coeff_corr_general):
    if coeff_corr_general < 0.1:
        corr_pow = "отсутствует"
    elif 0.1 <= coeff_corr_general <= 0.3:
        corr_pow = "слабая"
    elif 0.3 < coeff_corr_general <= 0.5:
        corr_pow = "умеренная, средняя"
    elif 0.5 < coeff_corr_general <= 0.7:
        corr_pow = "заметная, средняя"
    elif 0.7 < coeff_corr_general <= 0.9:
        corr_pow = "высокая, сильная"
    elif 0.9 < coeff_corr_general <= 1:
        corr_pow = "весьма высокая, сильная"
    else:
        corr_pow = ("ошибка")
    return(corr_pow)

"""![image.png](data:image/png;base64,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)"""

print("Коэффициент корреляции между кол-вом активных водителей и временем, проведённым онлайн, равен", coeff_corr_1,
", а сила взаимосвязи -", power_of_connection(coeff_corr_1))

sns.scatterplot(data=data, x="Active drivers", y="Online (h)")
plt.xticks(rotation=90)
plt.show()

"""Сильная и весьма высокая зависимость между активными водятелями и временем, проведённым онлайн

##Зависимость  спроса от кол-ва активных водителей Active drivers.

Раздельный спрос
"""

corrcoeff_active_drivers_ppl_saw_0_cars_only = calculating_of_corr(data['Active drivers'], data['People saw 0 cars (unique)']) [0, 1]
corrcoeff_active_drivers_ppl_saw_0_cars_only = corrcoeff_active_drivers_ppl_saw_0_cars_only.round(2)
corrcoeff_active_drivers_ppl_saw_0_cars_only

coeff_corr_2 = corrcoeff_active_drivers_ppl_saw_0_cars_only

print("Коэффициент корреляции между кол-вом активных водителей и кол-вом людей, увидевших 0 машин, равен", coeff_corr_2,
", а сила взаимосвязи -", power_of_connection(coeff_corr_2))

sns.scatterplot(data=data, x="Active drivers", y="People saw 0 cars (unique)")
plt.xticks(rotation=90)
plt.show()

corrcoeff_active_drivers_ppl_saw_1_plus_cars = calculating_of_corr(data['Active drivers'], data['People saw +1 cars (unique)']) [0, 1]
corrcoeff_active_drivers_ppl_saw_1_plus_cars = corrcoeff_active_drivers_ppl_saw_1_plus_cars.round(2)
corrcoeff_active_drivers_ppl_saw_1_plus_cars

coeff_corr_3 = corrcoeff_active_drivers_ppl_saw_1_plus_cars

print("Коэффициент корреляции между кол-вом активных водителей и кол-вом людей, увидевших +1 машину, равен", coeff_corr_3,
", а сила взаимосвязи -", power_of_connection(coeff_corr_3))

sns.scatterplot(data=data, x="Active drivers", y="People saw +1 cars (unique)")
plt.xticks(rotation=90)
plt.show()

"""Корреляция между активными водителями и людьми, увидевшими 0 машин, практически отсутствует.

Корреляция между активными водителями и людьми, увидевшими +1 машину, высокая, сильная.

Сильная зависимость спроса от кол-ва активных водителей

Совместный спрос
"""

data.head()

#столбец, соединяющий "people saw 0 cars" и "people saw +1 cars", в ячейке №131

corrcoeff_joint_dem_act_driv_ppl_saw_0_1_plus_cars = calculating_of_corr(data['Active drivers'], data['Joint Demand Sum']) [0, 1]
corrcoeff_joint_dem_act_driv_ppl_saw_0_1_plus_cars = corrcoeff_joint_dem_act_driv_ppl_saw_0_1_plus_cars.round(2)
corrcoeff_joint_dem_act_driv_ppl_saw_0_1_plus_cars

coeff_corr_4 = corrcoeff_joint_dem_act_driv_ppl_saw_0_1_plus_cars

print("Коэффициент корреляции между кол-вом активных водителей и кол-вом людей, увидевших 0 и +1 машину совместно, равен", coeff_corr_4,
", а сила взаимосвязи -", power_of_connection(coeff_corr_4))

sns.scatterplot(data=data, x="Active drivers", y="Joint Demand Sum")
plt.xticks(rotation=90)
plt.show()

"""Таким образом, совместный спрос средне коррелирует с кол-вом активных водителей, однако спрос от людей, увидевших +1 машину, довольно высокий и сильный."""