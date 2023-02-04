# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define N = Character("Noah")
define T = Character("Sap")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # These display lines of dialogue.

    T "That’s me.{w=1} Or,{w=0.5}I guess,{w=0.5}this is me"

    T "Hi!"

    T "My human’s the guy in the photo there."

    T "His name is Noah."

    # SCENE: Zoom into photo, spirits hand touches it

    T "Isn’t he precious?"

    T "Well, {w=0.5}it’s my job to take care of Mr.{w=1} Noah!"

    # SCENE: spirit looks a little sad in the mirror

    T "Noah’s always been {cps=10}struggling...{/cps} His family has been{cps=2}...{/cps} {cps=10}tough{/cps}{w=1}, to say the least."

    T "I wish I could talk to him outside of his dreams {w=0.3} which don’t even happen too often {cps=10}but...{/cps}"

    T "At least I can visit him in his dreams."

    T "At least I can do a little something,{w=0.5}{cps=20} despite being rooted down to this stagnant, silent form...{/cps}"

# SCENE 1
    # CUTSCENE: Younger N "
    N "Oh,{w=0.5} it’s you.{w=1} My guardian angel.{w=1}"

    N "Well,{w=0.5} tree angel I guess."

    T "Why hello! So cheery today."

    N "I’m such an idiot."

    menu:
        "Don’t say stuff like that to yourself!":
            N "Oh,{w=0.5}alright,{w=0.5}alright.{w=1} {cps=10}Anyways...{/cps}"
            N "I woke up late this morning,{w=0.5}right? So I left home in a hurry!{w=1} {cps=10}But...{/cps}"

        "Why? What happened?":
            N "I woke up late this morning,{w=0.5}right? So I left home in a hurry!{w=1} {cps=10}But…{/cps}"

    N "{cps=60}I accidentally left my wallet at home!{/cps} {w=1} I basically starved for an hour."

    N "Ezra chose to share his lunch with me though.{w=1} I’m very grateful."

    menu:
        "Wow.{w=1} So Ezra’s a good friend,{w=0.5}huh?":
            N "Exactly!{fast} He’s a bit annoying at times.{w=1}Like he says some stuff that downright pisses me off."

        "Aw, how kind of him!":
            N "Exactly!{fast} He’s a bit annoying at times.{w=1} Like he says some stuff that downright pisses me off."

    N "But, I {b}literally{/b} can’t live without him.{w=1} I mean,{w=0.5} I could’ve starved to death today if it weren’t for him."

    N "Not literally,{w=0.5}duh,{w=0.5}but he really does come in clutch,{w=0.5}saving my clumsy ass,{w=0.5}haha."

    N "He means a lot to me,{w=0.5}Sap."

    # [Time Skip, Noah looks older)

