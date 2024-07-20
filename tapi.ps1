$dockerHost = "localhost"  # Changed from host.docker.internal to localhost
$apiPort = "5000"

try {
    # Check if the server is accessible
    Write-Host "Checking root endpoint..."
    $rootResponse = Invoke-WebRequest -Method GET -Uri "http://${dockerHost}:${apiPort}/"
    Write-Host "Root endpoint response: $($rootResponse.StatusCode) $($rootResponse.StatusDescription)"
    Write-Host "Content: $($rootResponse.Content)"

    # Try to access the login endpoint
    Write-Host "`nTrying login endpoint..."
    $loginResponse = Invoke-WebRequest -Method POST -Uri "http://${dockerHost}:${apiPort}/login" -ContentType "application/json"
    $token = ($loginResponse.Content | ConvertFrom-Json).access_token
    Write-Host "Login response: $($loginResponse.StatusCode) $($loginResponse.StatusDescription)"
    Write-Host "Obtained token: $token"

    # Rest of your script...
} catch {
    Write-Host "An error occurred:"
    Write-Host $_.Exception.Message
    if ($_.Exception.Response) {
        $result = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($result)
        $reader.BaseStream.Position = 0
        $reader.DiscardBufferedData()
        $responseBody = $reader.ReadToEnd()
        Write-Host "Response Body: $responseBody"
    }
}