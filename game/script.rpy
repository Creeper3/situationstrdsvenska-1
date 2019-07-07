define an = Character('Anna', color="#c8c8ff")
define bt = Character('Bartender', color="B5651D")
define kr = Character('Kristian', color="0095D9")
define da = Character('Darek', color="7C0A02")

# The game starts here.

label start:

    scene bg home_background
    with fade

    show eileen concerned

    an "Detta är värsta dagen någonsin!"
    an "Darek gjorde slut med mig! Över sms till och med."
    an "suck..."
    an "Jag behöver tänka på något annat."

    menu:

        "Vad ska jag göra?"

        "Stanna hemma":
            jump stayHome

        "Gå till baren":
            jump barScene

        "Gå till resturangen":
            jump restaurantScene

    label stayHome:
        show eileen happy
        an "Jag stannar hemma."
        an "Tar och kollar på Titanic och Dirty dansing igen, var är glassen?"

        "Anna sitter hemma med katten och käkar glass med pasta. Under natten kollar hon på Titanic och Dirty Dancing. På morgonen käner hon sig fortfarande ledsen, men börjar komma över sitt ex."
        return

    label barScene:
        scene bg bar_background
        with fade
        "Anna går in i barren och sätter sig på en av barstolarna. Bartendern ser att hon är ledsen och går fram till henne"

        bt "Vad kan jag erbjuda?"

        menu:

            "Long Island Ice Tea":
                jump longTea

            "Wiskey":
                jump wiskey


        label longTea:
            an "Ge mig Long Island Ice Tea. Med påfylning"
            jump homeTravel


        label wiskey:
            an "Ge mig bara ett glass wiskey, och förbered tre till."

            jump homeTravel


        label homeTravel:
            "Efter några glass börjar Anna käna sig rätt full. Hon betalar och bestämmer sig för att resa hem."

            menu:

                "Gå hem":
                    jump walk

                "Kör hem":
                    jump drive

                "Ring Darek":
                    jump darek


            label walk:
                "Anna bestämmer sig för att gå hem. Hon vill inte riskera att köra berusad."

                scene bg bedroom_background
                with fade

                "När hon kommer hem lägger hon sig direkt. Nästa dag har hon huvudvärk och får långsamt pussla ihop gårdagen allteftersom minnena kommer tillbaka."
                return


            label drive:
                "Anna bestämmer sig för att köra hem. Det är inte så lång väg så det borde gå bra."
                scene bg road_background
                with fade

                "Ute på vägen börjar hon se lite dubbelt, hon får svårt att konsentrera sig och ser därför inte lastbilen som kommer mot henne."
                scene bg black_background
                with fade
                "De krockar."

                "Nästa dag vaknar hon i en sjukhussäng."
                "Doktorn säger att krocken bröt ena armen och några av revbenen. Eftersom hon krockade med sidan av lastbilen, istället för rakt på överlevde hon."
                "Några dagar senare kunde hon åka hem."

                return


            label darek:
                "Anna bestämer sig för att ringa Darek."

                an "Hej darek"
                da "Anna?"
                an "Ja, det är jag. Kan du plocka up mig?"
                da "...Du fick mitt sms va?"
                an "Ja... men du kan väl plocka up mig?"
                da "suck..."
                da "Var är du?"
                an "Jag är på neonbaren"
                da "Okej, jag kommer. Kan du vänta en stund?"
                an "Såklart."

                "Efter några minuter kör Dareks bil in."
                "Anna går ut till bilen."

                "I bilen sommnar Anna, och Darek tar henne hem till sig."
                "Dagen därpå vaknar Anna i Dareks säng. Under morgonen börjar de prata och bestämmer sig för att stanna som vänner."

                return



    label restaurantScene:
        show eileen concerned

        scene bg resturaunt_background
        with fade

        "När Anna säter sig ned kommer en servitör fram till henne nästan direkt."
        kr "Vad kan vi erbjuda?"

        menu:

            "Jag skulle vilja ha"
            "Hamburgare":
                jump burger

            "Laxpasta":
                jump lax


        label burger:
            an "Jag tar hamburgaren, den verkar god."
            "Servitören nickar"
            kr "En klassiker. Vill du ha något att dricka?"
            an "Jag kan ta vanligt vatten."
            kr "Okej. jag kommer snart tillbaka med din bestälning."

            "Efter några minuter kommer servitören tillbaka med en nygrilad hamburgare."
            kr "Här har du, trevlig måltid."
            an "Tack så mycket."
            "Medans Anna äter tänker hon tillbaka på Darek."
            "När hon tänkte efter hade de inte träffats på rätt länge."
            "Och när hon tänker efter känner hon sig inte så ledsen egentligen."
            "Det var snarare överaskningen som fick henne att reagera så starkt."

            scene bg home_background
            with fade

            "Senare på kvällen när hon komer hem bestämmer hon sig för att ringa Darek och försöka reda ut allting."
            scene bg black_background
            with fade
            return

        label lax:
            an "Jag tar laxpastan, den verkar god."
            "Servitören nickar"
            kr "Ett bra val, det är husets specialitet, vill du ha något att dricka?"
            an "Jag kan ta vanligt vatten."
            kr "Okej. jag kommer snart tillbaka med din bestälning."

            "Det tar ett tag innan matten kommer."
            kr "Förlåt att det tog sådan tid, vi hade lite problem i köket bara. Här är din beställning."
            an "Jaså? Vad var problemet?"
            kr "Åh, inget specielt, ugnen strulade bara lite. Här är din pasta."
            an "Tack så mycket"

            scene bg home_background
            with fade

            "När Anna kommer hem senare på dagen känner hon sig redo att gå vidare. Hon smsar Darek att hon håller med honnom. Hon plockar upp sin katt, sätter sig i soffan och sätter på sin favoritfilm."

            return


    # This ends the game.

    return
