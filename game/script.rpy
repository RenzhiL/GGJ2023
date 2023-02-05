# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define N = Character("Noah")
image N default = "images/character/nMeh.png"
image N back = "images/character/nBack.png"
image N angry = "images/character/nAngry.png"
image N annoyed = "images/character/n annoyed.png"
image N happy = "images/character/nHappy.png"
image N sad = "images/character/nSad.png"
image N sadder = "images/character/nSadder.png"
image N lookdown = "images/character/n lookdown.png"

image N root = "images/character/nRoots.png"
image N root_annoyed = "images/character/n roots annoyed.png"
image N root_sadder = "images/character/n roots sadder.png"
image N root_angry = "images/character/n roots angry.png"

image N consumed = "images/character/nConsumed.png"

define T = Character("Sap")
image T default = "images/character/sap1.png"

define yN = Character("Young Noah")
image N young = "images/character/nYoung.png"

image N photo = "images/character/picture.png"

image bg dark = "images/background/dark.PNG"
image bg medium = "images/background/medium.PNG"
image bg light = "images/background/light.PNG"
image bg neutral = "images/background/neutral.PNG"
image bg bad = "images/background/bad.png"
image bg meh = "images/background/meh.png"
image bg good = "images/background/good.png"

transform lowered:
    align (0.5, 0.5)

transform more_lowered:
    align (0.5, 0.3)

transform even_more_lowered:
    align (0.5, -0.1)

##music
define audio.reveal = "audio/Loranthaceae.wav"
define audio.casual = "audio/Viscaceae.wav"
define audio.think = "audio/Orobanchaceae.wav"
define audio.sad = "audio/Cordyceps.wav"
define audio.angry = "audio/Balanophoraceae.wav"
define audio.finale = "audio/Piano.wav"

# The game starts here.

label start:
    $ p = 0
    play music casual volume 0.4 fadein 1.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg neutral

    # These display lines of dialogue.

    show T default at lowered
    with fade

    T "That’s me.{w=1} Or, {w=0.5}I guess, {w=0.5}this is me."

    T "Hi!"

    show N photo at lowered
    hide T default

    T "My human’s the guy in the photo there."

    T "His name is Noah."

    # SCENE: Zoom into photo, spirits hand touches it

    T "Isn’t he precious?"

    T "Well, {w=0.5}it’s my job to take care of Mr.Noah!"

    # SCENE: spirit looks a little sad in the mirror

    T "Noah’s always been struggling{cps=10}...{/cps} His family has been{cps=2}...{/cps} {cps=10}tough, {/cps}{w=1} to say the least."

    T "I wish I could talk to him outside of his dreams{w=0.3} which don’t even happen too often {cps=10}but...{/cps}"

    T "At least I can visit him in his dreams."

    T "At least I can do a little something, {w=0.5} despite being rooted down to this{cps=20} stagnant, {w=0.5} silent form{/cps}{cps=10}...{/cps}"

# SCENE 1
    # CUTSCENE: Younger N "
    scene bg light

    show N young at lowered
    with fade

    yN "Oh, {w=0.5} it’s you.{w=1} My guardian angel."

    yN "Well, {w=0.5} tree angel I guess."

    T "Why hello!{w=1} So cheery today."

    yN "I’m such an idiot."

    menu:
        "Don’t say stuff like that to yourself!":
            $ p += 1
            yN "Oh, {w=0.5} alright, {w=0.5} alright.{w=1} {cps=15}Anyways...{/cps}"
            yN "I woke up late this morning, {w=0.3} right?{w=1} {cps=45}So I left home in a hurry!{/cps}{w=1} {cps=10}But...{/cps}"

        "Why? What happened?":
            yN "I woke up late this morning, {w=0.3} right?{w=1} {cps=45}So I left home in a hurry!{/cps}{w=1} {cps=10}But...{/cps}"

    yN "{cps=60}I accidentally left my wallet at home!{/cps}{w=1} I basically starved for an hour."

    yN "Ezra chose to share his lunch with me though.{w=1} I’m very grateful."

    menu:
        "Wow. So Ezra’s a good friend,huh?":
            yN "{cps=60}Exactly!{/cps}{w=1.5} {cps=45}He’s a bit annoying at times.{w=1}Like he says some stuff that downright pisses me off{/cps}."

        "Aw, how kind of him!":
            yN "{cps=60}Exactly!{/cps}{w=1.5} {cps=45}He’s a bit annoying at times.{w=1}Like he says some stuff that downright pisses me off{/cps}."

    yN "But, {w=0.3} I {i}literally{/i} can’t live without him.{w=1} I mean, {w=0.5} I could’ve starved to death today{w=0.1} if it weren’t for him."

    yN "Not literally, {w=0.5} duh, {w=0.5} but he really does come in clutch, {w=0.5} saving my clumsy ass, {w=0.5} haha."

    yN "He means a lot to me, {w=0.5} Sap."

    # [Time Skip, Noah looks older)

