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

    def test_walker_energy_equal( self ):
        walkerEnergy = 7
        walker = Walker( energy = walkerEnergy, terrain = Terrain( 'terrain' ) )
        self.assertEqual( walker.energy, walkerEnergy )

    def test_walker_has_energy( self ):
        walker = Walker( energy = 4, terrain = Terrain( 'terrain' ) )
        self.assertTrue( walker.has_energy( 1 ) )
        self.assertTrue( walker.has_energy( 2 ) )
        self.assertTrue( walker.has_energy( 3 ) )
        self.assertTrue( walker.has_energy( 4 ) )

    def test_walker_dont_have_energy( self ):
        walker = Walker( energy = 4, terrain = Terrain( 'terrain' ) )
        self.assertFalse( walker.has_energy( 5 ) )
        self.assertFalse( walker.has_energy( 6 ) )
        self.assertFalse( walker.has_energy( 7 ) )
        self.assertFalse( walker.has_energy( 8 ) )

    def test_walker_waste_energy( self ):
        init_energy = 4
        waste_energy = 2
        expected_energy = init_energy - waste_energy

        walker = Walker( energy = init_energy, terrain = Terrain( 'terrain' ) )
        walker.waste_energy( waste_energy )
        self.assertEqual( walker.energy, expected_energy )

    def test_walker_rest( self ):
        init_energy = 4
        waste_energy = 2
        expected_energy = init_energy

        walker = Walker( energy = init_energy, terrain = Terrain( 'terrain' ) )
        walker.waste_energy( waste_energy )
        walker.rest()

        self.assertEqual( walker.energy, expected_energy )

    def test_walker_is_in_terrain( self ):
        init_energy = 4
        terrain = Terrain( 'terrain' )
        walker = Walker( energy = init_energy, terrain = terrain )
        self.assertTrue( terrain.is_occupied_by( walker ) )

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
