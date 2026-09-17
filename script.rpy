define mc = Character("[mcname]", color="#a3573a")
define gabe = Character("Gabriel", color="#3f0303")
define haz = Character("Hazel", color="#FF6680")
define narrate = Character("")

default gabe_affection = 0
default hazel_affection = 0


# The game starts here.

label start:

    

    $ mcname = renpy.input("What is your name?", default = "Lottie", length=30)

    $ mcname = mcname.strip()


    if mcname == "":
        $ mcname = "Lottie"

    $ slowdissolve = Dissolve(2)

    scene train morning with slowdissolve:
        zoom 0.75

    stop music fadeout 2.0
    
    play music "trainday/pixel-playground-color-parade-main-version-25382-01-43.mp3" fadein 2.5

    mc "It's been 2 months since moving back home to help with the Cafe."

    mc "It feels so strange to be back, but also nothing is really even that different."

    mc "Well, except maybe the people."

    mc "When I came home I really didn't plan to be going on a date with one of my regulars, or heck even a date at all!"

    mc "I feel rusty! It's been so long! TwT"

    mc "Oh I should probably text them and let them know I'm on my way or something."


label choose_path:
  
    mc "Wait, who am I messaging again?"

    menu choose_character:
    
        "Hazel":
            jump hazel_chose
        "Gabriel":
            jump gabriel_chose

    label hazel_chose:

        mc "Oh yeah! Of course!"
        jump hazel_route

    label gabriel_chose:

        mc "Of course! How did I even forget!"
        jump gabriel_route
        

