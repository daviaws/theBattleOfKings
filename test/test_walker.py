import unittest

from core.walker import Walker
from core.terrain import Terrain
from core.movement import Movement

class TestWalker( unittest.TestCase ):

    def setUp( self ):
        self.terrain = Terrain('my_test')
        self.terrain1 = Terrain('my_test2')
        self.energy = 7
        self.energy1 = 3
        self.terrain_to_move = Terrain('to_move')
        self.energy_to_move = 4
        self.movement = Movement( self.energy_to_move, self.terrain_to_move )
        self.occupied_movement = Movement( self.energy_to_move, self.terrain1 )
        self.walker = Walker( self.energy, self.terrain )
        self.walker1 = Walker( self.energy1, self.terrain1 )

    def test_walker_energy( self ):
        self.assertIsNotNone( self.walker.energy )

    def test_walker_energy_equal( self ):
        self.assertEqual( self.walker.energy, self.energy )

    def test_walker_has_energy( self ):
        self.assertTrue( self.walker.has_energy(self.energy_to_move) )

    def test_walker_dont_have_energy( self ):
        self.assertFalse( self.walker1.has_energy(self.energy_to_move) )

    def test_walker_waste_energy( self ):
        energy = self.walker.energy
        total = energy - self.energy_to_move
        self.walker.waste_energy(self.energy_to_move)
        self.assertEqual( self.walker.energy, total )

    def test_walker_rest( self ):
        energy = self.walker.energy
        self.walker.waste_energy(self.energy_to_move)
        self.walker.rest()
        self.assertEqual( self.walker.energy, energy )

    def test_walker_is_in_terrain( self ):
        self.assertIs( self.walker.terrain, self.terrain)
        self.assertIs( self.terrain.occupant, self.walker)

    def test_walker_occupy_terrain( self ):      
        self.walker.occupy( self.terrain_to_move )
        self.assertIs( self.walker.terrain, self.terrain_to_move)
        self.assertIs( self.terrain_to_move.occupant, self.walker)

    def test_walker_move( self ):
        final_energy = self.walker.energy - self.energy_to_move
        self.assertTrue( self.walker.move( self.movement ) )
        self.assertEqual( self.walker.energy, final_energy )
        self.assertIsNone( self.terrain.occupant )
        self.assertIs( self.walker.terrain, self.terrain_to_move)
        self.assertIs( self.terrain_to_move.occupant, self.walker)

    def test_walker_move_without_energy( self ):
        final_energy = self.walker1.energy
        self.assertFalse( self.walker1.move( self.movement ) )
        self.assertEqual( self.walker1.energy, final_energy )
        self.assertIsNone( self.terrain_to_move.occupant )
        self.assertIs( self.walker1.terrain, self.terrain1)
        self.assertIs( self.terrain1.occupant, self.walker1)

    def test_walker_move_occupied_terrain( self ):
        final_energy = self.walker.energy
        self.assertFalse( self.walker.move( self.occupied_movement ) )
        self.assertEqual( self.walker.energy, final_energy )
        self.assertIs( self.terrain1.occupant, self.walker1 )
        self.assertIs( self.walker.terrain, self.terrain)
        self.assertIs( self.terrain.occupant, self.walker)

if __name__ == '__main__':
    unittest.main()