# SCENE 2:
    # CUTSCENE: Neutral Human
    N "Hey,{w=0.5}Sap"

    T "Yeah?"

    N "Do you remember a while back I told you that Ezra meant a lot to me."

    T "I mean… It's kind of obvious."

    T "He’s literally {b}all{/b} that you talk about."

    T "Do you… like him?"

    N "Yeah,{w=0.5}as a friend.{w=1} I mean,{w=0.5}he’s always been there for me."

    N "If anything,{w=0.5}he’s the only constant that keeps me grounded in the chaos of school and home."

    N "Like how he let me stay over with him that night Mom and Dad got into a huge fight over something stupid."

    N "Why do people fight over dumb things? Why can’t they just talk about it?"

    N "Like,{w=0.5}if you let a rotten branch fester,{w=0.5}it’ll kill the whole plant,{w=0.5}you know?"

    N "Or,{w=0.5}remember that time when Dad hit me? Well,{w=0.5}the most recent time that Dad hit me,{w=0.5}over stupid fucking grades?"

    N "It was Ezra who patched me up."

    N "Both the bruised lip and cut cheek,{w=0.5}but also from that mental shitshow I was going through."

    N "He means the world to me."

    N "I know him probably more than I know myself,{w=0.5}and he,{w=0.5}I."

    N "But something’s wrong,{w=0.5}you know? Like he feels so much more absent from my life compared to before."

    N "He doesn’t pick up my phone calls all the time anymore."

    N "He doesn’t let me hide out at his place after a fight with my parents."

    N "He just…"

    N "It feels like he doesn’t care."

    menu:
        "I’m sure he does,{w=0.5}Noah.":
            N "Right?"
            N "But something just feels,{w=0.5}{b}wrong{/b}.*"
            N "I don’t know."
            N "I’ll ask him what’s wrong,{w=0.5}okay? And I’ll help fix him,{w=0.5}like he fixed me."
            N "Thanks,{w=0.5}Sap.{w=1} I’ll see you soon."

        "I mean,{w=0.5}his past actions show that he clearly does.":
            N "But people {b}change{/b},{w=0.5}right?"
            N "Isn’t that what they’re supposed to do? {b}{sc=1}Grow?{/b}{/sc}"
            N "Or what,{w=0.5}are you saying we’re forever stagnant? That we’re forever tied down by our upbringing and stupid genetics?"
            N "Are you saying that I’m going to end up like my dirtbag fucking parents?"
            T "Noah,{w=0.5}you know that’s not that I mean."
            N "You sure? Because it sure as hell sounded like you did."
            N "Whatever,{w=0.5}I don’t want to talk to you anymore."
            N "I’m going to go talk to Ez,{w=0.5}because he always got me a little better than you did."

#SCENE 3:
    #CUTSCENE: N " appears, looking  at the ground, visibly upset, edges of the screen are dark, black vines are curled around N "’s arms and legs

    T "Noah?"

    #CUTSCENE: Noah looks up

    N "Hey."

    N "…"

    T "So?"

    N "So what?"

    T "So,{w=0.5}how are you?"

    N "…"

    N "Never better.{w=1} I mean my best friend is only being an annoying,{w=0.5}stupid piece of garbage."

    N "*sighs angrily*"

    N "Like,{w=0.5}when I tried to be civil and ask him if something was wrong,{w=0.5}he was like,{w=0.5}'I’m fine.'"

    N "And then next thing you know,{w=0.5}he’s canceling plans last minute.{w=1} Like,{w=0.5}does he not care how I feel?"

    N "If he didn’t give a flying fuck about me,{w=0.5}why should I care about him?"

    N "Why would I try to be friends with someone who obviously doesn’t care about me? "

    N "In all honesty,{w=0.5}it kind of feels like he’s avoiding me."

    #SCENE: Angry Human

    N "…"

    N """Ugh,{w=0.5}anyways I kind of lost it and gave him a piece of my mind today,
    asking him why he wouldn’t just tell me what’s wrong,{w=0.5}and you should have *seen* his face."""

    N "He looked {b}mad{/b}."

    N "What {b}right{/b} does {b}he{/b} have to get upset with *me*?"

    N "And you know what he said?"

    N "He said part of it was my fault.{w=1} And when I asked him why,{w=0.5}do you know the nonsense he spewed?"

    N "He said it was because he always put me first,{w=0.5}that in turn he neglected his own needs."

    N "Sap,{w=0.5}he’s wrong,{w=0.5}right? Isn’t he being kind of unreasonable?"

    menu:
        "Perhaps  little,{w=0.5}but he’s probably hurting,{w=0.5}too.":
                N "Okay,{w=0.5}but he never {b}tells{/b} me anything.{w=1} He just,{w=0.5}you know{nw}"
                N "Like,{w=0.5}why didn’t he say something sooner? Why did he bottle it up just for it to explode in our faces now?"
                N "…"
                #SCENE: Sad Human
                N """He’s going through it.{w=1} I {b}know{/b} that.{w=1} But he never talks about it
                and sometimes I just get so {b}angry{/b} because why can’t he just{nw}"""
                N "Why can’t he just {b}talk{/b} to me about it? That’s what friend are *for*,{w=0.5}right?"
                N "God,{w=0.5}he’s so dumb."

                menu:
                    "Well,{w=0.5}maybe try and apologize? Or try to talk to him more? It’s better than doing… nothing,{w=0.5}right?": #(-1)
                        N "No.{fast}"
                        T "Noah?"
                        N "Why should {b}I{/v} be the one apologizing? He’s at fault,{w=0.5}anyways."
                        T "That wasn’t what I was trying to{nw}"
                        N "I don’t {sc=1}care{/sc} what he’s going through.{w=1} The hell I’m going through is so much worse."
                        N "And if he can’t see that,{w=0.5}he doesn’t deserve an apology from me."
                        #SCENE: Angry Human
                        N "He doesn’t deserve *anything* from me."
                        N "I {sc=3}{b}HATE{/b}{/sc} him."
                        N "…"
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
                        N "…"
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
            N "You’re just a figment of {b}my{/b} dream.{w=1} You’re supposed to {b}always{/b} be on {sc}{b}MY{/b}{/sc} side."
            N "It’s people like *you* and *Ezra* that are the problem"
            N "…"
            # SCENE: Confused N "
            N "Or, am {b}I{/b} the problem?"
            T "Noah…"
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
                    N "He’s not going through tough things in life,{w=0.5}he’s going through *me.*"
                    N "*I’m* the problem in his life."
                    T "Noah,{w=0.5}stop–"
                    N "I know you’re thinking it."
                    T "Noah–"
                    N "You think I’m better off dead."
                    N "Of course you do."
                    #SCENE Sad Human
                    N "Of course you do…"
                    #CUTSCENE: Branches crowd screen more, everything darkens abruptly.

