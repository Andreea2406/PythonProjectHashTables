import random
f1 = open("Fete.txt", 'r')
f2 = open("Baieti.txt", 'r')
f3 = open("Nume.txt", 'r')
lista = []
# f = open("CNP.txt", 'w')

file = open("populatie.txt", "r")
file1 = open("cod_judet.txt", "r")


def Generare_CNP(numar):
    s = 0
    myfile = file.readlines()
    judet = 1
    for element in range(numar):
        for i in myfile:
            s = (numar * int(i)) // 20000000
            if judet == 53:
                break
            for item in range(s):
                CNP = []
                cnp = ''
                c = 0
                sex1 = random.randint(1, 100)
                anisor = random.randint(0, 100)
                if sex1 <= 45 and anisor > 22:
                    sex = 1
                elif sex1 <= 45 and anisor <= 22:
                    sex = 5
                elif sex1 > 45 and anisor > 22:
                    sex = 2
                elif sex1 > 45 and anisor <= 22:
                    sex = 6
                if sex == 1 or sex == 2:
                    an = random.randint(0, 99)
                else:
                    an = random.randint(0, 21)
                if an < 10:
                    an = '0' + str(an)
                luna = random.randint(1, 12)
                if luna < 10:
                    luna = '0' + str(luna)
                for luna in [1, 3, 5, 7, 8, 10, 12]:
                    zi = random.randint(1, 31)
                for luna in [4, 6, 9, 11]:
                    zi = random.randint(1, 30)
                if luna == 2:
                    zi = random.randint(1, 28)
                if zi < 10:
                    zi = '0' + str(zi)
                if judet == 41:
                    judet = 51
                if judet < 10:
                    judet2 = "0" + str(judet)
                else:
                    judet2 = str(judet)
                nnn = random.randint(1, 999)
                if nnn < 10:
                    nnn = '00' + str(nnn)
                elif nnn > 10 and nnn < 100:
                    nnn = '0' + str(nnn)
                else:
                    nnn = str(nnn)
                cnp = str(sex) + str(an) + str(luna) + str(zi) + str(judet2) + str(nnn)
                constant = "279146358279"
                for i in range(0, 10):
                    c += int(cnp[i]) * int(constant[i])
                if c % 11 < 10:
                    cnp = cnp + str(c % 11)
                else:
                    cnp = cnp + '1'
                full = []
                full.append(cnp)
                if sex % 2 == 0:
                    n = random.choice((open("Fete.txt").read().split()))
                    full.append(n)
                else:
                    B = random.choice((open("Baieti.txt").read().split()))
                    full.append(B)
                N = random.choice((open("Nume.txt").read().split()))
                full.append(N)
                complet = " ".join(map(str, full))
                CNP.append(complet)

                # for elemente in CNP:
                #     f.write(elemente + "\n")

            judet += 1


def generare_Hash(cnp):
    h = 0
    for caracter in cnp:
        h *= 3
        h += ord(caracter)
    h %= 1000
    return h


def Hash():
    l = []
    with open("CNP.txt", "r") as f:

        for line in f:
            l1 = line.split()
            l1[1] += ' ' + l1[2]
            l1.pop()
            l.append(l1)
    final_list = [[] for i in range(1000)]
    for elm in l:
        cnp = elm[0]
        h = generare_Hash(cnp)
        final_list[h].append(elm)

    return final_list


def cautare(cnp,hash):
    h = int(generare_Hash(cnp))
    for i in range(len(hash[h])):
        Element=hash[h][i]
        if Element[0]==cnp:
            print(f"Cnp ul:{cnp} se afla pe pozitia {i} a Hash-ului : "
                  f" {h} cu numele {Element[1]}")
            return i+1





if __name__ == '__main__':
    # Generare_CNP(1000000)
    # f.close()
    hash = Hash()
    iteratie = cautare('2771121029545',hash)
    print('Numarul de iteratii este',iteratie)