# SCENE 2:
    # CUTSCENE: Neutral Human
    scene bg light

    show N happy at even_more_lowered
    with fade

    N "Hey, {w=0.5} Sap"

    T "Yeah?"

    N "Today in biology we were learning about plants, {w=0.5} and it was really cool."

    N "You know, {w=0.5} there’s this really cool fungi thing called haustorium?{w=1} Haustorium for multiple."

    N "They’re so cool, {w=0.5} they use their roots to draw nutrition from not the soil, {w=0.5} but other plants."

    N "Kinda neat, {w=0.5} yeah?{w=1} That’s kinda super cool, {w=0.5} right?"

    menu:
        "...":
            N "Huh, {w=0.5} I thought you would be a bit more interested in learning about plants, {w=0.5} because {cps=15}you {i}are{/i} one{/cps}."

    N "But {cps=5}anywaysss{/cps}, {w=0.5} do you remember a while back I told you{w=0.3} {cps=25}that Ezra meant a lot to me?{/cps}"

    T "{cps=20}I mean{/cps}{cps=5}...{/cps} It's kind of obvious."

    T "He’s literally {i}all{/i} that you talk about."

    T "{cps=20}Do you{/cps}{cps=5}...{/cps} like him?"

    N "Yeah, {w=0.5} as a friend.{w=1} I mean, {w=0.5} he’s always been there for me."

    N "If anything, {w=0.5} {cps=25}he’s the only constant that keeps me grounded{w=0.2} in the chaos of school and home.{/cps}"

    N "{cps=25}Like how he let me stay over with him{w=0.3} {size=-3}that night Mom and Dad got into a huge fight over something stupid.{/size}{/cps}"

    N "Why do people fight over dumb things?{w=1} Why can’t they just talk about it?"

    N "Like, {w=0.5} if you let a rotten branch fester, {w=0.5} it’ll kill the whole plant, {w=0.3} you know?"

    #Noah talking about his dark past for christs sake
    show N sad at even_more_lowered

    N """Or, {w=0.5} remember that time when Dad hit me?{w=1}
    Well, {w=0.5} the most recent time that Dad hit me, {w=0.5} over stupid fucking grades?"""

    N "{cps=25}It was Ezra who patched me up.{/cps}"

    N "Both the bruised lip and cut cheek, {w=0.5} but also from that mental shitshow I was going through."

    N "{cps=25}He means the world to me.{/cps}"

    N "I know him probably more than I know myself, {w=0.5} and he, {w=0.5} I."

    stop music fadeout 5.0

    show N default at even_more_lowered

    N "But something’s wrong, {w=0.5} you know?"

    play music reveal volume 0.4 fadein 5.0

    N "Like he feels {cps=25}so much more absent from my life compared to before.{/cps}"

    N "{cps=30}He doesn’t pick up my phone calls all the time anymore.{/cps}"

    N "{cps=30}He doesn’t let me hide out at his place after a fight with my parents.{/cps}"

    N "{cps=20}He{/cps} {cps=10}just...{/cps}"

    N "It feels like he doesn’t care."

    menu:
        "I’m sure he does, Noah.":
            $ p += 1
            N "Right?"
            N "But something just feels, {w=0.5} {i}wrong{/i}."
            N "I don’t know."
            N "I’ll ask him what’s wrong, {w=0.5} okay? And I’ll help fix him, {w=0.5}like he fixed me."
            N "Thanks, {w=0.5} Sap.{w=1} I’ll see you soon."
            stop music fadeout 5.0

        "I mean, {w=0.5}his past actions show that he clearly does.":
            stop music fadeout 2.0
            N "But people {i}change{/i}, {w=0.5} right?"
            play music angry volume 0.8 fadein 3.0
            N "Isn’t that what they’re supposed to do?{w=1} {sc=1}{i}{size=+3}Grow{/size}{/i}{/sc}?"
            N "{size=+3}{cps=25}Or what, {w=0.5} are you saying we’re{/cps} {size=+1}{cps=10}forever stagnant?{/cps}{/size}{/size}"
            N """{sc=0.25}{size=+3}That we’re forever{/size} {size=+4}tied down by our \n
            upbringing and stupid genetics?{/size}{/sc}"""
            N """{cps=25}{sc=0.5}{size=+5}Are you saying that I’m going to end up \n
            like my dirtbag fucking parents?{/size}{/sc}{/cps}"""
            T "{cps=15}Noah, {w=0.5} you know that’s not what I mean.{/cps}"
            N "{size=+2}You sure?{/size}{w=1} {size=+4}{cps=25}Because it sure as hell sounded like you did.{/cps}{/size}"
            N "Whatever, {w=0.5} I don’t want to talk to you anymore."
            N "{cps=30}I’m going to go talk to Ez, {/cps}{w=0.5} {cps=20}{size=+1}because he always got me a little better than you did.{/size}{/cps}"
            stop music fadeout 2.0

