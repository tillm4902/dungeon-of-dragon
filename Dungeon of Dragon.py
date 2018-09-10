import time
import pygame
from pygame.locals import *
import random
import sys

# Space Time
secretpoints=0
# Within this comment you find what you seek
# In his house in R'lyeh, Cthulhu sleeps.

#Screen size
pygame.init()
pygame.display.init()

SCREEN_WIDTH=361
SCREEN_HEIGHT=361
size=(SCREEN_WIDTH,SCREEN_HEIGHT)
screen=pygame.display.set_mode((360,360), 0, 24)

#Title
pygame.display.set_caption("Dungeon of Dragon")

# Background
backgroundr=screen.get_rect()

def image(i):
    global screen
    global backgroundr
    screen.blit(i,backgroundr)
    pygame.display.flip()
    pygame.event.get()

image(pygame.image.load('titlei.png'))

# Dice

def d4():
    return random.randint(1,4)

def d6():
    return (random.randint(1,6))

def d8():
    return random.randint(1,8)

def d10():
    return random.randint(1,10)

def d12():
    return random.randint(1,12)

def d20():
    return random.randint(1,20)

def d100():
    return random.randint(1,100)

# Weapons List

sword={'name':'sword','fmod':0,'hmod':2,'hdie':d6,'high':75,'low':25,'i':pygame.image.load("swordi.png")}
axe={'name':'axe','fmod':0,'hmod':2,'hdie':d6,'high':75,'low':25,'i':pygame.image.load('axei.png')}
mace={'name':'mace','fmod':0,'hmod':2,'hdie':d6,'high':75,'low':25,'i':pygame.image.load('macei.png')}
fist={'name':'fist','fmod':0,'hmod':0,'hdie':d6,'high':1,'low':1,'i':pygame.image.load('fisti.png')}
stick={'name':'stick','fmod':0,'hmod':0,'hdie':d4,'high':30,'low':10,'i':pygame.image.load('sticki.png')}
knuckles={'name':'brass knuckles','fmod':4,'hmod':0,'hdie':d4,'high':80,'low':60,'i':pygame.image.load('knucklesi.png')}
greatsword={'name':'greatsword','fmod':2,'hmod':0,'hdie':d10,'high':100,'low':75,'i':pygame.image.load('greatswordi.png')}
greataxe={'name':'greataxe','fmod':0,'hmod':2,'hdie':d10,'high':100,'low':75,'i':pygame.image.load('greataxei.png')}
claws={'name':'claws','fmod':0,'hmod':6,'hdie':d6,'high':120,'low':85,'i':pygame.image.load('clawsi.png')}
Vorpal={'name':'Vorpal Blade','fmod':3,'hmod':8,'hdie':d8,'high':200,'low':125,'i':pygame.image.load('vorpali.png')}
Berserker={'name':'Berserker Axe','fmod':3,'hmod':8,'hdie':d8,'high':200,'low':125,'i':pygame.image.load('berserkeri.png')}

# Monster Weapons

dagger={'fmod':0,'hmod':2,'hdie':d4()}
club={'fmod':0,'hmod':0,'hdie':d4()}
broadsword={'fmod':0,'hmod':3,'hdie':d6()}
claw={'fmod':0,'hmod':0,'hdie':d6()+d4()}
longsword={'fmod':0,'hmod':5,'hdie':d6()}

# Armor

scrap={'name':'scrap armor','ac':6} # Skeleton only
cloth={'name':'cloth armor','ac':8,'high':50,'low':20,'i':pygame.image.load('clothi.png')}
leather={'name':'leather armor','ac':10,'high':75,'low':50,'i':pygame.image.load('leatheri.png')}
chain={'name':'chain armor','ac':12,'high':100,'low':75,'i':pygame.image.load('chaini.png')}
scale={'name':'scale armor','ac':14,'high':150,'low':100,'i':pygame.image.load('scalei.png')}
plate={'name':'plate armor','ac':16,'high':200,'low':150,'i':pygame.image.load('platei.png')}
body={'name':'body armor','ac':17,'high':300,'low':150,'i':pygame.image.load('bodyi.png')}

# Treasure

