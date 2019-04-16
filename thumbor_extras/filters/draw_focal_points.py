from thumbor.filters import BaseFilter, filter_method

class Filter(BaseFilter):
    @filter_method()
    def draw_focal_points(self):
        img = self.engine.image
        for focal_point in self.context.request.focal_points:
            width = focal_point.width
            height = focal_point.height
            x = focal_point.x - (width / 2)
            y = focal_point.y - (height / 2)
            self.engine.draw_rectangle(x, y, width, height)
