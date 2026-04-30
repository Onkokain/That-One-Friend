label start:
    # play bg music eerie
    $ mystery = "??#@!"
    scene bg black
    with fade
    empty "Have you ever wished you were never born.. or wished you could die without affecting those around you.."
    menu:
        "Yes..":
            you "Yes.. I have.."
            narrator "I know how you feel.."
            $ wanna_die=True
        "No..":
            you "No.. Why would I ever wish that??"
            narrator "Well.. I wish I could say the same for myself.."
            $ wanna_die=False
        "I don't know..":
            you "I don't know.. I have never ever thought about that before.."
            narrator "Nobody does for certain dear.."
            $ wanna_die=False
    #stop bg music eerie and play bg music default at park
    scene bg sunset with fade
    mystery "Look at the setting sun. it looks so beautiful.."
    mystery "I wish I could stay with you like this forever and ever.."

    scene bg park with fade
    mystery "Lets marry when we get older okay?"
    you "Yeah... I'll always be with you, no matter what."
    mystery "I know you will.. I'm sure you will.."
    you "I will.. no matter what..."
    mystery "I love y-------"
    empty "... ... ..."
    empty "... ... ..."
    # bg music fades out and alarm starts playing
    scene bg bed
    with fade
    empty "buzz.. buzz.. buzz.. buzz.."
    narrator "Your alarm rings loudly, waking you up from sleep."
    you "Huh...? What?? Was I in a dream?"
    you "Who was that? I don't remember anything about her..."
    you "Was she  about to say... 'I love you'??"
    you "That was a strange dream.. strange indeed.."
    you "I wish I knew who she was.. I wish I could get the chance to see her again.."
    empty "... ... ..."
    # turning off alarm sound
    # alarm stops

    scene bg black
    with fade

    narrator "It was an early summer morning.."
    narrator "You wake up to the sound of the alarm"
    narrator "Your mom hears you move around in the bed and asks you to get up."
    narrator "You hear her but you don't want to get up.. not yet.. not until you figure out who that girl was.."
    narrator "Your mom shouts again, 'You..? get up now!'"
    narrator "Wait.. What was your name again?"

    $ player = renpy.input("What is your name?")
    $ player = player.strip()
    $ player = player if player else 'Brandon'

    scene bg kitchen
    with fade
    # water flowing music starts to play

    mom "[player], get up now! It's already 7:00 do you plan on sleeping all day?"
    # water flowing music fades out
    scene bg bed with fade

    narrator "Your mom bolts into your room and asks you to get up.."
    mom "Wake up already, [player]. It's already early in the morning, you don't want to sleep all day do you?"
    you "No mom, I'll get up soon!"
    mom "Today is an important day for you. Don't forget."
    you "Important? how is today important??"
    mom "Did you forget.. you have to see [mystery] off at the Airport today."
    mom "She's leaving today and I think her flight leaves at 9:00 am. So we have to leave in around an hour.."
    you " [mystery]?? Who's that??"
    narrator "Your mom {i}Sighs..{/i}"
    mom "Stop joking around with me and get up.."
    mom "Did you forget about [mystery] before she even left?"
    # eerie bg music starts playing
    menu:
        "How could i ever forget about [mystery]..":
            $ remember = True
            call remember_route

        "I really don't know who [mystery] is..":
            $ remember= False
            call forgot_route

    mom "Now hurry up and get ready.. we have to leave to see her off soon.."
    mom "You wouldn't want to make her sad by being late right??"

    you "I don't mom.. I'll go get ready right away.."
    empty "{i}You don't know who she is but still decide to play along ahead instead of getting your mom angry..{/i}"
    you "I think i'll go take a bath, can you get my clothes ready for me?"
    mom "Yeah they're already on the hanger I thought you'd be excited and wake up before me today.."
    you "Oh.. Thanks mom.."

    scene bg washroom with fade

    empty"{i}I still cant stop thinking about her..{/i}"
    empty"{i} Who is [mystery].. is it the same person as in my dream??{/i}"
    empty "{i}No.. That couldn't be I don't even know who this [mystery] person is and the girl.. in my dream.. said she.. loved me??{/i}"
    empty "{i}I don't know what's even going on anymore..{/i}"
    empty"{i} Guess it's time to take a shower..{/i}"
    empty"{i} It's a cold day.. Do i really have to.."
    menu:
        "Yes, Take a shower..":
            empty"{i} Guess I do have to take a shower.. {/i}"
            scene bg shower with fade
            narrator "You take off your clothes and step into the shower.."

            if remember==False:
                empty "{i} I still can't stop thinking about her.. who is she?? {/i}"
                empty "{i} How do i even know her...{/i}"
                empty "{i} Mom told me that she has been with me since I was born.. but how do i not remember who she is... {/i}"
                empty "THUD!!"
                you "OWWWWW!!"
                narrator "You slip on the wet floor and hit your head on the wall.."
                narrator "You touch your head... there's a lot of blood on your hands.."
                narrator "Your breathing gets slower..."
                if wanna_die==True:
                    empty "{i} I guess this is it for me.. {/i}"
                    empty "{i} I hope I can see her again.. {/i}"

                    narrator 'You slowly lose yourself..'
                    narrator 'The blood from your head starts to pool around you..'
                    narrator 'You slowly lose consciousness...'
                    narrator 'Surrounded by the memories of her... You die..'
                    narrator 'Die in vain...'
                    empty "The end..."
                elif wanna_die==False:
                    empty "{i} There is no way I'm going out like this..{/i}"
                    empty "{i} I have to get out of here..{/i}"
                    empty "{i} I have to find out who she is..{/i}"
                    narrator "You try to get up but you are too weak to do anything.."
                    narrator "You muster up all your strength into a loud cry."
                    you "MOM!! PLEASE HELP ME!!"
                    narrator "Your mom hears you and runs towards the washroom."
                    mom "WHAT HAPPENED?? ARE YOU OKAY??"
                    narrator "Your mom sees you on the floor.."
                    mom "OH MY GOD AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!"
                    scene bg ambulance with fade
                    narrator "Your neighbours hear the screams and quickly dial 911.."
                    narrator "An anbulance arrives and you are rushed to the hospital.."
                    scene bg hospital with fade
                    doctor "He has a concussion and a few broken bones.."
                    doctor "We have to perform an immediate surgery to save his life.."
                    mom "Please do whatever you can to save him.. please.. please.."

                    narrator "The doctor and his team start the surgery without any delay.."
                    narrator "Your mom is praying to god for you.."
                    narrator "You are put under anesthesia and you slowly lose the little bit of consciousness you still had.."

                    scene bg park with fade
                    empty "{i} Where.. Where am I...{/i}"
                    mystery 'Hello there..'
                    you "Huh?? Who's there??"
                    mystery "It's me duhh"
                    you "Wait.. how do you know me??"
                    empty "{b} Pat! Thump!!{/b}"
                    narrator "She pats your head angrily"
                    mystery "How do you not remember me.. We've known each other for so long.."
                    you "Oww oww.."
                    you "Hitting me isn't going to help! I still dont remember who you are.."
                    mystery "You idiot.. I thought you were smarter than this.."
                    mystery " My name is .."
                    mystery "D- y*u r-me-b-r -* n0*?"
                    narrator "She tries to say her name but you don't understand what she is saying.."
                    narrator "Her voice starts to go lower and the words start to slur.."
                    narrator "You feel a sharp pain in your head and you collapse on the ground"
                    # play thump sound
                    empty "... ... ..."
                    scene bg hospital with fade
                    narrator 'The doctor and your mom are talking to each other '
                    doctor "The operation was a success he should wake up anytime soon."
                    mother "Ohh thank god.. thank you so much doctor.. I'm ever so grateful.."
                    doctor 'He should be fine but he might have some memory loss..'
                    doctor "His brain was damaged pretty badly.. so his words might be slurry or what he's saying might not make sense.."

                    narrator "Your mom notices you moving your eyes"
                    mom "[player]? Are you awake?? Can you hear me??"
                    you "Mom? Where am I?? What happened??"
                    mom "OHH my god dear.. you are awake!!"
                    mom "You had me so worried thank god you're okay.."
                    you "What happened?? Why am I here??"

                    scene bg shower with fade
                    mom "You had an accident in the shower! You slipped and fell and hit your head on the wall.."
                    mom "Thank god you're okay now.."
                    narrator 'You try to move around but the doctor stops you..'
                    doctor "Don't try to move around yet.. You're hurt bad you need to let your body heal.."

                    you "But.. but I have to go to the Airport!"
                    mom "Why'd you want to go to the airport dear?"
                    you "You told me.. [mystery] is leaving today.. I have to see her off.. no matter what.."
                    mom "[mystery] ?? Who's that??"
                    you "You were the one that told me I had to go see mystery off at the airport today.."
                    mom "I never said that dear.. You've hurt your head.. you need to rest and recover.."
                    narrator "The doctor whispers to your mom.."
                    doctor "{i}You don't need to worry about it. He's having some memory mismatches. A good night rest and he'll be all fine tomorrow.{/i}"
                    mother "{i} Oh thank you doctor.. I hope he gets better as soon as possible {/i}"
                    narrator "Your mom looks at you and smiles thinking you didn't hear the two of them.. but you heard everything.."

                    empty "{i}Memory loss?? What are they talking about{/i}"
                    mom "You need to rest dear. Sleep for a while, while I chop up some apples for you to eat."
                    you "I don't understand.. I clearly remember you telling me about [mystery].."
                    mom "You hurt your head bad and lost a lot of blood dear.. take rest for now you'll be all fine tomorrow.."
                    you "If you say so mom.."

            if remember==True:
                empty "{i} I still can't stop thinking about her.. who is she?? {/i}"
                empty "{i}I shouldn't have lied to mom about knowing who she was..{/i}"
                empty "{i} It just complicated things even more..{/i}"
                empty "{i} Is [unknown] even the same age as me.. or is she a friend of my mom's??{/i}"
                empty "{i} I don't know.. The way my mom told me about her made me feel like she was someone I am supposed to know..{/i}"
                empty "{i} I'll go ask mom about her..{/i}"

                narrator "You try to step out of the shower but suddenly.."
                empty "{b}THUD!!{/b}"
                # play thud sound
                narrator "You slip on the shower and fall on your back spraining your ankle in the process."
                you "OWWWWW!! THAT HURTS BADD"
                narrator "Your mom hears you and runs towards the washroom."
                mom "WHAT HAPPENED?? ARE YOU OKAY??"
                you "I slipped and sprained my ankle.. I can't get up.."
                mom "DON'T I TELL YOU ENOUGH TIMES TO TAKE MORE CARE OF YOURSELF WHILE IN THE SHOWER??"
                mom "... ...Can you walk?"
                you "I don't think I can.."
                mom "{i}Sigh..{/i} Let me help you get out.."
                narrator "Your mom helps you get out of the shower and helps you to your bed.."
                narrator "She helps you get comfortable and brings ice from the fridge and puts it on your ankle.."
                narrator "You were about to ask her about [mystery] but she suddenly interrupts you.."
                mom "How'll you be able to go to the airport now?? [mystery] will be so sad.."
                mom "This better teach you to be more careful in the shower from now on.."
                you "Yeah.. I know mom.. I'm sorry.."
                mom "It's okay dear.. rest in bed for now.."
                mom "I'll go to the airport alone and see [mystery] off.. I hope she'll understand how dumb you are and what happened to you.."
                you "Yeah mom.. I hope so too.."
                mom "Now go sleep for a while and take care of yourself.."

                narrator "Your mom leaves for the airport and you're left alone in the room.."
                you "I wonder who [mystery] is.. I wish I could go see her..."
                you "Guess I'll ask mom to tell me who she is when she returns back home.."

                narrator "Your ankle stars hurting again and you decide to sleep for a while.."
                empty "ring.. ring.. ring..ring.."
                narrator "You wake up to the sound of your phone ringing.."
                narrator "You check your phone and see that it's your neighbor calling you.."
                you "Hello??"
                neighbor "{i}panting..{/i} huh.. hahhh.."
                you "Are you okay?? What happened??"
                neighbor "I.. I don't know how to tell you this.. {i} panting..{/i} Your mom.. Your mom.."
                you "What?? What happened to mom?? Is she okay???"
                neighbor "She.. she got into an accident.. She's in the hospital right now.. The doctors are saying she's in critical condition.. They told me.. told me I should inform.. inform you.."
                you "Oh my god.. Oh my god.. I have to come.. I'm coming right now.."
                narrator "You quickly get up.. not caring about your ankle and rush straight to the hospital.."
                narrator "You see the doctor there and decide to talk to him.."
                you "Doctor.. How is my mom doing?? Is she going to be okay??"
                doctor "Your mom is in critical condition right now.. We're trying our best to save her but I can't say for sure if she'll make it.."
                you "Please.. Please do whatever you can to save her.. She's the only family I have left.. please.."
                doctor "I understand.. We'll do our best to save her.."
                narrator "You wait in the hospital for a while.."
                if wanna_die==True:





        "No, I don't want to take a shower..":
            empty"{i} I don't really feel like taking a shower.. guess I'll skip it.. {/i}"
            narrator "You decide to skip the shower and just rest for a while.."
            narrator "You go back to your bed and lay down for a while.."

            if remember==False:
                empty "{i} I still can't stop thinking about her.. who is she?? {/i}"
                empty "{i} I wished mom would just tell me already.. but I guess she thinks I'm just messing with her..{/i}"
                empty "{i} Let me dose off for a while.. maybe I'll see her in my dream again..{/i}"

                mom "[player], are you just going to lay there all day??"
                mom "Lets go it's time to go to the airport.."

                narrator "You wake up to the sound of your mom yelling.."
                you "Yeah.. I'm getting up.. Let's go."
                narrator "You get up put your nice clothes on and head out to the airport with your mom.."
                mom "I guess we arrived too early.. we have to wait for a while.."
                narrator "You and your mom wait for a while for [mystery] to arrive.."
                mom "Did i get the timing wrong? I thought the flight left at 9:00 am.. Oh my.. was it pm instead.."
                you "I don't know.. I don't remember anything about the flight.."
                narrator "Your mom looks at you and sighs.."
                mom "Honey I know it's early in the morning and you're still half asleep but don't joke around like that!"
                mom "I know you must be sad but you shouldn't behave like this! You ought to give [mystery] a proper goodbye.."

                you "Okay mom.."
                narrator "You and your mom wait for a while longer but [mystery] was nowhere in sight"
                mom "Guess I did get the timing wrong.. I thought the flight left at 9:00 am.. Oh my.. I guess it was pm instead.."
                you "{i}Sigh.. {/i} Let's return back there's no point in waiting here.."
                mom "Guess you are right.. Let's go shopping for a while and head back home."

                narrator "It was already noon by the time you left the airport.."
                narraotor "You and your mom went shopping for a while.. atleast it felt like a while.."

                narrator "You and your mom head back home.."
                narrator "You reached back home and saw that it was already 8:00 pm.. You had been shopping for 8hours straight.."

                narrator "You go to your room to rest for a while.."
                narrator "Since it was already very late and you had eaten a ton while shipping you decide to doze off.."
                narrator "You quickly fell asleep and you had a dream about [mystery] again.."
                narrator "And it went like..."
                jump start
            elif remember==True:

                empty "{i} I lied to mom about knowing who [mystery] was.. but who is she?? {/i}"
                empty "{i} I can't stop thinking about her.. Should I maybe just ask mom?.. {/i}"
                empty "{i} No.. I don't think I should ask her.. She'll probably think I'm insane..{/i}"
                empty "{i} Let me dose off for a while.. maybe I'll see her in my dream again..{/i}"

                mom "[player], are you just going to lay there all day??"
                mom "Lets go it's time to go to the airport.."

                narrator "You wake up to the sound of your mom yelling.."
                you "Yeah.. I'm getting up.. Let's go."
                narrator "You get up put your nice clothes on and head out to the airport with your mom.."
                mom "I guess we arrived too early.. we have to wait for a while.."
                narrator "You and your mom wait for a while for [mystery] to arrive.."
                mom "Did i get the timing wrong? I thought the flight left at 9:00 am.. Oh my.. was it pm instead.."
                you "Mom.. I lied to you.. I don't know who [mystery] is.."
                narrator "Your mom looks at you and sighs.."
                mom "Honey I know it's early in the morning and you're still half asleep but don't joke around like that!"
                mom "I know you must be sad but you shouldn't behave like this! You ought to give [mystery] a proper goodbye.."

                you "Okay mom.."
                narrator "You and your mom wait for a while longer but [mystery] was nowhere in sight"
                mom "Guess I did get the timing wrong.. I thought the flight left at 9:00 am.. Oh my.. I guess it was pm instead.."
                you "{i}Sigh.. {/i} Let's return back there's no point in waiting here.."
                mom "Guess you are right.. Let's go shopping for a while and head back home."

                narrator "It was already noon by the time you left the airport.."
                narraotor "You and your mom went shopping for a while.. atleast it felt like a while.."

                narrator "You and your mom head back home.."
                narrator "You reached back home and saw that it was already 8:00 pm.. You had been shopping for 8hours straight.."

                narrator "You go to your room to rest for a while.."
                narrator "Since it was already very late and you had eaten a ton while shipping you decide to doze off.."
                narrator "You quickly fell asleep and you had a dream about [mystery] again.."
                narrator "And it went like..."
                jump start




    return


label remember_route:
    you "How could i even forget about [mystery].. I've known her for ages.."
    you "It's just sad.. sad to see her go.."
    return


label forgot_route:
    you "Who is [mystery]"
    mom "What do you mean you don't know who [mystery] is? She has been with you since you were born!!"
    you "Since I was born?? I don't remember anything about her.."

    mom "Stop joking around with me and get up before I get mad.. I have other works to attend to.."
    mom "The flight leaves at 9:00 and we have to leave in an hour.."

    return
