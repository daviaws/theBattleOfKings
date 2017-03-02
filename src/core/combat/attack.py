class Attack:
	
	def __init__( self, name, damage, targeter  ):
		self.damageList = []
		self.damageList.append(damage)
		self.targeter = targeter
		self.name = name
		
	def __eq__ (self, other ):
		return self.name == other.name
		
	def __it__ (self , other ):
		return self.name < other.name
	
	
	def attack ( self, attacker ):
		targets = targeter.getTargets( attacker )
		for target in targets:
			self.attackTarget( attacker, target )
		
	def attackTarget(self ,attacker, defender):
		for dam in damageList:
			damage = attacker.calculateDamage( dam )
			defender.beAttacked ( attacker, damage )
			
		
    