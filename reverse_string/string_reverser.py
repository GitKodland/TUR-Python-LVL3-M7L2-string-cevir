# Metni tersine çeviren fonksiyon
def reverse_string(s):
    # Görev: Fonksiyonu burada tamamlayın
    '''
    Sonucu saklamak için boş bir string/metin oluşturun
    Girdi olarak alınan metindeki her karakteri sırayla dolaşın
    Mevcut karakteri sonuç stringin başına ekleyin
    Bu şekilde, son karakter ilk olur, sondan bir önceki ikinci olur ve böyle devam eder
    Return the reversed string Ters çevrilmiş stringi geri döndürün
    '''
    return


# Programın ana fonksiyonu
def main():
    # Kullanıcıdan ters çevirmek için bir metin girmesini isteyin
    user_input = input("Ters çevirmek istediğiniz metni girin: ")
    # Kullanıcının girdi metnini reverse_string fonksiyonuna gönderin
    # Ters çevrilmiş metni yazdırın
    print("Ters çevrilmiş metin:", reverse_string(user_input))


# Programın doğrudan çalıştırıldığını, modül olarak içe aktarılmadığını kontrol edin
if __name__ == "__main__":
    main()  # Program doğrudan çalıştırıldıysa ana fonksiyon çağrılır
