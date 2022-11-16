import matplotlib.pyplot as plt
 
def plotMho(z1,zf_abs,zf_angle):
    figure, axes = plt.subplots()
    Drawing_uncolored_circle = plt.Circle( (0.6, 0.6 ),
                                        0.3 ,
                                        fill = False )
    
    axes.set_aspect( 1 )
    axes.add_artist( Drawing_uncolored_circle )
    plt.title( 'Circle' )
    plt.show()