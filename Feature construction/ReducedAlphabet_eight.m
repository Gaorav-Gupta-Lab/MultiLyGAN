function ReducedAlphabet_eight_code = ReducedAlphabet_eight(seq)
%A,R,N,D,C,Q,E,G,H,I,L,K,M,F,P,S,T,W,V,Y����������
%ÿ���ж�Ӧ�İ�����
matrix1=['E' 'D' '0'];
matrix2=['H' 'K' 'R'];
matrix3=['F' 'Y' 'W'];
matrix4=['N' 'Q' '0'];
matrix5=['S' 'T' '0'];
matrix6=['C' 'M' '0'];
matrix7=['A' 'G' 'P'];
matrix8=['I' 'L' 'V'];
matrix9=['X' '0' '0'];
[m,n]=size(seq);%seq����Ĵ�С
le=size(matrix1,2);%ÿ�������Ĵ�С
matrix_code=[];matrix_code1=[];ReducedAlphabet_eight_code=[];
for i=1:m
    %��seq������ѭ��
    matrix_code1=[];matrix_code=[];%��ÿ�еı����ҵ��󣬽�matrix_code��matrix_code1������������һ�еı���
    %��seq�����н���ѭ�����ҵ�����ÿһ�а������Ӧ�ı���
    for  j=1:n
        for k=1:le
            %�ж�seq�еİ�����������һ�鲢������б���
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
        matrix_code1=[matrix_code];%seqÿ�еı���
    end
    ReducedAlphabet_eight_code=[ReducedAlphabet_eight_code;matrix_code1];%seq����ı���
end
end


