'''
Created on 102/4/7

@author: Ihc
'''
from 言語資料庫.公用資料 import 資料庫連線
from 言語資料庫.公用資料 import 語句
from 言語資料庫.公用資料 import 國語腔口
from 剖析相關工具.剖析工具 import 剖析工具
from 剖析相關工具.官方剖析工具 import 官方剖析工具
from 剖析相關工具.自設剖析工具 import 自設剖析工具
from symbol import except_clause

揣國語語句資料 = 資料庫連線.prepare('SELECT ' +
	'"流水號","來源","種類","腔口","地區","年代","組合","型體","音標","調變","音變"' +
	'FROM "言語"."文字" WHERE "種類"=$1 AND "腔口"=$2 ORDER BY "流水號"')(語句, 國語腔口)

資料庫加文字佮組合 = lambda 斷詞目標流水號, 來源, 種類, 年代, 型體: 資料庫連線.prepare(
	'INSERT INTO "言語"."斷詞暫時表" ' +
    '("斷詞目標流水號","來源","種類","年代","型體") ' +
    'VALUES ($1,$2,$3,$4,$5) ')(斷詞目標流水號, 來源, 種類, 年代, 型體)

揣剖析過遏袂 = lambda 斷詞目標流水號,剖析版本:資料庫連線.prepare('SELECT ' + '"斷詞目標流水號"' +
	'FROM "言語"."斷詞暫時表" WHERE "斷詞目標流水號"=$1 AND "來源"=$2 LIMIT 1').first(斷詞目標流水號,剖析版本)

剖析版本='線上測試版本'
剖析版本='全部分析版本'
if __name__ == '__main__':
	if 剖析版本=='線上測試版本':
		工具 = 官方剖析工具()
	else:
		工具 = 自設剖析工具()
# 	print(工具.剖析('我想吃飯。我想吃很多飯。'))
	for 流水號, 來源, 種類, 腔口, 地區, 年代, 組合, 型體, 音標, 調變, 音變 in 揣國語語句資料:
		if 揣剖析過遏袂(流水號,剖析版本)!=None:
			continue
		print(流水號)
		try:
			剖析結果 = 工具.剖析(型體)
		except UnicodeEncodeError:
			continue
		else:
			for 一个結果 in 剖析結果:
				資料庫加文字佮組合(流水號, 剖析版本, '斷詞', 102, 一个結果)
		# 			print(型體)
		# 			print(一个結果)

