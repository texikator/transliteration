$data = @{"account_data"="Гончаренко Иван"; "location"="field" ;}
$content_type = "application/json; charset=utf-8"
$url = 'http://localhost:5000/transliterate/api/v1.0/detailed'
$url_simple = 'http://localhost:5000/transliterate/api/v1.0/simple'
#$result = Invoke-WebRequest -Uri $url -Method POST -Body ($data | ConvertTo-Json) -ContentType $content_type


$response = Invoke-RestMethod -uri $url -ContentType $content_type -Method POST -Body ($data| ConvertTo-JSON)


$full_name = $response.data.full_name
write-host "full name is :  $full_name"



#$data_arr = $

$data = @{"text"= "треш и угар";}
$response = Invoke-RestMethod -uri $url_simple -Method POST -Body ($data | ConvertTo-JSON) -ContentType $content_type
#$result = Invoke-WebRequest -Uri $url_simple -Method POST -Body ($data | ConvertTo-Json) -ContentType $content_type

$transliterated_text = $response.data.text
write-host "text is '$transliterated_text'"
