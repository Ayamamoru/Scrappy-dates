# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

  
define e = Character('French pigeon',color="#00ff00")
define s = Character('Possum boi', color="#ff0000")
define m = Character('Me', color="#7373e7")
define d = Character('Alices rat', color="#ff00ea")
define k = Character('Trash can', color="#0033ff")
define good_points = 0
define bad_points = 0
define neutral_points = 0

default book = False

# The game starts here.

label start:
   $ bad_points = 0
   $ good_points = 0
   $ neutral_points = 0
   image French pigeon = Image("French pigeon.png")
   
   image Possum boi = Image("Possum boi.png")
   image Alices rat = Image("Alices rat.png")
   image Trash can = Image("Trash can.png")
   image Opening = Image("Opening (1).png")
   image Bad = Image("Bad.png")
   image Good = Image("Good.png")
   image Weird = Image("Weird end.png")
   image City = Image("City.png")
   image Scrapyard = Image("Scrapyard.png")
   image dumpster = Image("dumpster.png")
   image Scrap2 = Image("Scrap2.png")
   image question = Image("Question mark.png")
   image angry = Image("Rotting fruit.png")

   show French pigeon at left
   
   scene Opening
   e "Yo, you stink, are you new here?"
   scene Scrapyard with fade
   play music "Mysterious place.mp3"
   show French pigeon at left 
menu option_1:
      "Take offence":
         $ bad_points += 1
         jump take_offence
      "Ignore rude comment":
         $ good_points += 1
         jump ignore_comment

label take_offence:
   show French pigeon at left 
   m "Un, sorry, did you just say I stink?"
   e "Aye (french), no need to get angry here! Jeez."
   e "(Whispers) Mais c'est vrai que t moche. (English; But it's true that you're ugly.)"
   m "Rude. Anyways, I guess I am here."
   jump start_1

label ignore_comment:
   show French pigeon at left
   m "Um, yes I am."
   jump start_1

label start_1:
   show French pigeon at left 
   play music "Quiet Autumn.mp3"
   e "Well lucky for you, I'm very familier with the area. I can show you around."
   m "Great."
   scene Scrap2 with fade
   e "This is Epic awesome stank yard. There's a lot to do here, but I think the best area in Crazy sus negative rizz landfill."
   scene dumpster with fade
   e "Well this is it, isn't it wonderful. You can partially see the stench of this place. Yum yum."
   show Possum boi at right
   show French pigeon at left
menu option_2:
      "Are you the only one who lives here?":
         $ good_points += 1
         jump answer_1
      "Why do you look like that?":
         $ bad_points += 1
         jump answer_2
      "Why is the demonic possum looking at me?":
         $ neutral_points += 1
         jump answer_3
label answer_1:
   show French pigeon at left 
   e "Nope, there's lots of bacteria living here. Heh positive"
   jump start_2
label answer_2: 
   show French pigeon at left 
   e "I could ask you the same, but I have manners."
   jump start_2

label answer_3:
   show French pigeon at left 
   e "Oh he's just observing you to see if you could help him overthrow the rat king"
   jump start_2

label start_2:
   show French pigeon at left  
   e "Well anyway, why don't we go check out the-"
   show Alices rat 
   d "A new soul, wandering the Crazy sus negative rizz landfill! How fortuitous for you! For you to stand before an envoy of the Great One!"

menu option_3:
      "Uh... the Great One?":
         $ good_points += 1
         jump answer_4
      "You crawled out of a trash can. I don't trust you.":
         $ bad_points += 1
         jump answer_5

label answer_4:
   show Alices rat  
   show French pigeon at left
   d "Yes! The Rat King, ruler of the unseen! The whisper in the gutters! The many-tailed one! We are his faithful! And you... You could be one of us!"
   jump start_3

label answer_5:
   show Alices rat 
   show French pigeon at left
   d "A vessel of scared refuge, not mere trash, you ungrateful surface-dweller!"
   jump start_3

label start_3:
   show French pigeon at left 
   show Alices rat 
   show Possum boi at right
   s "Oh-hohh... a fresh little morsel, sniffing around for purpose." 
   e "Divorced cult leaders fighting for custody, classic."
   s "Why be a survent to the Rat King... when you could be free? No masters. No rules. Just the endless void."
   d "Lies! He will lead you into madness! The King offers purpose!"
   s "And I offer freedom. And... power. "
   e "That's enough from both of you."
   e "Let's go!"
   scene dumpster
   show French pigeon at left
   e "I'm sorry sbout them they are really passionate about there cults."
   m "I... get it?"
   e "Anyway how about we meet an elligable bachler?"

menu option_4:
      "What the sigma?":
         $ bad_points += 1
         jump answer_6
      "Nah, I'd win.(sure)":
         $ good_points += 1
         jump answer_7

label answer_6:    
   show French pigeon at left 
   e "Welp yo udon have a choice." 
   jump start_4

label answer_7:
   show French pigeon 
   e "Great lets go!" 
   jump start_4

