types = char('Acetylation','Glycation','Malonylation','Methylation','Succinylation','Sumoylation','Ubiquitination')
res = ['Record'];
for i = 1:7
    tmp_type = types(i,:)
    if ~exist(['./delhomoseq40/',tmp_type],'dir')
        mkdir(['./delhomoseq40/',tmp_type]);
    end
    tmp_dir = ['./',strtrim(tmp_type),'/*pos*.csv'];
    tmp_file_list = dir(tmp_dir);
    [m,n] = size(tmp_file_list);
    for j = 1:m
        file_name = tmp_file_list(j).name;
        [id,site,seq]=textread(['./',strtrim(tmp_type),'/',file_name],'%s%s%s','delimiter', ',', 'headerlines ' , 1 );
        id = char(id);
        site = char(site);
        seq = char(seq);
        [Seq,ID,Site]=Delhomoseq(seq,id,site);
        data = table(ID, Site,Seq);
        new_name = [file_name(1:end-4),'_D40',file_name(end-3:end)];
        writetable(data,['./delhomoseq40/',strtrim(tmp_type),'/',new_name]);
        res = char(res,[file_name,' dim: ',num2str(size(id,1)), ' after_dim: ',num2str(size(ID,1))]);
        disp(['Has finished  ',file_name])
    end
end
fid=fopen('./delhomoseq40/recoder.txt','wt');
for i = 1:size(res,1)
    fprintf(fid,'%s\n',res(i,:));
end
fclose(fid);
        
        