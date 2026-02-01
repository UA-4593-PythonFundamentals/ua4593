
def areas():
    def rectangle(width, longht):
        area_rectangle = width * longht
        return(area_rectangle)
    def triangle(base, hight):
        area_triangle = 0.5*base*hight
        return(area_triangle)
    def circle(radius, pi = 3.14):
        area_circle = radius**2*pi
        return(area_circle)
    return rectangle, triangle, circle
rect, tri, cir = areas()
print(rect(5, 10))
print(tri(4, 8))
print(cir(7))



