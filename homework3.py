class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, cpu):
        self.__cpu = cpu

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, memory):
        self.__memory = memory

    def  make_computations(self):
        return  self.__cpu * self.__memory

    def __str__(self):
        return f'computer: CPU{self.__cpu}, MEMORY{self.__memory}'

    def __eq__(self, other):
        return self.__memory == other.memory

    def __le__(self, other):
        return self.__memory < other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory

    def __ne__(self, other):
        return self.__memory != other.memory

    def __lt__(self, other):

        return self.__memory < other.memory


class Phone:
    def __init__(self,sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
         return    self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self,sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card_name = self.__sim_cards_list[sim_card_number - 1]
            print (f'There  is a call {call_to_number} from a SIM card {sim_card_number} - { sim_card_name}')
        else:
            print('Invalid SIM card number')

    def __str__(self):
        return f'Phone: Sim Card ={self.__sim_cards_list}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'building a route from  {location}')

    def __str__(self):
        return f'SmartPhone: CPU{self.cpu}, MEMORY{self.memory}, Sim card {self.sim_cards_list}'

computer = Computer(4, 8)
phone = Phone(["Beeline", "Megacom"])
smartphone1 = SmartPhone(8, 16, ["O!", "Megacom"])
smartphone2 = SmartPhone(6, 12, ["Beeline"])
print(computer)
print("Вычисления компьютера:", computer.make_computations())

phone.call(1, "+996 777 98 76 54")

smartphone1.use_gps("Бишкек")
print(smartphone1)

smartphone2.call(1, "+996 555 12 34 56")
print(smartphone2)


print("smartphone1 == smartphone2:", smartphone1 == smartphone2)
print("smartphone1 != smartphone2:", smartphone1 != smartphone2)
print("smartphone1 < smartphone2:", smartphone1 < smartphone2)
print("smartphone1 <= smartphone2:", smartphone1 <= smartphone2)
print("smartphone1 > smartphone2:", smartphone1 > smartphone2)
print("smartphone1 >= smartphone2:",smartphone1 >= smartphone2)














