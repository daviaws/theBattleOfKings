maxx=4
maxy=4

def square_connections():
    ''' 
    1-> = step 1
    2-> = step 2
    1* = reference_id jump source
    *1 = reference_id jump destination

    The last step exiting a cell is the next state
    
    Algorithm flow:
    
            *1
    [ ]1-> [ ]
     2      |
     |      |
     v      v
    [ ]1-> [ ]
     2      |
     |      |
     v      v 
    [ ]1-> [ ]
     2      |
     |      |
     v      v 
    [ ]1-> [ ]
     2
     |
     v
     1*
    '''

    maxid = maxx * ( maxy - 1 )
    for x in range( maxx ):
        if x < maxx - 1:
            print( 'x: {} {}'.format( x, x + 1 ) ) #Bind line
        for y in range( x, maxid, maxy):
            next_y = y + maxy
            print( '    y: {} {}'.format(y, next_y) ) #Bind column
            if x < maxx - 1:
                print( '        x: {} {}'.format( next_y, next_y + 1 ) ) #Bind column to next

square_connections()
