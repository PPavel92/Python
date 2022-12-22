from rewrite import rewrite
 
def remov_data(seek_out, data):
   seek_out_res = {}
   for i in range(len(data)):
    if seek_out in data[i]:
        seek_out_res[i] = data[i]
        print(seek_out_res)
   while (key_ := int(input('Введите Id контакта:_ '))) not in seek_out_res:
       print("Контакт с таким Id не наеден, ведите корректный Id: ") 
   else: 
       data.remove(seek_out_res[key_])
   rewrite(data)