# Lab 8 DieFace

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `DieFace.cs` · [[File Handling and Serial Ports]] · [[GUI and Event-Driven Programming]]

```csharp
using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;

namespace ExampleDieRollerGUI
{
    public static class DieFace
    {
        private static readonly Dictionary<int, Image> _cache = new();

        public static Image GetImage(int value)
        {
            if (value < 1 || value > 6)
            {
                return MakeFallbackBitmap("?", Color.LightCoral);
            }

            if (_cache.TryGetValue(value, out Image? img))
            {
                return img;
            }

            string exeDir = AppDomain.CurrentDomain.BaseDirectory;
            string path = Path.Combine(exeDir, "Assets", $"Die_{value}.png");

            if (!File.Exists(path))
            {
                img = MakeFallbackBitmap(value.ToString(),
                    Color.LightGoldenrodYellow);
                _cache[value] = img;
                return img;
            }

            using (Image tmp = Image.FromFile(path))
            {
                img = new Bitmap(tmp);
            }

            _cache[value] = img;
            return img;
        }

        public static Image GetPlaceholder()
        {
            return MakeFallbackBitmap("—", Color.LightGray);
        }

        private static Bitmap MakeFallbackBitmap(string text, Color backColor)
        {
            Bitmap bmp = new Bitmap(220, 220);

            using (Graphics g = Graphics.FromImage(bmp))
            {
                g.Clear(backColor);

                using Font font = new Font("Segoe UI", 48, FontStyle.Bold);
                using Brush brush = new SolidBrush(Color.Black);

                SizeF size = g.MeasureString(text, font);
                float x = (bmp.Width - size.Width) / 2.0f;
                float y = (bmp.Height - size.Height) / 2.0f;

                g.DrawString(text, font, brush, x, y);
                g.DrawRectangle(Pens.DimGray, 0, 0,
                    bmp.Width - 1, bmp.Height - 1);
            }

            return bmp;
        }

        public static void ClearCache()
        {
            foreach (Image img in _cache.Values)
            {
                img.Dispose();
            }
            _cache.Clear();
        }
    }
}
```
