import discord
import discord.client
import random
from discord.ext import commands

# Enter your bots custom token here
token = "Enter Your Token Here"

# Enable intents and define in developer portal to enable auto-role functionality
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)


# Check if bot is running and print username of bot in terminal
@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

# 8Ball Function - ask a question and get a randomized response
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.', 'As I see it, yes.',
                 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Dont count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.', 'Bruh you crazy?']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# Have bot say hello to user
@client.event
async def on_message(msg):
    if msg.author != client.user:
        if msg.content.lower().startswith("!hi"):
            await msg.channel.send(f"Hello, {msg.author.display_name}! You are looking very powerful and attractive today.")
    await client.process_commands(msg)

#Auto assigns guest role to users when invited to server
role = "Guest"
@client.event
async def on_member_join(member): 
    rank = discord.utils.get(member.guild.roles, name=role) #Bot get guild(server) roles
    await member.add_roles(rank)  

# Help Function - Provides users command inventory for the bot in channel
@client.command()
async def helpme(ctx):
    embed = discord.Embed(title="----- Help Menu -----", description='\n Current commands are:\n\n !8ball (Enter your question here without parenthesis) - Provides concrete reliable decision making guarenteed to work 100% of the time 20% of the time!\n\n !hi - Provides a nice hello message from the bot\n\n !poll (Poll topic here without parenthesis) - Call a vote in the current channel using emotes \n\n !coinflip - Flips a coin and spits out the randomized result\n\n !usernamegen - Generates a custom unique username if the one you actually wanted got taken'
                          )
    await ctx.send(embed=embed)


# Poll Function - call a vote with a user defined topic with results handled with emotes
@client.command()
async def poll(ctx, *, text: str):
    poll = await ctx.send("Current vote topic is: " + f"{text}")
    await poll.add_reaction("✅")
    await poll.add_reaction("❌")
    await poll.add_reaction("❓")

# Coin Flip - Random coin flip functionality
@client.command()
async def coinflip(ctx):
    cointoss_options = [0, 1]
    if random.choice(cointoss_options) == 1:
        embed = discord.Embed(
            title="Coinflip", description=f"{ctx.author.mention} Flipped a coin \n Result is: **Heads**!")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title="Coinflip", description=f"{ctx.author.mention} Flipped a coin\n Result is: **Tails**!")
        await ctx.send(embed=embed)


