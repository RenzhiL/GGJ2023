# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define N = Character("Noah")
define T = Character("Sap")
define yN = Character("young Noah")

$ p = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # These display lines of dialogue.

    T "That’s me.{w=1} Or, {w=0.5}I guess, {w=0.5}this is me."

    T "Hi!"

    T "My human’s the guy in the photo there."

    T "His name is Noah."

    # SCENE: Zoom into photo, spirits hand touches it

    T "Isn’t he precious?"

    T "Well, {w=0.5}it’s my job to take care of Mr.Noah!"

    # SCENE: spirit looks a little sad in the mirror

    T "Noah’s always been struggling{cps=10}...{/cps} His family has been{cps=2}...{/cps} {cps=10}tough,{/cps}{w=1} to say the least."

    T "I wish I could talk to him outside of his dreams{w=0.3} which don’t even happen too often {cps=10}but...{/cps}"

    T "At least I can visit him in his dreams."

    T "At least I can do a little something,{w=0.5} despite being rooted down to this{cps=20} stagnant,{w=0.5} silent form{/cps}{cps=10}...{/cps}"

# SCENE 1
    # CUTSCENE: Younger N "
    yN "Oh,{w=0.5} it’s you.{w=1} My guardian angel."

    yN "Well,{w=0.5} tree angel I guess."

    T "Why hello!{w=1} So cheery today."

    yN "I’m such an idiot."

    menu:
        "Don’t say stuff like that to yourself!":
            yN "Oh,{w=0.5} alright,{w=0.5} alright.{w=1} {cps=15}Anyways...{/cps}"
            yN "I woke up late this morning,{w=0.3} right?{w=1} {cps=45}So I left home in a hurry!{/cps}{w=1} {cps=10}But...{/cps}"

        "Why? What happened?":
            yN "I woke up late this morning,{w=0.3} right?{w=1} {cps=45}So I left home in a hurry!{/cps}{w=1} {cps=10}But...{/cps}"

    yN "{cps=60}I accidentally left my wallet at home!{/cps}{w=1} I basically starved for an hour."

    yN "Ezra chose to share his lunch with me though.{w=1} I’m very grateful."

    menu:
        "Wow. So Ezra’s a good friend,huh?":
            yN "{cps=60}Exactly!{/cps}{w=1.5} {cps=45}He’s a bit annoying at times.{w=1}Like he says some stuff that downright pisses me off{/cps}."

        "Aw, how kind of him!":
            yN "{cps=60}Exactly!{/cps}{w=1.5} {cps=45}He’s a bit annoying at times.{w=1}Like he says some stuff that downright pisses me off{/cps}."

    yN "But,{w=0.3} I {b}literally{/b} can’t live without him.{w=1} I mean,{w=0.5} I could’ve starved to death today{w=0.1} if it weren’t for him."

    yN "Not literally,{w=0.5} duh,{w=0.5} but he really does come in clutch,{w=0.5} saving my clumsy ass,{w=0.5} haha."

    yN "He means a lot to me,{w=0.5} Sap."

    # [Time Skip, Noah looks older)

