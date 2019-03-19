pkg load image;
img = imread("C:\\Users\\Owl\\OneDrive\\Documentos\\Programas\\Inteligencia Artificial\\Octave\\figuras bordes.png");
imshow(img);
title("Imagen a color,");
pause(0.5);
[R, C, M] = size(img);
for i = 1: R
  for j = 1: C  
    printf("La matriz en:\n")
    disp(R),disp(C)
    img(R, C, 1)
    img(R, C, 2)
    img(R, C, 3)
    printf("\n")
    if (img(R, C, 1) != 255 && img(R, C, 2) != 255 && img(R, C, 3) != 255)
      img(R, C, 1) = 0;
      img(R, C, 2) = 0;
      img(R, C, 3) = 0;
      endif
    endfor
endfor   
imshow(img);
title("Imagen en blanco y negro");
pause(2);