#  Generates random username for users 
@client.command()
async def usernamegen(ctx):
    adjectives = ['aback', 'abaft',  'abandoned',  'abashed',  'aberrant',  'abhorrent',
                  'abiding',  'abject',  'ablaze',  'able',  'abnormal', 'aboriginal',
                  'abortive', 'abounding',  'abrasive', 'abrupt',  'absent', 'absorbed',
                  'absorbing', 'abstracted', 'absurd', 'abundant', 'abusive',  'acceptable',
                  'accessible',  'accidental','warm',  'wary', 'wasteful', 'youthful',
                  'yummy', 'zany', 'zealous', 'zesty', 'zippy',  'zonked',
                  ]
    nouns = ["accelerator", "accordion", "account", "accountant", "acknowledgment", "acoustic", "acrylic", "act", "action", "active", "activity", "actor", "actress", "adapter", "addition", "address", "adjustment", "adult", "advantage", "advertisement", "advice", "afghanistan", "africa", "aftermath", "afternoon", "aftershave", "afterthought", "age", "agenda", "agreement", "air", "airbus", "airmail", "airplane", "airport", "airship", "alarm", "albatross", "alcohol", "algebra", "algeria", "alibi", "alley", "alligator", "alloy", "almanac", "alphabet", "alto", "aluminium", "aluminum", "ambulance", "america", "amount", "amusement", "anatomy", "anethesiologist", "anger", "angle", "angora", "animal", "anime", "ankle", "answer", "ant", "antarctica", "anteater", "antelope", "anthony", "anthropology", "apartment", "apology", "apparatus", "apparel", "appeal", "appendix", "apple", "appliance", "approval", "april", "aquarius", "arch", "archaeology", "archeology", "archer", "architecture", "area", "argentina", "argument", "aries", "arithmetic", "arm", "armadillo", "armchair", "armenian", "army", "arrow", "art", "ash", "ashtray", "asia", "asparagus", "asphalt", "asterisk", "astronomy", "athlete", "atm", "atom", "attack", "attempt", "attention", "attic", "attraction", "august", "aunt", "australia", "australian", "author", "authorisation", "authority", "authorization", "avenue", "babies", "baboon", "baby", "back", "backbone", "bacon", "badge", "badger", "bag", "bagel", "bagpipe", "bail", "bait", "baker", "bakery", "balance", "balinese", "ball", "balloon", "bamboo", "banana", "band", "bandana", "bangladesh", "bangle", "banjo", "bank", "bankbook", "banker", "bar", "barbara", "barber", "barge", "baritone", "barometer", "base", "baseball", "basement", "basin", "basket", "basketball", "bass", "bassoon", "bat", "bath", "bathroom", "bathtub", "battery", "battle", "bay", "beach", "bead", "beam", "bean", "bear", "beard", "beast", "beat", "beautician", "beauty", "beaver", "bed", "bedroom", "bee", "beech", "beef", "beer", "beet", "beetle", "beggar", "beginner", "begonia", "behavior", "belgian", "belief", "believe", "bell", "belt", "bench", "bengal", "beret", "berry", "bestseller", "betty", "bibliography", "bicycle", "bike", "bill", "billboard", "biology", "biplane", "birch", "bird", "birth", "birthday", "bit", "bite", "black", "bladder", "blade", "blanket", "blinker", "blizzard", "block", "blood", "blouse", "blow", "blowgun", "blue", "board", "boat", "bobcat", "body", "bolt", "bomb", "bomber", "bone", "bongo", "bonsai", "book", "bookcase", "booklet", "boot", "border", "botany", "bottle", "bottom", "boundary", "bow", "bowl", "bowling", "box", "boy", "bra", "brace", "bracket", "brain", "brake", "branch", "brand", "brandy", "brass", "brazil", "bread", "break", "breakfast", "breath", "brian", "brick", "bridge", "british", "broccoli", "brochure", "broker", "bronze", "brother", "brother-in-law", "brow", "brown", "brush", "bubble", "bucket", "budget", "buffer", "buffet", "bugle", "building", "bulb", "bull", "bulldozer", "bumper", "bun", "burglar", "burma", "burn", "burst", "bus", "bush", "business", "butane", "butcher", "butter", "button", "buzzard", "c-clamp", "cabbage", "cabinet", "cable", "cactus", "cafe", "cake", "calculator", "calculus", "calendar", "calf", "call", "camel", "camera", "camp", "can", "canada", "canadian", "cancer", "candle", "cannon", "canoe", "canvas", "cap", "capital", "cappelletti", "capricorn", "captain", "caption", "car", "caravan", "carbon", "card", "cardboard", "cardigan", "care", "carnation", "carol", "carp", "carpenter", "carriage", "carrot", "cart", "cartoon", "case", "cast", "castanet", "cat", "catamaran", "caterpillar", "cathedral", "catsup", "cattle", "cauliflower", "cause", "caution", "cave", "cd", "ceiling", "celery", "celeste", "cell", "cellar", "cello", "celsius", "cement", "cemetery", "cent", "centimeter", "century", "ceramic", "cereal", "certification", "chain", "chair", "chalk", "chance", "change", "channel", "character", "chard", "charles", "chauffeur", "check", "cheek", "cheese", "cheetah", "chef", "chemistry", "cheque", "cherries", "cherry", "chess", "chest", "chick", "chicken", "chicory", "chief", "child", "children", "chill", "chime", "chimpanzee", "chin", "china", "chinese", "chive", "chocolate", "chord", "christmas", "christopher", "chronometer", "church", "cicada", "cinema", "circle", "circulation", "cirrus", "citizenship", "city", "clam", "clarinet", "class", "claus", "clave", "clef", "clerk", "click", "client", "climb", "clipper", "cloakroom", "clock", "close", "closet", "cloth", "cloud", "cloudy", "clover", "club", "clutch", "coach", "coal", "coast", "coat", "cobweb", "cockroach", "cocktail", "cocoa", "cod", "coffee", "coil", "coin", "coke", "cold", "collar", "college", "collision", "colombia", "colon", "colony", "color", "colt", "column", "columnist", "comb", "comfort", "comic", "comma", "command", "commission", "committee", "community", "company", "comparison", "competition", "competitor",
             "composer", "composition", "computer", "condition", "condor", "cone", "confirmation", "conga", "congo", "conifer", "connection", "consonant", "continent", "control", "cook", "cooking", "copper", "copy", "copyright", "cord", "cork", "cormorant", "corn", "cornet", "correspondent", "cost", "cotton", "couch", "cougar", "cough", "country", "course", "court", "cousin", "cover", "cow", "cowbell", "crab", "crack", "cracker", "craftsman", "crate", "crawdad", "crayfish", "crayon", "cream", "creator", "creature", "credit", "creditor", "creek", "crib", "cricket", "crime", "criminal", "crocodile", "crocus", "croissant", "crook", "crop", "cross", "crow", "crowd", "crown", "crush", "cry", "cub", "cuban", "cucumber", "cultivator", "cup", "cupboard", "cupcake", "curler", "currency", "current", "curtain", "curve", "cushion", "custard", "customer", "cut", "cuticle", "cycle", "cyclone", "cylinder", "cymbal", "dad", "daffodil", "dahlia", "daisy", "damage", "dance", "dancer", "danger", "daniel", "dash", "dashboard", "database", "date", "daughter", "david", "day", "dead", "deadline", "deal", "death", "deborah", "debt", "debtor", "decade", "december", "decimal", "decision", "decrease", "dedication", "deer", "defense", "deficit", "degree", "delete", "delivery", "den", "denim", "dentist", "deodorant", "department", "deposit", "description", "desert", "design", "desire", "desk", "dessert", "destruction", "detail", "detective", "development", "dew", "diamond", "diaphragm", "dibble", "dictionary", "dietician", "difference", "digestion", "digger", "digital", "dill", "dime", "dimple", "dinghy", "dinner", "dinosaur", "diploma", "dipstick", "direction", "dirt", "disadvantage", "discovery", "discussion", "disease", "disgust", "dish", "distance", "distribution", "distributor", "diving", "division", "divorced", "dock", "doctor", "dog", "dogsled", "doll", "dollar", "dolphin", "domain", "donald", "donkey", "donna", "door", "dorothy", "double", "doubt", "downtown", "dragon", "dragonfly", "drain", "drake", "drama", "draw", "drawbridge", "drawer", "dream", "dredger", "dress", "dresser", "dressing", "drill", "drink", "drive", "driver", "driving", "drizzle", "drop", "drug", "drum", "dry", "dryer", "duck", "duckling", "dugout", "dungeon", "dust", "eagle", "ear", "earth", "earthquake", "ease", "east", "edge", "edger", "editor", "editorial", "education", "edward", "eel", "effect", "egg", "eggnog", "eggplant", "egypt", "eight", "elbow", "element", "elephant", "elizabeth", "ellipse", "emery", "employee", "employer", "encyclopedia", "end", "enemy", "energy", "engine", "engineer", "engineering", "english", "enquiry", "entrance", "environment", "epoch", "epoxy", "equinox", "equipment", "era", "error", "estimate", "ethernet", "ethiopia", "euphonium", "europe", "evening", "event", "ex-husband", "ex-wife", "examination", "example", "exchange", "exclamation", "exhaust", "existence", "expansion", "experience", "expert", "explanation", "eye", "eyebrow", "eyelash", "eyeliner", "face", "facilities", "fact", "factory", "fahrenheit", "fairies", "fall", "family", "fan", "fang", "farm", "farmer", "fat", "father", "father-in-law", "faucet", "fear", "feast", "feather", "feature", "february", "fedelini", "feedback", "feeling", "feet", "felony", "female", "fender", "ferry", "ferryboat", "fertilizer", "fiber", "fiberglass", "fibre", "fiction", "field", "fifth", "fight", "fighter", "file", "find", "fine", "finger", "fir", "fire", "fired", "fireman", "fireplace", "firewall", "fish", "fisherman", "flag", "flame", "flare", "flat", "flavor", "flax", "flesh", "flight", "flock", "flood", "floor", "flower", "flugelhorn", "flute", "fly", "foam", "fog", "fold", "font", "food", "foot", "football", "footnote", "force", "forecast", "forehead", "forest", "forgery", "fork", "form", "format", "fortnight", "foundation", "fountain", "fowl", "fox", "foxglove", "fragrance", "frame", "france", "freckle", "freeze", "freezer", "freighter", "french", "freon", "friction", "friday", "fridge", "friend", "frog", "front", "frost", "frown", "fruit", "fuel", "fur", "furniture", "galley", "gallon", "game", "gander", "garage", "garden", "garlic", "gas", "gasoline", "gate", "gateway", "gauge", "gazelle", "gear", "gearshift", "geese", "gemini", "gender", "geography", "geology", "geometry", "george", "geranium", "german", "germany", "ghana", "ghost", "giant", "giraffe", "girdle", "girl", "gladiolus", "glass", "glider", "gliding", "glockenspiel", "glove", "glue", "goal", "goat", "gold", "goldfish", "golf", "gondola", "gong", "good-bye", "goose", "gore-tex", "gorilla", "gosling", "government", "governor", "grade", "grain", "gram", "granddaughter", "grandfather", "grandmother", "grandson", "grape", "graphic", "grass", "grasshopper", "gray", "grease", "great-grandfather", "great-grandmother", "greece", "greek", "green", "grenade", "grey", "grill", "grip", "ground", "group", "grouse", "growth", "guarantee", "guatemalan", "guide", "guilty", "guitar", "gum", "gun", "gym", "gymnast", "hacksaw", "hail"]
    generatedname = random.choice(
        adjectives) + random.choice(nouns) + "%d" % random.randint(0, 600)
    await ctx.send(f'Your super cool username is: ' + generatedname)


client.run(token)
