wyniki=[60,50,60,58,54,54,58,50,52,54,48,69,34,55,51,52,44,
51,69,64,66,55,52,61,46,31,57,52,44,18,41,53,55,61,51,44]

dlugosc=len(wyniki)
najwyzszy_wynik=0

for i in range(dlugosc):
	print ('Wynik roztworu #'+ str(i), 'to:', wyniki[i])
	if wyniki[i]>najwyzszy_wynik:
		najwyzszy_wynik=wyniki[i];
print ('Liczba testow :', dlugosc)
print ('Najwyzszy wynik to:', najwyzszy_wynik)

najlepsze_roztwory=[]
for i in range(dlugosc):
	if najwyzszy_wynik == wyniki[i]:
	   najlepsze_roztwory.append(i)

print('Roztwory o najwyzszym wyniku:', najlepsze_roztwory)