# SCENE 2:
    # CUTSCENE: Neutral Human
    N "Hey,{w=0.5} Sap"

    T "Yeah?"

    N "Today in biology we were learning about plants,{w=0.5} and it was really cool."

    N "You know,{w=0.5} there’s this really cool fungi thing called haustorium?{w=1} Haustorium for multiple."

    N "They’re so cool,{w=0.5} they use their roots to draw nutrition from not the soil,{w=0.5} but other plants."

    N "Kinda neat,{w=0.5} yeah?{w=1} That’s kinda super cool,{w=0.5} right?"

    menu:
        "...":
            N "Huh,{w=0.5} I thought you would be a bit more interested in learning about plants,{w=0.5} because {cps=15}you {b}are{/b} one{/cps}."

    N "But {cps=5}anywaysss{/cps},{w=0.5} do you remember a while back I told you{w=0.3} {cps=25}that Ezra meant a lot to me?{/cps}"

    T "{cps=20}I mean{/cps}{cps=5}...{/cps} It's kind of obvious."

    T "He’s literally {b}all{/b} that you talk about."

    T "{cps=20}Do you{/cps}{cps=5}...{/cps} like him?"

    N "Yeah,{w=0.5} as a friend.{w=1} I mean,{w=0.5} he’s always been there for me."

    N "If anything,{w=0.5} {cps=25}he’s the only constant that keeps me grounded{w=0.2} in the chaos of school and home.{/cps}"

    N "{cps=25}Like how he let me stay over with him{w=0.3} {size=-3}that night Mom and Dad got into a huge fight over something stupid.{/size}{/cps}"

    N "Why do people fight over dumb things?{w=1} Why can’t they just talk about it?"

    N "Like,{w=0.5} if you let a rotten branch fester,{w=0.5} it’ll kill the whole plant,{w=0.3} you know?"

    N """Or,{w=0.5} remember that time when Dad hit me?{w=1}
    Well,{w=0.5} the most recent time that Dad hit me,{w=0.5} over stupid fucking grades?"""

    N "{cps=25}It was Ezra who patched me up.{/cps}"

    N "Both the bruised lip and cut cheek,{w=0.5} but also from that mental shitshow I was going through."

    N "{cps=25}He means the world to me.{/cps}"

    N "I know him probably more than I know myself,{w=0.5} and he,{w=0.5} I."

    N "But something’s wrong,{w=0.5} you know?{w=1} Like he feels {cps=25}so much more absent from my life compared to before.{/cps}"

    N "{cps=30}He doesn’t pick up my phone calls all the time anymore.{/cps}"

    N "{cps=30}He doesn’t let me hide out at his place after a fight with my parents.{/cps}"

    N "{cps=20}He{/cps} {cps=10}just...{/cps}"

    N "It feels like he doesn’t care."

    menu:
        "I’m sure he does, Noah.":
            N "Right?"
            N "But something just feels,{w=0.5} {b}wrong{/b}."
            N "I don’t know."
            N "I’ll ask him what’s wrong,{w=0.5} okay? And I’ll help fix him,{w=0.5}like he fixed me."
            N "Thanks,{w=0.5} Sap.{w=1} I’ll see you soon."

        "I mean,{w=0.5}his past actions show that he clearly does.":
            N "But people {b}change{/b},{w=0.5} right?"
            N "Isn’t that what they’re supposed to do?{w=1} {sc=1}{b}{size=+3}Grow{/size}{/b}{/sc}?"
            N "{size=+3}{cps=25}Or what,{w=0.5} are you saying we’re{/cps} {size=+1}{cps=10}forever stagnant?{/cps}{/size}{/size}"
            N """{sc=0.25}{size=+3}That we’re forever{/size} {size=+4}tied down by our \n
            upbringing and stupid genetics?{/size}{/sc}"""
            N """{cps=25}{sc=0.5}{size=+5}Are you saying that I’m going to end up \n
            like my dirtbag fucking parents?{/size}{/sc}{/cps}"""
            T "{cps=15}Noah,{w=0.5} you know that’s not that I mean.{/cps}"
            N "{size=+2}You sure?{/size}{w=1} {size=+4}{cps=25}Because it sure as hell sounded like you did.{/cps}{/size}"
            N "Whatever,{w=0.5} I don’t want to talk to you anymore."
            N "{cps=30}I’m going to go talk to Ez,{/cps}{w=0.5} {cps=20}{size=+1}because he always got me a little better than you did.{/size}{/cps}"

