function ReducedAlphabet_eight_code = ReducedAlphabet_eight(seq)
%A,R,N,D,C,Q,E,G,H,I,L,K,M,F,P,S,T,W,V,Y氨基酸排序
%每组中对应的氨基酸
matrix1=['E' 'D' '0'];
matrix2=['H' 'K' 'R'];
matrix3=['F' 'Y' 'W'];
matrix4=['N' 'Q' '0'];
matrix5=['S' 'T' '0'];
matrix6=['C' 'M' '0'];
matrix7=['A' 'G' 'P'];
matrix8=['I' 'L' 'V'];
matrix9=['X' '0' '0'];
[m,n]=size(seq);%seq矩阵的大小
le=size(matrix1,2);%每组向量的大小
matrix_code=[];matrix_code1=[];ReducedAlphabet_eight_code=[];
for i=1:m
    %对seq进行行循环
    matrix_code1=[];matrix_code=[];%将每行的编码找到后，将matrix_code和matrix_code1清空用来存放下一行的编码
    %对seq按照行进行循环，找到该行每一列氨基酸对应的编码
    for  j=1:n
        for k=1:le
            %判断seq中的氨基酸属于哪一组并对其进行编码
            if seq(i,j)==matrix1(k)
                matrix_code=[matrix_code,0 0 0 0 0 0 0 1 0];
            end
            if seq(i,j)==matrix2(k)
                matrix_code=[matrix_code,0 0 0 0 0 0 1 0 0];
            end
            if seq(i,j)==matrix3(k)
                matrix_code=[matrix_code,0 0 0 0 0 1 0 0 0];
            end
            if seq(i,j)==matrix4(k)
                matrix_code=[matrix_code,0 0 0 0 1 0 0 0 0];
            end
            if seq(i,j)==matrix5(k)
                matrix_code=[matrix_code,0 0 0 1 0 0 0 0 0];
            end
             if seq(i,j)==matrix6(k)
                matrix_code=[matrix_code,0 0 1 0 0 0 0 0 0];
             end
            if seq(i,j)==matrix7(k)
                matrix_code=[matrix_code,0 1 0 0 0 0 0 0 0];
            end
             if seq(i,j)==matrix8(k)
                matrix_code=[matrix_code,1 0 0 0 0 0 0 0 0];
             end
            if seq(i,j)==matrix9(k)
                matrix_code=[matrix_code,0 0 0 0 0 0 0 0 1];
            end
        end
        matrix_code1=[matrix_code];%seq每行的编码
    end
    ReducedAlphabet_eight_code=[ReducedAlphabet_eight_code;matrix_code1];%seq矩阵的编码
end
end


