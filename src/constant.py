"""
constants
"""

ACTION_SELECT = 0
ACTION_MOVE_SELECTED = 1
ACTION_RECT = 20
ACTION_ELLIPSE = 21
ACTION_ARROW = 22
ACTION_LINE = 23
ACTION_FREEPEN = 24
ACTION_TEXT = 25
ACTION_UNDO = 26
ACTION_SAVE = 27
ACTION_CANCEL = 28
ACTION_SURE = 29

DRAW_ACTION = [ACTION_RECT, ACTION_ELLIPSE, ACTION_ARROW, ACTION_LINE, ACTION_FREEPEN, ACTION_TEXT]

ON_THE_LEFT_SIDE = 10
ON_THE_RIGHT_SIDE = 11
ON_THE_UP_SIDE = 12
ON_THE_DOWN_SIDE = 13
ON_THE_TOP_LEFT_CORNOR = 14
ON_THE_TOP_RIGHT_CORNOR = 15
ON_THE_BOTTOM_LEFT_CORNOR = 16
ON_THE_BOTTOM_RIGHT_CORNOR = 17
INSIDE_AREA = 18
OUTSIDE_AREA = 19

# the range of judging if your mouse is on the side of selected area
ERRORRANGE = 6

PENCOLOR = '#ff0000'  #  red
PENSIZE = 1