#SCENE 3:
    #CUTSCENE: N " appears, looking  at the ground, visibly upset, edges of the screen are dark, black vines are curled around N "’s arms and legs

    T "Noah?"

    #CUTSCENE: Noah looks up

    N "Hey."

    "{cps=4}...{/cps}"

    T "So?"

    N "So what?"

    T "So,{w=0.5} how are you?"

    "{cps=4}...{/cps}"

    N "Never better.{w=1} {cps=20}I mean my best friend is only being an {size=+2}annoying,{w=0.5} stupid{w=0.5} piece of garbage{/size}{/cps}."

    N "*sighs angrily*{fast}"

    N "Like,{w=0.5} when I tried to be civil and ask him if something was wrong,{w=0.5} he was like,{w=0.5} \"I’m fine.\""

    N "And then next thing you know,{w=0.5} he’s canceling plans last minute.{w=1} Like,{w=0.5} {cps=20}{size=+1}does he not care how I feel?{/size}{/cps}"

    N "{size=+1}If he didn’t give a flying fuck about me,{w=0.5} why should I care about him?{/size}"

    N "{size=+1}{cps=25}Why would I try to be friends with someone who obviously doesn’t care about me?{/cps}{/size}"

    N "In all honesty,{w=0.5} it kind of feels like he’s avoiding me."

    #SCENE: Angry Human

    N "{cps=2}...{/cps}"

    N """Ugh,{w=0.5} anyways I kind of lost it and gave him a piece of my mind today,
    asking him why he wouldn’t just tell me what’s wrong,{w=0.5} and you should have {b}seen{/b} his face."""

    N "He looked {b}mad{/b}."

    N "What {b}right{/b} does {b}he{/b} have to get upset with {b}me{/b}?"

    N "And you know what he said?"

    N "He said part of it was my fault.{w=1} And when I asked him why,{w=0.5} do you know the nonsense he spewed?"

    N "He said it was because he always put me first,{w=0.5} that in turn he neglected his own needs."

    N "Sap,{w=0.5} he’s wrong,{w=0.5} right? Isn’t he being kind of unreasonable?"

    menu:
        "Perhaps  little,{w=0.5} but he’s probably hurting,{w=0.5} too.":
                N "Okay,{w=0.5} but he never {b}tells{/b} me anything.{w=1} He just,{w=0.5} you know{nw}"
                N "Like,{w=0.5} why didn’t he say something sooner?{w=1} Why did he bottle it up just for it to explode in our faces now?"
                N "{cps=2}...{/cps}"
                #SCENE: Sad Human
                N """He’s going through it.{w=1} I {b}know{/b} that.{w=1} But he never talks about it
                and sometimes I just get so {b}angry{/b} because why can’t he just{nw}"""
                N "Why can’t he just {b}talk{/b} to me about it? That’s what friend are {b}for{/b},{w=0.5} right?"
                N "God,{w=0.5}he’s so dumb."

                menu:
                    "Well,{w=0.5}maybe try and apologize? Or try to talk to him more? It’s better than doing... nothing,{w=0.5}right?": #(-1)
                        N "No.{fast}"
                        T "Noah?"
                        N "Why should {b}I{/v} be the one apologizing? He’s at fault,{w=0.5}anyways."
                        T "That wasn’t what I was trying to{nw}"
                        N "I don’t {sc=1}care{/sc} what he’s going through.{w=1} The hell I’m going through is so much worse."
                        N "And if he can’t see that,{w=0.5}he doesn’t deserve an apology from me."
                        #SCENE: Angry Human
                        N "He doesn’t deserve *anything* from me."
                        N "I {sc=3}{b}HATE{/b}{/sc} him."
                        N "{cps=2}...{/cps}"
                        N "And you know what,{w=0.3}Sap,{w=0.5}I hate everything."
                        N "{cps=10}Ezra,{w=1} you,{w=1} life.{w=1}{/cps}"
                        N "I hate it all."
                        #CUTSCENE: Branches crowd screen more, everything darkens abruptly.

                    "Give him space,{w=0.5}Noah.{w=1} You’ve always needed it,{w=0.5}so why not try and understand him and give him the same courtesy?": #(+0)
                        N "Ha.{w=1} You’re right."
                        N "If anything,{w=0.5}he should apologize to me *first.*"
                        N "Why should I go out of my way to help him,{w=0.5}if he’s never done anything for me to begin with."
                        T "Noah,{w=0.5}you know that’s not{nw}"
                        N "No,{w=0.5}he’s in the wrong."
                        N "He’s always been in the wrong."
                        B "I HATE him."
                        N "{cps=2}...{/cps}"
                        N "And you know what,{w=0.5}Sap,{w=0.5}I hate everything."
                        N "{cps=10}Ezra,{w=1} you,{w=1} life.{w=1}{/cps}"
                        N "I hate it all."
                        #CUTSCENE: Branches crowd screen more, everything darkens abruptly.

        "No, he’s not.{w=1} He’s done so much for you, and yet you didn’t notice anything wrong until now?":
            #CUTSCENE: Edges of screen darken
            N "Wow,{w=0.5}Sap,{w=0.5}even *you’re* not on my side?"
            N "God, first I lost my best friend and now I’m going to lose you too?"
            T "That’s not what I mean{nw}"
            T "Noah,{w=0.5}you’re making assumptions{nw}"
            N "No.{w=1} You shut up.{w=1} You don’t {b}get{/b} to talk to me."
            N "You’re just a figment of {b}my{/b} dream.{w=1} You’re supposed to {b}always{/b} be on {sc=1}{b}MY{/b}{/sc} side."
            N "It’s people like {b}you{/b} and {b}Ezra{/b} that are the problem"
            N "{cps=2}...{/cps}"
            # SCENE: Confused N "
            N "Or, {w=0.5}am {b}I{/b} the problem?"
            T "Noah..."
            N "I’m the problem."

            menu:
                "That’s not true": #(+0)
                    N "Not you being a {b}fucking{/b} liar too."
                    N "I see it on your stupid,{w=0.5}pitying face.{w=1} You hate me too."
                    N "But you know what?"
                    N "I hate you too."
                    N "I hate everything."
                    N "Ezra,{w=0.5}you,{w=0.5}life."
                    N "I hate it all."
                    #CUTSCENE: Branches crowd screen more, everything darkens abruptly.

                "Noah, stop.{w=1} You’re jumping to conclusions.": #(-1)
                    N "No,{w=0.5}I’m not."
                    N "It’s true,{w=0.5}right?"
                    N "He’s not going through tough things in life,{w=0.5}he’s going through {b}me{/b}."
                    N "*I’m* the problem in his life."
                    T "Noah,{w=0.5}stop–{nw}"
                    N "I know you’re thinking it."
                    T "Noah–{nw}"
                    N "You think I’m better off dead."
                    N "Of course you do."
                    #SCENE Sad Human
                    N "Of course you do..."
                    #CUTSCENE: Branches crowd screen more, everything darkens abruptly.

