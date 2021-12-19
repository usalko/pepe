from remi.gui import *

class SvgComposedPoly(SvgGroup):
    """ A group of polyline and circles
    """
    def __init__(self, x, y, maxlen, stroke, color, *args, **kwargs):
        super(SvgComposedPoly, self).__init__(*args, **kwargs)
        self.maxlen = maxlen
        self.plotData = SvgPolyline(self.maxlen)
        self.plotData.set_fill('none')
        self.append(self.plotData)
        self.set_stroke(stroke, color)
        self.set_fill(color)
        self.circle_radius = stroke
        self.circles_list = list()
        self.x_factor = 1.0
        self.y_factor = 1.0

    def add_coord(self, x, y):
        """ Adds a coord to the polyline and creates another circle
        """
        x = x*self.x_factor
        y = y*self.y_factor
        self.plotData.add_coord(x, y)
        self.circles_list.append(SvgCircle(x, y, self.circle_radius))
        self.append(self.circles_list[-1])
        if len(self.circles_list) > self.maxlen:
            self.remove_child(self.circles_list[0])
            del self.circles_list[0]

    def scale(self, x_factor, y_factor):
        self.x_factor = x_factor/self.x_factor
        self.y_factor = y_factor/self.y_factor
        self.plotData.attributes['points'] = "" 
        tmpx = collections.deque()
        tmpy = collections.deque()

        for c in self.circles_list:
            self.remove_child(c)
        self.circles_list = list()

        while len(self.plotData.coordsX)>0:
            tmpx.append( self.plotData.coordsX.popleft() )
            tmpy.append( self.plotData.coordsY.popleft() )

        while len(tmpx)>0:
            self.add_coord(tmpx.popleft(), tmpy.popleft())
            
        self.x_factor = x_factor
        self.y_factor = y_factor
        