garnet={'name':'garnet','val':100,'high':150,'low':50,'i':pygame.image.load('garneti.png')}
saphire={'name':'saphire','val':150,'high':200,'low':100,'i':pygame.image.load('saphirei.png')}
ruby={'name':'ruby','val':200,'high':250,'low':150,'i':pygame.image.load('rubyi.png')}
diamond={'name':'diamond','val':250,'high':300,'low':200,'i':pygame.image.load('diamondi.png')}
ring={'name':'ring','val':300,'high':350,'low':250,'i':pygame.image.load('ringi.png')}
bangle={'name':'bangle','val':350,'high':400,'low':300,'i':pygame.image.load('banglei.png')}
necklace={'name':'necklace','val':400,'high':450,'low':350,'i':pygame.image.load('necklacei.png')}
tiara={'name':'tiara','val':450,'high':500,'low':400,'i':pygame.image.load('tiarai.png')}
crown={'name':'crown','val':500,'high':550,'low':450,'i':pygame.image.load('crowni.png')}
chalice={'name':'chalice','val':600,'high':650,'low':550,'i':pygame.image.load('chalicei.png')}
painting={'name':'painting','val':750,'high':800,'low':700,'i':pygame.image.load('paintingi.png')}
philosopher={'name':"Philosopher's Stone",'val':1000,'high':1500,'low':750}

# Items

weapons=[sword,sword,sword,stick,knuckles,greatsword,greatsword,greataxe,greataxe,claws,claws,Vorpal,Berserker]

armor=[cloth,leather,chain,scale,plate,body]

loot=[garnet,saphire,ruby,diamond,ring,bangle,necklace,tiara,crown,chalice,painting,philosopher]

# Player

travel=0

placeholder=1

player={'name':'name','wep':placeholder,'wfmod':0,'hmod':2,'hdie':d6,'lvl':1,'dmod':0,'hp':25,'armor':[cloth],'ac':8,'mhp':25,'fmod':4,'mp':15,'mmp':15,'xp':0,'mxp':100,'gp':0}

player['name']=str(input("What is you're name traveller? "))
while player['wep']==placeholder:
    pygame.event.get()
    pygame.mixer.init(44100, -16, 2, 2048)
    pygame.mixer.music.load('song.wav')
    pygame.mixer.music.play(0)
    wepchoice=input('\nWhat is you weapon of choice?\n    -Sword\n    -Axe\n    -Mace\n').lower()
    
    if  wepchoice=='sword':
        image(sword['i'])
        player['wep']=sword['name']
            
    elif  wepchoice=='axe':
        image(axe['i'])
        player['wep']=axe['name']
        
    elif  wepchoice=='mace':
        image(mace['i'])
        player['wep']=mace['name']
        
    elif wepchoice=='none':
        image(fists['i'])
        print('Fists it is!')
        player['wep']=fist['name']
        player['wfmod']=fist['fmod']
        player['hmod']=fist['hmod']
        player['hdie']=fist['hdie']
        
    elif  wepchoice=='zyxxy':
        player['wep']='Test Sabre 9000'
        player['wfmod']=20
        player['hmod']=100
        player['hdie']=d12()*4

    else:
        print('Invalid Input')
    pygame.event.get()
    pygame.event.wait()

inventory=[]

score=0

# Functions

def monsterChoice(player):
    global cr
    num=player['lvl']/2
    if num==float:
        num=int(num-0.5)
    else:
        num=int(num)
    crnum=cr[(num)]
    return random.choice(crnum)

def encounter(player):
    global travel
    monster=(monsterChoice(player))
    encounter=d100()
    if encounter>=0 and encounter<=80:
        image(monster['i'])
        pygame.display.flip()
        combat(monster)
        travel+=1
    if encounter>80 and encounter<=85:
        lifeSpring()
        travel+=7
    if encounter>85 and encounter<=90:       
        image(pygame.image.load('shopi.png'))
        pygame.display.flip()
        shop()
        travel+=5
    if encounter>90 and encounter<=94:
        image(pygame.image.load('puzzlei.png'))
        puzzle()
        travel+=7
    if encounter==95:
        image(pygame.image.load('leprechaunni.png'))
        leprechaunn()
        travel+=5
    if encounter>96 and encounter<=97:
        image(pygame.image.load('treasurei.png'))
        mimic
        travel+=10
    if encounter==98:
        image(pygame.image.load('secreti.png'))
        secret1()
        travel+=3
    if encounter==99:
        image(pygame.image.load('secreti.png'))
        secret2()
        travel+=3
    if encounter==100:
        image(pygame.image.load('treasurei.png')) 
        treasure()
        travel+=10

