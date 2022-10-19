import os, sys, subprocess
import ezdxf
import numpy as np

# ========================================================= #
# ===  make__dxf.py                                     === #
# ========================================================= #

def make__dxf( holeFile="dat/circles.dat", edgeFile="dat/edge.dat", outFile="out.dxf", delimiter=None ):

    xc_, yc_, rc_, sw_= 0, 1, 2, 3

    # ------------------------------------------------- #
    # --- [1] open project                          --- #
    # ------------------------------------------------- #
    doc   = ezdxf.new( "R2010" )
    model = doc.modelspace()

    # ------------------------------------------------- #
    # --- [2] draw body line                        --- #
    # ------------------------------------------------- #
    with open( edgeFile, "r" ) as f:
        points = np.loadtxt( f, delimiter=delimiter )
    for ik in np.arange( points.shape[0]-1 ):
        line = model.add_line(  ( points[ik  ,xc_],points[ik  ,yc_] ), \
                                ( points[ik+1,xc_],points[ik+1,yc_] )  )
        
    # ------------------------------------------------- #
    # --- [3] draw circles                          --- #
    # ------------------------------------------------- #
    with open( holeFile, "r" ) as f:
        circles = np.loadtxt( f, delimiter=delimiter )
    randomize = + 0.8
    if ( randomize > 0.0 ):
        nCircles    = circles.shape[0]
        nTrue       = int( nCircles * randomize )
        nFalse      = int( nCircles - nTrue     )
        sws         = np.concatenate( [ np.ones ( (nTrue ,) ), \
                                        np.zeros( (nFalse,) ) ] )
        index       = np.arange( nCircles )
        np.random.shuffle( index )
        sws         = sws[index]
        circles[:,sw_] = np.copy( sws )
    else:
        nCircles       = circles.shape[0]
        circles[:,sw_] = np.ones( (nCircles,) )
        
    for acircle in circles:
        if ( acircle[sw_] == 1 ):
            model.add_circle( acircle[xc_:yc_+1], radius=acircle[rc_] )
        #     model.add_circle( acircle[xc_:yc_+1], radius=acircle[rc_] )

    # ------------------------------------------------- #
    # --- [4] save in a file                        --- #
    # ------------------------------------------------- #
    doc.saveas( outFile )
    return()


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):

    edgeFile = "dat/edge.dat"
    holeFile = "dat/circles.dat"
    outFile  = "dxf/out.dxf" 
    make__dxf( edgeFile=edgeFile, holeFile=holeFile, outFile=outFile )
    
