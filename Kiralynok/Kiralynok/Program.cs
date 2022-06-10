using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Kiralynok
{
    class Tábla
    {
        private char[,] T;
        private char ÜresCella;

        public Tábla(char ch)
        {
            T = new char[8, 8];
            ÜresCella = ch;
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 8; j++)
                    T[i, j] = ch;
        }
        //4. feladat
        public void Megjelenít()
        {
            for (int i = 0; i < 8; i++)
            {
                for (int j = 0; j < 8; j++)
                    Console.Write(T[i, j]);
                Console.WriteLine();
            }
        }
        //5. feladat
        public void Elhelyez(int N)
        {
            Random r = new Random();
            int n = 0;
            for(int k=0;k<N;k++)
            {
                do
                {
                    n = r.Next(64);
                } while (T[n / 8, n % 8] == 'K');
                T[n / 8, n % 8] = 'K';
            }
        }

        public bool ÜresOszlop(int a)
        {
            int i = 0;
            while (i < 8 && T[i, a] != 'K') i++;
            if (i == 8) return true;
            else return false;
        }

        public bool ÜresSor(int a)
        {
            int i = 0;
            while (i < 8 && T[a, i] != 'K') i++;
            if (i == 8) return true;
            else return false;
        }

        public int ÜresOszlopokSzáma {
            get
            {
                int db = 0;
                for (int i = 0; i < 8; i++)
                    if (ÜresOszlop(i)) db++;
                return db;
            }
        }

        public int ÜresSorokSzáma
        {
            get
            {
                int db = 0;
                for (int i = 0; i < 8; i++)
                    if (ÜresSor(i)) db++;
                return db;
            }
        }
        //10. feladat
        public string[] Fajlbaír()
        {
            string s;
            string[] st = new string[8];
            for(int i = 0; i < 8; i++)
            {
                s = "";
                for (int j = 0; j < 8; j++) s += T[i, j];
                st[i] = s;
            }
            return st;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //4. feladat
            Console.WriteLine("4. feladat: Az üres tábla:");
            Tábla sakk = new Tábla('#');
            sakk.Megjelenít();

            //6. feladat
            Console.WriteLine("\n6. feladat: A feltöltött tábla:");
            sakk.Elhelyez(8);
            sakk.Megjelenít();

            //9. feladat
            Console.WriteLine("\n9. feladat: Üres oszlopok és sorok száma:");
            Console.WriteLine("Oszlopok: {0}\nSorok: {1}", sakk.ÜresOszlopokSzáma, sakk.ÜresSorokSzáma);

            //10. feladat
            if (File.Exists("tablak64.txt")) File.Delete("tablak64.txt");
            List<string> ki = new List<string>();
            for(int k = 0; k < 64; k++)
            {
                Tábla t = new Kiralynok.Tábla('*');
                t.Elhelyez(k);
                string[] a = t.Fajlbaír();
                foreach (var p in a) ki.Add(p);
                ki.Add(" ");
            }
            File.WriteAllLines("tablak64.txt", ki);

            Console.ReadKey();
        }
    }
}
