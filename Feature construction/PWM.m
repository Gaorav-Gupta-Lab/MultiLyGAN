function PWM_pos = PWM(pos)%pos为输入的正类序列，neg为输入的负类序列
[m1,n1]=size(pos);%正类序列的大小
%A,R,N,D,C,Q,E,G,H,I,L,K,M,F,P,S,T,W,V,Y氨基酸排序
B=['A'    'R'    'N'    'D'    'C'    'Q'    'E'  ...
    'G'    'H'    'I'    'L'    'K'    'M'    'F' ...
    'P'    'S'    'T'    'W'    'V'    'Y'   'X'];%氨基酸序列对应的字母

C=[];D=[];
for i=1:n1%对pos进行列循环
    C=[];
    for k=1:21
        posi=find( pos(:,i)==B(k));%找到每列中的氨基酸对应B矩阵中的氨基酸的位置
        b=length(posi);%每列中每种氨基酸的个数
        c=b/m1;%每种氨基酸在该列所占的比例
        C=[C;c];%每列每种氨基酸在该列所占的比例 
    end
    D=[D,C];%pos矩阵中每种氨基酸在该列所占的比例，每行按照氨基酸序列排列（即第一行对应A,第二行对应R,以此类推）
end
 matrix_code1=[];  matrix_code2=[];  PWM_pos=[];
for i=1:m1%对行进行循环
    matrix_code2=[];%将每行的编码找到后，将matrix_code2清空用来存放下一行的编码
    %对pos按照行进行循环，找到该行每一列氨基酸对应的编码
    for j=1:n1
        for k=1:21
            if pos(i,j)==B(k)
                matrix_code1=[D(k,:)];%找到pos中每行每个氨基酸对应的D的行
            end
        end
        matrix_code2=[matrix_code2; matrix_code1];%pos每行氨基酸所对应的D的行，则生成一个n1*size(D,1)矩阵
        DIAG1=diag( matrix_code2);%取matrix_code2的对角元素
    end
    PWM_pos=[PWM_pos;DIAG1'];%pos矩阵的编码
end
end
