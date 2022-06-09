using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Haromszogek
{
    class DHaromszog
    {
        double aOldal, bOldal, cOldal;
        public double a { get; set; }
        public double b { get; set; }
        public double c { get; set; }
        bool EllDerekszogu { get; }
        bool EllMegszerkesztheto { get; }
        bool EllNovekvosorrend { get; }
        public double Kerulet { get; }
        public double Terulet { get; }
        public int SorSzama { get; set; }

        public DHaromszog(string sor, int SorSzáma)
        {
            string[] s = sor.Split(' ');
            SorSzama = SorSzáma;
            a = double.Parse(s[0]);
            b = double.Parse(s[1]);
            c = double.Parse(s[2]);
            if (a>0 && b>0 && c > 0)
            {
                EllNovekvosorrend = (a <= b && b <= c);
                if (!EllNovekvosorrend) throw new System.Exception(SorSzama + ". sor: Az adatok nincsenek növekvő sorrendben!");
                EllMegszerkesztheto = a + b > c;
                if (!EllMegszerkesztheto) throw new System.Exception(SorSzama + ". sor: A háromszöget nem lehet megszerkeszteni!");
                EllDerekszogu = a * a + b * b == c * c;
                if (!EllDerekszogu) throw new Exception(SorSzama + ". sor: A háromszög nem derékszögű!");
                aOldal = a;
                bOldal = b;
                cOldal = c;
                Kerulet = a + b + c;
                Terulet = a * b / 2;
            }
            else
            {
                if (a <= 0) throw new Exception(SorSzama + ". sor: Az 'a' oldal nem lehet nulla vagy negatív!");
                if (b <= 0) throw new Exception(SorSzama + ". sor: A 'b' oldal nem lehet nulla vagy negatív!");
                if (c <= 0) throw new Exception(SorSzama + ". sor: A 'c' oldal nem lehet nulla vagy negatív!");
            }
        }

    }

    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }
    }
}
