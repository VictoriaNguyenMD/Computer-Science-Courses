class Car:
    def __init__(self, model, year, license_num, speed = 0.0, acceleration = 10.0, color = "black", horn_sound = "HONK"):
        self.model = model
        self.year = year
        self.license_num = license_num
        self.speed = speed
        self.acceleration = acceleration
        self.color = color
        self.horn_sound = horn_sound
    
    def honk(self):
        return self.horn_sound
    
    def describe(self):
        return "A %s %s %s, with license plate number %s." % (self.color, self.year, self.model, self.license_num)
        
    def change_plate(self, new_plate):
        self.license_num = new_plate
    
    def how_fast(self):
        return self.speed
    
    def accelerate(self, time):
        self.speed += (self.acceleration*time)
    
    def brake(self, time):
        self.speed += (-10.0*time)
        if self.speed < 0:
            self.speed = 0


c = Car("Ford GT Turbo", "1999", "H4X0RZ", 5.5, 15.0, "blue", "HONK")
print(c.how_fast())# 5.5
c.accelerate(9.5)
print(c.how_fast()) # 148.0
c.brake(10.55)
print(c.how_fast()) # 42.5
c.brake(5.0)
print(c.how_fast()) # == 0.0
