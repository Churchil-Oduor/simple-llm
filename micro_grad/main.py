from neuron import Neuron
from neuron import Layer
from neuron import MLP
from engine import Value

xs = [
        [2, 3, -1],
        [24, 6, 6],
        [12, 4, 5],
        [23, 4, 6]

        ]


n = MLP(3, [4, 4, 1])
ys = [1, -1, 1, -1]
ypred = []
for k in range(1000):
    # forward_pass
    ypred = [n(x) for x in xs]

    loss = sum((yout - ygt)**2 for ygt, yout in zip(ys, ypred))


    # backward pass
    for p in n.parameters():
        p.grad = 0.0
    loss.backward()

    for p in n.parameters():
        p.data += -0.01 * p.grad

    print(k, loss.data)

print(ys)
print(ypred)
