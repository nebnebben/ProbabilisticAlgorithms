import math


class HyperLogLog:

    def __init__(self, number_registers):
        if not math.log2(number_registers).is_integer():
            print("Number of registers should be a power of 2!")
            raise

        self.number_registers = number_registers
        self.max_zero_bits = [0] * number_registers

    def calculate_number_zeros(self, binary_hash):
        i = 0
        while i < len(binary_hash) and binary_hash[i] == '0':
            i += 1
        return i

    def add(self, number):
        number_hash = hash(str(number))
        binary_hash = bin(number_hash)[3:]
        registry_number_bits = int(math.log2(self.number_registers))
        register_number = int(binary_hash[:registry_number_bits], 2)

        other_bits = binary_hash[registry_number_bits:]
        number_zeroes = self.calculate_number_zeros(other_bits)

        self.max_zero_bits[register_number] = max(self.max_zero_bits[register_number], number_zeroes)

    def calculate_harmonic_mean(self):
        return sum([2 ** (-num_zeroes) for num_zeroes in self.max_zero_bits])**-1

    def estimate_constant(self):
        return 0.7213 / (1 + (1.079 / self.number_registers))

    def count(self):
        print(self.max_zero_bits)
        harmonic_mean = self.calculate_harmonic_mean()
        alpha = self.estimate_constant()
        return alpha * (self.number_registers ** 2) * harmonic_mean
