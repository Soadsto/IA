#pkg load image
img = imread()
imshow(img)
title("Imagen en color")
pause(4)
gris = rgb2gray(img);
imshow(gris)
title("Imagen en esacala de grises");
pause(4)
[nRen, nCol] = size(gris);
bn = zeros(nRen, nCol);
for i = 1: nRen
  for j = 1:nCol
    if gris(i , j) > 128
      bn(i, j) = 255;
    endif
  endfor
endfor
imshow(bn)
title("En blanco y negro con umbral");
pause(3)
tmp = conv2 (gris, ones (5, 5) / 25, "same");
tmp2 = uint8(tmp);
imshow(tmp2);
title("Imagen suavizada con filtro 5*5");