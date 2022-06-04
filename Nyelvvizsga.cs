using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Nyelvvizsga
{
    class Vizsga
    {
        public string nyelv;
        public List<int> siker, slen, osszes;

        public Vizsga(string sor1,string sor2)
        {
            string[] s1 = sor1.Split(';');
            string[] s2 = sor2.Split(';');
            nyelv = s1[0];
            siker = new List<int>();
            slen = new List<int>();
            osszes = new List<int>();
            for(int i = 1; i < s1.Length; i++)
            {
                siker.Add(int.Parse(s1[i]));
                slen.Add(int.Parse(s2[i]));
                osszes.Add(siker[i - 1] + slen[i - 1]);
            }
        }
    }

    class Nyelvvizsga
    {
        static void Main(string[] args) 
        { 
            //1. feladat
            string[] inp1 = File.ReadAllLines("sikertelen.csv",Encoding.Default);
            string[] inp2 = File.ReadAllLines("sikeres.csv",Encoding.Default);
            List<Vizsga> lv = new List<Vizsga>();
            for (int i = 1; i < inp1.Length; i++)
                lv.Add(new Vizsga(inp1[i], inp2[i]));

            //2. feladat
            List<Vizsga> sorrend=new List<Vizsga>(lv.OrderByDescending(x => x.osszes.Sum()).ToList().Take(3));
            Console.WriteLine($"2. feladat: A legnépszerűbb nyelvek:");
            foreach (var k in sorrend)
                Console.WriteLine($"\t{k.nyelv}");

            //3. feladat
            Console.WriteLine("3. feladat:");
            int ev;
            do
            {
                Console.Write("\tVizsgáladó év: ");
                ev = int.Parse(Console.ReadLine());
            } while (ev < 2009 || ev > 2017);

            //4. feladat
            Vizsga leg = lv.Where(x => x.osszes[ev - 2009] != 0).ToList().OrderByDescending(x=>(double)x.slen[ev-2009]/x.osszes[ev-2009]).ToList().First();
            Console.WriteLine($"\t{ev}-ben {leg.nyelv} nyelvből a sikertelen vizsgázók aránya {(double)leg.slen[ev-2009]/leg.osszes[ev - 2009]:P2} ");

            //5. feladat
            Console.WriteLine("5. feladat");
            List<Vizsga> nemvolt = new List<Vizsga>(lv.Where(x => x.osszes[ev - 2009] == 0).ToList());
            if (nemvolt.Count == 0) Console.WriteLine("Minden nyelvből volt vizsgázó.");
            else foreach (var k in nemvolt) Console.WriteLine($"\t{k.nyelv}");

            //6. feladat
            List<string> output = new List<string>();
            foreach (var k in lv)
                output.Add(k.nyelv + ";" + k.osszes.Sum().ToString() + ";" + Math.Round((double)k.siker.Sum() / k.osszes.Sum()*100, 2).ToString()+"%");
            File.WriteAllLines("osszesites.csv", output);                

            Console.ReadKey();
        }
    }
}
