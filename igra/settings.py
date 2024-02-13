class Settings:

    def __init__(self):

        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (65, 74, 76)

        self.ship_limit = 1

        self.bullet_width = 4
        self.bullet_height = 10
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 8


        self.fleet_drop_speed = 25

        self.speedup_scale = 1.05
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.06
        self.bullet_speed_factor = 1.33
        self.alien_speed_factor = 0.35


        self.alien_points = 25
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
