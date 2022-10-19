import numpy as np

# ========================================================= #
# ===  make__points.py                                  === #
# ========================================================= #

def make__points():

    xc_, yc_, rc_, sw_ = 0, 1, 2, 3

    # ------------------------------------------------- #
    # --- [2] make circle centers1                  --- #
    # ------------------------------------------------- #
    radius   = 3.00e-3
    pitch_y  = 5.00e-3 * 2
    LJ       = 10
    xMin     = 8.66e-3 * 2 * (-5)
    xMax     = 8.66e-3 * 2 * (+5)
    yMin     = 30.0e-3
    yMax     = yMin + pitch_y * (LJ-1)
    
    xcoord1  = np.zeros( (LJ,) ) + xMin
    xcoord2  = np.zeros( (LJ,) ) + xMax
    ycoord   = np.linspace( yMin, yMax, LJ )
    zcoord   = np.zeros( (LJ,) ) + radius
    fcoord   = np.ones ( (LJ,) )
    coord1   = np.concatenate( [xcoord1[:,None],ycoord[:,None],\
                                zcoord[:,None],fcoord[:,None]], axis=1 )
    coord2   = np.concatenate( [xcoord2[:,None],ycoord[:,None],\
                                zcoord[:,None],fcoord[:,None]], axis=1 )
    circles  = np.concatenate( [coord1,coord2], axis=0 )
    print( circles.shape )
    
    # ------------------------------------------------- #
    # --- [4] save in a file                        --- #
    # ------------------------------------------------- #
    import nkUtilities.save__pointFile as spf
    outFile   = "dat/circles3.dat"
    spf.save__pointFile( outFile=outFile, Data=circles )


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    make__points()
