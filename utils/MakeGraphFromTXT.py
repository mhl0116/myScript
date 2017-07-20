import ROOT

def MakeGraph(txtfile, cut, xIndex1, xIndex2, yIndex, yErrIndex=-1):

    data = [line.strip().split() for line in open(txtfile, 'r') if cut in line]
    print txtfile, cut
    print data
    x,y,xErr,yErr = array('f'),array('f'),array('f'),array('f')
    for i in range(len(data)):
        x.append( (float(data[i][xIndex1]) + float(data[i][xIndex2]) )/2 )
        xErr.append((float(data[i][xIndex2]) - float(data[i][xIndex1]) )/2)
        y.append( float(data[i][yIndex]) )
        if yErrIndex == -1:
           yErr.append( 0 )
        else:
           yErr.append( float(data[i][yErrIndex]) )
    gr = TGraphErrors(len(x),x,y,xErr,yErr)
    return gr

