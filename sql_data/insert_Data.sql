/*
  2023-10-29 15:48
  �û�: FxDr
  ������: FXX-LEGION
  ���ݿ�: community_web
  Ӧ�ó���: CommunityWeb 
*/
-- ��ׯ��Ϣ�����������
INSERT INTO community_web.excellentcase_villageinfo (province, population, resources, industry, terrain, village_size,
                                                     avg_income, village_name)
VALUES ('����ʡ', 12000000, '�ḻ��ũ��Ʒ�Ϳ����Դ', 'ũҵ�Ϳ�ҵ', '�������', '�еȹ�ģ', 48000.00, 'Village A'),
       ('�㶫ʡ', 18000000, '���������ҵ����ҵ��Դ', '����ҵ�ͷ���ҵ', 'ƽԭ����', '���ģ', 60000.00, 'Village B'),
       ('�Ĵ�ʡ', 15000000, '�ḻ��ˮ��Դ��ũҵ��Դ', 'ũҵ��ˮ��ҵ', 'ɽ�ص���', '�еȹ�ģ', 55000.00, 'Village C'),
       ('�㽭ʡ', 10000000, '�������Ϣ����������ҵ��Դ', '��Ϣ����������ҵ', '�غ�����', '�еȹ�ģ', 52000.00,
        'Village D'),
       ('�ӱ�ʡ', 13000000, '�ḻ��ũҵ��ú̿��Դ', 'ũҵ��ú̿��ҵ', 'ƽԭ����', '�еȹ�ģ', 50000.00, 'Village E');


# ���㰸���Ĳ����������
INSERT INTO excellentcase_excellentcase (title, experience, village_info_id, category)
VALUES ('��ҵ���˰���1', '����һ�����ڲ�ҵ���˵ľ���������', 1, 'industrial'),
       ('�˲����˰���1', '����һ�������˲����˵ľ���������', 2, 'talent'),
       ('�Ļ����˰���1', '����һ�������Ļ����˵ľ���������', 3, 'cultural'),
       ('��̬���˰���1', '����һ��������̬���˵ľ���������', 4, 'ecological'),
       ('��֯���˰���1', '����һ��������֯���˵ľ���������', 5, 'organizational');