label hazel_route:
   
    mc "I can't believe I'm going on a date with my childhood friend!"
    mc "I dreamt of going out with her when I was younger haha."
    mc "Oh I think she just messaged me!"


    label hazel_phone:

        show hazel phone 1:
            xalign 1.0
            zoom 0.75
        with Dissolve(0.3)
        with Pause(1.5)
        

        menu hazel_phone_choice:

            "Hii! Almost there!!":
                $ hazel_affection += 1
                jump hazel_bubbly

            "Hello Hazel. I will be there soon.":
                $ hazel_affection -= 1
                jump hazel_formal

        
    label hazel_bubbly:
        
        show hazel phone opt 1:
            xalign 1.0
            zoom 0.75
        with Pause(1.5)
        jump hazel_woohoo
        
    
    label hazel_woohoo:

        show hazel phone response 1:
            xalign 1.0
            zoom 0.75
        with Pause(1.5)

        mc "Ah she's so cute!"

        jump hazel_cont_1

    label hazel_cont_1:

        show hazel phone cont 1:
            xalign 1.0
            zoom 0.75
        with Pause(1.5)

        mc "Of course she's lost, why am not surprised!"
        mc "It's kind of cute though hehe."
       
        hide hazel phone cont 1
        with dissolve
        mc "oh think I'm here!"

        jump hazel_aquarium

    label hazel_formal:

        show hazel phone opt 2:
            xalign 1.0
            zoom 0.75
        with Pause(1.5)
        jump hazel_relax

    
    label hazel_relax:

        show hazel phone response 2:
            xalign 1.0
            zoom 0.75
        with Pause(1.5)

        mc "Ah whoops..."

        jump hazel_cont_2

    label hazel_cont_2:

        show hazel phone cont 2:
            xalign 1.0
            zoom 0.75
        with Pause(1.5)

        mc "Of course she's lost, why am I not surprised!"
        mc "It's kind of cute though hehe."
       
        hide hazel phone cont 2
        with dissolve
        mc "oh I think I'm here!"

        jump hazel_aquarium



    label hazel_aquarium:

        stop music fadeout 1.5
        play music "audio/aquarium/hazel/23 - honeys waltz.mp3" fadein 1.5

        scene aqua finish with fade:
            zoom 0.77
            blur 4

        mc "Okay, wow. This place is WAYYY prettier than I remembered as a kid!"
        mc "but I should really focus on finding Haze-"

        show hazel neutral with vpunch:
            xpos 0.10
        haz "BOO!!"
        mc "AHHHH!"

        show hazel happy wink:
            xpos 0.10
        haz "You found me!! Hehe hi [mcname]."
        narrate "Hazel gave me a tight hug."
        haz "You're looking real pretty today!"

        menu hazel_compliment:
            
            "Thanks!":
                mc "Thanks Hazel! I tried my best haha."

                jump hazel_thanks

            "You look beautiful.":
                mc "Yeah well you look beautiful!"
                $ hazel_affection += 1

                jump hazel_complimented

            "I guess you look okay?":
                mc "Thanks. I guess you look okay today too?"
                $ hazel_affection -= 1

                jump hazel_just_okay

    label hazel_thanks:

        haz "No probs! I know how you love compliments hehe."

        jump hazel_wonder_around

    label hazel_complimented:

        haz "Yeah well, you're gorgeous! I win!"
        mc "I feel like I win here."

        jump hazel_wonder_around

    label hazel_just_okay:

        show hazel pout:
            xpos 0.10
        
        haz "Oh. Thanks? I guess?"

        jump hazel_wonder_around

    label hazel_wonder_around:

        show hazel neutral:
            xpos 0.10
        haz "So anyway! What do you wanna see first?"
        narrate "She asks me but she's already leading me around."
        narrate "At least we're holding hands."
        
        mc "Surprise me! I bet you know this place by heart, yeah?"
        show hazel wink:
            xpos 0.10
        haz "Even the new exhibits!"
        narrate "I laugh lightly at her antics."
        narrate "I'm not even surprised at her anymore."

        mc "It makes so much sense you're studying this stuff now."
        mc "I mean I swear in school you studied more about fish than you did actual subjects."  

        show hazel pout:
            xpos 0.10
        haz "I still passed!"

        show hazel happy:
            xpos 0.10
        haz "But yeah, I love it! Maybe in another life I was a fish."
        narrate "She drives the sentiment home by pursing her lips together to replicate how a fish looks."

        haz "Hey! If I were a fish what do you think I would be?"
        mc "It already sounds like you've given this a lot of thought haha."

        show hazel pout:
            xpos 0.10
        haz "Well duh! But I wanna know what you think!"

        menu hazel_what_fish:
            
            "A seabunny!":
                mc "I mean obviously Sea Bunny! You're adorable and bouncy!"
                $ hazel_affection += 1

                jump hazel_seabunny

            "Clownfish.":
                mc "Obviously a clownfish."

                jump hazel_clownfish
            
            "I dunno.":
                mc "I dunno, they're all just fish. What does it matter?"
                $ hazel_affection -= 1

                jump hazel_dunno

    label hazel_seabunny:
        
        show hazel neutral:
            xpos 0.10
        haz "You know they don't actually bounce right?"

        show hazel happy:
            xpos 0.10
        haz "But they are adorable!"
        haz "Did you know my tights are based off them?!"

        mc "Duh! I notice these little things about you!"

        show hazel embarrased:
            xpos 0.10
        
        haz "Hey no fair!"

        show hazel pout with dissolve:
            xpos 0.10
        
        haz "I'm supposed to be the best at complimenting!"
        
        jump hazel_look_around

    label hazel_clownfish:
        
        haz "Ha. Ha. You're sooooo funny!"
        haz "You're the clown here not me!"
        haz "You cl-clownfish!"

        mc "Oooh good comeback!"
        narrate "We both burst out laughing at eachother."
 
        jump hazel_look_around

    label hazel_dunno:

        show hazel sad:
            xpos 0.10
        
        haz "It's just for fun... No need to be mean..."
        narrate "She shakes herself slightly, as if she's shaking off what I said."

        jump hazel_look_around

    label hazel_look_around:

        show hazel neutral:
            xpos 0.10
        haz "Come on, let's look around some more!"

        hide hazel neutral with dissolve

        narrate "I turn to face the tank in front of me."
        mc "Woah! That is one ugly fish! I wonder what it's call-"

        haz "AHHHH!" with vpunch
        mc "Are you okay?!"

        show hazel happy:
            xpos 0.10
        
        haz "Stingrays! Look! Look!"
        narrate "Please... I'm begging you... stop scaring me."
        narrate "I should've know it would be something like this."
        narrate "God if it isn't cute how excited she gets though. I can feel my heart flutter at her smile."
        narrate "She grabs both my hands and practically bounces in excitement."

        haz "Did you know that Stingrays have no bones! It's all just cartilage!"
        haz "Just like sharks! Which makes sense cause they're related."

        show hazel neutral with dissolve:
            xpos 0.10
        haz "Oh and did you know that fossils date Stingrays back to 150 million years ago!"
        haz "Like the Jurassic period! With Dinosaurs!"

        show hazel happy with dissolve:
            xpos 0.10
        haz "Oh! Also some people even keep them as pets!"
        haz "And-"

        show hazel embarrased:
            xpos 0.10
        haz "Oh sorry, that was probably a lot right?"

        menu ramble:
            
            "Way too much!":
                mc "Uh yeah! That's a lot Hazel!"
                $ hazel_affection -= 1

                jump hazel_a_lot

            "Hey, no biggie.":
                mc "Hey, It's no biggie."

                jump hazel_no_biggie

            "Let's just calm down.":
                mc "Maybe... Let's just calm down a bit yeah?"
                $ hazel_affection -= 1

                jump hazel_calm_down

            "I love hearing you talk.":
                mc "Not at all. I love hearing you talk, especially when you're so passionate!"
                $ hazel_affection += 1

                jump hazel_talking
    
    label hazel_a_lot:

        show hazel sad:
            xpos 0.10
        
        haz "I'll just be quiet then..."

        jump hazel_ending_evaluation
    
    label hazel_no_biggie:

        show hazel neutral:
            xpos 0.10
        
        haz "Ah cool! Sorry still haha."

        jump hazel_final_cont

    label hazel_calm_down:

        show hazel pout:
            xpos 0.10
        
        haz "Sorry..."

        jump hazel_ending_evaluation

    label hazel_talking:

        show hazel embarrased:
            xpos 0.10
        
        haz "Wha- I-"

        show hazel happy blush with dissolve:
            xpos 0.10
        
        haz "God you really make my heart beat fast haha!"

        jump hazel_final_cont
    
    label hazel_final_cont:
        
        show hazel happy with dissolve:
            xpos 0.10
        
        haz "Hey! Come look at this with me!"

        hide hazel happy with dissolve

        narrate "She grabs my hand and leads me around again."
        narrate "Somehow she knows a fact about every fish we go up to."
        narrate "It only makes the date that more endearing."
        narrate "Plus I'm learning a lot!"
        narrate "Before we know it, it's dark and the aquarium is closing soon."

        mc "Hey, I had a lot of fun today!"

        jump hazel_ending_evaluation
      

    
