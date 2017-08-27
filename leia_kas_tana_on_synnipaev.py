from datetime import date

# mõelda funktsioon mis skripti iseeneset
# iga 24h järel käima tõmbaks (module time?)

today = date.today()
kp = today.strftime('%d.%m')
synnipaev_nimekiri = open('synnipaevade_nimekiri.txt')


for line in synnipaev_nimekiri:
    if kp in line:
        #line = line.split(' ')
        print(line[0:-6])
        synnipaev_on = line[0:-6]

        tana_on_synipaev = open('tana_on_synnipäev.txt', 'w')

        # probleem, et kui sama kp on mitmel kirjel siis
        # lisatakse ainult viimane kirje. täiendada skripti.
        tana_on_synipaev.write(synnipaev_on)

        tana_on_synipaev.close()

synnipaev_nimekiri.close()