#SCENE 3:
    #CUTSCENE: N " appears, looking  at the ground, visibly upset, edges of the screen are dark, black vines are curled around N "’s arms and legs

    scene bg medium

    show N lookdown at even_more_lowered
    with fade

    play music think volume 0.8 fadein 5.0

    T "Noah?"

    #CUTSCENE: Noah looks up

    show N sad at even_more_lowered

    N "Hey."

    "{cps=2}...{/cps}"

    T "So?"

    N "So what?"

    T "So, {w=0.5} how are you?"

    "{cps=2}...{/cps}"

    N "Never better.{w=1} {cps=20}My best friend is only being an {size=+2}annoying, {w=0.5} stupid{w=0.5} piece of garbage{/size}{/cps}."

    N "{sc=0.5}*sighs angrily*{fast}{/sc}"

    N "Like, {w=0.5} when I tried to be civil and ask him if something was wrong, {w=0.5} he was like, {w=0.5} \"I’m fine.\""

    N "And then next thing you know, {w=0.5} he’s canceling plans last minute.{w=1} Like, {w=0.5} {cps=20}{size=+1}does he not care how I feel?{/size}{/cps}"

    N "{size=+1}{cps=50}If he didn’t give a flying {i}fuck{/i} about me, {w=0.5} why should I care about him?{/cps}{/size}"

    N "{size=+1}{cps=25}Why would I try to be friends with someone who obviously doesn’t care about me?{/cps}{/size}"

    N "In all honesty, {w=0.5} it kind of feels like he’s avoiding me."

    #SCENE: Angry Human

    show N annoyed at even_more_lowered

    N "{cps=2}...{/cps}"

    N "Ugh, {w=0.5} anyways I kind of lost it and gave him a piece of my mind today, {w=0.5}
    asking him why he wouldn’t just tell me what’s wrong.{w=0.5}"

    N "You should have {i}seen{/i} his face."

    N "{size=+1}He looked {i}mad{/i}.{/size}"

    show N angry at even_more_lowered

    N "{sc=1}{cps=60}{size=+1}What{w=0.3} right{w=0.3} does{w=0.3} he{w=0.3} have{w=0.3} to get{w=0.3} upset{w=0.3} with{w=0.3} me?{/size}{/cps}{/sc}"

    N "And you know what he said?"

    N "He said part of it was my fault.{w=1} And when I asked him why, {w=0.5} do you know the nonsense he spewed?"

    N "He said it was because he always put me first, {w=0.5} that he'd neglected his own needs."

    N "Sap, {w=0.5} he’s wrong, {w=0.5} right?{w=1} Isn’t he being kind of unreasonable?"

    menu:
        "Perhaps a little, but he’s probably hurting, too.":
                $ p += 1
                show N annoyed at even_more_lowered
                N "Okay, {w=0.5} but he never {i}tells{/i} me anything.{w=1} He just, {w=0.5} you know-{w=0.3}{nw}"
                N "Like, {w=0.5} why didn’t he say something sooner?{w=1} Why did he bottle it up just for it to explode in our faces now?"
                "{cps=2}...{/cps}"
                #SCENE: Sad Human
                show N sad at even_more_lowered
                N """He’s going through it.{w=0.6} I know that.{w=0.6} But he never talks about it{w=0.3}
                and sometimes I just get so {i}angry{/i} because why can’t he just{w=0.8}{nw}"""
                N "Why can’t he just {i}talk{/i} to me about it?{w=1} That’s what friend are {i}for{/i}, {w=0.5} right?"
                N "God, {w=0.5} he’s so dumb."

                menu:
                    "Well, maybe try and apologize? Or try to talk to him more? It’s better than doing... nothing, right?": #(-1)
                        stop music fadeout 2.0
                        N "No.{fast}"
                        T "Noah?"
                        play music angry volume 1.0 fadein 2.0
                        N "Why should I be the one apologizing?\n{w=1} {i}He’s{/i} at fault, {w=0.3}anyways."
                        T "That wasn’t what I was trying to{w=0.4}{nw}"
                        N "I don’t {sc=1}care{/sc} what he’s going through.{w=1} The {sc=1}hell{/sc} I’m going through is {sc=1}so much worse{/sc}."
                        N "And if he can’t see that, {w=0.5} he doesn’t deserve an apology from me."
                        #SCENE: Angry Human
                        show N angry at even_more_lowered
                        N "{cps=20}{size=+2}He{w=0.3} doesn’t{w=0.3} deserve{w=0.3} {i}anything{/i}{w=0.3} from me.{/size}{/cps}{w=1}{nw}"
                        N "{size=+4}I{w=0.3} {sc=3}{i}HATE{/i}{/sc}{w=0.3} him.{/size}{w=1}{nw}"
                        "{cps=2}...{/cps}{w=0.3}{nw}"
                        show N root at even_more_lowered
                        N "And you know what, {w=0.3} Sap, {w=0.5} I hate everything.{w=1}{nw}"
                        N "{size=+2}{cps=10}Ezra, {w=1} you, {w=1} life.{w=1}{/cps}{/size}{nw}"
                        N "I hate it all."
                        stop music fadeout 2.0
                        #CUTSCENE: Branches crowd screen more, everything darkens abruptly.

                    "Give him space, Noah. You’ve always needed it, so why not try and understand him and give him the same courtesy?": #(+0)
                        stop music fadeout 2.0
                        play music angry volume 1.0 fadein 2.0
                        $ p -= 1
                        N "Ha.{w=1} You’re right."
                        N "If anything, {w=0.5}he should apologize to me {i}first{/i}."
                        N "Why should I go out of my way to help him, {w=0.5}if he’s never done anything for me to begin with."
                        T "Noah, {w=0.5}you know that’s not{w=0.6}{nw}"
                        N "No, {w=0.5}he’s in the wrong.{w=1}{nw}"
                        N "{size=+2}He’s always been in the wrong.{/size}{w=1}{nw}"
                        N "{size=+4}I{w=0.3} {sc=3}{i}HATE{/i}{/sc}{w=0.3} him.{/size}{w=1}{nw}"
                        "{cps=2}...{/cps}{w=0.3}{nw}"
                        show N root at even_more_lowered
                        N "And you know what, {w=0.3} Sap, {w=0.5} I hate everything.{w=1}{nw}"
                        N "{size=+2}{cps=10}Ezra, {w=1} you, {w=1} life.{w=1}{/cps}{/size}{nw}"
                        N "I hate it all."
                        stop music fadeout 2.0
                        #CUTSCENE: Branches crowd screen more, everything darkens abruptly.

        "No, he’s not. He’s done so much for you, and yet you didn’t notice anything wrong until now?":
            stop music fadeout 2.0
            play music angry volume 1.0 fadein 2.0
            $ p -= 1
            #CUTSCENE: Edges of screen darken
            show N angry at even_more_lowered
            N "Wow, {w=0.5} Sap, {w=0.5} even {i}you’re{/i} not on my side?"
            N "God, {w=0.5} first I lost my best friend{w=0.5} and now I’m going to lose you too?"
            menu:
                "That’s not what I mean.":
                    N "No.{w=1} You shut up.{w=1} You{w=0.3} don’t{w=0.3} {i}get{/i}{w=0.3} to{w=0.3} talk{w=0.3} to{w=0.3} me.{w=1}{nw}"
                "Noah, you’re making assumptions":
                    N "No.{w=1} You shut up.{w=1} You{w=0.3} don’t{w=0.3} {i}get{/i}{w=0.3} to{w=0.3} talk{w=0.3} to{w=0.3} me.{w=1}{nw}"
            N "{cps=25}You’re just a figment of {i}my{/i} dream.{w=1} You’re supposed to \n{sc=1}{i}always{/i} be on {sc=1}{i}MY{/i}{/sc} side{/sc}.{/cps}"
            N "{cps=20}It’s people like {i}you{/i} and {i}Ezra{/i} that are the problem.{/cps}{w=1}{nw}"
            stop music fadeout 2.0
            "{cps=2}...{/cps}{w=1}{nw}"
            # SCENE: Confused N "
            show N sadder at even_more_lowered
            N "{cps=20}{size=-2}Or{/size}, {size=-1}{w=0.5}am {i}I{/i} the problem?{/size}{/cps}"
            T "{size=-2}{cps=15}Noah...{/cps}{/size}"
            N "{cps=15}I{w=0.5} {i}am{/i}{w=0.5} the{w=0.5} problem.{/cps}{w=1}{nw}"

            menu:
                "That’s not true":
                    play music angry volume 1.2 fadein 2.0
                    show N angry at even_more_lowered
                    $ p += 1
                    N "{size=+2}{cps=20}Not you being a {i}fucking{/i} liar too.{/cps}{/size}{w=1}{nw}"
                    N "{size=+2}{cps=20}I see it on your stupid, {w=0.5} pitying face.{w=1} You hate me too.{/cps}{/size}{w=1.4}{nw}"
                    N "{size=+2}{cps=20}But you know what?{/cps}{/size}{w=1.4}{nw}"
                    N "{size=+2}{cps=20}I hate you too.{/cps}{/size}{w=1.4}{nw}"
                    show N root at even_more_lowered
                    N "And you know what, {w=0.3} Sap, {w=0.5} I hate everything.{w=1}{nw}"
                    N "{size=+2}{cps=10}Ezra, {w=1} you, {w=1} life.{w=1}{/cps}{/size}{nw}"
                    N "I hate it all."
                    stop music fadeout 2.0
                    #CUTSCENE: Branches crowd screen more, everything darkens abruptly.

                "Noah, stop. You’re jumping to conclusions.":
                    play music sad fadein 2.0
                    show N sad at even_more_lowered
                    N "{size=+2}No, {w=0.5} I’m not.{w=2}{nw}{/size}"
                    N "{cps=20}It’s true, {w=0.5} right?{w=1.4}{nw}{/cps}"
                    N "{cps=20}He’s not going through tough things in life, {w=1} he’s going through {i}me{/i}.{w=2}{nw}{/cps}"
                    N "{i}I{/i} am the problem in his life.{w=2}{nw}"
                    T "Noah, {w=0.5}stop–{w=1}{nw}"
                    N "I know you’re thinking it.{w=2}{nw}"
                    T "Noah–{w=0.6}{nw}"
                    N "You think I’m better off dead.{w=1.4}{nw}"
                    N "Of course you do.{w=2}{nw}"
                    #SCENE Sad Human
                    show N sadder at even_more_lowered
                    N "{size=-2}{cps=20}Of course you do{/cps}{cps=2}...{/cps}{/size}"
                    stop music fadeout 2.0
                    #CUTSCENE: Branches crowd screen more, everything darkens abruptly.

