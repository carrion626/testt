#odna oshibka i ti oshibsya


def divide(a, dev):
    try:
        return a / dev
    except ZeroDivisionError as ex:
        print(f'error bleat: {ex}')
    except:
        print('hui znaet, brat, sho to tut ne tak')

dev = int(input())
print(divide(4, dev))

##########################################################################################

def get_int():
    while True:
        try:
            vvod = int(input('vvedi chislo uebok:'))
            #eto budet cicle esli ne postavit break, ili return
            return vvod
        except:
            print('eto ne chislo, uebok')
            continue

get_int()