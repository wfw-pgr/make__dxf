import ezdxf
from ezdxf import recover
from ezdxf.addons.drawing import matplotlib


def convert_dxf_to_png( inpFile=None, outFile=None ):
    
    try:
        dxf, auditor = recover.readfile( inpFile )
    except IOError as ioerror:
        print(ioerror)
        raise ioerror
    except ezdxf.DXFStructureError as dxf_structure_error:
        print(dxf_structure_error)
        raise dxf_structure_error

    if not auditor.has_errors:
        matplotlib.qsave(dxf.modelspace(), outFile )

if __name__ == "__main__":

    inpFile = "dxf/out.dxf"
    outFile = "png/out.png"
    
    convert_dxf_to_png( inpFile=inpFile, outFile=outFile )
