import matplotlib.pyplot as plt

def plot_detection(img, img_detected):
    plt.figure(figsize=(8,4))
    plt.subplot(1,2,1)
    plt.title("Original")
    plt.imshow(img[:,:,::-1])
    plt.subplot(1,2,2)
    plt.title("Detecção")
    plt.imshow(img_detected[:,:,::-1])
    plt.show()
