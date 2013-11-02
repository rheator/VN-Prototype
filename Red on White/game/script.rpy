# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg snowy = "images/snowy.jpg"
image bg room = "images/room.jpg"
image bg outside = "images/snowbranch.jpg"
image bg indoor = "images/indoor.jpg"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
define puddlesmusic = "music/Raindrops_and_puddles.mp3"
define town1 = "Grendjor"

init:
    image white = Solid((255, 255, 255, 255))

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
    
    stop music fadeout 2.0

    "Every night it creeps a little bit closer"
    
    scene white with Dissolve(0.3)
    
    scene bg room with Dissolve(5.0)
    
    "........."
    
    "I wake gradually to the crisp morning air"
    
    "It is quiet, but in a comfortable kind of way"
    
    play music puddlesmusic fadein 2.0
    
    "The air hung gently, and as I sat up and drew the sheets aside, the air pricked my exposed skin with its lingering chill"
    
    "I shuddered, stretched and yawned heartily in a belowing cloud of condensation"
    
    "It was a quiet morning, and a quiet morning is a good one"
    
    "Outside, the black bark of trees stood contentedly in the still air, covered snugly in neat, thick layers of fresh snow"
    
    "And though the air is cold it is a cold that is soft and yielding, one that could be dispelled by a brisk walk or a warm breakfast"
    
    "Mornings, especially quiet ones like these, tended to be the gentlest, most pleasant part of the day in recent times"
    
    "The intense storms that howl and ravage the lands in the depths of night unravel with the dawn"
    
    "Leaving behind a dense cover of new snow and a fluffy blanket of fresh-scented air"
    
    "I get up and go about my usual morning routine, moving around the relatively small space of my sleeping quarters as I washed up and prepared to go out"
    
    "Before long I am wrapped snugly in my robes. Pulling on a leather cloak for good measure, I head outside"
    
    scene bg outside with Dissolve(0.5)
    
    play music puddlesmusic fadein 2.0

    "The loose snow crunched underfoot as I walked"
    
    "The immediate vicinity of the dormitory in which I lived is lightly wooded, being at the lowest level of the town."
    
    "The town of [town1] where I lived was a layered town etched into the side of a steep, rocky mountain, with horizontal rows of stone buildings running up the steep slopes in zig-zag fashion, forming levels of roads and dwellings from the base up"
    
    "Most of my peers lived in the Church, at the very highest level of the town. But I, who have always loved the open fields and woods that only existed at the mountain's base, chose to live in the small, Church-run dormitories here and tend to the people living near the base"
    
    return