#SCENE 4:
    #SCENE: Noah looks defeated (or just sad)

    N "{cps=2}...{/cps}"

    T "Noah?"

    N "{cps=2}...{/cps}"

    T "Noah?"

    N "{cps=2}...{/cps}"

    T "{cps=5}N–{nw}{/cps}"

    N "He doesn’t... He wouldn’t..."

    N "He wouldn’t even talk to me.{w=1} I saw the look on his face... He wouldn’t even look me in the eyes..."

    menu:
        "Oh, Noah...":
            #SCENE Angry Noah
            N "Just {sz+=5}STOP{/sz}."
            N "Stop with the pity.{w=1} Stop,{w=0.5}please."
            N "I don’t want your comfort.{w=1} I don’t want your anything."
            N " +=5}I lost him! I have nothing except for him! }"
            N "No friends.{w=1} No home.{w=1} No family.{w=1} No nothing.{w=1} Ezra was my *everything.*"
            N " And weren’t you supposed to be my 'guardian angel'? Weren’t you supposed to protect me from all this happening?"
            #SCENE Sad N " (hopeless)
            N " -=5}Weren’t you supposed to make me better? }"
            N "{cps=2}...{/cps}"
            T "{cps=10}Noah–{nw}{/cps}"
            #SCENE Angry Human
            N "So tell me,{w=0.5}why the *fuck* are things the way they are?"
            N "Why can’t you do anything right?"
            N "{cps=2}...{/cps}"
            N "{sc=2} +=5}{cps=20}YOU WERE SUPPOSED TO {b}FIX{/b} ME.{/cps} }{/sc}"
            N "{sc=2} +=5}{cps=20}THIS IS {b}YOUR{b} FAULT.{/cps} }{/sc}"
            N "This is {b}all{/b} your fault."
            N "You’re useless.{w=1} You’re worse than useless."
            N " -=5}{cps=20}If I didn’t listen to you... } }"
            N "If only I didn’t try like you told me to..."
            N "Then none of this would have happened."
            N "I wish I had never met you."
            N "So leave."
            T "{cps=20}Noah-{nw}{/cps}"
            N "Leave."
            N "Please."
            #SCENE Noah has his back turned to you

        "Why are you so upset?":
            T "Maybe he just needs more space and time,{w=0.5}Noah."
            T "Isn’t that what they say?"
            T "{cps=10}Time–{nw}{/cps}"
            #SCENE Angry N "
            N "{sc=1}{b}Time heals all wounds?{/b}{/sc}"
            N "I’m sick of your nonsense."
            N "And did you say I’m {b}upset{/b}?"
            N "That doesn’t even {b}begin{/b} to capture how I feel."
            N "How I feel,{w=0.5}because of {b}you{/b}."
            N """{sc=1}I’m fucking done.{w=1} I’m going to fuck up everything anyways,
            {w=0.5}so why even try and salvage this?{/sc}"""
            N "Why even try and fix a lost cause,{w=0.5}when this is all that I am?"
            N "And all that I will be?"
            N "So fuck you."
            N "I give up."
            N "And you should have given up on me,{w=0.5}too.{w=1} A long,{w=0.5}long time ago."
            #SCENE N " has his back turned on you

        "(Hug)": #click on Character
            #$ p = p + 1
            #SCENE Tree spirit hugs Noah
            N "*sobbing*"
            T "Everything is going to be alright."
            N " +=5}No it’s not! {w=1} I hurt him! {w=1} I WANTED to hurt him! }"
            T "Maybe you’re right.{w=1} Maybe Ezra will hate you for the rest of your life."
            T """The pain you feel might overwhelm you.{w=1} It consumes a part of you.
            Perhaps,{w=0.5}Ezra was a part of you that ripped away."""
            N "{cps=2}...{/cps}"
            T "But what’s important to you? {w=1} Is Ezra really THAT important to you?"
            N "{cps=2}...{/cps}"
            T """Be courageous,{w=0.5}my little hero.{w=1} Find the part of you that
            bravely faces rejection and scorn.{w=1} Find the part of you that seeks love."""
            N "{cps=2}...{/cps}"
            N "... and then?"
            T "Simple.{w=1} Go and apologize."

