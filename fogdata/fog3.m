img_name = '00070.jpg';
 
    I=imread(img_name);
    I1 = imresize(I,[200,300]);
    %subplot(2,2,1);
    %figure(1);
    %imshow(I1);
    %imagesc(I1);
    I1=double(I1)/255;
    I = I1;

    Im_dealt = I;
    [row,col,z] = size(Im_dealt);
    landline = 0;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Iw = I;
    A = 0.8;
    m = 100;
    n = 300;
    tidx = 2;
	beta = 0.05;  %:0.05:0.15  % for beta = 0.20:0.05:0.30

    for i=1:3
        for j=landline+1:row
            for l=1:col
                d(j,l) = 1/((j-landline)^.05 + 0.0001);
                d2(j,l) = d(j,l)*8;
                if j < landline
                    d(j,l) = -0.04*landline + 18;
                    td(j,l) = exp(-beta*d(j,l));
                    Iw(j,l,i) = I(landline,l,i)*td(landline,l) + A*(1-td(j,l));

                else
                    d(j,l) = -0.04*sqrt((j-m).^2+(l-n).^2) + 17;
                    td(j,l) = exp(-beta*d(j,l));
                    Iw(j,l,i) = I(j,l,i)*td(j,l) + A*(1-td(j,l));
                end

            end
        end
    end
    for k = 1:landline
        for kj = 1:col
            Iw(k,kj,: ) = Iw(landline+1,100,:);
        end
    end
    %figure(tidx);imshow(Iw);
    filename = strcat('.\', '005.jpg');
    %filename = filename{1};
    imwrite(Iw,filename);

    a = sprintf('%s %f','beta=',beta);
    title(a);
    tidx = tidx+1;