label gabriel_route:

    mc "Ah! I'm nervous but also so excited!"
    mc "Oh, he just messaged me!"


    label gabriel_phone:

        show gabe phone 1:
            xalign 1.0
            zoom 0.75
        with Dissolve(0.3)
        with Pause(1.5)

        menu gabe_phone_choice:

            "Oh is that today?":
                $ gabe_affection -= 1
                jump gabe_opt_1

            "Hi! Sure thing!":
                $ gabe_affection += 1
                jump gabe_opt_2

    
    label gabe_opt_1:

        show gabe phone opt 1:
            xalign 1.0
            zoom 0.75
        with Pause(1.5)
        jump gabe_response_1

    label gabe_response_1:

        show gabe phone response 1:
            xalign 1.0
            zoom 0.75
        with Pause(1.5)

        mc "Ah, I think I upset him..."
        mc "I'm sure it'll be fine."

        jump gabe_cont

    
    label gabe_opt_2:

        show gabe phone opt 2:
            xalign 1.0
            zoom 0.75
        with Pause(1.5)
        jump gabe_response_2

    label gabe_response_2:

        show gabe phone response 2:
            xalign 1.0
            zoom 0.75
        with Pause(1.5)

        mc "Hehe, he's so cute!"
        
        jump gabe_cont


    label gabe_cont:

        hide gabe phone response 1
        with dissolve

        hide hazel phone response 2
        with dissolve

        mc "Cool, I guess we're meeting inside."
        mc "Wait. Where inside?"
        mc "Eh, I dont think it'll be that hard to find him."
       

        jump gabe_aqaurium


    label gabe_aqaurium:

        scene aqua finish with fade:
            zoom 0.77
            blur 4
    
        stop music fadeout 1.5

        play music "audio/aquarium/gabe/14 - boy meets girl.mp3" fadein 1

        mc "Right! Where is that tall guy lurking? "
        mc "Aha! There he is!"
        mc "Gabe!! Hi!"

        narrate "I wave with both hands in his direction."

        show gabe happy with dissolve:
            xpos 0.10


        gabe "Oh, hi [mcname]! I'm glad we found eachother so easily!"
        narrate "Of course we did, he's like six feet tall.."


    label gabe_compliment:

        show gabe blush:
            xpos 0.10
        gabe "You look really nice!"

        menu gabe_first_choice:
            
            "Coming from you!":
                mc "Psh! Coming from you!"
                jump gabe_complimented

            "You look awkward...":
                mc "You look really awkward and stiff..."
                jump gabe_awkward

            "Awh, thanks!":
                "Awh, thanks!"
                jump gabe_thanks

    
    label gabe_complimented:

        show gabe blush happy:
            xpos 0.10
        gabe "O-oh! Haha thanks..."
        $ gabe_affection += 1

        jump gabe_nervous
            

    label gabe_awkward:

        show gabe sad neutral:
            xpos 0.10
        gabe "Oh, do I? Sorry..."
        $ gabe_affection -= 1

        jump gabe_nervous

    
    label gabe_thanks:

        show gabe neutral blush:
            xpos 0.10
        gabe "It's okay!"

        jump gabe_nervous

    
    label gabe_nervous:

        show gabe blush:
            xpos 0.10
        gabe "So... uh..."

        mc "Umm..."
        narrate "I think he's nervous."
        narrate "That's fine! I got this!"

        mc "So! How did you know about this place? I thought you didn't grow up here?"

        show gabe excited 
        gabe "Oh, I went here on a school trip once!"
        show gabe happy with dissolve
        gabe "I'm pretty sure it was the only aquarium close by, so we came here a lot."

        mc "No way! I went here on a school trip too!"
        mc "I swear, It's like every school comes to the same places for class trips."

        show gabe neutral blush:
            xpos 0.10
        gabe "Ha, maybe they're in a hivemind or something."
        gabe "Somehow the aquarium just {i}summons{/i} all nearby schools, haha."

        narrate "He looks a little more relaxed now! Mission success!"
        narrate "Wow his smile is so pretty."
        mc "Soooo, what do you wanna look at first?"

        gabe "Can we just kind of... wonder around?"
        show gabe blush:
            xpos 0.10
        gabe "I think it's fun just to look at the fish."

        mc "Hehe, cute."
        narrate "We wonder around the tanks aimlessly, stopping for a while when we see something shiny or bright."
        mc "Have you got a favourite fish? Or?"

        show gabe neutral blush:
            xpos 0.10
        gabe "I feel like its stereotypical, but honestly sharks."
        show gabe excited:
            xpos 0.10
        gabe "I mean come on!! They're so cool! How could I not?"
        gabe "I like Goblin sharks the most."
        show gabe happy with dissolve:
            xpos 0.10
        gabe "People say they're ugly or weird looking but I dunno... I think they look cool in a kind of cute and creepy way."
        narrate "I nod along as he speaks."
        narrate "When he gets so excited he looks so cute!"

    label favourite_fish:
        
        gabe "What about you though? What's your favourite?"

        menu favourite_fish_choice:

            "Shrimp.":
                mc "Oh I like shrimp! Especially Bullet shrimp. They punch at like 60mph."
                mc "Why would a shrimp even need to do that? To be cool obviously."
                jump shrimp

            "Sharks.":
                mc "Oh mines sharks too! Though I like whale sharks."
                mc "Not that Goblin sharks aren't cool! I just think Whale sharks are big as hell and pretty as hell too."
                jump sharks

            "Nemo":
                mc "Nemo obviously. No doubt about it."
                jump nemo
            
            "Goldfish?":
                mc "Do Goldfish count? I think they should count."
                jump goldfish
            
            "That's a boring question.":
                mc "Isn't that kind of a boring question to ask?"
                $ gabe_affection -= 1
            
                jump boring

    label shrimp:

        show gabe excited:
            xpos 0.10
        gabe "Oh, that's sick. In both a cool way and a way that surely that breaks the laws of physics."
        gabe "Hey, maybe we could get some plushies of our favourites later?"
        mc "*gasp* A Bullet Shrimp plushie?, I need one!"
        mc "Plus, it'll be a nice souvenir from today..."
        narrate "I wink at him."

        jump aquarium_cont

    label sharks:

        show gabe excited:
            xpos 0.10
        gabe "Woah, Twins! Or close enough I guess!"
        gabe "I'm glad someone else gets it!"
        gabe "Hey, maybe we could get some plushies of our favourites later?"
        mc "I hope they're HUGE."
        mc "It'll be a nice souvenir from today."
        narrate "I wink at him."

        jump aquarium_cont

    label nemo:

        show gabe blush happy:
            xpos 0.10
        gabe "Hey, I get it. He's just a little fish in a deep blue sea, ya know?"
        gabe "God, thats such a comfort film."
        gabe "Hey, maybe we could get some plushies of our favourites later?"
        mc "If he's here, I'll find him in that gift shop."
        mc "Plus, it'll be a nice souvenir from today."
        narrate "I wink at him."

        jump aquarium_cont

    label goldfish:

        
        show gabe blush happy:
            xpos 0.10
        gabe "Why not right? They're still fish!"
        gabe "Hey, maybe we could get some plushies of our favourites later?"
        mc "Oh, I want one of those little guys!"
        mc "Plus, it'll be a nice souvenir from today."
        narrate "I wink at him."

        jump aquarium_cont

    label boring:

        show gabe sad:
            xpos 0.10
        gabe "Oh, sorry I guess? I just thought it would be nice to ask."
        gabe "Let's just look around some more then..."

        jump aquarium_cont
    
    label aquarium_cont:
        hide gabe sad with dissolve

        hide gabe blush happy with dissolve
        narrate "We both turn our attention back to the tanks and walk around some more."
        narrate "We take turns pointing out which fish we think resembles each other and begin pointing out ones we think look pretty."

        show gabe neutral blush:
            xpos 0.10
        gabe "Ya know this place is super inspiring art wise! Maybe I should come here more often!"

        show gabe blush with dissolve:
            xpos 0.10
        gabe "And you know... you can always join."

        mc "Yeah? I'll take you up on that offer."
        mc "Oh, I've actually been wanting to ask what got you into art and tattooing?"

        show gabe neutral blush:
            xpos 0.10
        gabe "I think I've just always liked it?"
        gabe "I mean, I can't really remember a time that I wasn't drawing."
        gabe "And tattoos are basically just art for your skin..."
        gabe "Plus they can make people who dont feel comfortbale in their own skin happier."

        show gabe blush happy with dissolve:
            xpos 0.10
        gabe "I guess it just made sense to me to wanna use my art for that."

        narrate "His smile is so gentle."
        narrate "I can tell he really loves what he does."
        narrate "It's really sweet."

    label sketchbook:

        show gabe blush:
            xpos 0.10
        gabe "All this talking about art is making me wish I brought my sketchbooks, is that bad? Haha."

        menu sketch:

            "It's fine.":
                mc "It's fine. I mean I get it, you probably draw all the time."

                jump fine
            
            "No, it's cute!":
                mc "No, I think it's cute!"
                mc "Maybe next date we can bring some sketcbooks! A doodle date!"
                $ gabe_affection += 1

                jump doodle_date

            "I mean yeah?":
                mc "I mean yeah kinda? Like that feels ignorant if you did?"
                $ gabe_affection -= 1

                jump ignorant

    label fine:

        show gabe neutral blush:
            xpos 0.10
        gabe "Haha yeah, just feeling inspired by the scenery, ya know?"

        jump gabe_final_cont

    label doodle_date:

        show gabe blush happy:
            xpos 0.10
        gabe "That's a real cute idea. Yeah, Let's do that."

        jump gabe_final_cont

    label ignorant:

        show gabe sad:
            xpos 0.10
        gabe "Oh, that's not what I meant at all. You really think I would just ignore you?"

        jump gabe_ending_evaluation

    label gabe_final_cont:

        show gabe neutral blush:
            xpos 0.10
        gabe "Hey, let's go look at the jellyfish!"

        hide gabe neutral blush with dissolve

        narrate "Gabe shyly takes my hand and leads the way."
        narrate "His hand is warm and comforting. I can feel my heart flutter."
        narrate "We go from exhibit to exhibit until we realise that the aquarium is about to close for the day."

        jump gabe_ending_evaluation



    

