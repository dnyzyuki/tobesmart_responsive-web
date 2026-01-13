Add-Type -AssemblyName System.Drawing

function Trim-Image {
    param (
        [string]$ImagePath
    )

    try {
        $bmp = [System.Drawing.Bitmap]::FromFile($ImagePath)
        $width = $bmp.Width
        $height = $bmp.Height

        $minX = $width
        $minY = $height
        $maxX = 0
        $maxY = 0
        $hasContent = $false

        # Lock bits for speed would be better, but simple GetPixel loop is easier to write
        # Optimization: Scan lines with stride
        
        for ($y = 0; $y -lt $height; $y++) {
            for ($x = 0; $x -lt $width; $x++) {
                $color = $bmp.GetPixel($x, $y)
                # Check for non-white (allowing some noise/antialiasing near white)
                if ($color.R -lt 240 -or $color.G -lt 240 -or $color.B -lt 240) {
                    if ($x -lt $minX) { $minX = $x }
                    if ($x -gt $maxX) { $maxX = $x }
                    if ($y -lt $minY) { $minY = $y }
                    if ($y -gt $maxY) { $maxY = $y }
                    $hasContent = $true
                }
            }
        }

        if ($hasContent) {
            $rect = New-Object System.Drawing.Rectangle $minX, $minY, ($maxX - $minX + 1), ($maxY - $minY + 1)
            $cropped = $bmp.Clone($rect, $bmp.PixelFormat)
            $bmp.Dispose()
            $cropped.Save($ImagePath, [System.Drawing.Imaging.ImageFormat]::Png)
            $cropped.Dispose()
            Write-Host "Trimmed $ImagePath"
        }
        else {
            $bmp.Dispose()
            Write-Host "No content found in $ImagePath"
        }
    }
    catch {
        Write-Host "Error processing ${ImagePath}: $_"
    }
}

$directory = "C:\Users\kangdo\tobesmart-website\images"
for ($i = 1; $i -le 16; $i++) {
    $path = Join-Path $directory "partner_logo_$i.png"
    Trim-Image -ImagePath $path
}
