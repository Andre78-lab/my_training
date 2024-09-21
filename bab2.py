number_dz = 12
number_dz_h = 1.5
course_name = "Python"
time_1_dz = 1.5 / 12
hours_n = int(time_1_dz)
minutes_dr = (time_1_dz-hours_n)*60
minutes_n = int(minutes_dr)
seconds_n =int((minutes_dr - minutes_n)*60)

print("Количество выполненных ДЗ -", number_dz)
print("Количество затраченных часов -", number_dz_h)
print("Название курса -", course_name)
print("Среднее время потрачено на одно задание - ", time_1_dz, " часа или ", hours_n, "ч", minutes_n, "мин", seconds_n, "сек" )

print("Курс:",course_name, "всего задач:", number_dz, "затрачено часов:", number_dz_h, "среднее время выполнения", time_1_dz, " часа или ", hours_n, "ч", minutes_n, "мин", seconds_n, "сек")