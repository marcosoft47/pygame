import cv2
import numpy as np

imagem = cv2.imread('perspectiva_1.jpeg')
largura, altura = 480, 270

pontos_1 = np.float32([[110, 78],[352, 70], [44, 222], [420, 208]])
pontos_2 = np.float32([[0,0], [largura,0],[0,altura],[largura,altura]])
matrix = cv2.getPerspectiveTransform(pontos_1,pontos_2)
imagem_corrigida = cv2.warpPerspective(imagem,matrix,(largura,altura))

cv2.circle(imagem,(int(pontos_1[0][0]),int(pontos_1[0][1])),5,(0,255,255),cv2.FILLED)
cv2.circle(imagem,(int(pontos_1[1][0]),int(pontos_1[1][1])),5,(255,0,0),cv2.FILLED)
cv2.circle(imagem,(int(pontos_1[2][0]),int(pontos_1[2][1])),5,(0,0,255),cv2.FILLED)
cv2.circle(imagem,(int(pontos_1[3][0]),int(pontos_1[3][1])),5,(0,255,0),cv2.FILLED)


cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem Corrigida", imagem_corrigida)
cv2.waitKey(0)