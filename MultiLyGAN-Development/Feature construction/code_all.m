res = ['Record'];
coder = char('AAIndex','Binary','CKspace','FoldAmyloid','PWM','ReduceAlphabet')
for i = 1:size(coder,1)
    if ~exist(coder(i,:),'dir')
        mkdir(coder(i,:));
    end
end
for win = 3:25
    file_name = ['combine_filtered',num2str(win),'.csv']
    [id,site,seq,label]=textread(['./combine_filtered/',file_name],'%s%s%s%s','delimiter', ',', 'headerlines ' , 0 );
    id = char(id);
    site = char(site);
    seq = char(seq);
    % AAIndex
    AAIndexcode=AAIndex_fourteen(seq);
    data = table(AAIndexcode);
    new_name = [strtrim(coder(1,:)),'_',num2str(win),'.csv'];
    writetable(data,[strtrim(coder(1,:)),'/',new_name],'WriteVariableNames',false);
    % Binary
    Binarycode= Binary1(seq);
    data = table(Binarycode);
    new_name = [strtrim(coder(2,:)),'_',num2str(win),'.csv'];
    writetable(data,[strtrim(coder(2,:)),'/',new_name],'WriteVariableNames',false);
    % CKspace
    CKspacecode=CKspace(seq);
    data = table(CKspacecode);
    new_name = [strtrim(coder(3,:)),'_',num2str(win),'.csv'];
    writetable(data,[strtrim(coder(3,:)),'/',new_name],'WriteVariableNames',false);    
    % FoldAmyloid
    FoldAmyloid_code=FoldAmyloid(seq);
    data = table(FoldAmyloid_code);
    new_name = [strtrim(coder(4,:)),'_',num2str(win),'.csv'];
    writetable(data,[strtrim(coder(4,:)),'/',new_name],'WriteVariableNames',false);
    % PWM
    PWMcode = PWM(seq);
    data = table(PWMcode);
    new_name = [strtrim(coder(5,:)),'_',num2str(win),'.csv'];
    writetable(data,[strtrim(coder(5,:)),'/',new_name],'WriteVariableNames',false);
    % ReducedAlphabet
    ReducedAlphabet_eight_code = ReducedAlphabet_eight(seq);
    data = table(ReducedAlphabet_eight_code);
    new_name = [strtrim(coder(6,:)),'_',num2str(win),'.csv'];
    writetable(data,[strtrim(coder(6,:)),'/',new_name],'WriteVariableNames',false);
    disp(['Has finished  ',file_name])
end

        
        