def playerXP(player):
    if player['xp']>=player['mxp']:
        player['mhp']+=10
        player['hp']=player['mhp']
        player['mmp']+=10
        player['mp']=player['mmp']
        player['fmod']+=1
        print('Level up!')
        player['mxp']=round(player['mxp']*2.5,0)
        player['lvl']+=1
        time.sleep(3)

# Encounter Types

def treasure():
    global inventory
    global player
    gold=random.randint(10,250)
    item1=0
    item2=0
    item3=0
    if d6()==6:
        item1=random.choice(weapons)
    if d6()==6 and item1==0:
        item2=random.choice(armor)
    if d6()==6:
        item3=random.choice(loot)
    print('You found a treasure chest!')
    choice=0
    while choice!='y' and choice!='n':
        choice=str(input('Will you open it? (Y/N) ')).lower()
        if choice=='y':
            print('\n\nIt holds:\n',gold,' gold pieces',sep='')
            if item1!=0:
                print(item1['name'])
            if item2!=0:
                print(item2['name'])
            if item3!=0:
                print(item3[0])
            time.sleep(0.5)
            if item1!=0:
                choice=0
                prompt=('Will you switch your weapon to the '+item1['name']+'?(Y/N) ')
                image(item1['i'])
                while choice!='y' and choice!='n':
                    choice=input(prompt).lower()
                    if choice=='y':
                        player['wep']=item1['name']
                        player['wfmod']=item1['fmod']
                        player['hmod']=item1['hmod']
                        player['hdie']=item1['hdie']
                        print('You equip the ',item1['name'],'.',sep='')
                        time.sleep(0.1)
                    else:
                        print('You decided to leave the ',item1['name'],' behind.',sep='')
                        time.sleep(0.1)
            if item2!=0:
                choice=0
                prompt=('Will you switch your armor to the '+item2['name']+'? (Y/N) ')
                image(item2['i'])
                while choice!='y' and choice!='n':
                    choice=input(prompt).lower()
                    if choice=='y':
                        player['armor']=item2['name']
                        player['ac']=item2['ac']
                        print('You equip the ',item2['name'],'.',sep='')
                        time.sleep(0.1)
                    else:
                        print('You decide to leave the ',item2['name'],' behind.',sep='')
                        time.sleep(0.1)
            if item3!=0:
                print('You add the ',item3[0],' to your treasure sack.',sep='')
                image(item3['i'])
                inventory.append(item3)
                time.sleep(0.1)
            player['gp']+=gold
        elif choice=='n':
            print('You can never be too safe.')
        elif choice!='y' and choice!='n':
            print('Invalid Input.')

def combat(monster):
    print('\nA ',monster['name'],' appears!',sep='')
    time.sleep(0.2)
    while monster['hp']>0 and player['hp']>0:
        if monster['hp']<=monster['mhp']/2:
            print('\nThe ',monster['name'],' is bloodied.',sep='')
            time.sleep(1)
        else:
            print('\nThe ',monster['name'],' looks ready to fight.',sep='')
            time.sleep(1)
        if player['hp']<=player['mhp']/2:
            print('\nYou feel weak...')
            time.sleep(1)
        print('\n',player['name'],', You have ',player['hp'],' out of ',player['mhp'],' HP remaining, and ',player['mp'],' out of ',player['mmp'],' MP remaining.\n',sep='')
        time.sleep(0.5)
        print('What will you do?\n')
        time.sleep(0.5)
        print('+------------------------------+\n|(f)ight | (d)efend | (s)pells |\n+------------------------------+\n',sep='')
        choice=input('Choice: ')
        mchoice=random.randint(0,3)
        while choice!='f' and choice!='fight' and choice!='d' and choice!='defend' and choice!='s' and choice!='spells':
            print('Invalid input.')
            choice=input('Choice: ')
        if choice=='s' or choice=='spells':
            spells(monster)
            time.sleep(1)
        if mchoice==3:
            print('The ',monster['name'],' braces itself.',sep='')
            time.sleep(1)
            monster['dmod']=5
        if choice=='f' or choice=='fight':
            dmg(player,monster)
            time.sleep(1)
        elif choice=='d' or choice=='defend':
            player['dmod']=3
            print('You brace for the ',monster['name'],str("'s attack."),sep='')
            time.sleep(1)
        if monster['hp']<=0:
            break
        if mchoice!=3:
            dmg(monster,player)
            time.sleep(1)
        monster['dmod']=0
        player['dmod']=0
        if player['mp']<player['mmp']:
            player['mp']+=1
    if player['hp']<=0:
        print('\nYou have been defeated.\nAnd thus ends the story of ',player['name'],'...',sep='')
    else:
        gold=random.randint(((player['lvl'])*3),((player['lvl'])*10))
        print("\nThe ",monster['name']," falls down, defeated.\nYou gain ",monster['xp']," xp, and ",gold," gp.",sep='')
        player['xp']+=monster['xp']
        player['gp']+=gold
        playerXP(player)
        monster['hp']=monster['mhp']
        time.sleep(2)

