# this module will be imported in the into your flowgraph

f1 = 2800e6
f2 = 3200e6
# f1 = 2800e6
# f2 = 3200e6

f=f1
NR_OF_STEPS = 200
step = (f2 - f1) / NR_OF_STEPS
#counter = 0

def sweeper(prob_lvl):
    global f1, f2, f, step#, counter
    if prob_lvl:
        f += step
        #counter +=1
    if f >= f2:
        f = f1
        #counter = 0
    #print(bool(prob_lvl), counter)
    return f