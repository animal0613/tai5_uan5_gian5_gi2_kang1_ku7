from 資料庫.資料庫連線 import 資料庫連線

class 辭典條目:
	揣言語層的字詞 = lambda self, 腔口, 語言層:資料庫連線.prepare('SELECT ' + 
		'DISTINCT "乙流水號" FROM "言語"."關係" ' + 
		'WHERE "乙對甲的關係類型"=$1 AND "關係性質"=$2 '
		'ORDER BY "乙流水號"')('仝字，用佇無仝言語層', 語言層)
	
	揣腔口資料 = lambda self, 腔口:資料庫連線.prepare('SELECT ' + 
		'"子"."流水號","子"."型體","子"."音標" ' + 
		'FROM "言語"."文字" AS "子" ' + 
		' WHERE "子"."腔口" LIKE $1 ' + 
		' AND "子"."種類"=\'字詞\' ' + 
		'ORDER BY "子"."流水號"')(腔口 + '%')
		
	揣腔口字詞資料 = lambda self, 腔口:資料庫連線.prepare('SELECT ' + 
		'"子"."流水號","子"."型體","子"."音標" ' + 
		'FROM "言語"."文字" AS "子" ' + 
		' WHERE "子"."腔口" LIKE $1 ' + 
		'ORDER BY "子"."流水號"')(腔口 + '%')
	
# 	揣腔口型體資料 = lambda self,腔口, 型態:資料庫連線.prepare('SELECT ' +
# 		'"子"."流水號","子"."型體","子"."音標" ' +
# 		'FROM "言語"."文字" AS "子" ' +
# 		' WHERE "子"."腔口" LIKE $1 AND "子"."型體"=$2 '+
# 		' AND "子"."流水號"<1164335'+#莫拆字結果
# 		'ORDER BY "子"."流水號"')(腔口+'%', 型態)