#SCENE 4:
    #SCENE: Noah looks defeated (or just sad)
    scene bg medium

    show N root_sadder at even_more_lowered
    with fade

    play music sad volume 0.6 fadein 2.0

    "{cps=2}...{/cps}"

    T "Noah?{w=1}{nw}"

    "{cps=2}...{/cps}"

    T "Noah?{w=1}{nw}"

    "{cps=2}...{/cps}"

    T "{cps=5}N–{w=0.6}{nw}{/cps}"

    N "{size=-2}{cps=10}He doesn’t{/cps}{cps=2}...{/cps}{w=1}{/size} {size=-2}{cps=10}He wouldn’t{/cps}{/size}{cps=2}...{/cps}{w=2}{nw}"

    N "{cps=15}He wouldn’t even talk to me.{w=1} I saw the look on his face{/cps}{cps=2}...{/cps} {cps=15}He wouldn’t even look me in the eyes{/cps}{cps=2}...{/cps}{w=2}{nw}"

    menu:
        "Oh, Noah...":
            stop music
            play music angry volume 1.2 fadein 1.0
            #SCENE Angry Noah
            show N root_annoyed at even_more_lowered
            N "Just{w=0.8} {size=+4}{i}STOP{/i}{/size}."
            N "{size=+4}Stop with the pity.{/size}{w=2}{nw}"
            N "{size=+2}Stop, {w=0.5}please.{w=2}{nw}{/size}"
            N "{sc=1}I don’t want your comfort.{w=1} I don’t want your anything.{w=2}{nw}{/sc}{w=2}{nw}"
            N "{sc=2}{cps=45}{size=+4}I lost him!{w=1} I have nothing except for him!{/size}{/cps}{/sc}{w=2}{nw}"
            N "{sc=1}{size=+1}No friends.{w=1} No home.{w=1} No family.{w=1} No nothing.{w=1}{/size}{/sc} \n{sc=2}Ezra was my {i}everything{/i}{/sc}.{w=2}{nw}"
            show N root_angry at even_more_lowered
            N "{sc=0.5}{size=+2}{i}Weren’t you supposed to be my \"guardian angel\"?{w=1}\n
            Weren’t you supposed to protect me from \nall this happening?{/i}{/size}{/sc}{w=2}{nw}"
            #SCENE Sad N " (hopeless)
            show N root_sadder at even_more_lowered
            N "{sc=0.25}{size=-1}Weren’t you supposed to make me better?{/size}{/sc}{w=2}{nw}"
            N "{cps=2}...{/cps}"
            T "{cps=10}Noah–{w=0.6}{nw}{/cps}"
            #SCENE Angry Human
            show N root_angry at even_more_lowered
            N "{size=+2}So tell me, {w=0.5}{/size} {sc=0.5}{size=+2}why the {i}fuck{/i} are things \nthe way they are?{/size}{/sc}{w=2}{nw}"
            N "{sc=0.5}{size=+2}Why can’t you do anything right?{/size}{/sc}{w=3}{nw}"
            N "{sc=2}{size=+5}{cps=20}YOU WERE SUPPOSED TO {i}FIX{/i} ME.{/cps}{/size}{/sc}{w=2}{nw}"
            N "{sc=2}{size=+5}{cps=20}THIS IS {i}YOUR{/i} FAULT.{/cps}{/size}{/sc}{w=2}{nw}"
            N "{sc=0.25}{size=+2}This is all {i}your{/i} fault.{/size}{/sc}{w=2}{nw}"
            N "{size=+2}You’re useless.{w=1} You’re worse than useless.{/size}{w=2}{nw}"
            N "{sc=0.5}{cps=20}If I didn’t listen to you{/cps}{cps=1}...{/cps}{/sc}{w=2}{nw}"
            N "{sc}{size=-2}{cps=20}If only I didn’t try like you told me to{/cps}{cps=1}...{/cps}{/size}{/sc}{w=2}{nw}"
            N "Then none of this would have happened.{w=2}{nw}"
            N "I wish I had never met you.{w=2}{nw}"
            N "So leave."
            T "{cps=20}Noah-{w=1}{nw}{/cps}"
            N "Leave.{w=1}{nw}"
            N "{sc=0.5}Please.{/sc}{w=1}{nw}"
            #SCENE Noah has his back turned to you
            show N back at even_more_lowered

        "Why are you so upset?":
            $ p -= 1
            show N root_annoyed at even_more_lowered
            T "Maybe he just needs more space and time, {w=0.5}Noah."
            T "Isn’t that what they say?"
            T "{cps=10}Time–{nw}{/cps}"
            #SCENE Angry N "
            show N root_angry at even_more_lowered
            stop music
            play music angry volume 1.2 fadein 1.0
            N "{sc=1}{size=+4}{i}Time heals all wounds?{/i}{/size}{/sc}{w=2}{nw}"
            N "{size=+2}I’m sick of your nonsense.{/size}{w=2}{nw}"
            N "{size=+2}And did you say I’m {i}upset{/i}?{/size}{w=2}{nw}"
            N "{size=+2}That doesn’t even {i}begin{/i} to capture how I feel.{/size}{w=2}{nw}"
            N "{size=+2}How I feel, {w=0.5}because of {i}you{/i}.{/size}{w=2}{nw}"
            N """{sc=0.5}{size=+2}I’m fucking done.{w=1} I’m going to fuck up everything anyways,
            {w=0.5}so why even try and salvage this?{/size}{/sc}{w=2}{nw}"""
            N "{sc=0.5}{size=+2}Why even try and fix a lost cause, {w=0.5}when this is all that I am?{/size}{/sc}{w=2}{nw}"
            N "{sc=0.5}{size=+2}And all that I will be?{/size}{/sc}{w=2}{nw}"
            N "{size=+2}So fuck you.{/size}{w=2}{nw}"
            show n root at even_more_lowered
            N "{size=+2}I give up.{/size}{w=2}{nw}"
            N "{size=+2}And you should have given up on me, {w=0.5}too.{w=1}\n
            A long, {w=0.5}long time ago.{/size}"
            #SCENE N " has his back turned on you
            show N back at even_more_lowered

        "(Hug)": #click on Character
            stop music fadeout 2.0
            play music reveal volume 0.6 fadein 5.0
            $ p += 1
            #SCENE Tree spirit hugs Noah
            show N root_sadder at even_more_lowered
            N "*sobbing*{fast}"
            T "Everything is going to be alright."
            N " {cps=45}{size=+4}No it’s not! {w=1} I hurt him! {w=1} I WANTED to hurt him!{/size}{/cps}"
            T "Maybe you’re right.{w=1} Maybe Ezra will hate you for the rest of your life."
            T """The pain you feel might overwhelm you.{w=1} It consumes a part of you.
            Perhaps, {w=0.5}Ezra was a part of you that ripped away."""
            N "{cps=2}...{/cps}"
            T "But what’s important to you? {w=1} Is Ezra really THAT important to you?"
            N "{cps=2}...{/cps}"
            T """Be courageous, {w=0.5}my little hero.{w=1} Find the part of you that
            bravely faces rejection and scorn.{w=1} Find the part of you that seeks love."""
            "{cps=2}...{/cps}"
            N "{size=-2}{cps=2}...{/cps} and then?{/size}"
            T "Simple.{w=1} Go and apologize."
            stop music fadeout 5.0