#SCENE 5:
    #CUTSCENE: Neutral N ", colorless dreamspace
    N "Sap."

    N "Sap,{w=0.5}do you want to know something funny?"

    menu:
        "Yes.":
            N "Remember a long,{w=0.5}long time ago when I first told you about Ezra."

    N "And the lunch he shared with me?"

    menu:
         "Yes.":
             N "Do you remember what else I said?"

    menu:
        "{cps=2}...{/cps}":
            N "I said,{w=0.5}“I can’t live without him."

    N "And you know,{w=0.5}now that I’m living it,{w=0.5}that statement is still true."

    N "It’s so dark.{w=1} It feels so meaningless.{w=1} It’s so empty."

    N "He was my light,{w=0.5}Sap.{w=1} My *sun.*"

    N "And just like how you need the sun’s warmth to grow,{w=0.5}I needed his warmth to find any value in this..."

    N "To find any value in this shitty,{w=0.5}awful life."

    N "I lost him,{w=0.5}Sap."

    N "He left me.{w=1} He *abandoned* me."

    N "He hates me.{w=1} *Life* hates me."

    N "It’s not fair."

    N "*None* of this is fair."

    N "So I give up,{w=0.5}okay?"

    N "I.{w=1} Give.{w=1} Up."
    #CUTSCENE: Human disappears

#SCENE 6:
    #CUTSCENE: Empty dream space, colorless

    menu:
         "Noah?":
            "{cps=2}......{/cps}" #there must be some code following the menu choice
         "(Where is he...?)":
            "{cps=2}......{/cps}" #so I put these here as placeholder

    #SCENE: Roots are everywhere.
    #CUTSCENE: Can see Sap’s hands, they’re covered in black vines and roots.
    #(something that maybe alludes to N " dying)
    #SCENE fades to black
    if p <= 2:
        jump bad

    elif p > 4:
        jump good

    else:
        jump meh



#BAD END: (< 3 points)
    #CUTSCENE: Dream space almost pitch black, N "’s there, roots all over his form, back facing camera
label bad:
    T "Noah?"

    "{cps=2}...{/cps}"

    T "Noah,{w=0.5}please."

    "{cps=2}...{/cps}"

    T "Noah{nw}"

    N "I’m not sorry."

    T "Noah?"

    N "{cps=2}...{/cps}"

    N "Wanna know something ironic,{w=0.5} though?"

    N "Remember a long time ago I told you about haustoria?{w=1} Those parasitic plants?"

    N "Maybe that’s what everything was."

    N "I’m the plant,{w=0.5} trying my best to live in this shitty world and all the bad was just the roots strangling me and wringing me dry."

    N "Maybe that’s why I found them so fascinating."

    N "Because they’re a reflection of this life of mine."

    N "{cps=2}...{/cps}"

    N "This shitty, unfair, ruined world.{w=1} And to that, you know what I’ll say?"

    N "Good riddance"

    N "Because these dumb roots may have won against me,{w=0.5} but in my own defeat I will drag it down with me,{w=0.5} too."

    #scene be with fade
    #CUTSCENE: Dead tree, smashed photo with word “end.” on top

    return

