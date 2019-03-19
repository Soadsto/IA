pkg load image
#Cargamos la imagen a memoria
img = imread("C:\\Users\\Owl\\OneDrive\\Documentos\\Programas\\Inteligencia Artificial\\Octave\\etiquetado.bmp");
imshow(img);
title("Imagen a color");
pause(1);
#Conversion a imagen a B&W con 1 y 0 
img = im2bw(img);
imshow(img);
title("Imagen en B&W");
#Conteo de objetos
[l, n] = bwlabel(img);
#Recorrer todos los objetos, por renglones y columna
l
function perimetro = conteoPerimetro(l, n)
  [r, c] = size(l);
  legal = 0;
  perimetro = zeros(n);
  for i = 1: n
    for j = 1: r
      for k = 1: c
        legal = vecindad4(i, j, k, l);
        if (legal == 1)
          perimetro(i)++;
        endif
      endfor
    endfor
  endfor  
endfunction
###################################
function area = conteoArea(l, n)
  [r, c] = size(l);
  area = zeros(n);
  for i = 1: n
    for j = 1: r
      for k = 1: c
        if (l(j, k) == i)
          area(i)++;
        endif
      endfor
    endfor
  endfor
endfunction
###################################
function legal = vecindad4(n, i, j, l)
  [r, c] = size(l);
  legal = 0;
  if (l(i, j) != n)
    return
  endif
  if (i - 1 > 1) #Vecino de arriba
    if(l(i - 1, j) != n)
      legal = 1;
    endif
  endif
  if (j + 1 < c) #Vecino de la derecha
    if (l(i, j + 1) != n)
      legal = 1;
    endif
  endif
  if (i + 1 < r) #Vecino de abajo
    if (l(i + 1, j) != n)  
      legal = 1;
    endif
  endif
  if (j - 1 > 1) #Vecino de la izquierda
   if (l(i, j - 1) != n)
      legal = 1;
    endif
  endif
endfunction
###################################
area = conteoArea(l, n);
#Impresion de las n areas
for i = 1: n
  printf("El area del objeto: %d\tes = %d", i, area(i));
  printf("\n");
endfor
#Impresion de los n perimetros
perimetro = conteoPerimetro(l, n);
for i = 1: n
  printf("El perimetro del objeto: %d\tes = %d", i, perimetro(i));
  printf("\n");
endfor