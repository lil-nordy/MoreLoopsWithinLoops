"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathaniel Neil Nate Nordquist.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------

    # key insight; don't build from the middle out! Start from the leftmost rectangle. Move the rectangle to the proper
    # row, build across the columns, then mutate to the next proper spot. Nested loops + reset statements!
    height = rectangle.get_height()
    width = rectangle.get_width()
    y1 = rectangle.get_lower_left_corner().y
    y2 = rectangle.get_upper_right_corner().y
    for k in range(n):
        x1 = rectangle.get_lower_left_corner().x - k * (width / 2)
        x2 = rectangle.get_upper_right_corner().x - k * (width / 2)
        for i in range(k + 1):
            rectangle_drawn = rg.Rectangle(rg.Point(x1, y1), rg.Point(x2, y2))
            rectangle_drawn.attach_to(window)
            x1 += width
            x2 += width
        y1 -= height
        y2 -= height
    window.render()
# Methods:
# This tested to see where the firs
# t rectangle will be drawn, and where you should build up from...
# rectangle.attach_to(window)
# window.render()

# Failed attempts:
# center_x = rectangle.get_center().x
# center_y = rectangle.get_center().y
# height = rectangle.get_height()
# width = rectangle.get_width()
# # corner1 is lower right, corner2 is upper left.
# corner1 = rg.Point(center_x + (width / 2), center_y + (height / 2))
# corner2 = rg.Point(center_x - (width / 2), center_y - (height / 2))
#
# for k in range(n):
#     for i in range(k):
#         draw_rectangle = rg.Rectangle(rg.Point(corner1.x + i * (width), corner1.y - k * (width)),
#                                       rg.Point(corner2.x - i * (width), corner2.y - k * (width)))
#         draw_rectangle.attach_to(window)
# window.render()




# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------

main()