def lifeSpring():
    global player
    print('You find a small spring of magic water. Your wounds are restored!')
    player['hp']=player['mhp']
    time.sleep(2)

def strangeMan():
    global bandit
    print('You encounter a strange cloaked figure. He says with a rough and gravelly voice, "Show me your hand traveller...". Will you listen to him? (Y/N)')
    choice=str(input('> ')).lower()
    luck=random.randint(1,2)
    if choice=='y' and luck==1:
        print('The strange man places a small coin pouch in your hands. It contains 20 gold!')
        player['gp']+=20
    if choice=='y' and luck==2:
        print("The cloaked figure reveals themselves to be a bandit! They strike you while you're open!")
        player['hp']-=d6()
        combat(bandit)
    elif choice=='n':
        print('You decide not to risk it, and ignore the strange man.')
    time.sleep(2)

def puzzle():
    global player
    functions=['+','-','*']
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    function=random.choice(functions)
    if function=='+':
        solution=((num1)+(num2))
    if function=='-':
        solution=((num1)-(num2))
    if function=='*':
        solution=((num1)*(num2))
    print('You find a strange room with a series of runes and buttons.')
    time.sleep(1)
    print('.',end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)
    print('After spending some time, you decipher the runes as saying:\n',num1,' ',function,' ',num2,' = ',sep='')
    answer=int(input('What is your answer? '))
    if answer==solution:
        print('You hear a series of clicks and bangs, before a secret panel opens in the wall.')
        treasure()
    else:
        print("Nothing happens. You figure it's mostly gibberish and continue on your way.")
    time.sleep(2)

def leprechaunn():
    global player
    print('You find a strange little man dressed in all green, huddled over a glittering pot. He says to you, "Hands off me gold!".')
    choice=0
    while choice!='y' and choice!='n':
        choice=str(input('Will you attempt to take the gold? (Y/N) ')).lower()
        if choice=='y':
            print('The leprechaun attacks!')
            combat(leprechaun)
            player['gp']+=250
            print("You retrieve 250 gp from the pot.")
        if choice=='n':
            print('On second thought, he probably needs it more than you.')
    time.sleep(2)

def mimic():
    global player
    global mimic
    print('You found a traesure chest!')
    choice=0
    while choice!='y' and choice!='n':
        choice=str(input('Will you open it? (Y/N) ')).lower()
        if choice=='y':
            print('AAH! It was a mimic!')
            combat(mimic)
        if choice=='n':
            print('You can never be too safe.')
        else:
            print('Invalid Input')
    time.sleep(2)

def secret1():
    global secretpoints
    global player
    print('You stumble across a strange tome.\nInside it reads, "Open the fabrics of space and time, write unto me what it is that you find...".')
    time.sleep(3)
    choice=str(input('What do you write? ')).lower()
    print('. ',end='')
    time.sleep(0.5)
    print('. ',end='')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    if choice=="in his house in r'lyeh, cthulhu sleeps.":
        print('The book bursts into flames, but does not hurt you, instead it fills you with a newfound vigor. Your wounds are healed.')
        player['hp']=player['mhp']
        secretpoints+=1
        time.sleep(2)
    else:
        print('Nothing happens. You should get going...')
        time.sleep(2)

def secret2():
    global secretpoints
    global player
    global wep1
    print('You find yourself blinded by white light, as random numbers and letters become engraved in your mind.')
    time.sleep(1)
    print('536f206d75636820746f2077696e2c20736f206d75636820746f206c6f73652e20497420616c6c20646570656e6473206f6e207768617420796f752063686f6f73652e')
    time.sleep(1)
    choice=str(input('How do you respond? ')).lower()
    print('. ',end='')
    time.sleep(0.5)
    print('. ',end='')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    if choice==wep1:
        print('Wise choice...')
        secretpoints+=1
        time.sleep(2)
    else:
        print('Nothing happens.')
        time.sleep(2)

