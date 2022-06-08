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

namespace Haromszogek
{
    public partial class Form1 : Form
    {
        static List<DHaromszog> ldh = new List<DHaromszog>();

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox2.Items.Clear();
            listBox3.Items.Clear();
            openFileDialog1.ShowDialog();
            string f = openFileDialog1.FileName.ToString();
            string[] be = File.ReadAllLines(f);
            int i = 1;
            foreach(var k in be)
            {
                try
                {
                    DHaromszog h = new DHaromszog(k, i);
                    listBox2.Items.Add(h.SorSzama + ". sor: a=" + h.a + " b=" + h.b + " c=" + h.c);
                    ldh.Add(h);
                }
                catch (Exception p)
                {
                    listBox1.Items.Add(p.Message);
                }
                i++;
            }
        }

        private void listBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
            listBox3.Items.Clear();
            string[] s = listBox2.SelectedItem.ToString().Split(' ');
            int k = int.Parse(s[0].Substring(0, s[0].Length - 1));
            int j = 0;
            while (j < ldh.Count && ldh[j].SorSzama != k) j++;
            listBox3.Items.Add(" ");
            listBox3.Items.Add("Kerület = " + ldh[j].Kerulet);
            listBox3.Items.Add(" ");
            listBox3.Items.Add("Terület = " + ldh[j].Terulet);
        }
    }
}
