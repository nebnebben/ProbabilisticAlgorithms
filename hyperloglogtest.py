from HyperLogLog import HyperLogLog

number_elements = int(10e6)
number_distinct_elements = int(10e5)

diff = number_elements//number_distinct_elements

element_list = [i for i in range(number_distinct_elements)] * diff
print(len(element_list))

hyperloglog = HyperLogLog(number_registers=16)
for i in range(len(element_list)):
    if i % int(10e4) == 0:
        print(i)
    hyperloglog.add(element_list[i])

estimated_count = hyperloglog.count()
print(estimated_count, number_distinct_elements)
print(f'% diff is {estimated_count/number_distinct_elements}')