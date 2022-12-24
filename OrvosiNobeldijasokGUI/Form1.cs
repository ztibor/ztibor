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

namespace OrvosiNobeldijasokGUI
{
    public partial class Form1 : Form
    {
        List<string> ls;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ls = new List<string>();
            string s = "Év;Név;SzületésHalálozás;Országkód";
            ls.Add(s);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Length == 0 || textBox2.Text.Length == 0 || textBox3.Text.Length == 0 || textBox4.Text.Length == 0)
                MessageBox.Show("Töltsön ki minden mezőt!");
            else
            {
                int ev = int.Parse(textBox1.Text);
                if (ev <= 1989)
                {
                    MessageBox.Show("Hiba! Az évszám nem megfelelő.");

                }
                else
                {
                    ls.Add(textBox1.Text + ";" + textBox2.Text + ";" + textBox3.Text + ";" + textBox4.Text);
                    try
                    {
                        File.WriteAllLines("uj_dijazott.txt", ls);
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show(ex.Message);
                    }
                    textBox1.Clear();
                    textBox2.Clear();
                    textBox3.Clear();
                    textBox4.Clear();
                }
            }
        }       
    }
}
