function PWM_pos = PWM(pos)%posΪ������������У�negΪ����ĸ�������
[m1,n1]=size(pos);%�������еĴ�С
%A,R,N,D,C,Q,E,G,H,I,L,K,M,F,P,S,T,W,V,Y����������
B=['A'    'R'    'N'    'D'    'C'    'Q'    'E'  ...
    'G'    'H'    'I'    'L'    'K'    'M'    'F' ...
    'P'    'S'    'T'    'W'    'V'    'Y'   'X'];%���������ж�Ӧ����ĸ

C=[];D=[];
for i=1:n1%��pos������ѭ��
    C=[];
    for k=1:21
        posi=find( pos(:,i)==B(k));%�ҵ�ÿ���еİ������ӦB�����еİ������λ��
        b=length(posi);%ÿ����ÿ�ְ�����ĸ���
        c=b/m1;%ÿ�ְ������ڸ�����ռ�ı���
        C=[C;c];%ÿ��ÿ�ְ������ڸ�����ռ�ı��� 
    end
    D=[D,C];%pos������ÿ�ְ������ڸ�����ռ�ı�����ÿ�а��հ������������У�����һ�ж�ӦA,�ڶ��ж�ӦR,�Դ����ƣ�
end
 matrix_code1=[];  matrix_code2=[];  PWM_pos=[];
for i=1:m1%���н���ѭ��
    matrix_code2=[];%��ÿ�еı����ҵ��󣬽�matrix_code2������������һ�еı���
    %��pos�����н���ѭ�����ҵ�����ÿһ�а������Ӧ�ı���
    for j=1:n1
        for k=1:21
            if pos(i,j)==B(k)
                matrix_code1=[D(k,:)];%�ҵ�pos��ÿ��ÿ���������Ӧ��D����
            end
        end
        matrix_code2=[matrix_code2; matrix_code1];%posÿ�а���������Ӧ��D���У�������һ��n1*size(D,1)����
        DIAG1=diag( matrix_code2);%ȡmatrix_code2�ĶԽ�Ԫ��
    end
    PWM_pos=[PWM_pos;DIAG1'];%pos����ı���
end
end