label start_4:
   show French pigeon at left
   show Trash can at right 
   e "Yo, Looks Smaxer 3000 I have someone for you." 
   k "If it's another one of those rats, I swear I'll personally escort you to the nearest boulangerie and make sure you end up as the secret ingredient in tomorrow's baguette."
   e "Uh non merci en plus t vraiment moche ew laid degeu."
   play music "Run!.mp3"

menu option_5:
      "Run (Drag Pigeon with you.)":
         $ bad_points += 1
        
      "Run (Go to epic yard.)":
         $ neutral_points += 1
    
      "Run (Epic sigma option.)":
         $ good_points += 1

         if neutral_points == 2:
            jump weird
         if good_points >= bad_points:
            jump good
         if bad_points >= good_points:
            jump bad
        
label weird:
   scene Scrapyard
   show Alices rat
   m"WOAH OMG THE RAT IS STILL HERE"
   d"Yo, you want a ribbon"
   m"Uh sure"
   d"heh, that's so sigma of you"
   m"eerrrmmmmm"
   hide Alices rat
   scene Weird
   m"OBTAINED WEIRD ENDING.... just why..."
   
   jump cred


label good: 
   scene Scrapyard
   play music "THE HOLY.mp3"
   m"HEHEHHEHEHEHEHE"
   m"little did they know..."
   scene Good
   m"THAT IT WAS ALL A RUSE!!!"
   m"I, player, am the most powerful cult leader and now all of you are to join my cult. (or else)"
   m"OBTAINED UHH GOOD-KINDA ENDING.."
   jump cred

label bad:
   show French pigeon 
   e"OH NO YOU DON'T. YOU CAN'T RUN... THE DISRESPECT!!"
   m"HUH?????"
   e"JUST YOU WAIT"
   m"LET GO OF ME"
   hide French pigeon
   scene Bad
   m"You were dropped into the ocean by the french pigeon."
   m"OBTAINED BAD ENDING"
   jump cred

label cred:
   transform credits_scroll(speed):
      ypos 600
      linear speed ypos -260000

screen credits():

      ## Ensure that the game_menu screens can't be stopped
      key "K_ESCAPE" action NullAction()
      key "K_MENU" action NullAction()
      key "mouseup_3" action NullAction()

      style_prefix "credits"
 
      timer 60.0 action Return() ## Adjust this number to control when the Credits screen is hidden and the game
      ## returns to its normal flow.

      frame at credits_scroll(100.0): #bigger is slower
         ## Adjust this number to control the speed at which the credits scroll.
         background None
         xalign 0.5

         vbox:
            label "Credits" xalign 0.5
            null height 150
            label "Producer" xalign 0.5
            null height 75
            text "Team Sewer Rats"
            null height 10
            text "Selina Tung and Sarah Ford"
            null height 150
            label "Sprites" xalign 0.5
            null height 75
            text "Team Sewer Rats"
            null height 150
            label "Backgrounds" xalign 0.5
            null height 75
            text "Team Sewer Rats"         
            null height 150
            label "Scene art" xalign 0.5
            null height 75
            text "Selina Tung"
            null height 150
            label "Programming" xalign 0.5
            null height 75
            text "Team Sewer Rats"
            null height 150
            label "Code contributions (with perm)" xalign 0.5
            null height 10
            label "BadMustard(reddit), scrolling credits" xalign 0.5
            null height 10
            label "TormentedStudios(reddit), multi ends tutorial" xalign 0.5
            null height 150
            label "Music used (in order of usage)" xalign 0.5
            null height 10
            label "Mysterious Place - Toby Fox" xalign 0.5
            null height 10
            label "Field of Hopes and Dreams - Toby Fox" xalign 0.5
            null height 10
            text "Quiet Autumn - Toby Fox" xalign 0.5
            null height 10
            text "THE HOLY - Toby Fox" xalign 0.5
            null height 10
            label "Run! - Toby Fox" xalign 0.5
            null height 10
            label "Alphys - Toby Fox" xalign 0.5
            null height 10
            text "Premonition - Toby Fox" xalign 0.5
            null height 10
            text "Dating Start! - Toby Fox" xalign 0.5
            null height 150
            label "Special Thanks " xalign 0.5
            null height 10
            label "To" xalign 0.5
            null height 10
            label " all Scrapyard Ottawa organizers," xalign 0.5
            null height 10
            text "Hack Club,"
            null height 10
            text "WATER,"
            null height 10
            text "Reddit,"
            null height 10
            text "Youtube tu  torials,"
            null height 10
            text "and everybody else here!!"
            null height 10  
            label "Thanks for Playing!" xalign 0.5
            
            
style credits_hbox:
      spacing 40
      ysize 30

style credits_vbox:
      xalign 0.5
      text_align 0.5

style credits_label_text:
      xalign 0.5
      justify True
      size 125
      text_align 0.5
      color "#ff0000"

style credits_text:
      xalign 0.5
      size 60
      justify True
      text_align 0.5
      color "#ffffff"
return
