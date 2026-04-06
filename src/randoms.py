import character
from faker import Faker
from faker.providers import DynamicProvider as dp
import random as r
#A faker dynamic provider that gets a class
def random_char():
    f=Faker()
    class_provider = dp(provider_name="class_provider", elements=["archer", "knight", "wizard"])
    f.add_provider(class_provider)

    items_provider=dp(provider_name='items_provider',elements=[
    {"Sunfire Amulet": "A gold medallion that glows warmer as it nears undead creatures."},
    {"Whispering Dagger": "An ornate blade that whispers the secrets of those it has tasted."},
    {"Cloak of Mists": "A grey garment that allows the wearer to become semi-transparent in fog."},
    {"Bottomless Waterskin": "A leather pouch that never runs dry, though it only pours lukewarm water."},
    {"Gale-Force Boots": "Footwear that increases movement speed but leaves a trail of swirling dust."},
    {"Everlight Lantern": "A glass lantern containing a captured star fragment; never needs oil."},
    {"Ironroot Staff": "A heavy wooden staff that can take root in any soil to become an immovable pillar."},
    {"Midas's Thimble": "An item that turns any small sewing needle into solid gold once per day."},
    {"Phase Coin": "A silver coin that can pass through solid glass when flipped."},
    {"Shadow-Stitch Thread": "Silk thread used to sew a person's shadow back on if it's been lost."},
    {"Echoing Horn": "A horn whose blast repeats itself three times, each quieter than the last."},
    {"Frostbite Ring": "Keeps the wearer's body temperature perfectly cool, even in a volcano."},
    {"Gravity Marble": "A small black sphere that falls toward the nearest source of magic instead of the ground."},
    {"Key of Portals": "A rusty key that can lock any door so it cannot be opened by any means for an hour."},
    {"Soul-Bound Compass": "A compass that points toward the person the holder loves most."},
    {"Cinder-Glass Shield": "A shield made of volcanic glass that bursts into flames when struck."},
    {"Dream-Catcher Web": "A net that can physically capture a sleeping person's dream as a misty orb."},
    {"Feather-Weight Maul": "A massive hammer that weighs nothing to the wielder but hits with full force."},
    {"Living Map": "A parchment that updates itself in real-time based on the user's surroundings."},
    {"Phoenix Down Quill": "A pen that allows the writer to see what they wrote even in total darkness."},
    {"Siren's Pearl": "A blue pearl that allows the user to breathe underwater for ten minutes."},
    {"Stone-Singer's Flute": "A flute that causes small pebbles to dance and form patterns."},
    {"Void-Bound Quiver": "A quiver that slowly regenerates wooden arrows over several hours."},
    {"Wind-Runner's Cape": "A light cape that allows the wearer to fall from any height without taking damage."},
    {"Clockwork Beetle": "A small mechanical insect that can record and playback 30 seconds of audio."},
    {"Aegis of Dawn": "A shield that emits a blinding flash of light once per day."},
    {"Blood-Moon Blade": "A sword that grows sharper and glows red during a lunar eclipse."},
    {"Chameleon Tunic": "Clothing that changes color to match the wearer's environment."},
    {"Dragon-Scale Mail": "Armor made from the scales of a red dragon, granting fire resistance."},
    {"Eldritch Eye": "A floating mechanical eye that can see into the ethereal plane."},
    {"Flame-Tongue Whip": "A whip that leaves a trail of symbols and deals fire damage."},
    {"Ghost-Step Sandals": "Sandals that allow the wearer to walk silently on any surface."},
    {"Heart-Seeker Bow": "A bow that grants a bonus to hit targets the wielder has fought before."},
    {"Ice-Shard Dagger": "A blade made of eternal ice that never melts and freezes what it cuts."},
    {"Jester's Mask": "A mask that forces the wearer to speak only in rhymes."},
    {"Kraken's Tooth": "A dagger that deals extra damage to seafaring creatures."},
    {"Lightning-Rod Spear": "A spear that attracts lightning during a storm and can discharge it."},
    {"Mirror-Shield of Reflection": "A shield that can reflect magical projectiles back at the caster."},
    {"Night-Crawler's Gloves": "Gloves that allow the wearer to climb vertical surfaces like a spider."},
    {"Oak-Heart Amulet": "An amulet that grants the wearer extra resilience and health."},
    {"Plague-Doctor's Mask": "A mask that protects the wearer from airborne toxins and diseases."},
    {"Quicksilver Boots": "Boots that allow the wearer to walk on water for short bursts."},
    {"Raven's Wing Cloak": "A cloak that allows the wearer to glide through the air."},
    {"Star-Dust Potion": "A potion that grants the drinker a temporary boost to their magical power."},
    {"Thunder-Clap Warhammer": "A hammer that creates a deafening boom when it strikes an object."},
    {"Unicorn-Horn Wand": "A wand that excels at healing and restorative magic."},
    {"Vampire's Fang Dagger": "A dagger that heals the wielder for a portion of damage dealt."},
    {"Wraith-Bone Armor": "Armor made from the bones of a wraith, granting necrotic resistance."},
    {"Xenon-Glow Orb": "A glowing orb that illuminates a large area with a steady blue light."},
    {"Yggdrasil Leaf": "A leaf from the world tree that can revive a fallen ally."},
    {"Zephyr's Veil": "A thin veil that protects the wearer from strong winds."},
    {"Arcane Lock-Pick": "A set of lock-picks that can bypass magical locks."},
    {"Basilisk-Eye Lens": "A lens that allows the user to see through illusions."},
    {"Cursed Coin of Greed": "A coin that compels the holder to seek more wealth."},
    {"Dream-Walker's Elixir": "A potion that allows the drinker to enter another person's dreams."},
    {"Ebon-Flame Torch": "A torch that emits black flames providing light but no heat."},
    {"Frost-Giant's Belt": "A belt that grants the wearer the strength of a frost giant."},
    {"Gorgon's Gaze Mirror": "A mirror that can temporarily petrify a creature."},
    {"Hidden-Blade Gauntlet": "A gauntlet with a concealed blade for quick deployment."},
    {"Inferno-Core Gem": "A gem that can be shattered to release a fire explosion."},
    {"Jade-Dragon Statue": "A small statue that can be summoned to life as a companion."},
    {"King's Ransom Pouch": "A pouch that always contains gold for a small purchase."},
    {"Labyrinth-Key Compass": "A compass that points toward the exit of a maze."},
    {"Moon-Shadow Ring": "A ring that allows the wearer to become invisible in dim light."},
    {"Necromancer's Phylactery": "A vessel used to store the soul of a powerful undead being."},
    {"Orb of Scrying": "A crystal ball that allows the user to view distant locations."},
    {"Phantom-Steed Whistle": "A whistle that summons a ghostly horse."},
    {"Quake-Maker Maul": "A massive hammer that can create localized earthquakes."},
    {"Rune-Carved Shield": "A shield inscribed with runes for elemental protection."},
    {"Soul-Eater Blade": "A sword that traps souls to grow more powerful."},
    {"Tome of Ancient Secrets": "A book containing lost knowledge and powerful spells."},
    {"Umbra-Dagger": "A dagger that can strike a target's shadow to deal damage."},
    {"Void-Walker's Robes": "Robes that allow the wearer to blink short distances."},
    {"War-Horn of Valhalla": "A horn that summons ghostly warriors to fight."},
    {"Xylophone of Echoes": "An instrument that plays back sounds from the last hour."},
    {"Yeti-Fur Cloak": "A cloak providing immunity to extreme cold."},
    {"Zodiac-Stone Amulet": "An amulet granting bonuses based on astrological signs."},
    {"Alchemist's Catalyst": "A substance that speeds up potion brewing."},
    {"Banshee's Wail Crystal": "A crystal that releases a shriek when shattered."},
    {"Celestial-Silver Chainmail": "Armor made from silver forged in celestial realms."},
    {"Demon-Hunter's Crossbow": "A crossbow that deals extra damage to fiends."},
    {"Emerald-Growth Seed": "A seed that instantly grows into a large tree."},
    {"Falconer's Glove": "A glove that allows communication with birds of prey."},
    {"Glimmer-Dust Powder": "A powder that reveals invisible creatures."},
    {"Harpy-Feather Fan": "A fan that can create a powerful gust of wind."},
    {"Iron-Will Circlet": "A circlet that protects from charms and compulsions."},
    {"Juggernaut's Plate": "Heavy armor that makes the wearer nearly impossible to move."},
    {"Knowledge-Seeker's Spectacles": "Glasses that allow the wearer to read any language."},
    {"Lich-Hand Scepter": "A scepter that can cast necrotic spells."},
    {"Misty-Step Boots": "Boots that allow the wearer to teleport short distances."},
    {"Night-Owl Goggles": "Goggles that grant the wearer darkvision."},
    {"Ooze-Skin Suit": "A suit allowing the wearer to squeeze through tight spaces."},
    {"Phoenix-Ash Urn": "An urn that can bring a creature back to life once."},
    {"Quick-Draw Quiver": "A quiver for drawing and firing arrows with incredible speed."},
    {"Rogue's Shadow-Mask": "A mask that obscures the wearer's face in darkness."},
    {"Storm-Caller's Trident": "A trident that can summon rain and lightning."},
    {"Talisman of Luck": "A charm allowing one reroll of a failed roll per day."},
    {"Under-Dark Lantern": "A lantern visible only to those with darkvision."},
    {"Valkyrie's Spear": "A spear that glows and deals extra damage to undead."},
    {"Willow-Wisp Bottle": "A jar containing a wisp that provides soft light."}
]
)
    f.add_provider(items_provider)

    skills={'archer':{'Snipe':'Ranged weapon range is doubled','Pierce Armor':'Double damage of ranged weapons.'},'knight':{'Parry':'Use a melee attack to negate an enemy\'s next attack','Disarm':'Use a melee attack to remove an enemy\'s weapon.'},'wizard':{'Quick Spell':'Cast two spells as one attack.','Change Spell':'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}}
    name = f.name()
    clas = f.class_provider()
    level = r.randint(1,2)
    if level==1: max=r.randint(5,10)
    else: max=r.randint(10,20)
    choices=[]
    for i in range(2):
        choices.append(r.randint(0,max))
        max-=choices[-1]
    choices.append(max)
    str=r.choice(choices)
    choices.remove(str)
    spd=r.choice(choices)
    choices.remove(spd)
    mag=choices[0]
    if level==1:
        skill={list(skills[clas].keys())[0]:skills[clas][list(skills[clas].keys())[0]]}
    else:
        snme=r.choice(list(skills[clas]))
        skill={snme:skills[clas][snme]}
    invent={}
    for i in range(r.randint(0,10)):
        invent|=f.items_provider()
    return character.Character([name,clas,str,spd,mag,skill,invent,level])