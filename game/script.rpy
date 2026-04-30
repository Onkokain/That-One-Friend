label start:
    # play bg music eerie
    $ mystery = "???"
    scene bg black
    with fade
    empty "Have you ever wished you were never born.. or you could die without it affecting anyone else.."
    menu:
        "Yes..":
            mystery "I know how you feel.."
            $ wanna_die=True
        "No..":
            mystery "Well.. I wish I could say the same for myself.."
            $ wanna_die=False
        "I don't know..":
            mystery "Nobody does for certain dear.."
            $ wanna_die=False
    #stop bg music eerie and play bg music default at park
    scene bg park
    with fade

    mystery "Lets marry when we get older okay?"
    you "Yeah... I'll always be with you, no matter what."
    you "No matter what..."

    scene bg bed
    with fade

    you "Huh...? What?? Was I in a dream?"
    you "Who was that? I don't remember anything about her..."
    empty "... ... ..."

    scene bg black
    with fade

    narrator "It was an early summer morning.."
    narrator "You wake up to the sound of your mom washing the dishes in the kitchen."
    narrator "She hears you move around in the bed and asks you to get up."
    narrator "You hear her but you don't want to get up.. not yet.. not until you figure out who that girl was.."
    narrator "Your mom shouts again, 'You..? get up now!'"
    narrator "Wait.. What was your name again?"

    $ player = renpy.input("What is your name?")
    $ player = player.strip()
    $ player = player if player else 'Brandon'

    scene bg kitchen
    with fade

    mom "[player], get up now! It's already 7:00 do you plan on sleeping all day?"
    mom "Did you forget.. you have to see [mystery] off at the Airport today."
    mom "You didn't forget.. did you?"

    menu:
        "How could i ever forget about [mystery]..":
            $ remember = True
            call remember_route

        "Who is [mystery]":
            $ remember= False
            call forgot_route

        "... ... ...":
            $ remember= "default"
            call default_route

    mom "Now hurry up and get ready.. we have to leave to see her off soon.."

    scene bg washroom with fade

    empty"{i}I still cant stop thinking about her..{/i}"
    empty"{i} Who is [mystery].. is it the same person as in my dream??{/i}"
    empty"{i} Guess it's time to take a shower..{/i}"
    menu:
        "Take a shower":
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
                if wanna_die:
                    empty "{i} I guess this is it for me.. {/i}"
                    empty "{i} I hope I can see her again.. {/i}"

                    narrator 'You slowly lose yourself..'
                    narrator 'The blood from your head starts to pool around you..'
                    narrator 'You slowly lose consciousness...'
                    narrator 'Surrounded by the memories of her... You die..'
                    narrator 'Die in vain...'
                    empty "The end..."
                else:
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
                    doctor 'Don't try to move around yet.. You're hurt bad you need to let your body heal..'

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







        "Don't take a shower":
            empty"{i} I don't really feel like taking a shower.. guess I'll skip it.. {/i}"

    return


label remember_route:
    you "How could i even forget about [mystery].. I've known her for ages.."
    you "It's just sad.. sad to see her go.."
    return


label forgot_route:
    you "Who is [mystery]"
    mom "What do you mean you don't know who [mystery] is? She has been with you since you were born!!"
    you "Since I was born?? I don't remember anything about her.."

    narrator "Your mom walks in your room and sees you still asleep.."
    mom "Stop joking around with me and get up.."
    mom "The flight leaves at 9:00 and we have to leave in an hour.."

    return


label default_route:
    you "... ... ..."
    return
