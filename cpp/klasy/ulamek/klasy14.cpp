class Ulamek
{
  int licznik;
  int mianownik;
public:
  Ulamek()	// definicja pierwszego konstruktora (bezparametrowego)
  {
    licznik = 1;	// licznikowi u�amka przypisujemy wartos� 1
    mianownik = 1;  // mianownikowi u�amka przypisujemy wartos� 1
  }	
  Ulamek (int l, int m); // deklaracja drugiego konstruktora (z parametrami)
  void wypisz()
  {
    cout << licznik << "/" << mianownik;}
  };					// koniec definicji klasy

Ulamek::Ulamek(int l, int m) // definicja konstruktora z parametrami
{
  licznik = ul;
  if (m!=0)
    mianownik = m;
  else
  {
    cout << "Mianownik nie moze miec wartosci 0 ";
    getchar();
    exit(1);
  }
}