#SCENE 4:
    #SCENE: Noah looks defeated (or just sad)

    N "…"

    T "Noah?"

    N "…"

    T "Noah?"

    N "…"

    T "N–"

    N "He doesn’t… He wouldn’t…"

    N "He wouldn’t even talk to me.{w=1} I saw the look on his face… He wouldn’t even look me in the eyes…"

    menu:
        "Oh, Noah…":
            #SCENE Angry Noah
            N "Just STOP."
            N "Stop with the pity.{w=1} Stop,{w=0.5}please."
            N "I don’t want your comfort.{w=1} I don’t want your anything."
            N "I lost him! I have nothing except for him!"
            N "No friends.{w=1} No home.{w=1} No family.{w=1} No nothing.{w=1} Ezra was my *everything.*"
            N " And weren’t you supposed to be my 'guardian angel'? Weren’t you supposed to protect me from all this happening?"
            #SCENE Sad N " (hopeless)
            N "Weren’t you supposed to make me better?"
            N "…"
            T "Noah–"
            #SCENE Angry Human
            N "So tell me,{w=0.5}why the *fuck* are things the way they are?"
            N "Why can’t you do anything right?"
            N "…"
            N "YOU WERE SUPPOSED TO *FIX* ME."
            N "THIS IS *YOUR* FAULT."
            N "This is *all* your fault."
            N "You’re useless.{w=1} You’re worse than useless."
            N "If I didn’t listen to you…"
            N "If only I didn’t try like you told me to…"
            N "Then none of this would have happened."
            N "I wish I had never met you."
            N "So leave."
            T "Noah{nw}"
            N "Leave."
            N "Please."
            #SCENE Noah has his back turned to you

        "Why are you so upset?":
            T "Maybe he just needs more space and time,{w=0.5}Noah."
            T "Isn’t that what they say?"
            T "Time–"
            #SCENE Angry N "
            N "*Time heals all wounds?*"
            N "I’m sick of your nonsense."
            N "And did you say I’m *upset?*"
            N "That doesn’t even *begin* to capture how I feel."
            N "How I feel,{w=0.5}because of *you.*"
            N "I’m fucking done.{w=1} I’m going to fuck up everything anyways,{w=0.5}so why even try and salvage this?"
            N "Why even try and fix a lost cause,{w=0.5}when this is all that I am?"
            N "And all that I will be?"
            N "So fuck you."
            N "I give up."
            N "And you should have given up on me,{w=0.5}too.{w=1} A long,{w=0.5}long time ago."
            #SCENE N " has his back turned on you

        "(Hug)": #click on Character
            #SCENE Tree spirit hugs Noah
            N "*sobbing*"
            T "Everything is going to be alright."
            N "No it’s not! I hurt him! I WANTED to hurt him!"
            T "Maybe you’re right.{w=1} Maybe Ezra will hate you for the rest of your life."
            T """The pain you feel might overwhelm you.{w=1} It consumes a part of you.
            Perhaps,{w=0.5}Ezra was a part of you that ripped away."""
            N "…"
            T "But what’s important to you? Is Ezra really THAT important to you?"
            N "…"
            T """Be courageous,{w=0.5}my little hero.{w=1} Find the part of you that
            bravely faces rejection and scorn.{w=1} Find the part of you that seeks love."""
            N "…"
            N "… and then?"
            T "Simple.{w=1} Go and apologize."