#SCENE 5:
    #CUTSCENE: Neutral N ", colorless dreamspace
    scene bg neutral

    show N root at even_more_lowered
    with fade

    play music think volume 0.8 fadein 20

    N "Sap."

    N "Sap, {w=0.5}do you want to know something funny?"

    menu:
        "Yea?":
            N "Remember a long, {w=0.5}long time ago when I first told you about Ezra?"

    N "And the lunch he shared with me?"

    menu:
        "Mhm.":
            N "Do you remember what else I said?"

    menu:
        "{cps=2}...{/cps}":
            N "I said, {w=0.5}“I can’t live without him."

    N "{cps=20}And you know, {w=0.5}now that I’m living it, {w=0.5}that statement is still true.{/cps}{w=2}{nw}"

    N "{cps=20}It’s so dark.{w=1} It feels so meaningless.{w=1} It’s so empty.{/cps}{w=2}{nw}"

    N "{cps=20}He was my light, {w=0.5}Sap.{w=1} My {i}sun{/i}.{/cps}{w=2}{nw}"

    N "{cps=20}And just like how you need the sun’s warmth to grow, {w=0.5} I needed his warmth to find any value in this{/cps}{cps=2}...{/cps}{w=2}{nw}"

    N "{cps=20}To find any value in this shitty, {w=0.5} awful life.{/cps}{w=2}{nw}"

    N "{cps=20}I lost him, {w=0.5} Sap.{/cps}{w=2}{nw}"

    N "{cps=20}He left me.{w=1} He {i}abandoned{/i} me.{/cps}{w=2}{nw}"

    N "{cps=20}He hates me.{w=1} {i}Life{/i} hates me.{/cps}{w=2}{nw}"

    N "{cps=20}{sc=0.5}{size=-1}It’s not fair{/size}.{/sc}{/cps}{w=2}{nw}"

    N "{sc=0.5}{cps=20}{i}None{/i} of this is fair.{/cps}{/sc}{w=2}{nw}"

    N "{cps=20}So I give up, {w=0.5}okay?{/cps}"

    N "I.{w=1} Give.{w=1} Up."
    stop music fadeout 2.0
    #CUTSCENE: Human disappears