def shop():
    global player
    global inventory
    global weapons
    global armor
    global loot
    items=[weapons,armor,loot]
    itemt1=(list.pop(items,(random.randint(0,2))))
    itemt2=0
    if d6()==5 or d6()==6:
        itemt2=(list.pop(items,(random.randint(0,1))))
    item1=random.choice(itemt1)
    item2=0
    if itemt2!=0:
        item2=random.choice(itemt2)
    p1=random.randint((item1['low']),(item1['high']))
    p2=0
    if itemt2!=0:
        p2=random.randint((item2['low']),(item2['high']))
    print("You meet a wandering hermit, who says he's willing to part with some of his items, for a price.")
    choice=str(input('Will you look at his wares? (Y/N) ')).lower()
    while choice!='y' and choice!='yes' and choice!='n' and choice!='no':
        print('Invalid Input.')
        time.sleep(0.3)
        choice=str(input('Will you look at his wares? (Y/N) ')).lower()
    if choice=='y' or choice=='yes':
        print('"This is what I can part with."')
        time.sleep(0.2)
        buy=0
        while buy!='e' and buy!='exit':
            if itemt1==0 and itemt2==0:
                buy='e'
                break
            if itemt1!=0:
                print('1. ',item1['name'],' - ',p1,'gp',sep='')
                time.sleep(0.2)
            if itemt2!=0:
                print('2. ',item2['name'],' - ',p2,'gp',sep='')
                time.sleep(0.2)
            print('Select the item you want to buy, or type "e" to exit.')
            time.sleep(0.1)
            print('You have ',player['gp'],'gp.',sep='')
            buy=input('> ').lower()        
            if itemt2!=0:
                while buy!='1' and buy!=item1['name'] and buy!='2' and buy!=item2['name'] and buy!='e' and buy!='exit' and buy!='steal':
                    print('Invalid Input.')
                    buy=input('> ').lower()
            if itemt1==0:
                while buy!='2' and buy!=item2['name'] and buy!='e' and buy!='exit' and buy!='steal':
                    print('Invalid Input.')
                    buy=input('> ').lower()
            else:
                while buy!='1' and buy!=item1['name'] and buy!='e' and buy!='exit' and buy!='steal':
                    print('Invalid Input.')
                    buy=input('> ').lower()
            if buy=='1' or buy==item1['name'] and itemt1!=0:
                if p1>player['gp']:
                    print("You don't have enough gp!")
                else:
                    print('You exchange ',p1,'gp for the ',item1['name'],'.',sep='')
                    if itemt1==armor:
                        player['ac']=item1['ac']
                        player['armor']=item1['name']
                    elif itemt1==weapons:
                        player['wep']=item1['name']
                        player['wfmod']=item1['fmod']
                        player['hmod']=item1['hmod']
                        player['hdie']=item1['hdie']
                    elif itemt1==loot:
                        inventory.append(item1)
                    player['gp']-=p1
                    itemt1=0
            if itemt2!=0:
                if buy=='2' or buy==item2['name']:
                    if p2>player['gp']:
                        print("You don't have enough gp!")
                    else:
                        print('You exchange ',p2,'gp for the ',item2['name'],'.',sep='')
                        if itemt2==armor:
                            player['ac']=item2['ac']
                            player['armor']=item2['name']
                        if itemt2==weapons:
                            player['wep']=item2['name']
                            player['wfmod']=item2['fmod']
                            player['hmod']=item2['hmod']
                            player['hdie']=item2['hdie']
                        if itemt2==loot:
                            inventory.append(item2)
                        player['gp']-=p2
            if buy=='steal':
                regret=str("You're gonna regret that!")
                print(regret)
                combat(shopkeep)
                if player['hp']<=0:
                    buy='e'
                    break
                else:
                    print('You steal 500gp from the shopkeep, but everything else was destroyed in the combat.')
                    player['gp']+=500
                    buy='e'
                    break
            if buy=='e' or buy=='exit':
                break
        print('You and the hermit part ways.')
    if choice=='n' or choice=='no':
        print('You should probably save your coin.')
    time.sleep(2)

