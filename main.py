from func.total_start import total_start
import time

start = time.time() ## точка отсчета времени
total_start()
end = int(time.time() - start) ## собственно время работы программы
print(f" {end} sec") ## вывод времени


