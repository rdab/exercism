def convert(number):
    mapp = {'3':'Pling', '5':'Plang', '7':'Plong'}
    drops = [mapp[i] for i in mapp if number % int(i) == 0]
    return ''.join(drops) if drops else str(number)