def score():
    global inventory
    global player
    global cscore
    print('You Found:\n\n - ',player['gp'],' gp\n - ',inventory.count(garnet),' Garnet - val. 100 gp\n - ',inventory.count(saphire),' Saphire - val. 150 gp\n - ',inventory.count(ruby),' Ruby - val. 200 gp\n - ',inventory.count(diamond),' Diamond - val. 250 gp\n - ',inventory.count(ring),' Ring - val. 300 gp\n - ',inventory.count(bangle),' Bangle - val. 350 gp\n - ',inventory.count(necklace),' Necklace - val. 400 gp\n - ',inventory.count(tiara),' Tiara - val. 450 gp\n - ',inventory.count(crown),' Crown - val. 500 gp\n - ',inventory.count(chalice),' Chalice - val. 600 gp\n - ',inventory.count(painting),' Painting - val. 750 gp\n - ',inventory.count(philosopher)," Philospher's Stone - val. 1000 gp\n",sep='')
    cscore+=player['gp']+(inventory.count(garnet)*100)+(inventory.count(saphire)*150)+(inventory.count(ruby)*200)+(inventory.count(diamond)*250)+(inventory.count(ring)*300)+(inventory.count(bangle)*350)+(inventory.count(necklace)*400)+(inventory.count(tiara)*450)+(inventory.count(crown)*500)+(inventory.count(chalice)*600)+(inventory.count(painting)*750)+(inventory.count(philosopher)*1000)
    print('Your current score is: ',cscore,sep='')
    inventory=[]
# Spell Functions

def spells(monster):
    global player
    spell=1
    print('+','-'*8,'+\n| Spells |\n+','-'*8,'+',sep='')
    print('1. Magic Missile (3 MP)\n2. Lay on Hands (5 MP)\n3. Mage Armor (5 MP)\n')
    while True:
        try:
            choice=int(input('Choice: '))
            while choice!=1 and choice!=2 and choice!=3:
                print('Invalid Input.')
                choice=int(input('Choice: '))
            break
        except TypeError and ValueError:
            print('Invalid Input.')
    if choice==1:
        if player['mp']-3 < 0:
            print("You don't have enough MP!")
        else:
            magicMissile(player,monster)
    if choice==2:
        if player['mp']-5 < 0:
            print("You don't have enough MP!")
        else:
            layOnHands(player)
    if choice==3:
        if player['mp']-5 < 0:
            print("You don't have enough MP!")
        else:
            mageArmor(player)
   
def magicMissile(player,monster):
    dmg=d4()*(player['lvl'])
    monster['hp']-=dmg
    print('You blast the ',monster['name'],' with a flurry of magic missiles, dealing ',dmg,' damage!',sep='')
    player['mp']-=3

def layOnHands(player):
    dmg=d8()*(player['lvl'])
    player['hp']+=dmg
    if player['hp']>player['mhp']:
        player['hp']=player['mhp']
    print('You channel divine energies, recovering ',dmg,' HP!')
    player['mp']-=5

def mageArmor(player):
    player['dmod']=8
    print('You conjure a shield of arcane energies, and brace yourself for an attack.')
    player['mp']-=5

def dmg(cha1,cha2):
    die=d20()
    if die+cha1['fmod']+cha1['wfmod']>cha2['ac']+cha2['dmod']:
        if die==20:
            dmg=(cha1['hdie']())*2+cha1['hmod']

            cha2['hp']=cha2['hp']-dmg
            print("Critical Hit!\n",cha1['name']," strikes ",cha2['name']," with their ",cha1['wep'],", dealing ",dmg," damage!",sep="")
        else:
            dmg=(cha1['hdie']())+cha1['hmod']
            cha2['hp']=cha2['hp']-dmg
            print(cha1['name']," strikes ",cha2['name']," with their ",cha1['wep'],", dealing ",dmg," damage!",sep="")
    else:
        print(cha1['name'],' misses ',cha2['name'],' with their ',cha1['wep'],'.',sep='')

# Monsters

# Special Monsters
leprechaun={'name':'leprechaun','wep':'horseshoe','wfmod':3,'hmod':4,'hdie':d12,'hp':40,'armor':'tophat','ac':8,'mhp':40,'dmod':0,'xp':100,'fmod':0,'i':pygame.image.load("leprechauni.png")}
mimic={'name':'mimic','wep':'mouth','wfmod':2,'hmod':8,'hdie':d8,'hp':45,'armor':'wood','ac':12,'mhp':45,'dmod':0,'xp':75,'fmod':0,'i':pygame.image.load("mimici.png")}
shopkeep={'name':'shopkeeper','wep':'Blade of Vengance','wfmod':10,'hmod':20,'hdie':d20,'hp':500,'armor':'Diamond','ac':20,'mhp':500,'dmod':0,'xp':10000,'fmod':0,'i':pygame.image.load("shopkeepi.png")}

