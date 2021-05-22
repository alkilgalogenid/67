x=[random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600)]
y=[random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600),random (600)]
def setup():
    size(600,400)
    strokeWeight(30)
    stroke(255)
    frameRate(10)
    
def draw():
    background(100)
    global y
    for a in range (15):
        point (x[a],y[a])
        y[a]=y[a]+1
        if y[a]==400:
            y[a]=0
