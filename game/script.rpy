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

    T "That’s me. Or, I guess, this is me"

    T "Hi!"

    T "My human’s the guy in the photo there."

    T "His name is Noah."

    # SCENE: Zoom into photo, spirits hand touches it

    T "Isn’t he precious?"

    T "Well, it’s my job to take care of Mr. Noah!"

    # SCENE: spirit looks a little sad in the mirror

    T "Noah’s always been struggling… His family has been… tough, to say the least."

    T "I wish I could talk to him outside of his dreams which don’t even happen too often but…"

    T "At least I can visit him in his dreams."

    T "At least I can do a little something, despite being rooted down to this stagnant, silent form…"

# SCENE 1
    # CUTSCENE: Younger N "
    N "Oh, it’s you. My guardian angel. "

    N "Well, tree angel I guess."

    T "Why hello! So cheery today."

    N "I’m such an idiot."

    T"""Don’t say stuff like that to yourself!
    Why? What happened?"""

    #1. Oh, alright, alright. Anyways…
    #2. -moves straight to the next dialogue-

    N "I woke up late this morning, right? So I left home in a hurry! But…"

    N "I accidentally left my wallet at home! I basically starved for an hour."

    N "Ezra chose to share his lunch with me though. I’m very grateful."

    T"""Wow. So Ezra’s a good friend, huh?
    Aw, how kind of him!"""

    N "Exactly! He’s a bit annoying at times. Like he says some stuff that downright pisses me off."

    N "But, I literally can’t live without him. I mean, I could’ve starved to death today if it weren’t for him."

    N "Not literally, duh, but he really does come in clutch, saving my clumsy ass, haha."

    N "He means a lot to me, Sap."

    # [Time Skip, Noah looks older)

# SCENE 2:
    # CUTSCENE: Neutral Human
    N "Hey, Sap"

    T "Yeah?"

    N "Do you remember a while back I told you that Ezra meant a lot to me."

    T "I mean… It's kind of obvious."

    T "He’s literally *all* that you talk about."

    T "Do you… like him?"

    N "Yeah, as a friend. I mean, he’s always been there for me."

    N "If anything, he’s the only constant that keeps me grounded in the chaos of school and home."

    N "Like how he let me stay over with him that night Mom and Dad got into a huge fight over something stupid."

    N "Why do people fight over dumb things? Why can’t they just talk about it?"

    N "Like, if you let a rotten branch fester, it’ll kill the whole plant, you know?"

    N "Or, remember that time when Dad hit me? Well, the most recent time that Dad hit me, over stupid fucking grades?"

    N "It was Ezra who patched me up."

    N "Both the bruised lip and cut cheek, but also from that mental shitshow I was going through."

    N "He means the world to me."

    N "I know him probably more than I know myself, and he, I."

    N "But something’s wrong, you know? Like he feels so much more absent from my life compared to before."

    N "He doesn’t pick up my phone calls all the time anymore."

    N "He doesn’t let me hide out at his place after a fight with my parents."

    N "He just…"

    N "It feels like he doesn’t care."

    menu:
        "I’m sure he does, Noah.":
            N "Right?"
            N "But something just feels, *wrong.*"
            N "I don’t know."
            N "I’ll ask him what’s wrong, okay? And I’ll help fix him, like he fixed me."
            N "Thanks, Sap. I’ll see you soon."

        "I mean, his past actions show that he clearly does.":
            N "But people *change,* right?"
            N "Isn’t that what they’re supposed to do? *Grow?*"
            N "Or what, are you saying we’re forever stagnant? That we’re forever tied down by our upbringing and stupid genetics?"
            N "Are you saying that I’m going to end up like my dirtbag fucking parents?"
            T "Noah, you know that’s not that I mean."
            N "You sure? Because it sure as hell sounded like you did."
            N "Whatever, I don’t want to talk to you anymore."
            N "I’m going to go talk to Ez, because he always got me a little better than you did."

