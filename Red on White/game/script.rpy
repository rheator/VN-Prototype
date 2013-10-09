# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg snowy = "images/snowy.jpg"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:
    scene bg snowy
    "The bitter cold sweeps the land"
    
    "Night after night"
    
    "In treacherous wind and relentless storm"
    
    "Wrought by a cold of malignant resilience"
    
    "A cold that sieges, encroaches, inscribes"
    
    "That envelopes and invades the very soul of the land"
    
    "And the desperate warmth of the people sheltered and huddled against it"
    
    "Every night we retreat into our furnaces and our fur and cloth"
    
    "Keeping the cold at bay"
    
    scene black with Dissolve(2.0)
    
    "Every night it creeps a little bit closer"

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    return
