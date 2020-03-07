import matplotlib.pyplot as plt

def getImageData(filepath):
    return plt.imread(filepath)

def saveImage(image, filepath):
    plt.imsave(filepath, image)
