import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

def main():
    path = "./img/lena.jpg"

    # Abre a imagem
    def get_image():
        img = mpimg.imread(path)
        return img

    # Converte a imagem escala de cinza
    def Converte_Cinza():
        R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
        img_gray = 0.2989 * R + 0.5870 * G + 0.1140 * B
        return img_gray




    # Converte a imagem escala Binária
    def Converte_PeB():
        img = cv2.imread(path, 2)
        ret, binI = cv2.threshold(img,  110, 255, cv2.THRESH_BINARY)
        return binI


    # Exibir a Redução de Dimensionalidade
    def exibir_Conver():

        titles = ['Imagem Original', 'Imagem em Cinza', 'Imagem Binária']
        images = [img, imgGray, binI]

        fig = plt.figure()


        for i in range(3):

            plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])

        fig.set_figheight(6)
        fig.set_figwidth(14)
        plt.show()



    img = get_image()
    imgGray= Converte_Cinza()
    binI = Converte_PeB()
    exibir_Conver()

if __name__ == "__main__":
    main()


