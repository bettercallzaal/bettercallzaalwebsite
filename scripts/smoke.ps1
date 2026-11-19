$routes = @('/','zao/','wavewarz/','bczyapz/','streaming/','Maine/','outdoors/','engineering-past/','zaostock/','zabalgames.html','nexus.html','kit.html','poidh.html','privacy.html','terms.html','refund.html')
foreach ($r in $routes) {
  try {
    $code = (Invoke-WebRequest -Uri "http://127.0.0.1:8765/$r" -UseBasicParsing -TimeoutSec 5).StatusCode
  } catch {
    $code = $_.Exception.Response.StatusCode.value__
  }
  '{0,-25} {1}' -f $r, $code
}