label gabe_ending_evaluation:
        
        stop music fadeout 1.0
        play music "trainnight/end/28 - moonlight.mp3" fadein 1


        if gabe_affection >= 2:
            jump gabe_best_ending
        elif gabe_affection == 1:
            jump gabe_good_ending
        else:
            jump gabe_bad_ending

label hazel_ending_evaluation:
        
        stop music fadeout 1.0

        play music "trainnight/end/28 - moonlight.mp3" fadein 1

        if hazel_affection >= 3:
            jump hazel_best_ending
        elif hazel_affection >= 1:
            jump hazel_good_ending
        else: 
            jump hazel_bad_ending

    
label gabe_bad_ending:

    show gabe sad:
        xpos 0.10
    gabe "Actually, I think I might head home early."
    
    show gabe disappointed:
        xpos 0.10
    gabe "I wish we had a nicer time together."
    gabe "But, I'll see you at the cafe at some point."
    gabe "Get home safe..."
    hide gabe disappointed with dissolve
    
    mc "Ah wait-"

    
    narrate "He left."
    narrate "Well that could've gone better."
    jump badend
    return

label gabe_good_ending:
    
    show gabe neutral blush:
        xpos 0.10
    
    mc "Hey, I had a lot of fun today!"
    gabe "Yeah, it was nice! We should definitely do it again sometime!"
    gabe "You're taking the train right? Tell me when you get home safe!"
    show gabe happy:
        xpos 0.10
    gabe "see ya!"

    hide gabe happy with dissolve

    scene train night with slowdissolve: 
        zoom 0.75

    mc "That was nice! Though, maybe it could've gone a little better?"
    mc "Oh well! We both still had fun!"
    mc "Let's hope we do this again!"
    jump goodend
    return

