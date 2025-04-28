import threading
import time
import random

class Lightswitch:
    def _init_(self):
        self.count = 0
        self.mutex = threading.Lock()

    def lock(self, semaphore):
        self.mutex.acquire()
        self.count += 1
        if self.count == 1:
            semaphore.acquire()
        self.mutex.release()

    def unlock(self, semaphore):
        self.mutex.acquire()
        self.count -= 1
        if self.count == 0:
            semaphore.release()
            print("Tuvalet boş.")
        self.mutex.release()

# Semaforlar ve Lightswitch'ler
empty = threading.Semaphore(1)
maleSwitch = Lightswitch()
femaleSwitch = Lightswitch()
maleMultiplex = threading.Semaphore(3)
femaleMultiplex = threading.Semaphore(3)
turnstile = threading.Semaphore(1)

# Erkeklerin tuvalete girişi
def male_use_bathroom(id):
    time.sleep(random.uniform(0.1, 0.5))
    turnstile.acquire()
    maleSwitch.lock(empty)
    turnstile.release()

    maleMultiplex.acquire()
    print(f"Erkek {id} tuvaleti kullanıyor.")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"Erkek {id} tuvaletten çıktı.")
    maleMultiplex.release()
    maleSwitch.unlock(empty)


# Thread'lerin oluşturulması ve çalıştırılması
threads = []

# Kadın ve erkek oluşturma
for i in range(5):
    t = threading.Thread(target=male_use_bathroom, args=(i,))
    threads.append(t)

    t = threading.Thread(target=female_use_bathroom, args=(i,))
    threads.append(t)

# Thread'leri rastgele karıştırma
random.shuffle(threads)

# Tüm thread'leri başlatılması ve bitirilmesi
for t in threads:
    t.start()

for t in threads:
    t.join()