from remi.gui import *


class SvgGlass(Svg):

    def __init__(self, _width=None, _height=None):
        super(SvgGlass, self).__init__(width=_width, height=_height)
        self.width = _width
        self.height = _height
        self.polyList = []
        self.font_size = 15
        self.plot_inner_border = self.font_size
        # self.textYMin = SvgText(0, self.height + self.font_size, 'min')
        # self.textYMax = SvgText(0, 0, 'max')
        # self.textYMin.style['font-size'] = to_pix(self.font_size)
        # self.textYMax.style['font-size'] = to_pix(self.font_size)
        # self.append([self.textYMin, self.textYMax])

    def append_poly(self, polys):
        for poly in polys:
            self.append(poly)
            self.polyList.append(poly)
            poly.textXMin = SvgText(0, 0, 'actualValue')
            poly.textXMax = SvgText(0, 0, 'actualValue')
            poly.textYVal = SvgText(0, 0, 'actualValue')
            poly.textYVal.style['font-size'] = to_pix(self.font_size)

            poly.lineYValIndicator = SvgLine(0, 0, 0, 0)
            poly.lineXMinIndicator = SvgLine(0, 0, 0, 0)
            poly.lineXMaxIndicator = SvgLine(0, 0, 0, 0)
            self.append([poly.textXMin, poly.textXMax, poly.textYVal, poly.lineYValIndicator,
                         poly.lineXMinIndicator, poly.lineXMaxIndicator])

    def remove_poly(self, poly):
        self.remove_child(poly)
        self.polyList.remove(poly)
        self.remove_child(poly.textXMin)
        self.remove_child(poly.textXMax)
        self.remove_child(poly.textYVal)

    def remove_child(self, child):
        super().remove_child(child)
        self.polyList.remove(child)

    def append(self, child):
        super().append(child)
        self.polyList.append(child)

    def has_the_same_center(self, x: float, y: float, radius: float):
        remove_candidates = []
        for poly in self.polyList:
            if isinstance(poly, SvgCircle):
                e: SvgCircle = poly
                if ((float(e.attr_cx) - float(x)) ** 2 + (float(e.attr_cy) - float(y)) ** 2) <= float(radius) ** 2:
                    remove_candidates.append(e)
        return remove_candidates

    def clear(self):
        for svg_item in self.polyList[:]:
            self.remove_child(svg_item)
        self.polyList.clear()

    def render(self):
        # self.set_viewbox(-self.plot_inner_border, -self.plot_inner_border, self.width + self.plot_inner_border * 2,
        #                  self.height + self.plot_inner_border * 2)
        # if len(self.polyList) < 1:
        #     return
        # minX = min(self.polyList[0].plotData.coordsX)
        # maxX = max(self.polyList[0].plotData.coordsX)
        # minY = min(self.polyList[0].plotData.coordsY)
        # maxY = max(self.polyList[0].plotData.coordsY)

        # for poly in self.polyList:
        #     minX = min(minX, min(poly.plotData.coordsX))
        #     maxX = max(maxX, max(poly.plotData.coordsX))
        #     minY = min(minY, min(poly.plotData.coordsY))
        #     maxY = max(maxY, max(poly.plotData.coordsY))
        # self.textYMin.set_text('min:%s' % minY)
        # self.textYMax.set_text('max:%s' % maxY)

        # i = 1
        # for poly in self.polyList:
        #     scaledTranslatedYpos = (
        #         -poly.plotData.coordsY[-1] + maxY + (self.height-(maxY-minY))/2.0)

        #     textXpos = self.height / (len(self.polyList) + 1) * i

        #     poly.textXMin.set_text(str(min(poly.plotData.coordsX)))
        #     poly.textXMin.set_fill(poly.attributes['stroke'])

        #     poly.textXMin.set_position(-textXpos,
        #                                (min(poly.plotData.coordsX) - minX))
        #     poly.textXMin.attributes['transform'] = 'rotate(%s)' % (-90)
        #     poly.textXMax.set_text(str(max(poly.plotData.coordsX)))
        #     poly.textXMax.set_fill(poly.attributes['stroke'])
        #     poly.textXMax.set_position(-textXpos,
        #                                (max(poly.plotData.coordsX) - minX))

        #     poly.textXMax.attributes['transform'] = 'rotate(%s)' % (-90)
        #     poly.textYVal.set_text(str(poly.plotData.coordsY[-1]))
        #     poly.textYVal.set_fill(poly.attributes['stroke'])
        #     poly.textYVal.set_position(0, scaledTranslatedYpos)

        #     poly.lineYValIndicator.set_stroke(1, poly.attributes['stroke'])
        #     poly.lineXMinIndicator.set_stroke(1, poly.attributes['stroke'])
        #     poly.lineXMaxIndicator.set_stroke(1, poly.attributes['stroke'])
        #     poly.lineYValIndicator.set_coords(
        #         0, scaledTranslatedYpos, self.width, scaledTranslatedYpos)
        #     poly.lineXMinIndicator.set_coords((min(poly.plotData.coordsX) - minX), 0,
        #                                       (min(poly.plotData.coordsX) - minX), self.height)
        #     poly.lineXMaxIndicator.set_coords((max(poly.plotData.coordsX) - minX), 0,
        #                                       (max(poly.plotData.coordsX) - minX), self.height)
        #     poly.attributes['transform'] = ('translate(%s,%s)' % (-minX, maxY + (self.height-(maxY-minY))/2.0) +
        #                                     ' scale(%s,%s)' % ((1.0), -(1.0)))
        #     i = i + 1
        ...