label gabe_best_ending:

    stop music fadeout 1.0

    play music "trainnight/bestend/30 - hot cocoa.mp3" fadein 1.0

    show gabe blush happy:
        xpos 0.10
    
    mc "Hey, I had a lot of fun today!"
    gabe "Yeah, actually I think this might be the best date I've ever been on."
    gabe "I mean I've only been on like 2 dates but this definitely tops them."

    narrate "Gabriel smiles sweetly at me."
    mc "I think this might be my favourite date as well."
    narrate "I smile just as sweetly back at him."

    gabe "Can I-?"
    narrate "I nod and he leans in to kiss my cheek."
    narrate "When he pulls away we're both flushed and smiling like idiots."
    gabe "Get home safe, [mcname]."

    hide gabe blush happy with dissolve

    scene train night with slowdissolve:
        zoom 0.75
    
    mc "Ahh! That was so much fun!"
    mc "I'm so glad it went well. I feel so happy right now!"
    mc "Oh, he messaged me!"

    show gabe phone final:
            xalign 1.0
            zoom 0.75
    with Dissolve(0.3)
    with Pause(3)
    

    hide gabe phone final with dissolve

    mc "I cant wait either."
    jump bestend
    return

label hazel_bad_ending:


    show hazel pout:
        xpos 0.10
    
    haz "Ya know... I think I'm gonna head home."
    haz "I would say I had fun but..."

    mc "Hazel wait-"
    haz "Get home safe [mcname]."

    hide hazel pout with dissolve
    narrate "She left."
    narrate "I really messed up."
    jump badend
    return

