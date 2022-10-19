import numpy as np

# ========================================================= #
# ===  make__points.py                                  === #
# ========================================================= #

def make__points():

    xc_, yc_, rc_, sw_ = 0, 1, 2, 3
    
    # ------------------------------------------------- #
    # --- [1] parameters                            --- #
    # ------------------------------------------------- #
    radius   = 3.0e-3
    xoffset  = 8.66e-3 * 2 * (-4)
    yoffset  = 10.0e-3
    pitch_x  = 8.66e-3 * 2
    pitch_y  = 5.00e-3 * 2
    LI       =  9
    LJ       = 12
    nCirc    = 100
    xMin     = xoffset
    xMax     = xMin + pitch_x * (LI-1)
    yMin     = yoffset
    yMax     = yMin + pitch_y * (LJ-1)

    # ------------------------------------------------- #
    # --- [2] make circle centers1                  --- #
    # ------------------------------------------------- #
    import nkUtilities.equiSpaceGrid as esg
    x1MinMaxNum = [ xMin, xMax, LI ]
    x2MinMaxNum = [ yMin, yMax, LJ ]
    x3MinMaxNum = [  0.0,  1.0,  1 ]
    ret         = esg.equiSpaceGrid( x1MinMaxNum=x1MinMaxNum, x2MinMaxNum=x2MinMaxNum, \
                                     x3MinMaxNum=x3MinMaxNum, returnType = "point" )
    ret[:,rc_]  = radius
    sws         = np.concatenate( [np.ones( nCirc, ), np.zeros( (LI*LJ-nCirc,) ) ] )
    index       = np.arange( sws.shape[0] )
    np.random.shuffle( index )
    sws         = sws[index]
    circles     = np.concatenate( [ret,sws[:,None]], axis=1 )

    # ------------------------------------------------- #
    # --- [4] save in a file                        --- #
    # ------------------------------------------------- #
    import nkUtilities.save__pointFile as spf
    outFile   = "dat/circles1.dat"
    spf.save__pointFile( outFile=outFile, Data=circles )


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    make__points()
