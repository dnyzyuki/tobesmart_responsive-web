Add-Type -AssemblyName System.Drawing
$sourcePath = "C:\Users\kangdo\.gemini\antigravity\brain\b61de6a0-852c-4442-bc31-a1b174707b51\uploaded_image_1768207843773.png"
$outputDir = "C:\Users\kangdo\tobesmart-website\images"
if (!(Test-Path $outputDir)) { New-Item -ItemType Directory -Path $outputDir }

$img = [System.Drawing.Image]::FromFile($sourcePath)
$cellW = 256
$cellH = 117 # 470 / 4 approx

for ($row = 0; $row -lt 4; $row++) {
    for ($col = 0; $col -lt 4; $col++) {
        $index = ($row * 4) + $col + 1
        $x = $col * $cellW
        $y = $row * $cellH
        
        $rect = New-Object System.Drawing.Rectangle $x, $y, $cellW, $cellH
        $bmp = New-Object System.Drawing.Bitmap $cellW, $cellH
        $g = [System.Drawing.Graphics]::FromImage($bmp)
        $g.Clear([System.Drawing.Color]::White)
        $g.DrawImage($img, (New-Object System.Drawing.Rectangle 0, 0, $cellW, $cellH), $rect, [System.Drawing.GraphicsUnit]::Pixel)
        
        $outPath = Join-Path $outputDir "partner_logo_$index.png"
        $bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
        $g.Dispose()
        $bmp.Dispose()
    }
}
$img.Dispose()
Write-Host "Done cropping 16 logos."
