# sample code from openapi

from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus


url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getForeignTuristStatsList'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '39r0FFTOZrR/sPXd3DR/3h+sCsomBP+bhBiPgt8o+Oke+iTQJ3GWonJ8gjDhq2TY6AAnz9bUo8MUGlVn8Ct+bg==', quote_plus('YM') : '201201', quote_plus('NAT_CD') : '155', quote_plus('AGE_CD') : '40', quote_plus('TRA_PURP_CD') : '02', quote_plus('PORT_CD') : 'KJ', quote_plus('SEX_CD') : 'F' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print response_body




