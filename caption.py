from scapy.sendrecv import sniff

from packet import *

import matplotlib.pyplot as plt
from scapy.layers.inet import IP,TCP,Ether,UDP
import functools

class Singleton(type):

    def __init__(cls,name,bases,attrs,**kwargs):
        super().__init__(name,bases,attrs)
        cls._instance=None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=super().__call__(*args,**kwargs)
        return cls._instance


class Captura(Pachete,metaclass=Singleton):

    def __init__(self):
        pass

    def calltracker(func):
        @functools.wraps(func)
        def wrapper(*args):
            wrapper.has_been_called = True
            return func(*args)

        wrapper.has_been_called = False
        return wrapper

    def plot_graph(self):
        new_list=[len(self.pachete[UDP]),len(self.pachete[TCP])]
        my_labels = 'UDP', 'TCP'
        plt.pie(new_list, labels=my_labels,startangle=15, shadow = True, autopct='%1.1f%%')
        plt.title('UDP/TCP Percent')
        plt.axis('equal')
        plt.show()


    def print_capture(self):
        self.pachete = sniff(timeout=5,prn=lambda x:x.summary())
        print("\n")

    @calltracker
    def show_packet_info(self):
        self.pachete=sniff(timeout=5)
        for pachet in self.pachete:
            print(pachet.show())
        print("\n")

    def save_as_json(self):
        pachete_json=[]
        for i in range (0,len(self.pachete)):
            if self.pachete[i].haslayer(IP) and self.pachete[i].haslayer(TCP) and not self.pachete[i].haslayer(UDP) and self.pachete[i].haslayer(Ether):
                pachete_json.append(Pachete(self.pachete[i][Ether].dst,
                                            self.pachete[i][Ether].src,
                                            self.pachete[i][IP].src,
                                            self.pachete[i][IP].dst,
                                            self.pachete[i][IP].version,
                                            self.pachete[i][IP].proto,
                                            self.pachete[i][TCP].sport,
                                            self.pachete[i][TCP].dport,
                                            '',
                                            ''))



        for j in range(0,len(pachete_json)):
            print(pachete_json[j].__str__())

        path = os.getcwd()
        file_name = 'packet_info.json'
        complete_path = os.path.join(path, file_name)
        final=[]
        with open(complete_path, 'w', encoding='utf-8') as f:
            for i in range(0,len(pachete_json)):
                final.append(json.dump(pachete_json[i].__str__().split("\n"), f, ensure_ascii=False, indent=4))


