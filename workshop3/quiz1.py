import random
dieren1 = ['aap', 'duif', 'eend', 'eland', 'ezel', 'adder', 'leeuw', 'tijger', 'haai', 'walvis', 'kikker', 'hamerhaai', 'kat', 'hond', 'cavia']
dieren2 = ['uil', 'giraffe', 'havik', 'jaguar', 'luipaard', 'krokodil', 'slang', 'vogel', 'adelaar']
dier = dieren1 + dieren2


antwoord=input('noem een dier op? ')

dier



def antwoorden_goed_of_fout(antwoord, getal):

        antwoorden = {

        'goed': ['ja goed gedaan ', 'zeer goed ', ' perfect','goed bezig', 'zal wel goed zijn ', 'wow goed ','goed!!!' ],

        'fout': ['nee jammer dit ', 'dikke fout', 'jij bent niet naar school geweest', 'dombo ', 'dikke kruis','domme zak!','fout!!!!'],

        }
        print(antwoorden[antwoord][getal])


      

# if

       # punten += 1

        #print('geluk.')

        # antwoorden_goed_of_fout('goed',(random.randint(0,6)) ), dier()
# else:

# antwoorden_goed_of_fout('fout',(random.randint(0,5)) ),dier()

if antwoord.lower() in dier:
        print('goed!')

        
        print('\n\n\nWelkom bij de gigantische Webdevelopers Quiz 2023')

        antwoord=input('Ben je klaar om de Quiz te spelen? (ja/nee) :')
        punten=0
        aantal_vragen=10
        
        if antwoord.lower()=='ja':

            print('\n\nMooi. Dan gaat de gigantische Webdevelopers Quiz 2023 beginnen!!\nGeef bij iedere vraag de juiste antwoord.\n\n')

            antwoord=input('Vraag 1: het is een harige dier en lijkt op de mens? ')
            if antwoord.lower()=='aap' or antwoord.lower()=='aap':
                punten += 1
                antwoorden_goed_of_fout('goed',(random.randint(0,6)) ), 

            else:
                 antwoorden_goed_of_fout('fout',(random.randint(0,5)) ),
        
            antwoord=input('Vraag 2: het vliegt en het is grijs ze zitten veel op de dam? ')
            if antwoord.lower()=='duif':
                punten += 1
                antwoorden_goed_of_fout('goed',(random.randint(0,6)) ), 
            else:
                antwoorden_goed_of_fout('fout',(random.randint(0,5)) ),

            antwoord=input('Vraag 3: het lijkt op een paard en is dom ')
            if antwoord.lower()=='ezel':
                punten += 1
                antwoorden_goed_of_fout('goed',(random.randint(0,6)) ),
            else:
               antwoorden_goed_of_fout('fout',(random.randint(0,5)) ),

            antwoord=input('Vraag 4: het is groen en leeft in het water ')
            if antwoord.lower()=='krokodil':
                punten += 1
                antwoorden_goed_of_fout('goed',(random.randint(0,6)) ),
            else:
               antwoorden_goed_of_fout('fout',(random.randint(0,5)) ),

            antwoord=input('Vraag 5: het hangt aan de boom en is lui ')
            if antwoord.lower()=='luipaard':
                punten += 1
                antwoorden_goed_of_fout('goed',(random.randint(0,6)) ),
            else:
                antwoorden_goed_of_fout('fout',(random.randint(0,5)) ),

            antwoord=input('Vraag 6: het is een huisdier en het is heel zacht ')
            if antwoord.lower()=='kat':
                punten += 1
                antwoorden_goed_of_fout('goed',(random.randint(0,6)) ),
            else:
               antwoorden_goed_of_fout('fout',(random.randint(0,5)) ),

            antwoord=input('Vraag 7: het heeft een hele lange nek ')
            if antwoord.lower()=='giraffe':
                punten += 1
                antwoorden_goed_of_fout('goed',(random.randint(0,6)) ),
            else:
               antwoorden_goed_of_fout('fout',(random.randint(0,5)) ),

            antwoord=input('Vraag 8: het is een hele grote vis ')
            if antwoord.lower()=='walvis':
                punten += 1
                antwoorden_goed_of_fout('goed',(random.randint(0,6)) ),
            else:
                antwoorden_goed_of_fout('fout',(random.randint(0,5)) ),

            antwoord=input('Vraag 9: het is lang en het slist ')
            if antwoord.lower()=='slang':
                punten += 1
                antwoorden_goed_of_fout('goed',(random.randint(0,6)) ),
            else:
                antwoorden_goed_of_fout('fout',(random.randint(0,5)) ),

            antwoord=input('Vraag 10: het is een vogel die in de avonden geluid maakt')
            if antwoord.lower()=='uil':
                punten += 1
                antwoorden_goed_of_fout('goed',(random.randint(0,6)) ),
            else:
               antwoorden_goed_of_fout('fout',(random.randint(0,5)) ),

            print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
            cijfer = round(float(10/aantal_vragen*punten), 1)
            print('Je cijfer voor dit project komt daarmee op een voorlopige '+str(cijfer)+'.')
            if punten >= 2: print('Goed bezig!')
            else:           print('Hmmm, kan beter... nog even oefenen chef.\n\n')
            antwoord.lower()=='nee'
            print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
        else:
            print('Dit antwoord ken ik niet!')




        








