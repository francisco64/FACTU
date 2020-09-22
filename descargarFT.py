import fasttext
import fasttext.util

try:
    fasttext.util.download_model('es', if_exists='ignore')
    ft = fasttext.load_model('cc.es.300.bin')
    fasttext.util.reduce_model(ft, 100)
    ft.save_model('cc.es.100.bin')
except:
  print("An exception occurred")
