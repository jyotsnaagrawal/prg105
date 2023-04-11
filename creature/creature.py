class Creature:
    def __init__(self, type_of_creature, friendly, position, image):
        # type_of_creature is a short string
        self.type_of_creature = type_of_creature
        # friendly should have a True/False value
        self.friendly = friendly
        # The position should be a tuple like (x, y, z) where x, y, z are integers
        self.position = position
        # The image should be a string holding an image name
        self.image = image

    # mutators (setters)
    def set_type_of_creature(self, type_of_creature):
        self.type_of_creature = type_of_creature

    def set_friendly(self, friendly):
        self.friendly = friendly

    def set_position(self, position):
        self.position = position

    def set_image(self, image):
        self.image = image

    # accessors (getters)
    def get_type_of_creature(self):
        return self.type_of_creature

    def get_friendly(self):
        return self.friendly

    def get_position(self):
        return self.position

    def get_image(self):
        return self.image

    # return a string describing the creature
    def __str__(self):
        if self.friendly:
            description = f"This friendly {self.type_of_creature} is located at "
        else:
            description = f"This unfriendly {self.type_of_creature} is located at "
        return description + str(self.position) + " and uses the image asset: " + self.image


class Orc(Creature):
    def __init__(self, weapon, max_hit_points, current_hit_points, position, image):
        super().__init__("Orc", False, position, image)
        self.weapon = weapon
        self.max_hit_points = max_hit_points
        self.current_hit_points = current_hit_points

    def set_weapon(self, weapon):
        self.weapon = weapon

    def set_max_hit_points(self, max_hit_points):
        self.max_hit_points = max_hit_points

    def set_current_hit_points(self, current_hit_points):
        self.current_hit_points = current_hit_points

    def get_weapon(self):
        return self.weapon

    def get_max_hit_points(self):
        return self.max_hit_points

    def get_current_hit_points(self):
        return self.current_hit_points

    def __str__(self):
        creature_description = super().__str__()
        return f"\nThis Orc uses a(n) {self.weapon} and has HP: {self.current_hit_points}/{self.max_hit_points} \n" \
            + creature_description


class OrcBoss(Orc):
    def __init__(self, weapon, max_hit_points, current_hit_points, position, image, name, special_move):
        super().__init__(weapon, max_hit_points, current_hit_points, position, image)
        self.name = name
        self.special_move = special_move

    def set_name(self, name):
        self.name = name

    def set_special_move(self, special_move):
        self.special_move = special_move

    def get_name(self):
        return self.name

    def get_special_move(self):
        return self.special_move

    def __str__(self):
        orc_description = super().__str__()
        return f"\n{self.name} is an Orc boss with {self.special_move} as a special move. " + orc_description

