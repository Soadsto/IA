pkg load image
img = imread("bob.jpg");
imshow(img)
pause(2)
gris = rgb2gray(img);
imshow(gris)
pause(2)
cont = zeros(256);
[m, n] = size(gris);
for i=1:m
  for j=1:n
      cont(gris(i,j)+1) = cont(gris(i,j)+1) +1;
  endfor
endfor
bar(0:255, cont)

#z = reshape(gris, m*n,1);
#hist(z, 256)