label hazel_good_ending:


    
    show hazel neutral:
        xpos 0.10
    
    haz "Yeah me too!"
    haz "Maybe we can go here again sometime!"
    
    show hazel wink:
        xpos 0.10
    
    haz "And I'll tell you even more facts!"

    show hazel neutral:
        xpos 0.10
    
    haz "You're getting the train home right? Get home safe!"

    hide hazel neutral with dissolve

    narrate "She waves goodbye and leaves."

    scene train night with slowdissolve:
        zoom 0.75
    
    mc "That was fun, but maybe not quite the date I really wanted with her."
    mc "At least we got to hang out again!"
    mc "All in all, it was a nice day out."
    jump goodend
    return

label hazel_best_ending:

    stop music fadeout 1.0

    play music "trainnight/bestend/30 - hot cocoa.mp3" fadein 1.0

    show hazel happy blush:
        xpos 0.10
    
    haz "Yeah! me too!"

    show hazel embarrased:
        xpos 0.10

    haz "Wanna know something embarrasing? I actually planned this date for us in school."
    haz "But I was wayyyy to scared to ask you out!"

    narrate "I feel my cheeks go red. Is it embarassing? Maybe. Is it cute? God yes!"
    mc "Better late than never right?"

    show hazel happy blush with dissolve:
        xpos 0.10

    haz "Yeah... Definitely better."
    narrate "She leans in and kisses my cheek shyly. I guess she's still kind of embarrased."
    narrate "I feel my heart flutter and when she pulls away I know for sure we both look like grinning idiots."

    haz "Get home safe [mcname]."

    hide hazel happy blush with dissolve

    scene train night with slowdissolve:
        zoom 0.75
    
    mc "Ahh! I'm so glad today went well!"
    mc "I can't believe I waited so long to ask her out!"
    mc "But it was so worth it!"
    mc "Oh I think she just messaged me!"

    show hazel phone final:
            xalign 1.0
            zoom 0.75
    with Dissolve(0.3)
    with Pause(3)
    
    hide hazel phone final with dissolve
    mc "Yeah, me neither..."
    jump bestend

label bestend:
    scene bestend with slowdissolve
    with Pause(999)
    
    return

label goodend:
    scene goodend with slowdissolve
    with Pause(999)
    
    return

label badend:
    scene badend with slowdissolve
    with Pause(999)
    
    return