#SCENE 6:
    #CUTSCENE: Empty dream space, colorless
    scene bg neutral
    with fade

    menu:
        "Noah?":
            "{cps=2}......{/cps}" #there must be some code following the menu choice
        "(Where is he...?)":
            "{cps=2}......{/cps}" #so I put these here as placeholder

    #SCENE: Roots are everywhere.
    #CUTSCENE: Can see Sap’s hands, they’re covered in black vines and roots.
    #(something that maybe alludes to N " dying)
    #SCENE fades to black
    with fade
    if p <= 1:
        jump bad

    elif p > 2:
        jump good

    else:
        jump meh

    with fade

#BAD END: (< 3 points)
    #CUTSCENE: Dream space almost pitch black, N "’s there, roots all over his form, back facing camera
label bad:
    scene bg dark

    show N consumed at even_more_lowered
    with fade

    play music angry volume 1.0 fadein 2.0

    T "Noah?"

    "{cps=2}...{/cps}"

    T "Noah, {w=0.5}please."

    "{cps=2}...{/cps}"

    T "Noah{nw}"

    N "I’m not sorry."

    T "Noah?"

    N "{cps=2}...{/cps}{w=1}{nw}"

    N "{cps=20}Wanna know something ironic, {w=0.5} though?{/cps}"

    N "{cps=20}Remember a long time ago I told you about haustoria?{w=1} Those parasitic plants?{/cps}{w=2}{nw}"

    N "{cps=20}Maybe that’s what everything was.{/cps}{w=2}{nw}"

    N "{cps=20}I’m the plant, {w=0.5} trying my best to live in this shitty world and all the bad was just the roots strangling me and wringing me dry.{/cps}{w=2}{nw}"

    N "{cps=20}Maybe that’s why I found them so fascinating.{/cps}{w=2}{nw}"

    N "{cps=20}Because they’re a reflection of this life of mine.{/cps}{w=2}{nw}"

    N "{cps=2}...{/cps}{w=1}{nw}"

    N "{cps=20}This shitty, unfair, ruined world.{w=1} And to that, you know what I’ll say?{/cps}{w=2}{nw}"

    N "{cps=20}Good riddance{/cps}{w=2}{nw}"

    N "{cps=20}Because these dumb roots may have won against me, {w=0.5} but in my own defeat I will drag it down with me, {w=0.5} too.{/cps}"

    stop music fadeout 2.0

    #scene be with fade
    #CUTSCENE: Dead tree, smashed photo with word “end.” on top

    return