#MEH END:
    #CUTSCENE Dreamspace almost pitch black, but N " can be scene with his form completely overtaken by the dark roots
label meh:

    T "Noah!"

    N "{cps=2}...{/cps}"

    T "Noah?"

    N "Sap."

    "{cps=2}...{/cps}"

    N "Sap I’m sorry."

    T "Sorry about what?"

    N "{cps=10}For{/cps}{cps=5}...{/cps} this."

    N "I just got angry.{w=1} And I couldn’t take it anymore,{w=0.5}okay?"

    N "I tried my best but I can’t escape it."

    T "Escape what?"

    N "I can’t escape my past,{w=0.5}okay?" #(my past)

    N "Just like how you’re just a stupid tree rooted in a pot of rotting soil,{w=0.5}I’m a stupid human rooted down by my–"

    N "By my–{nw}"

    #SCENE Confused Human

    N "What was so wrong about my life?"

    N """Was it my awful parents and a home that didn’t quite ever feel like it?
    Or was it me and these emotions that ran too deep that eventually
    I absorbed and drowned in all the poison around me?"""

    N "What was I tied down by?"

    T "Nothing,{w=0.5}Noah.{w=1} *Nothing.*"

    T "We’re not the same Noah."

    #Choice
    menu:
        "Why didn’t you try harder? Why did you give up?":
            N "Because *nobody* cared.{w=1} I was trying so hard and for *what*?"
            N "Tell me,{w=0.5}Sap."
            N "{b}What did I live for?{/b}"
            N "For the sake of surviving?"
            N "That’s not living,{w=0.5}Sap."
            N "That’s hell."
            N "At least I’ll  be free of it now.{w=1} Even if I have to put everyone around me through it."
            N "And,{w=0.5}hey,{w=0.5}at least Ez will be free of the burden of me.{w=1} It was for the best,{w=0.5}anyways."

        "But it’ll be okay.":
            N "Right."
            N "It’ll be okay.{w=1} It’s always been like that."
            N "And Ez will be okay,{w=0.5}too.{w=1} He’ll be better,{w=0.5}right,{w=0.5}Sap?"
            N "Can you visit him,{w=0.5}too? Can you see how he’s doing? Is he doing okay?"
            N "I mean,{w=0.5}I’m no longer weighing him down with my needless emotions and burdens and traumas."
            N "Ez no longer has to be Atlas,{w=0.5}holding up the weight of my world,{w=0.5}right?"
            T "Ez is doing –"
            N "Wait,{w=0.5}don’t finish that sentence."
            N "I don’t want to know."
            N "{cps=10}It doesn’t...{/cps} make a difference to me anymore."
            N "But I hope he’s happy.{w=1} That’s all I have ever wanted."
            N "Because that’s all I need so that things can be okay."
            N "And things are,{w=0.5}or at least will be,{w=0.5}okay."
    return

#GOOD END:
label good:

    N "Sap."

    T "Noah!"

    N "Sap,{w=0.5}I miss him."

    N "I miss Ezra."

    #SCENE: Crying Human

    N "I–"

    N "God,{w=0.5}I hate this."

    N "Why,{w=0.5}Sap,{w=0.5}*why*?"

    T "Why what?"

    N "I might not have been able to stand a life without Ezrea in it,{w=0.5}but he was still there,{w=0.5}you know?"

    N "Even if he wouldn’t have been in my life,{w=0.5}he was still looking at the same sky,{w=0.5}breathing the same air."

    N "Why did I give that up?"

    N "I’m not stupid,{w=0.5}am I?"

    T "No,{w=0.5}you’re not."

    N " -=5}I just wanted to show that... }"

    N "I just wanted to show Ezra he meant to much to me and that I cared so much about him that I was willing to {sc}{b}die{/b}{/sc} for him."

    N "Because in those breaths without him,{w=0.5}it felt like there was no tomorrow.{w=1} It felt like the end."

    N "But,{w=0.5}I didn’t get to say goodbye.{w=1} Why did I have to end things like this?"

    N "And why,{w=0.5}Sap,{w=0.5}was it so lonely? Why,{w=0.5}in my last moments,{w=0.5}did I have to be alone?"

    N "Tell him I’m sorry."

    N "And to you too,{w=0.5}Sap.{w=1} I’m sorry."

    return
