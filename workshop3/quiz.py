namen1 = ['danny', 'sean', 'thomas', 'marc', 'thijmen', 'maurits', 'bram', 'dean', 'soufyan', 'conrad', 'stef', 'ross', 'sylvie', 'mathieu', 'steven', 'sebastiaan', 'kaj', 'michelle']
namen2 = ['thijmen', 'maureen', 'owen', 'demi', 'imran', 'jabir', 'casper', 'stijn', 'niels', 'norma', 'jayden', 'ahsen', 'adil', 'jesse', 'isis', 'garon']
namen = namen1 + namen2

antwoord=input('wie? ')

if antwoord.lower() in namen:
        print('goed!')

        
        print('\n\n\nWelkom bij de gigantische Webdevelopers Quiz 2023')

        antwoord=input('Ben je klaar om de Quiz te spelen? (ja/nee) :')
        punten=0
        aantal_vragen=3
        
        if antwoord.lower()=='ja':

            print('\n\nMooi. Dan gaat de gigantische Webdevelopers Quiz 2023 beginnen!!\nGeef bij iedere vraag als antwoord de voornaam van een student uit de klas op.\n\n')

            antwoord=input('Vraag 1: Welke student heeft in het eerste leerjaar een sequenser (muziek-maak-programma) geprogrammeerd? ')
            if antwoord.lower()=='garon' or antwoord.lower()=='garon':
                punten += 1
                print('goed!')
            else:
                print('fout!')
        
            antwoord=input('Vraag 2: Welke student heeft vorig jaar een schaak-robot geprogrammeerd? ')
            if antwoord.lower()=='sebastiaan':
                punten += 1
                print('goed')
            else:
                print('fout')

            antwoord=input('Vraag 3: Welke student heeft de stoelen-selectie van de Annex Bios-opdracht werkend gekregen? ')
            if antwoord.lower()=='stef':
                punten += 1
                print('goed')
            else:
                print('fout')

            print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
            cijfer = round(float(10/aantal_vragen*punten), 1)
            print('Je cijfer voor dit project komt daarmee op een voorlopige '+str(cijfer)+'.')
            if punten >= 2: print('Goed bezig!')
            else:           print('Hmmm, kan beter... nog even oefenen chef.\n\n')
        elif antwoord.lower()=='nee':
            print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
        else:
            print('Dit antwoord ken ik niet!')



else:
        print('fout!')