#MEH END:
    #CUTSCENE Dreamspace almost pitch black, but N " can be scene with his form completely overtaken by the dark roots
label meh:
    scene bg dark

    show N consumed at even_more_lowered
    with fade

    play music sad volume 1.0 fadein 2.0

    T "Noah!"

    N "{cps=2}...{/cps}"

    T "Noah?"

    N "Sap."

    "{cps=2}...{/cps}"

    N "{cps=20}Sap I’m sorry.{/cps}"

    T "Sorry about what?"

    N "{cps=10}For{/cps}{cps=5}...{/cps} this.{w=2}{nw}"

    N "{cps=20}I just got angry.{w=1} And I couldn’t take it anymore.{/cps}{w=2}{nw}"

    N "{cps=20}I tried my best but I can’t escape it.{/cps}{w=2}{nw}"

    T "{cps=20}Escape what?{/cps}{w=2}{nw}"

    N "{cps=20}I can’t escape my past.{/cps}{w=2}{nw}"

    N "{cps=20}Just like how you’re just a stupid tree rooted in a pot of rotting soil, {w=0.5}I’m a stupid human rooted down by my–{/cps}{w=2}{nw}"

    N "{cps=20}By my–{nw}{/cps}{w=2}{nw}"

    #SCENE Confused Human

    N "{cps=20}What was so wrong about my life?{w=2}{nw}{/cps}"

    N """{sc=0.5}{cps=20}Was it my awful parents and a home that didn’t quite ever feel like it? \n
    Or was it me and these emotions that ran too deep that eventually \n
    I absorbed and drowned in all the poison around me?{/cps}{w=2}{nw}{/sc}"""

    N "{cps=20}What was I tied down by?{/cps}"

    menu:
        "Nothing, Noah. {i}Nothing{/i}":
            T "We’re not the same Noah."

    menu:
        "Why didn’t you try harder? Why did you give up?":
            N "{cps=20}Because {i}nobody{/i} cared.{w=1} I was trying so hard and for {i}what{/i}?{/cps}{w=2}{nw}"
            N "{cps=20}Tell me, {w=0.5}Sap.{/cps}{w=2}{nw}"
            N "{cps=20}{i}What did I live for?{/i}{/cps}{w=2}{nw}"
            N "{cps=20}For the sake of surviving?{/cps}{w=2}{nw}"
            N "{cps=20}That’s not living, {w=0.5}Sap.{/cps}{w=2}{nw}"
            N "{cps=20}That’s hell.{/cps}{w=2}{nw}"
            N "{cps=20}At least I’ll  be free of it now.{w=1} Even if I have to put everyone around me through it.{/cps}{w=2}{nw}"
            N "{cps=20}And, {w=0.5}hey, {w=0.5}at least Ez will be free of the burden of me.{w=1} It was for the best, {w=0.5}anyways.{/cps}"
            stop music fadeout 2.0

        "But it’ll be okay.":
            N "Right.{w=1}{nw}"
            N "{cps=20}It’ll be okay.{w=1} It’s always been like that.{/cps}{w=2}{nw}"
            N "{cps=20}And Ez will be okay, {w=0.5}too.{w=1} He’ll be better, {w=0.5}right, {w=0.5}Sap?{/cps}{w=2}{nw}"
            N "{cps=20}Can you visit him, {w=0.5}too? Can you see how he’s doing? Is he doing okay?{/cps}{w=2}{nw}"
            N "{cps=20}I mean, {w=0.5}I’m no longer weighing him down with my needless emotions and burdens and traumas.{/cps}{w=2}{nw}"
            N "{cps=20}Ez no longer has to be Atlas, {w=0.5}holding up the weight of my world, {w=0.5}right?{/cps}"
            T "Ez is doing –"
            N "{cps=20}Wait, {w=0.5}don’t finish that sentence.{/cps}{w=2}{nw}"
            N "{cps=20}I don’t want to know.{/cps}{w=2}{nw}"
            N "{cps=10}It doesn’t...{/cps} make a difference to me anymore.{w=2}{nw}"
            N "{cps=20}But I hope he’s happy.{w=1} That’s all I have ever wanted.{/cps}{w=2}{nw}"
            N "{cps=20}Because that’s all I need so that things can be okay.{/cps}{w=2}{nw}"
            N "{cps=20}And things are, {w=0.5} or at least will be, {w=0.5} okay.{/cps}"
            stop music fadeout 2.0
    return