# CR 1
goblin={'name':'goblin','wep':'club','wfmod':0,'hmod':0,'hdie':d4,'hp':12,'armor':'cloth','ac':8,'mhp':12,'dmod':0,'xp':25,'fmod':0,'i':pygame.image.load("goblini.png")}
bandit={'name':'bandit','wep':'dagger','wfmod':0,'hmod':0,'hdie':d6,'hp':12,'armor':'leather','ac':10,'mhp':12,'dmod':0,'xp':25,'fmod':0,'i':pygame.image.load("banditi.png")}
skeleton={'name':'skeleton','wep':'club','wfmod':0,'hmod':-2,'hdie':d6,'hp':12,'armor':'scrap','ac':6,'mhp':12,'dmod':0,'xp':25,'fmod':0,'i':pygame.image.load("skeletoni.png")}
cr1=[goblin,bandit,skeleton]

# CR 2
hobgoblin={'name':'hobgoblin','wep':'broadsword','wfmod':0,'hmod':3,'hdie':d6,'hp':25,'armor':'leather','ac':10,'mhp':25,'dmod':0,'xp':50,'fmod':0,'i':pygame.image.load("hobgoblini.png")}
zombie={'name':'zombie','wep':'claw','hmod':0,'wfmod':3,'hdie':d6,'hp':25,'armor':'cloth','ac':8,'mhp':30,'dmod':0,'xp':25,'fmod':0,'i':pygame.image.load("zombiei.png")}
bandit_captain={'name':'bandit captain','wep':'longsword','wfmod':0,'hmod':5,'hdie':d6,'hp':25,'armor':'chain','ac':14,'mhp':25,'dmod':0,'xp':50,'fmod':0,'i':pygame.image.load("bandit_captaini.png")}
cr2=[hobgoblin,zombie,bandit_captain]

# CR 3
orc={'name':'orc','wep':'battleaxe','wfmod':0,'hmod':3,'hdie':d12,'hp':30,'armor':'leather','ac':10,'mhp':30,'dmod':0,'xp':100,'fmod':0,'i':pygame.image.load("orci.png")}
wraith={'name':'wraith','wep':'life steal','wfmod':0,'hmod':8,'hdie':d6,'hp':27,'armor':'spectral','ac':10,'mhp':27,'dmod':0,'xp':100,'fmod':0,'i':pygame.image.load("wraithi.png")}
centaur={'name':'centaur','wep':'trident','wfmod':0,'hmod':6,'hdie':d10,'hp':28,'armor':'chain','ac':14,'mhp':28,'dmod':0,'xp':100,'fmod':0,'i':pygame.image.load("centauri.png")}
cr3=[orc,wraith,centaur]

# CR 4
cave_troll={'name':'cave troll','wep':'greatest club','wfmod':2,'hmod':4,'hdie':d12,'hp':35,'armor':'plate leather','ac':14,'mhp':35,'dmod':0,'xp':200,'fmod':0,'i':pygame.image.load("cave_trolli.png")}
ghoul={'name':'ghoul','wep':'infernal claws','wfmod':0,'hmod':12,'hdie':d8,'hp':30,'armor':'spectral','ac':12,'mhp':30,'dmod':0,'xp':200,'fmod':0,'i':pygame.image.load("ghouli.png")}
stone_golem={'name':'stone golem','wep':'decimating fists','wfmod':0,'hmod':0,'hdie':d8,'hp':40,'armor':'stone','ac':16,'mhp':40,'dmod':0,'xp':200,'fmod':0,'i':pygame.image.load("stone_golemi.png")}
cr4=[cave_troll,ghoul,stone_golem]

#CR 5
ogre={'name':'ogre','wep':'cleaver','wfmod':0,'hmod':6,'hdie':d12,'hp':40,'armor':'heavy leather','ac':17,'mhp':40,'dmod':0,'xp':400,'fmod':0,'i':pygame.image.load("ogrei.png")}
ghast={'name':'ghast','wep':'shadow punch','wfmod':0,'hmod':10,'hdie':d10,'hp':35,'armor':'cursed spectral','ac':14,'mhp':35,'dmod':0,'xp':400,'fmod':0,'i':pygame.image.load("ghasti.png")}
gargoyle={'name':'gargoyle','wep':'halberd','wfmod':0,'hmod':6,'hdie':d12,'hp':38,'armor':'stone','ac':16,'mhp':38,'dmod':0,'xp':400,'fmod':0,'i':pygame.image.load("gargoylei.png")}
cr5=[ogre,ghast,gargoyle]

