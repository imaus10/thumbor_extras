from thumbor.filters import BaseFilter, filter_method

class Filter(BaseFilter):
    @filter_method()
    def draw_focal_points(self):
        img = self.engine.image
        for focal_point in self.context.request.focal_points:
            self.engine.draw_rectangle(focal_point.x, focal_point.y, focal_point.width, focal_point.height)