#SCENE 5:
    #CUTSCENE: Neutral N ", colorless dreamspace
    N "Sap."

    N "Sap,{w=0.5}do you want to know something funny?"

    T "Yes?"

    N "Remember a long,{w=0.5}long time ago when I first told you about Ezra."

    N "And the lunch he shared with me?"

    T "Yes."

    N "Do you remember what else I said?"

    T "…"

    N "I said,{w=0.5}“I can’t live without him."

    N "And you know,{w=0.5}now that I’m living it,{w=0.5}that statement is still true."

    N "It’s so dark.{w=1} It feels so meaningless.{w=1} It’s so empty."

    N "He was my light,{w=0.5}Sap.{w=1} My *sun.*"

    N "And just like how you need the sun’s warmth to grow,{w=0.5}I needed his warmth to find any value in this…"

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

    T "Noah?"

    "(Where is he…?)"

    #SCENE: Roots are everywhere.
    #CUTSCENE: Can see Sap’s hands, they’re covered in black vines and roots.
    #(something that maybe alludes to N " dying)
    #SCENE fades to black

#BAD END: (< 3 points)
    #CUTSCENE: Dream space almost pitch black, N "’s there, roots all over his form, back facing camera
    T "Noah?"

    "…"

    T "Noah,{w=0.5}please."

    "…"

    T "Noah{nw}"

    N "I’m not sorry."

    N "This was always the answer.{w=1} It was the {b}ONLY{/b} answer."

    #SCENE fades to black
    #CUTSCENE: Dead tree, smashed photo with word “end.” on top

#MEH END:
    #CUTSCENE Dreamspace almost pitch black, but N " can be scene with his form completely overtaken by the dark roots

    T "Noah!"

    N "…"

    T "Noah?"

    N "Sap."

    "..."

    N "Sap I’m sorry."

    T "Sorry about what?"

    N "For… this."

    N "I just got angry.{w=1} And I couldn’t take it anymore,{w=0.5}okay?"

    N "I tried my best but I can’t(couldn’t) escape it(/)."

    T "Escape what?"

    N "I can’t escape my past,{w=0.5}okay?" #(my past)

    N "Just like how you’re just a stupid tree rooted in a pot of rotting soil,{w=0.5}I’m a stupid human rooted down by my–"

    N "By my–"

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
            N "*What did I live for?*"
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
            N "It doesn’t… make a difference to me anymore."
            N "But I hope he’s happy.{w=1} That’s all I have ever wanted."
            N "Because that’s all I need so that things can be okay."
            N "And things are,{w=0.5}or at least will be,{w=0.5}okay."

#GOOD END:

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

    N "I just wanted to show that…"

    N "I just wanted to show Ezra he meant to much to me and that I cared so much about him that I was willing to *die* for him."

    N "Because in those breaths without him,{w=0.5}it felt like there was no tomorrow.{w=1} It felt like the end."

    N "But,{w=0.5}I didn’t get to say goodbye.{w=1} Why did I have to end things like this?"

    N "And why,{w=0.5}Sap,{w=0.5}was it so lonely? Why,{w=0.5}in my last moments,{w=0.5}did I have to be alone?"

    N "Tell him I’m sorry."

    N "And to you too,{w=0.5}Sap.{w=1} I’m sorry."

    # This ends the game.

    return
