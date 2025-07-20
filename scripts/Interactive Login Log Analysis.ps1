$outputDir = "C:\Users\watte\Documents\PythonProjects\logs"
if (!(Test-Path $outputDir)) {
    New-Item -Path $outputDir -ItemType Directory
}

$logonEvents = Get-WinEvent -FilterHashtable @{
    LogName = 'Security';
    Id = 4624;
    StartTime = (Get-Date).AddDays(-30)
} | Where-Object {
    ($_.Properties[8].Value -eq 2 -or $_.Properties[8].Value -eq 10) -and
    ($_.Properties[5].Value -ne 'ANONYMOUS LOGON')
} | Select-Object TimeCreated, 
    @{Name="User";Expression={$_.Properties[5].Value}},
    @{Name="LogonType";Expression={$_.Properties[8].Value}},
    @{Name="IPAddress";Expression={$_.Properties[18].Value}}

$grouped = $logonEvents | Group-Object User

foreach ($group in $grouped) {
    $safeName = $group.Name -replace '[\\/:*?"<>|]', '_'
    $filePath = Join-Path $outputDir "$safeName-logins.csv"
    $group.Group | Export-Csv -Path $filePath -NoTypeInformation
}

Write-Host "Login reports saved to $outputDir"