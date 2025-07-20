# AuditUsers.ps1
$OutputFile = "$env:USERPROFILE\Documents\PythonProjects\scripts\UserAudit_$(Get-Date -Format 'yyyyMMdd_HHmmss').txt"

# Get local user accounts
"==== LOCAL USERS ====" | Out-File -FilePath $OutputFile
Get-LocalUser | Format-List Name, Enabled, LastLogon | Out-File -Append -FilePath $OutputFile

# Get local group membership
"`n==== ADMIN GROUP MEMBERS ====" | Out-File -Append -FilePath $OutputFile
Get-LocalGroupMember -Group "Administrators" | Format-List Name, ObjectClass | Out-File -Append -FilePath $OutputFile

# Check for recent login sessions
"`n==== RECENT LOGINS ====" | Out-File -Append -FilePath $OutputFile
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4624} -MaxEvents 20 | 
    ForEach-Object {
        [PSCustomObject]@{
            TimeCreated = $_.TimeCreated
            AccountName = $_.Properties[5].Value
            LogonType   = $_.Properties[8].Value
            IPAddress   = $_.Properties[18].Value
        }
    } | Out-File -Append -FilePath $OutputFile

# Notify completion
Write-Host "✅ Audit complete. Results saved to: $OutputFile"
