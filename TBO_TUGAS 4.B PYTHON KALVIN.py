#.TUGAS 4.B - Kuliah TBO
#.Dosen - Arnes Vandika, M.Kom
#. IF NESTED (IF BERSARANG)
print("NAMA = NIKOLAS KALVIN");
print("NPM = 21421002");
#
#input data
var_umur = input("Berapa Umur Anda : ")

#Statement IF Bersarang
if (int(var_umur) < 25) :
    if (int(var_umur) < 20) :
        print("Anda Masih Sekolah")
    else :
      print("Anda Sudah Bekerja")
elif(int(var_umur) > 25) :
   if (int(var_umur) < 30) :
      print("Harusnya Anda Sudah Menikah")
   else :
      print("Anda Sudah Punya Anak 3")
else :
   print("Maaf, Jawaban Anda Salah")
