from BloomFilter import BloomFilter
number_bits = int(10e4*1.6)
bloomfilter = BloomFilter(number_hash_functions=10, number_bits=number_bits)
test_key = 352
bloomfilter.add_key(test_key)
print(bloomfilter.check_key(test_key))
other_key = 450
print(bloomfilter.check_key(other_key))
for i in range(int(10e3)):
    bloomfilter.add_key(i)
print('CHECK FOR FALSE POSITIVES')
for i in range(int(10e3), int(10e3)*2):
    if bloomfilter.check_key(i):
        print(i, ' FALSE! ALARM!')

print('done')