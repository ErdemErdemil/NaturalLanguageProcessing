#IMPORTLAR
from warnings import filterwarnings
import pandas as pd
from nltk.corpus import stopwords
import nltk

#DOSYA OKUMALARI
filterwarnings('ignore')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df= pd.read_csv(r"C:\Users\erdem\OneDrive\Masaüstü\Erdem_Guven_Erdemil_212803063_NLP\entries.csv",encoding='ISO-8859-1',on_bad_lines='skip',lineterminator=';')

#NUMERIK IFADELERI TEMIZLEME
df['data'] = df['data'].str.replace('\d' , '')
df['data'] = df['data'].str.replace(r'[^\w\s]', '').str.replace(r'\b\d+\b', '', regex=True)


#OZEL KARAKTERLERI VE NOKTALAMA ISARETLERINI TEMIZLEME
df['data'] = df['data'].str.replace('[^\w\s]' , '')
df['data'] = df['data'].str.replace('[%<>\-]', '', regex=True)
df['data'] = df['data'].str.replace('.' , '')
df['data'] = df['data'].str.replace('"', '')


#TURKCE STOPWORD'LERI TEMIZLEME
gereksiz_kelimeler = ["a","acaba","alti","altmis","ama","ancak","arada","artik","asla","aslinda","aslinda","ayrica","az","bana","bazen","bazi","bazilari","belki","ben","benden","beni","benim","beri","bes","bile","bilhassa","bin","bir","biraz","bircogu","bircok","biri","birisi","birkac","birsey","biz","bizden","bize","bizi","bizim","boyle","boylece","bu","buna","bunda","bundan","bunlar","bunlari","bunlarin","bunu","bunun","burada","butun","cogu","cogunu","cok","cunku","da","daha","dahi","dan","de","defa","degil","diger","digeri","digerleri","diye","doksan","dokuz","dolayi","dolayisiyla","dort","e","edecek","eden","ederek","edilecek","ediliyor","edilmesi","ediyor","eger","elbette","elli","en","etmesi","etti","ettigi","ettigini","fakat","falan","filan","gene","geregi","gerek","gibi","gore","hala","halde","halen","hangi","hangisi","hani","hatta","hem","henuz","hep","hepsi","her","herhangi","herkes","herkese","herkesi","herkesin","hic","hicbir","hicbiri","i","icin","icinde","iki","ile","ilgili","ise","iste","itibaren","itibariyle","kac","kadar","karsin","kendi","kendilerine","kendine","kendini","kendisi","kendisine","kendisini","kez","ki","kim","kime","kimi","kimin","kimisi","kimse","kirk","madem","mi","mi","milyar","milyon","mu","mu","nasil","ne","neden","nedenle","nerde","nerede","nereye","neyse","nicin","nin","nin","niye","nun","nun","o","obur","olan","olarak","oldu","oldugu","oldugunu","olduklarini","olmadi","olmadigi","olmak","olmasi","olmayan","olmaz","olsa","olsun","olup","olur","olur","olursa","oluyor","on","on","ona","once","ondan","onlar","onlara","onlardan","onlari","onlarin","onu","onun","orada","ote","oturu","otuz","oyle","oysa","pek","ragmen","sana","sanki","sanki","sayet","sekilde","sekiz","seksen","sen","senden","seni","senin","sey","seyden","seye","seyi","seyler","simdi","siz","siz","sizden","sizden","size","sizi","sizi","sizin","sizin","sonra","soyle","su","suna","sunlari","sunu","ta","tabii","tam","tamam","tamamen","tarafindan","trilyon","tum","tumu","u","u","uc","un","un","uzere","var","vardi","ve","veya","ya","yani","yapacak","yapilan","yapilmasi","yapiyor","yapmak","yapti","yaptigi","yaptigini","yaptiklari","ye","yedi","yerine","yetmis","yi","yi","yine","yirmi","yoksa","yu","yuz","zaten","zira"]
df['data'] = df['data'].apply(lambda x: " ".join(x for x in str(x).split() if x not in gereksiz_kelimeler))
 
#KONUDAN BAGIMSIZ KELIMELERDEN ARINDIRMA
temp_df=pd.Series(' '.join(df['data']).split()).value_counts()
drops=temp_df[temp_df <= 1]
df['data'] = df["data"].apply(lambda x:" ".join(x for x in str(x).split() if x not in drops))

#DOSYAYI KAYDETME
df.to_csv('arindirilmisveri.csv', index=False)

#DOSYAYI ONIZLEME
df.head()