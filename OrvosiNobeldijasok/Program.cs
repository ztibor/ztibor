using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
//1. feladat
namespace OrvosiNobeldijasok
{
    class Dijasok
    {
        public int Év;
        public string Név;
        public string SzületésHalálozás;
        public string Országkód;

        public Dijasok(string a)
        {
            string[] s = a.Split(';');
            Év = int.Parse(s[0]);
            Név = s[1];
            SzületésHalálozás = s[2];
            Országkód = s[3];
        }
    }
    //7. feladat
    class Elethossz
    {
        private int Tol { get; set; }
        private int Ig { get; set; }
        public int ElethosszEvekben => Tol == -1 || Ig == -1 ? -1 : Ig - Tol;

        public bool IsmertAzElethossz => ElethosszEvekben != -1;

        public Elethossz(string SzuletesHalalozas)
        {
            string[] m = SzuletesHalalozas.Split('-');
            try
            {
                Tol = int.Parse(m[0]);
            }
            catch (Exception)
            {
                Tol = -1;
            }
            try
            {
                Ig = int.Parse(m[1]);
            }
            catch (Exception)
            {
                Ig = -1;
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //2. feladat
            string[] be = File.ReadAllLines("orvosi_nobeldijak.txt");
            List<Dijasok> ld = new List<Dijasok>();
            foreach (var k in be.Skip(1)) ld.Add(new Dijasok(k));

            //3. feladat
            Console.WriteLine("3. feladat: Díjazottak száma: {0} fő", ld.Count);

            //4. feladat
            Console.WriteLine("4. feladat: Utolsó év: {0}", ld.OrderByDescending(x => x.Év).ToList().First().Év);

            //5. feladat
            Console.Write("5. feladat: KÉrem adja meg egy ország kódját: ");
            string orsz = Console.ReadLine();
            List<Dijasok> lor = ld.Where(x => x.Országkód.Equals(orsz)).ToList();
            if (lor.Count == 0) Console.WriteLine("A megadott országból nem volt díjazott");
            else if (lor.Count == 1) Console.WriteLine("A megadott ország díjazottja:\n\tÉv: {0}\n\tNév: {1}\n\tSz/H: {2}", lor.First().Év, lor.First().Név, lor.First().SzületésHalálozás);
            else Console.WriteLine("A megadott országból {0} fő díjazott volt", lor.Count);

            //6. feladat
            Dictionary<string, int> ds = new Dictionary<string, int>();
            foreach (var k in ld)
                if (ds.ContainsKey(k.Országkód)) ds[k.Országkód]++;
                else ds.Add(k.Országkód, 1);
            Console.WriteLine("6. Statisztika:");
            foreach (var k in ds)
                if (k.Value > 5) Console.WriteLine("\t{0} - {1}", k.Key, k.Value);

            //7. feladat
            double szum = 0;
            int db = 0;
            foreach(var k in ld)
            {
                Elethossz eh = new Elethossz(k.SzületésHalálozás);
                if (eh.IsmertAzElethossz)
                {
                    szum += eh.ElethosszEvekben;
                    db++;
                }
            }
            Console.WriteLine("7. feladat: A keresett átlag: {0:N1} év", szum / db);

            Console.ReadKey();
        }
    }
}
