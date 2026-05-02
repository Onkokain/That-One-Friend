label start:
    # play bg music eerie
    scene bg black
    with fade
    death "Have you ever {i}wished{/i} you were never born.. or wished you could {color=#444444}{b}{size=+6}die{/size}{/b}{/color} without any {i}consequences{/i}.."
    menu:
        "Yes..":
            you "Yes.. {b}I have{/b}.."
            death "I know how you {i}feel{/i}.."
            $ wanna_die=True
        "No..":
            you "No.. Why would I ever {i}wish{/i} that??"
            death "Well.. I wish I could say the same for {b}myself{/b}.."
            $ wanna_die=False
        "I don't know..":
            you "I don't know.. I have {b}never{/b} ever thought about that before.."
            death "{i}Nobody{/i} does for certain dear.."
            $ wanna_die=False
    #stop bg music eerie and play bg music default at park
    scene bg sunset with fade
    mystery "Look at the setting {color=#ff5e3a}sun{/color}. it looks so {color=#ffb6c1}beautiful{/color}.."
    mystery "I {i}wish{/i} I could stay with you like this {u}forever and ever{/u}.."

    scene bg park with fade
    mystery "Lets {size=+6}marry{/size} when we get older okay?"
    you "{i}Yeah...{i} I'll {b}{u}always{/u}{/b} be with you, {size=+4}no matter what{/size}."
    mystery "I {b}know{b} you will.. I'm {i}sure{/i} you will.."
    you "I {b}{u}will{/u}{/b}.. no matter what..."
    mystery "{size=+2}{color=#ffb6c1}I love y---{/color}{/size}"
    empty "... ... ..."
    empty "... ... ..."
    # bg music fades out and alarm starts playing
    scene bg bed
    with fade
    empty "{b}{size=+4}buzz.. buzz.. buzz.. buzz..{/size}{/b}"
    speaker "Your alarm rings {b}loudly{b}, waking you up from sleep."
    you "{i}grunting..{/i} Huh what?? Was I in a dream?"
    you "Who was that? I {b}don't{/b} remember anything about her..."
    you "Was she  about to say... {color=#ffb6c1}'I love you'{/color}??"
    you "That was a {i}strange{/i} {b}dream{/b}.. strange indeed.."
    you "I {i}wish{/i} I knew who {i}she{/i} was.. I wish I could get the {i}chance{/i} to see her again.."
    empty "... ... ..."
    # turning off alarm sound
    scene bg room
    with fade

    speaker "It was an early summer morning.."
    speaker "You wake up to the sound of the alarm"
    speaker "Your mom hears you move around in the bed and asks you to get up."
    # start playing tap water sound
    scene bg kitchen
    with fade
    speaker "She is washing dishes and you hear the sound of the water flowing from the tap clearly.."
    # stop playing tap water sound
    speaker "You hear her but you don't want to get up.. not yet.. not until you figure out who that girl was.."
    speaker "Your mom {b}shouts{b} again.."
    mom "{b}{i}You..?{/i}{/b} get up {b}right now!{/b}"
    speaker "Wait.. What was your {b}name{/b} again?"

    $ player = renpy.input("What is your name?")
    $ player = player.strip()
    $ player = player if player else 'Brandon'

    # water flowing music starts to play
    mom "[player], get up {b}now{/b}! It's already 7:00 do you plan on sleeping all day?"
    # water flowing music fades out
    scene bg bed with fade
    speaker "Your mom bolts into your room and asks you to get up.."
    mom "I said..{size=+11}Wake up{/size} [player]. It's already early in the morning, you don't want to sleep {b}all day{/b}, {i}do you{/i}?"
    you "No mom waitt, I'll get up {u}{i}soon{/i}{u}!"
    mom "Today is an {u}important{/u} day for you. Don't forget."
    you "{b}{size=+5}Important{/size}{/b}? how is today important??"
    mom "Did you forget.. you have to see [mystery] off at the {i}Airport{/i} today."
    mom "She's leaving today and {i}I think{/i} her flight leaves at 9:00 am. So we have to leave in around an hour.."
    you " [mystery]?? Who's that??"
    mom "{i}Sigh....{/i} {b}Stop{/b} joking around with me and get up.."
    mom "Are you telling me that you forgot about [mystery] {b}{size=+3}before{/size}{/b} she even left?"
    # eerie bg music starts playing
    menu:
        "How could i ever forget about [mystery]..":
            $ remember = True
            you "How could i even forget about [mystery].. I've known her for ages.."
            you "It's just sad.. sad to see her go.."
        "I really don't know who [mystery] is..":
            $ remember= False
            you "Who is [mystery]"
            mom "What do you mean you don't know who [mystery] is? She has been with you since you were born!!"
            you "Since I was born?? I don't remember anything about her.."

            mom "Stop joking around with me and get up before I get mad.. I have other works to attend to.."
            mom "The flight leaves at 9:00 and we have to leave in an hour.."
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
            speaker "You take off your clothes and step into the shower.."

            if remember==False:
                empty "{i} I still can't stop thinking about her.. who is she?? {/i}"
                empty "{i} How do i even know her...{/i}"
                empty "{i} Mom told me that she has been with me since I was born.. but how do i not remember who she is... {/i}"
                empty "THUD!!"
                you "OWWWWW!!"
                speaker "You slip on the wet floor and hit your head on the wall.."
                speaker "You touch your head... there's a lot of blood on your hands.."
                speaker "Your breathing gets slower..."
                if wanna_die==True:
                    empty "{i} I guess this is it for me.. {/i}"
                    empty "{i} I hope I can see her again.. {/i}"

                    speaker 'You slowly lose yourself..'
                    speaker 'The blood from your head starts to pool around you..'
                    speaker 'You slowly lose consciousness...'
                    speaker 'Surrounded by the memories of her... You die..'
                    speaker 'Die in vain...'
                    empty "The end..."
                elif wanna_die==False:
                    empty "{i} There is no way I'm going out like this..{/i}"
                    empty "{i} I have to get out of here..{/i}"
                    empty "{i} I have to find out who she is..{/i}"
                    speaker "You try to get up but you are too weak to do anything.."
                    speaker "You muster up all your strength into a loud cry."
                    you "MOM!! PLEASE HELP ME!!"
                    speaker "Your mom hears you and runs towards the washroom."
                    mom "WHAT HAPPENED?? ARE YOU OKAY??"
                    speaker "Your mom sees you on the floor.."
                    mom "OH MY GOD AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!"
                    scene bg ambulance with fade
                    speaker "Your neighbours hear the screams and quickly dial 911.."
                    speaker "An anbulance arrives and you are rushed to the hospital.."
                    scene bg hospital with fade
                    doctor "He has a concussion and a few broken bones.."
                    doctor "We have to perform an immediate surgery to save his life.."
                    mom "Please do whatever you can to save him.. please.. please.."

                    speaker "The doctor and his team start the surgery without any delay.."
                    speaker "Your mom is praying to god for you.."
                    speaker "You are put under anesthesia and you slowly lose the little bit of consciousness you still had.."

                    scene bg park with fade
                    empty "{i} Where.. Where am I...{/i}"
                    mystery 'Hello there..'
                    you "Huh?? Who's there??"
                    mystery "It's me duhh"
                    you "Wait.. how do you know me??"
                    empty "{b} Pat! Thump!!{/b}"
                    speaker "She pats your head angrily"
                    mystery "How do you not remember me.. We've known each other for so long.."
                    you "Oww oww.."
                    you "Hitting me isn't going to help! I still dont remember who you are.."
                    mystery "You idiot.. I thought you were smarter than this.."
                    mystery " My name is .."
                    mystery "D- y*u r-me-b-r -* n0*?"
                    speaker "She tries to say her name but you don't understand what she is saying.."
                    speaker "Her voice starts to go lower and the words start to slur.."
                    speaker "You feel a sharp pain in your head and you collapse on the ground"
                    # play thump sound
                    empty "... ... ..."
                    scene bg hospital with fade
                    speaker 'The doctor and your mom are talking to each other '
                    doctor "The operation was a success he should wake up anytime soon."
                    mom "Ohh thank god.. thank you so much doctor.. I'm ever so grateful.."
                    doctor 'He should be fine but he might have some memory loss..'
                    doctor "His brain was damaged pretty badly.. so his words might be slurry or what he's saying might not make sense.."

                    speaker "Your mom notices you moving your eyes"
                    mom "[player]? Are you awake?? Can you hear me??"
                    you "Mom? Where am I?? What happened??"
                    mom "OHH my god dear.. you are awake!!"
                    mom "You had me so worried thank god you're okay.."
                    you "What happened?? Why am I here??"

                    scene bg shower with fade
                    mom "You had an accident in the shower! You slipped and fell and hit your head on the wall.."
                    mom "Thank god you're okay now.."
                    speaker 'You try to move around but the doctor stops you..'
                    doctor "Don't try to move around yet.. You're hurt bad you need to let your body heal.."

                    you "But.. but I have to go to the Airport!"
                    mom "Why'd you want to go to the airport dear?"
                    you "You told me.. [mystery] is leaving today.. I have to see her off.. no matter what.."
                    mom "[mystery] ?? Who's that??"
                    you "You were the one that told me I had to go see mystery off at the airport today.."
                    mom "I never said that dear.. You've hurt your head.. you need to rest and recover.."
                    speaker "The doctor whispers to your mom.."
                    doctor "{i}You don't need to worry about it. He's having some memory mismatches. A good night rest and he'll be all fine tomorrow.{/i}"
                    mom "{i} Oh thank you doctor.. I hope he gets better as soon as possible {/i}"
                    speaker "Your mom looks at you and smiles thinking you didn't hear the two of them.. but you heard everything.."

                    empty "{i}Memory loss?? What are they talking about{/i}"
                    mom "You need to rest dear. Sleep for a while, while I chop up some apples for you to eat."
                    you "I don't understand.. I clearly remember you telling me about [mystery].."
                    mom "You hurt your head bad and lost a lot of blood dear.. take rest for now you'll be all fine tomorrow.."
                    you "If you say so mom.."
                    # main ending 1
                    speaker "Your mom and the docotor leave the room and you're left all alone in the hospital room.."
                    empty "{i} Was that.. all just a dream.. {/i}"
                    empty "{i}Does {mystery} exist....{/i}"
                    empty "{i}Was it all just a dream..{/i}"
                    empty "{i}No... That can't be..{/i}"
                    empty "{i}I can't think straight..{/i}"
                    empty "{i}Let me try sleeping for now..{/i}"
                    speaker "You try not to think about anything and rest for a while.."
                    speaker "You quickly fall asleep due to some of the anaesthesia still being in your system..."

                    scene bg park with fade
                    you "Huh?? Where am I??"
                    you "I was in the hospital right before this.. how did I get here.."
                    mystery "London bridge is falling down, falling down, falling down....."
                    mystery "London bridge is falling down, my fair lady.."
                    you "Who.. Who's there... Who's singing that.."
                    mystery "Do you not remember me.."
                    mystery "You promised.. promised to stay with me forever and ever.."
                    you "I don't know who you are.."
                    mystery "Guess you really don't remember me.."
                    speaker "You hear a loud hissing sound and fell on your knees covering your ears.."
                    speaker "The loud hissing sound causes you to lose conciousness.."
                    you "AHHHH! WHAT IS THAT SOUND??"
                    empty "{i}Huhh.. Where am I.. This is the.. hospital?{/i}"
                    speaker "Your scream was heard by your mother who was waiting just outside the room.."
                    mom "What happened?? Are you okay??"
                    you "I don't know.. I just had a bad dream..."
                    mom "What was the dream about??"
                    you "It was about [mystery].. The girl you told me about..."
                    mom "Honey, I don't know who you're talking about..."
                    empty "{i}What is happening with me.. Why do i remember my mom telling me about [mystery]...{/i}"
                    speaker "You look at your mom and say.."
                    menu:
                            "It's nothing mom I'm fine..":
                                $ in_dream=False
                                you "It's nothing mom.. I'm fine.. I just had a bad dream that's all.."
                                mom "Okay dear.. If you say so.."
                                empty "{i} I'm so lost what is this supposed to mean..{/i}"
                                speaker "You  decide to rest for a while again and think about it tomorrow.."
                                speaker "With an uneasy mind you take a while but eventually dose off.."
                                empty "... ... ..."
                                empty "... ... ..."
                                empty "{i}I feel like I saw something in my dream.. but.. I don't remember{/i}"

                                ##########
                            "How do you not know who [mystery] is.. You're the one who told me about her..":
                                $ in_dream=True
                                you "How do you not know who [mystery] is?? You're the one who told me about her.."
                                mom "[player]... This is not the time for this.."
                                you "Mom.. please just tell me what you know about her.. please.."
                                mom "{i}Sigh...{/i}"
                                you "Mom.. please.."
                                mom "[player]... You're not who you truly think you are.. there is something.. something special about you.."
                                you "What do you mean mom-"
                                speaker "Before you could complete your sentence your mom runs out.."
                                speaker "You try to follow her; running towards the stairs.."
                                speaker "Your mom was trying to go down the stairs but.."
                                speaker "She slips and falls.."
                                speaker "Blood pouring out of head..."
                                speaker "Doctors rush towards her.. but it's already too late..."
                                speaker "Your mom passes away in that instant...."
                                you "MOMM!! Mom...  What happened... What did I do.."
                                speaker "You fell on your knees looking at her dead body lying on the ground near the stairs.."
                                speaker "There is nothing you can do.."
                                empty "{i}What just happened.... What did she mean.. by me being special..{/i}"
                                empty "{i}I can't think straight...{/i}"
                                speaker "On your knees and crying you succumb to the pain and faint.."
                                empty "... ... ..."
                                empty "... ... ..."
                                speaker "You wake up.. back in the hospital bed.."
                                you "Where.. where am I.. was that a dream.."
                empty "... ... ..."
                mom "Goodmorning honey."
                if in_dream:
                    you "Mom??! Are you okay??"
                    mom "What happened honey.. Another bad nightmare??"
                    empty "{i}Thank god.. Guess it was a dream...{/i}"
                    you "No mom I'm fine it was nothing.."
                    mom "If you say so honey.."
                else:
                    you "Goodmorning Mom."
                    mom "Did you sleep well?"
                    you "Yeah.. I think I had a dream but I don't remember what it was.."
                    mom "Don't worry honey it was probably nothing important!"
                    mom "Yeah I think so too..."






            if remember==True:
                empty "{i} I still can't stop thinking about her.. who is she?? {/i}"
                empty "{i}I shouldn't have lied to mom about knowing who she was..{/i}"
                empty "{i} It just complicated things even more..{/i}"
                empty "{i} Is [mystery] even the same age as me.. or is she a friend of my mom's??{/i}"
                empty "{i} I don't know.. The way my mom told me about her made me feel like she was someone I am supposed to know..{/i}"
                empty "{i} I'll go ask mom about her..{/i}"

                speaker "You try to step out of the shower but suddenly.."
                empty "{b}THUD!!{/b}"
                # play thud sound
                speaker "You slip on the shower and fall on your back spraining your ankle in the process."
                you "OWWWWW!! THAT HURTS BADD"
                speaker "Your mom hears you and runs towards the washroom."
                mom "WHAT HAPPENED?? ARE YOU OKAY??"
                you "I slipped and sprained my ankle.. I can't get up.."
                mom "DON'T I TELL YOU ENOUGH TIMES TO TAKE MORE CARE OF YOURSELF WHILE IN THE SHOWER??"
                mom "... ...Can you walk?"
                you "I don't think I can.."
                mom "{i}Sigh..{/i} Let me help you get out.."
                speaker "Your mom helps you get out of the shower and helps you to your bed.."
                speaker "She helps you get comfortable and brings ice from the fridge and puts it on your ankle.."
                speaker "You were about to ask her about [mystery] but she suddenly interrupts you.."
                mom "How'll you be able to go to the airport now?? [mystery] will be so sad.."
                mom "This better teach you to be more careful in the shower from now on.."
                you "Yeah.. I know mom.. I'm sorry.."
                mom "It's okay dear.. rest in bed for now.."
                mom "I'll go to the airport alone and see [mystery] off.. I hope she'll understand how dumb you are and what happened to you.."
                you "Yeah mom.. I hope so too.."
                mom "Now go sleep for a while and take care of yourself.."

                speaker "Your mom leaves for the airport and you're left alone in the room.."
                you "I wonder who [mystery] is.. I wish I could go see her..."
                you "Guess I'll ask mom to tell me who she is when she returns back home.."

                speaker "Your ankle stars hurting again and you decide to sleep for a while.."
                empty "ring.. ring.. ring..ring.."
                speaker "You wake up to the sound of your phone ringing.."
                speaker "You check your phone and see that it's your neighbor calling you.."
                you "Hello??"
                neighbor "{i}panting..{/i} huh.. hahhh.."
                you "Are you okay?? What happened??"
                neighbor "I.. I don't know how to tell you this.. {i} panting..{/i} Your mom.. Your mom.."
                you "What?? What happened to mom?? Is she okay???"
                neighbor "She.. she got into an accident.. She's in the hospital right now.. The doctors are saying she's in critical condition.. They told me.. told me I should inform.. inform you.."
                you "Oh my god.. Oh my god.. I have to come.. I'm coming right now.."
                speaker "You quickly get up.. not caring about your ankle and rush straight to the hospital.."
                speaker "You see the doctor there and decide to talk to him.."
                you "Doctor.. How is my mom doing?? Is she going to be okay??"
                doctor "Your mom is in critical condition right now.. We're trying our best to save her but I can't say for sure if she'll make it.."
                you "Please.. Please do whatever you can to save her.. She's the only family I have left.. please.."
                doctor "I understand.. We'll do our best to save her.."
                speaker "You wait in the hospital for a while.."
                if wanna_die==True:
                    speaker 'The doctor comes out of the operation room..'
                    speaker "He walks up to you with a report on his hand.."
                    you "Doctor.. Is my mom okay?? What happened to the operation.."
                    doctor "The operation was a success but.."
                    you "But?? Is my mom okay?? Please tell me doctor.."
                    doctor "The operation was a success but your mom's legs were damaged badly.. She won't be able to walk ever again.."

                    speaker 'You feel a sharp pain in your heart..'
                    speaker "Your eyes give out and you faint on the spot.."
                    death "Hello there.."
                    you "Huh?? Who's there??"
                    death "I'm **********.."
                    you "Huh who're you??"
                    death "I'm the one who asked you the question in the beginning.."
                    death "It's a pity that you wished you were never born or wished that you'd die.."
                    death "I give you this opportunity to choose for thy are in front of the bringer of death himself.."
                    death "Your life for your mom's."
                    death "That's the offer I have for you."
                    death "Now it's up to you to decide."
                    death "Do you wish to die for the sake of someone else?"
                    menu:
                        "Yes..":
                            you  "Yes.. Please save my mom.."
                            death "You are a kind soul.."
                            death "May you rest in peace.."
                            speaker "You sacrificed yourself for your mom's sake"
                            speaker "You never woke up again.."
                            speaker "Your mother's legs were suddenly healed.."
                            speaker "She woke up and was able to walk again.."
                            speaker "You never figured out who [mystery] was did you..."
                            speaker "The end..."

                        "No..":
                            you "No.. I don't want to die.."
                            death "I see.."
                            death "Lying to death was not a good idea.."
                            death "You are a coward.."
                            death "You will never see your mom again.. For I am healing her and taking your life as tribute for your cowardice.."
                            you "No.. Please.. I want to live.. Please don't do this.."
                            death "She doesn't deserve a child like you.. She'll never remember you.."
                            speaker "Death ignores your pleas and takes your life away from you.."
                            speaker "Your soul leaves your body and your mom forgets you ever existed.."
                            speaker "She wakes up and is able to walk again.."
                            speaker "She lives the rest of her life happily without you.."
                            speaker "Your death was in vain.. You disappointed death himself.. You could never figure out who [mystery] was could you..."
                            speaker "Hope you'll learn not to be a coward in your next life.."
                            speaker "The end..."
                elif wanna_die==False:
                    speaker 'The doctor comes out of the operation room..'
                    speaker "He walks up to you with a report on his hand.."
                    you "Doctor.. Is my mom okay?? What happened to the operation.."
                    doctor "I'm sorry to inform you that.."
                    you "What?? Please tell me doctor.."
                    doctor "I'm so sorry we couldn't save her.. Your mom passed away during the operation.."
                    you "No.. No.. Please.. Please save her.. I want to see her again.. Please don't do this to me.."
                    doctor "I'm sorry I can't help you anymore.."
                    speaker "You break down in tears and scream in agony.."
                    speaker "You are devastated by the loss of your mom.."
                    speaker "You hear a voice calling out to you.."
                    death "Hello there.."
                    you "Huh?? Who's there??"
                    death "Now that your mom is gone.. Do you still don't wish you were never born or you could die without any consequences.."
                    you "Who.. who are you.."
                    death "I'm the one who asked you the question in the beginning.."
                    death "Now I give you the opportunity to answer the same question again.."
                    death "Do you wish you were never born or wish you could die without any consequences.."
                    window hide
                    menu:
                        "Yes..":
                            you "Yes.. I have.."
                            death "Guess opinions do change.. don't they.."
                            death "I can't save your mom anymore but I can take you with me.."
                            speaker "You accept death's offer and take your own life.."
                            speaker "You lay down and close your eyes for the last time.."
                            speaker "Your soul leaves your body and you are with death now.."
                            speaker "You didn't get to figure out who [mystery] was but you'll atleast be with your mom again.."
                            speaker "The end..."
                        "No..":
                            you "No.. I don't.. I still have to figure out who [mystery] is.. I have to find who my mom was talking about.."
                            death "Some choices are tough to make... but you seem to have made up your mind.."
                            death "I can't save your mom but I'll give you more time to find out who [mystery] is.."
                            death "You have my blessing.."
                            speaker "You hear someone whisper into your ears.."
                            empty "{i}WheN you travEl bAck in time, youR present becomes Your past and yOur past becomes yoUr future But yoU can'T change your past and make it affect the Future but you cAn change the pResent by changing the future..{/i}"
                            # main ending 1
                    window show









        "No, I don't want to take a shower..":
            empty"{i} I don't really feel like taking a shower.. guess I'll skip it.. {/i}"
            speaker "You decide to skip the shower and just rest for a while.."
            speaker "You go back to your bed and lay down for a while.."

            if remember==False:
                empty "{i} I still can't stop thinking about her.. who is she?? {/i}"
                empty "{i} I wished mom would just tell me already.. but I guess she thinks I'm just messing with her..{/i}"
                empty "{i} Let me dose off for a while.. maybe I'll see her in my dream again..{/i}"

                mom "[player], are you just going to lay there all day??"
                mom "Lets go it's time to go to the airport.."

                speaker "You wake up to the sound of your mom yelling.."
                you "Yeah.. I'm getting up.. Let's go."
                speaker "You get up put your nice clothes on and head out to the airport with your mom.."
                mom "I guess we arrived too early.. we have to wait for a while.."
                speaker "You and your mom wait for a while for [mystery] to arrive.."
                mom "Did i get the timing wrong? I thought the flight left at 9:00 am.. Oh my.. was it pm instead.."
                you "I don't know.. I don't remember anything about the flight.."
                speaker "Your mom looks at you and sighs.."
                mom "Honey I know it's early in the morning and you're still half asleep but don't joke around like that!"
                mom "I know you must be sad but you shouldn't behave like this! You ought to give [mystery] a proper goodbye.."

                you "Okay mom.."
                speaker "You and your mom wait for a while longer but [mystery] was nowhere in sight"
                mom "Guess I did get the timing wrong.. I thought the flight left at 9:00 am.. Oh my.. I guess it was pm instead.."
                you "{i}Sigh.. {/i} Let's return back there's no point in waiting here.."
                mom "Guess you are right.. Let's go shopping for a while and head back home."

                speaker "It was already noon by the time you left the airport.."
                speaker "You and your mom went shopping for a while.. atleast it felt like a while.."

                speaker "You and your mom head back home.."
                speaker "You reached back home and saw that it was already 8:00 pm.. You had been shopping for 8hours straight.."

                speaker "You go to your room to rest for a while.."
                speaker "Since it was already very late and you had eaten a ton while shipping you decide to doze off.."
                speaker "You quickly fell asleep and you had a dream about [mystery] again.."
                speaker "And it went like..."
                jump start
            elif remember==True:

                empty "{i} I lied to mom about knowing who [mystery] was.. but who is she?? {/i}"
                empty "{i} I can't stop thinking about her.. Should I maybe just ask mom?.. {/i}"
                empty "{i} No.. I don't think I should ask her.. She'll probably think I'm insane..{/i}"
                empty "{i} Let me dose off for a while.. maybe I'll see her in my dream again..{/i}"

                mom "[player], are you just going to lay there all day??"
                mom "Lets go it's time to go to the airport.."

                speaker "You wake up to the sound of your mom yelling.."
                you "Yeah.. I'm getting up.. Let's go."
                speaker "You get up put your nice clothes on and head out to the airport with your mom.."
                mom "I guess we arrived too early.. we have to wait for a while.."
                speaker "You and your mom wait for a while for [mystery] to arrive.."
                mom "Did i get the timing wrong? I thought the flight left at 9:00 am.. Oh my.. was it pm instead.."
                you "Mom.. I lied to you.. I don't know who [mystery] is.."
                speaker "Your mom looks at you and sighs.."
                mom "Honey I know it's early in the morning and you're still half asleep but don't joke around like that!"
                mom "I know you must be sad but you shouldn't behave like this! You ought to give [mystery] a proper goodbye.."

                you "Okay mom.."
                speaker "You and your mom wait for a while longer but [mystery] was nowhere in sight"
                mom "Guess I did get the timing wrong.. I thought the flight left at 9:00 am.. Oh my.. I guess it was pm instead.."
                you "{i}Sigh.. {/i} Let's return back there's no point in waiting here.."
                mom "Guess you are right.. Let's go shopping for a while and head back home."

                speaker "It was already noon by the time you left the airport.."
                narraotor "You and your mom went shopping for a while.. atleast it felt like a while.."

                speaker "You and your mom head back home.."
                speaker "You reached back home and saw that it was already 8:00 pm.. You had been shopping for 8hours straight.."

                speaker "You go to your room to rest for a while.."
                speaker "Since it was already very late and you had eaten a ton while shipping you decide to doze off.."
                speaker "You quickly fell asleep and you had a dream about [mystery] again.."
                speaker "And it went like..."
                jump start




    return