# CR List
cr=[cr1,cr2,cr3,cr4,cr5]

# Bosses
minotaur={'name':'Minotaur','wep':'Greataxe','wfmod':2,'hmod':4,'hdie':d8,'hp':55,'armor':'Plate Leather','ac':14,'mhp':55,'dmod':0,'xp':150,'fmod':0,'i':pygame.image.load("minotauri.png")}
beholder={'name':'Beholder','wep':'Destruction Ray','wfmod':5,'hmod':8,'hdie':d10,'hp':120,'armor':'Natural','ac':16,'mhp':120,'dmod':0,'xp':300,'fmod':0,'i':pygame.image.load("beholderi.png")}
red_dragon={'name':'Red Dragon','wep':'Fire Breath','wfmod':6,'hmod':12,'hdie':d12,'hp':250,'armor':'Dragon Scale','ac':18,'mhp':250,'dmod':0,'xp':1000,'fmod':0,'i':pygame.image.load("red_dragoni.png")}
orf={'name':'Orf the Orc','wep':'club reinforced with human body','wfmod':10,'hmod':12,'hdie':d20,'hp':500,'armor':'Thicc','ac':20,'mhp':500,'dmod':0,'xp':10000,'fmod':0,'i':pygame.image.load("orfi.png")}

# Main
print('loading...')
time.sleep(2)
travel=0
clock = pygame.time.Clock()
while player['hp']>=0:
    screen.fill(0)
    clock.tick(60)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
    print("You travel down the dark and winding forest, towards the infamous Dungeon of Dragon on a quest to find your fortune in the labyrinth's many riches...\nand dangers.")
    time.sleep(5)
    while travel<25:
        encounter(player)
        pygame.event.get()
        if player['hp']<=0:
            image(pygame.image.load('losei.png'))
            break
    if player['hp']<=0:
        image(pygame.image.load('losei.png'))
        break
    travel=0
    print('You stumble into a dark, dank room. On the other side of it you can hear heavy breathing, and the trotting of hooves...')
    time.sleep(3)
    combat(minotaur)
    if player['hp']<=0:
        break
    print("You venture deeper into the dungeon, as the walls shift from unshapely cavernous rock, to neatly layed bricks lined with damp moss.")
    time.sleep(3)
    while travel<50:
        encounter(player)
        if player['hp']<=0:
            image(pygame.image.load('losei.png'))
            break
    if player['hp']<=0:
        image(pygame.image.load('losei.png'))
        break
    travel=0
    print("Deeper in the dungeon still, you come across a seemingly empty room...")
    time.sleep(1)
    print("/nAnd yet you can't seem to shake the feeling that you're being watched...")
    time.sleep(3)
    combat(beholder)
    if player['hp']<=0:
        image(pygame.image.load('losei.png'))
        break
    print("With the many eyes of the beholder strewn around you, you push deeper as the walls seemingly grow and tower above you, until you find yourself in the halls of what was once a mighty dwarven empire.")
    while travel<75:
        encounter(player)
        if player['hp']<=0:
            image(pygame.image.load('losei.png'))
            break
    if player['hp']<=0:
        image(pygame.image.load('losei.png'))
        break
    travel=0
    print("Tired and weary from your quest, you push further into one final room, sweltering with heat, and filled to the brim with glittering gold.")
    time.sleep(3)
    combat(red_dragon)
    player['gp']+=1000
    print("You have done it.")
    time.sleep(1)
    print("The ferocious red dragon lies defeated beneath your blade, and before you lie the spoils of war. Quickly, you shovel as many gold coins as you can into your bag, and a magic field transports you to the dungeons entrance, that you stood before seemingly so long ago.")
    image(pygame.image.load('wini.png'))
    if player['hp']<=0:
        image(pygame.image.load('losei.png'))
        break
    if secretpoints==2:
        combat(orf)
        image(pygame.image.load(orf['i']))
        secretpoints=0
    if player['hp']<=0:
        image(pygame.image.load('losei.png'))
        break
    score()
    print('You finally found your fortune, a whole ',score,' gp.\nAnd yet... the rush of adventure still flows through you, and you can feel the dungeons entrance calling to you once more...',sep='')
    time.sleep(3)
    choice=str(input('Will you go back? (Y/N): ')).lower()
    if choice=='n' or choice=='no':
        print('You have what you came for, best to not risk losing it all.')
        break

