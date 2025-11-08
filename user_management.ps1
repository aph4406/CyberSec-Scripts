# Save as user_management.ps1
$KeepList = @("Administrator", "defaultuser0", "User3")
$ExcludeFromPasswordChange = @("ServiceAccount1")
$Password = ConvertTo-SecureString "ChangeMeNow!2025" -AsPlainText -Force

# Remove extra users
Get-LocalUser | Where-Object { $_.Name -notin $KeepList } | ForEach-Object {
    Remove-LocalUser -Name $_.Name
    Write-Output "Removed: $($_.Name)"
}

# Change passwords
foreach ($user in $KeepList) {
    if ($user -in $ExcludeFromPasswordChange) { continue }
    Set-LocalUser -Name $user -Password $Password
    Write-Output "Password changed: $user"
}
