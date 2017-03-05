import unittest

from core.walker import Walker
from core.terrain import Terrain
from core.movement import Movement

class TestWalker( unittest.TestCase ):

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
        origTerrain = Terrain( 'terrain_01' )
        destTerrain = Terrain( 'terrain_02' )
        movement = Movement( cost = 10, terrain = destTerrain )
        init_energy = 100
        expected_energy = init_energy - movement.cost

        walker = Walker( energy = init_energy, terrain = origTerrain )

        self.assertTrue( walker.move( movement ) )
        self.assertEqual( walker.energy, expected_energy )
        self.assertTrue( walker.is_at_terrain( destTerrain ) )
        self.assertFalse( walker.is_at_terrain( origTerrain ) )

    def test_walker_move_without_energy( self ):
        origTerrain = Terrain( 'terrain_01' )
        destTerrain = Terrain( 'terrain_02' )
        init_energy = 100
        expected_energy = init_energy

        movement = Movement( cost = 200, terrain = destTerrain )
        walker = Walker( energy = init_energy, terrain = origTerrain )

        self.assertFalse( walker.move( movement ) )
        self.assertEqual( walker.energy, expected_energy )
        self.assertTrue( walker.is_at_terrain( origTerrain ) )
        self.assertFalse( walker.is_at_terrain( destTerrain ) )

    def test_walker_move_occupied_terrain( self ):
        origTerrain = Terrain( 'terrain_01' )
        destTerrain = Terrain( 'terrain_02' )
        init_energy = 100
        expected_energy = init_energy

        walker = Walker( energy = init_energy, terrain = origTerrain )
        walkerEnemy = Walker( energy = init_energy, terrain = destTerrain )
        movement = Movement( cost = 10, terrain = destTerrain )

        self.assertFalse( walker.move( movement ) )
        self.assertEqual( walker.energy, expected_energy )
        self.assertTrue( walker.is_at_terrain( origTerrain ) )
        self.assertFalse( walker.is_at_terrain( destTerrain ) )

        self.assertTrue( walkerEnemy.is_at_terrain( destTerrain ) )

    def test_is_at_terrain( self ):
        myTerrain = Terrain( 'terrain_01' )
        otherTerrain = Terrain( 'terrain_02' )
        walker = Walker( energy = 100, terrain = myTerrain )

        self.assertTrue( walker.is_at_terrain( myTerrain ) )
        self.assertFalse( walker.is_at_terrain( otherTerrain ) )
        self.assertFalse( walker.is_at_terrain( None ) )

if __name__ == '__main__':
    unittest.main()