#SCENE 3:
    #CUTSCENE: N " appears, looking  at the ground, visibly upset, edges of the screen are dark, black vines are curled around N "’s arms and legs

    T "Noah?"

    #CUTSCENE: Noah looks up

    N "Hey."

    N "…"

    T "So?"

    N "So what?"

    T "So, how are you?"

    N "…"

    N "Never better. I mean my best friend is only being an annoying, stupid piece of garbage."

    N "*sighs angrily*"

    N "Like, when I tried to be civil and ask him if something was wrong, he was like, 'I’m fine.'"

    N "And then next thing you know, he’s canceling plans last minute. Like, does he not care how I feel?"

    N "If he didn’t give a flying fuck about me, why should I care about him?"

    N "Why would I try to be friends with someone who obviously doesn’t care about me? "

    N "In all honesty, it kind of feels like he’s avoiding me."

    #SCENE: Angry Human

    N "…"

    N """Ugh, anyways I kind of lost it and gave him a piece of my mind today,
    asking him why he wouldn’t just tell me what’s wrong, and you should have *seen* his face."""

    N "He looked *mad.* "

    N "What *right* does *he* have to get upset with *me*?"

    N "And you know what he said?"

    N "He said part of it was my fault. And when I asked him why, do you know the nonsense he spewed?"

    N "He said it was because he always put me first, that in turn he neglected his own needs."

    N "Sap, he’s wrong, right? Isn’t he being kind of unreasonable?"

    menu:
        "Perhaps  little, but he’s probably hurting, too.":
                N "Okay, but he never *tells* me anything. He just, you know-"
                N "Like, why didn’t he say something sooner? Why did he bottle it up just for it to explode in our faces now?"
                N "…"
                #SCENE: Sad Human
                N """He’s going through it. I *know* that. But he never talks about it
                and sometimes I just get so *angry* because why can’t he just –"""
                N "Why can’t he just *talk* to me about it? That’s what friend are *for*, right?"
                N "God, he’s so dumb."

                menu:
                    "Well, maybe try and apologize? Or try to talk to him more? It’s better than doing… nothing, right?": #(-1)
                        N "No."
                        T "Noah?"
                        N "Why should *I* be the one apologizing? He’s at fault, anyways."
                        T "That wasn’t what I was trying to–"
                        N "I don’t *care* what he’s going through. The hell I’m going through is so much worse."
                        N "And if he can’t see that, he doesn’t deserve an apology from me."
                        #SCENE: Angry Human
                        N "He doesn’t deserve *anything* from me."
                        N "I *hate* him."
                        N "…"
                        N "And you know what, Sap, I hate everything."
                        N "Ezra, you, life."
                        N "I hate it all."
                        #CUTSCENE: Branches crowd screen more, everything darkens abruptly.

                    "Give him space, Noah. You’ve always needed it, so why not try and understand him and give him the same courtesy?": #(+0)
                        N "Ha. You’re right."
                        N "If anything, he should apologize to me *first.*"
                        N "Why should I go out of my way to help him, if he’s never done anything for me to begin with."
                        T "Noah, you know that’s not --"
                        N "No, he’s in the wrong."
                        N "He’s always been in the wrong."
                        N "I *hate* him."
                        N "…"
                        N "And you know what, Sap, I hate everything."
                        N "Ezra, you, life."
                        N "I hate it all."
                        #CUTSCENE: Branches crowd screen more, everything darkens abruptly.

        "No, he’s not. He’s done so much for you, and yet you didn’t notice anything wrong until now?":
            #CUTSCENE: Edges of screen darken
            N "Wow, Sap, even *you’re* not on my side?"
            N "God, first I lost my best friend and now I’m going to lose you too?"
            T "That’s not what I mean–"
            T "Noah, you’re making assumptions–"
            N "No. You shut up. You don’t *get* to talk to me."
            N "You’re just a figment of *my* dream.(MY guardian angel). You’re supposed to *always*(/) be on my(*) side."
            N "It’s people like *you* and *Ezra* that are the problem"
            N "…"
            # SCENE: Confused N "
            N "Or, am *I* the problem?"
            T "Noah…"
            N "I’m the problem."

            menu:
                "That’s not true": #(+0)
                    N "Not you being a *fucking* liar too."
                    N "I see it on your stupid, pitying face. You hate me too."
                    N "But you know what?"
                    N "I hate you too."
                    N "I hate everything."
                    N "Ezra, you, life."
                    N "I hate it all."
                    #CUTSCENE: Branches crowd screen more, everything darkens abruptly.

                "Noah, stop. You’re jumping to conclusions.": #(-1)
                    N "No, I’m not."
                    N "It’s true, right?"
                    N "He’s not going through tough things in life, he’s going through *me.*"
                    N "*I’m* the problem in his life."
                    T "Noah, stop–"
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

    N "He wouldn’t even talk to me. I saw the look on his face… He wouldn’t even look me in the eyes…"

    menu:
        "Oh, Noah…":
            #SCENE Angry Noah
            N "Just STOP."
            N "Stop with the pity. Stop, please."
            N "I don’t want your comfort. I don’t want your anything."
            N "I lost him! I have nothing except for him!"
            N "No friends. No home. No family. No nothing. Ezra was my *everything.*"
            N " And weren’t you supposed to be my 'guardian angel'? Weren’t you supposed to protect me from all this happening?"
            #SCENE Sad N " (hopeless)
            N "Weren’t you supposed to make me better?"
            N "…"
            T "Noah–"
            #SCENE Angry Human
            N "So tell me, why the *fuck* are things the way they are?"
            N "Why can’t you do anything right?"
            N "…"
            N "YOU WERE SUPPOSED TO *FIX* ME."
            N "THIS IS *YOUR* FAULT."
            N "This is *all* your fault."
            N "You’re useless. You’re worse than useless."
            N "If I didn’t listen to you…"
            N "If only I didn’t try like you told me to…"
            N "Then none of this would have happened."
            N "I wish I had never met you."
            N "So leave."
            T "Noah-"
            N "Leave."
            N "Please."
            #SCENE Noah has his back turned to you

        "Why are you so upset?":
            T "Maybe he just needs more space and time, Noah."
            T "Isn’t that what they say?"
            T "Time–"
            #SCENE Angry N "
            N "*Time heals all wounds?*"
            N "I’m sick of your nonsense."
            N "And did you say I’m *upset?*"
            N "That doesn’t even *begin* to capture how I feel."
            N "How I feel, because of *you.*"
            N "I’m fucking done. I’m going to fuck up everything anyways, so why even try and salvage this?"
            N "Why even try and fix a lost cause, when this is all that I am?"
            N "And all that I will be?"
            N "So fuck you."
            N "I give up."
            N "And you should have given up on me, too. A long, long time ago."
            #SCENE N " has his back turned on you

        "(Hug)": #click on Character
            #SCENE Tree spirit hugs Noah
            N "*sobbing*"
            T "Everything is going to be alright."
            N "No it’s not! I hurt him! I WANTED to hurt him!"
            T "Maybe you’re right. Maybe Ezra will hate you for the rest of your life."
            T """The pain you feel might overwhelm you. It consumes a part of you.
            Perhaps, Ezra was a part of you that ripped away."""
            N "…"
            T "But what’s important to you? Is Ezra really THAT important to you?"
            N "…"
            T """Be courageous, my little hero. Find the part of you that
            bravely faces rejection and scorn. Find the part of you that seeks love."""
            N "…"
            N "… and then?"
            T "Simple. Go and apologize."

