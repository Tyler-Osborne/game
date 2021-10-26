# The script of the game goes in this file.

image sj movie = Movie(play="spriteless_jerks.m4v")
image cmg movie = Movie(play="click_me_godot.m4v")
image ds3 = "ds3_dancer.jpg"
image gc = "godotchan.png"
image intro = "Intro_Slide.png"
image nfm = "night_full_moon.jpg"
image mrm = "mrm.png"
image mffaaf = "mffaaf.png"
image bp = "bandlab_profile.png"
image ecwls = "ecwls.png"
image ims = "ims.png"
image djpimi = "djpimi.png"

default preferences.text_cps = 50

# The game starts here.

label start:
    scene bg
    show intro:
        xalign 0.5
        yalign 0.5
    with fade
    play music "audio/I Dream - Nukleah.ogg"
    ""

label mrm:
    scene bg
    show mrm
    with fade
    ""
    show black
    with fade
    centered """I dabble in a lot of activities:\n{w}
    • Playing Video Games\n{w}
    • Music Production\n{w}
    • Developing Software\n{w}
    • Novice Game Development"""
    nvl clear

label sdtg:
    scene bg
    centered "I prefer skill based single player games.\n{w}I'll show you some examples."
    show ds3
    with fade
    "This game is called Dark Souls 3.\n{w}It is difficult but overcoming the challenges is so rewarding."
    show nfm
    with fade
    "This is Night of the Full Moon.\n{w}It's a very addicting Roguelike Deckbuilder that I used to play multiple times a day."
    hide ds3
    hide nfm
    with fade
    centered "The thrill of learning pattern recognition and\napplying it to real life has been very beneficial to me."
    
label mffaaf:
    scene bg
    with Dissolve(2.0)
    show mffaaf
    with fade
    ""
    show bp
    with fade
    "This is my Bandlab Profile.\n{w}That is where I publish music that I have produced."
    "In fact, the track that has been playing this whole time is one I call \"I Dream\""
    "I produce EDM but have been looking into how to make Trap music as I have taken a liking to it."

label ecwls:
    scene bg
    with Dissolve(2.0)
    show ecwls
    with fade
    ""
    hide ecwls
    with fade
    "I love C#. {w}I am becoming more proficient with it every time I use it."
    show ics
    with fade
    "This is a prototype for an Inventory Control System I made with C#."
    hide ics
    with fade
    centered "I am currently developing a numerology calculator with cross-platform targets."

label djpimi:
    

return