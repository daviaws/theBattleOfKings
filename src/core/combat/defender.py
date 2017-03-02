class Defender: 
	def __init__(self, defenses, health):
		self.health = health
	
	
	def getHealth(self):
		return self.health
	
	def calculateDefense(self, type, attacker = None):
	
	
	def beAttacked(self, damage, attacker = None):
		totalDamage = calculateDefense( damage, attacker)
		self.health -= totalDamage
			