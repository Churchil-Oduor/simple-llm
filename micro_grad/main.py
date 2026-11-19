from engine import Value
from draw_network import draw_dot

x = Value(2)
y = Value(-3)
x *= y + Value(4)

draw_dot(x)

