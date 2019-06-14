hours_from = int(input("input hours "))
minutes_from = int(input("input minutes "))
seconds_from = int(input("input seconds "))

hours_to = int(input("input hours "))
minutes_to = int(input("input minutes "))
seconds_to = int(input("input seconds "))



def time_deference(hours, minutes, seconds):
  total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
  return total_seconds

result_from = time_deference(hours_from, minutes_from, seconds_from)
result_to = time_deference(hours_to, minutes_to, seconds_to)
time_deference  = result_to - result_from 
print(result)

''''generator i eterator 
ternarnyi operator'''