#GOOD END:
label good:
    play music finale fadein 5.0
    scene bg light
    show N sad at even_more_lowered
    with fade

    N "Sap."

    T "Noah!"

    N "{size=-1}Sap,{w=0.5} I miss him.{/size}{w=2}{nw}"

    N "{size=-2}I miss Ezra.{/size}{w=2}{nw}"

    #SCENE: Crying Human
    show N sadder at even_more_lowered

    N "{cps=20}I–{/cps}{w=2}{nw}"

    N "{cps=20}God, {w=0.5}I hate this.{/cps}{w=2}{nw}"

    N "{cps=20}Why, {w=0.5}Sap, {w=0.5}{i}why{/i}?{/cps}"

    T "{cps=20}Why what?{/cps}"

    N "{cps=20}I might not have been able to stand a life without Ezrea in it, {w=0.5} but he was still there, {w=0.5} you know?{/cps}"

    N "{cps=20}Even if he wouldn’t have been in my life, {w=0.5} he was still looking at the same sky, {w=0.5} breathing the same air.{/cps}"

    N "{cps=20}Why did I give that up?{/cps}"

    N "{cps=20}I’m not stupid, {w=0.5}am I?{/cps}"

    T "{cps=20}No, {w=0.5}you’re not.{/cps}"

    N "{cps=20}{size=-2}I just wanted to show that{/size}{/cps}{cps=2}...{/cps}"

    N "{cps=20}I just wanted to show Ezra he meant to much to me{w=0.5} and that I cared so much about him that I was willing to {sc}{i}die{/i}{/sc} for him.{/cps}"

    N "{cps=20}Because in those breaths without him, {w=0.5} it felt like there was no tomorrow.{w=1} It felt like the end.{/cps}"

    N "{cps=20}But, {w=0.5}I didn’t get to say goodbye.{w=1} Why did I have to end things like this?{/cps}"

    N "{cps=20}And why, {w=0.5}Sap, {w=0.5}was it so lonely?{w=1} Why, {w=0.5}in my last moments, {w=0.5}did I have to be alone?{/cps}"

    N "{cps=20}Tell him I’m sorry.{/cps}"

    N "{cps=20}And to you too, {w=0.5}Sap.{w=1} I’m sorry.{/cps}"

    stop music fadeout 2.0

    return
