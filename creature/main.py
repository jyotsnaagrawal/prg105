from creature import Creature, Orc, OrcBoss

creature = Creature("rabbit", True, (10, 250, 10), "bunny.gif")
print(creature)

orc = Orc("axe", 150, 150, (-100, 200, 50), "rabbit.gif")
print(orc)

orc_boss = OrcBoss("greatsword", 350, 200, (300, 150, 35), "orc_boss.gif", "Griksnak", "jump and slash")
print(orc_boss)