#SCENE 5:
    #CUTSCENE: Neutral N ", colorless dreamspace
    N "Sap."

    N "Sap, do you want to know something funny?"

    T "Yes?"

    N "Remember a long, long time ago when I first told you about Ezra."

    N "And the lunch he shared with me?"

    T "Yes."

    N "Do you remember what else I said?"

    T "…"

    N "I said, “I can’t live without him."

    N "And you know, now that I’m living it, that statement is still true."

    N "It’s so dark. It feels so meaningless. It’s so empty."

    N "He was my light, Sap. My *sun.*"

    N "And just like how you need the sun’s warmth to grow, I needed his warmth to find any value in this…"

    N "To find any value in this shitty, awful life."

    N "I lost him, Sap."

    N "He left me. He *abandoned* me."

    N "He hates me. *Life* hates me."

    N "It’s not fair."

    N "*None* of this is fair."

    N "So I give up, okay?"

    N "I. Give. Up."
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

    T "Noah, please."

    "…"

    T "Noah-"

    N "(interrupts) I’m not sorry."

    N "This was always the answer. It was the *only* answer."

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

    N "I just got angry. And I couldn’t take it anymore, okay?"

    N "I tried my best but I can’t(couldn’t) escape it(/)."

    T "Escape what?"

    N "I can’t escape my past, okay?" #(my past)

    N "Just like how you’re just a stupid tree rooted in a pot of rotting soil, I’m a stupid human rooted down by my–"

    N "By my–"

    #SCENE Confused Human

    N "What was so wrong about my life?"

    N """Was it my awful parents and a home that didn’t quite ever feel like it?
    Or was it me and these emotions that ran too deep that eventually
    I absorbed and drowned in all the poison around me?"""

    N "What was I tied down by?"

    T "Nothing, Noah. *Nothing.*"

    T "We’re not the same Noah."

    #Choice
    menu:
        "Why didn’t you try harder? Why did you give up?":
            N "Because *nobody* cared. I was trying so hard and for *what*?"
            N "Tell me, Sap."
            N "*What did I live for?*"
            N "For the sake of surviving?"
            N "That’s not living, Sap."
            N "That’s hell."
            N "At least I’ll  be free of it now. Even if I have to put everyone around me through it."
            N "And, hey, at least Ez will be free of the burden of me. It was for the best, anyways."

        "But it’ll be okay.":
            N "Right."
            N "It’ll be okay. It’s always been like that."
            N "And Ez will be okay, too. He’ll be better, right, Sap?"
            N "Can you visit him, too? Can you see how he’s doing? Is he doing okay?"
            N "I mean, I’m no longer weighing him down with my needless emotions and burdens and traumas."
            N "Ez no longer has to be Atlas, holding up the weight of my world, right?"
            T "Ez is doing –"
            N "Wait, don’t finish that sentence."
            N "I don’t want to know."
            N "It doesn’t… make a difference to me anymore."
            N "But I hope he’s happy. That’s all I have ever wanted."
            N "Because that’s all I need so that things can be okay."
            N "And things are, or at least will be, okay."

#GOOD END:

    N "Sap."

    T "Noah!"

    N "Sap, I miss him."

    N "I miss Ezra."

    #SCENE: Crying Human

    N "I–"

    N "God, I hate this."

    N "Why, Sap, *why*?"

    T "Why what?"

    N "I might not have been able to stand a life without Ezrea in it, but he was still there, you know?"

    N "Even if he wouldn’t have been in my life, he was still looking at the same sky, breathing the same air."

    N "Why did I give that up?"

    N "I’m not stupid, am I?"

    T "No, you’re not."

    N "I just wanted to show that…"

    N "I just wanted to show Ezra he meant to much to me and that I cared so much about him that I was willing to *die* for him."

    N "Because in those breaths without him, it felt like there was no tomorrow. It felt like the end."

    N "But, I didn’t get to say goodbye. Why did I have to end things like this?"

    N "And why, Sap, was it so lonely? Why, in my last moments, did I have to be alone?"

    N "Tell him I’m sorry."

    N "And to you too, Sap. I’m sorry."

    # This ends the game.

    return
