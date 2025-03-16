# Scrap DAtes
 Unhinged VN ft. lots of scraps
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
