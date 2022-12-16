using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
//1. feladat
namespace Egyszamjatek
{
    class Jatekos
    {
        public string nev;
        public int[] tipp;

        public Jatekos(string sor)
        {
            string[] s= sor.Split(' ');
            nev = s[0];
            tipp = new int[s.Length-1];
            for(int i = 1; i < s.Length; i++)
                tipp[i - 1] = int.Parse(s[i]);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //2. feladat
            var lj = new List<Jatekos>();
            foreach (var x in File.ReadAllLines("egyszamjatek1.txt"))
                lj.Add(new Jatekos(x));

            //3. feladat
            Console.WriteLine("Játékosok száma: {0} fő", lj.Count);

            //4. feladat
            Console.Write("4. feladat: Kérem a forduló sorszámát:");
            int sor = int.Parse(Console.ReadLine());

            //5. feladat
            var atlag = lj.Select(x=>x.tipp[sor-1]).ToList().Average();                
            Console.WriteLine("5. feladat: A megadott forduló tippjeinek átlaga: {0:F2}",atlag);
            
            Console.ReadLine();
        }
    }
}
