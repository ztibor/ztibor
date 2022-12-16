using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace EgyszamjatekGUI
{
   
    
    public partial class Form1 : Form
    {
        public static List<Jatekos> lj;  

        public Form1()
        {
            InitializeComponent();
             
    }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            int s = textBox2.Text.Trim().Split(' ').Length;
            label3.Text = Convert.ToString(s) + " db";
        }

       
        private void button1_Click(object sender, EventArgs e)
        {
            List<Jatekos> lj = new List<Jatekos>();
            foreach (var k in File.ReadAllLines("egyszamjatek2.txt"))
                lj.Add(new Jatekos(k));
            int ldb = lj.Where(x => x.nev == textBox1.Text).ToList().Count;
            int tippsz = lj[0].tipp.Count;
            int tp = Convert.ToInt32(label3.Text.Substring(0, label3.Text.Length - 3));
            if (ldb != 0)
                MessageBox.Show("Van már ilyen nevű játékos","Hiba");
            else if (tippsz != tp)
                MessageBox.Show("Tippek száma nem megfelelő", "Hiba");
            else
            {
                StreamWriter fs = File.AppendText("egyszamjatek2.txt");
                string s = "";
                s += textBox1.Text + " ";
                foreach (var k in textBox2.Text.Trim().Split(' '))
                    s += k + " ";
                s = s.Trim()+"\n";
                fs.Write(s);
                fs.Close();
                MessageBox.Show("Az állomány bővítése sikeres volt", "Üzenet");
            }
        }
    }

    public class Jatekos
    {
        public string nev;
        public List<int> tipp;

        public Jatekos(string sor)
        {
            string[] s = sor.Trim().Split(' ');
            nev = s[0];
            int db = s.Length - 1;
            tipp = new List<int>();
            foreach (var k in s.Skip(1))
                tipp.Add(int.Parse(k));
        }
    }
}
