import urllib,requests;
initURL = "http://www.berkshirehathaway.com/letters/";
for i in range( 2004 , 2018 ):
    print(i);
    finalURL = initURL+str(i)+"ltr.pdf";
    print(finalURL);
    r = requests.get(finalURL,stream=True,allow_redirects=True);
    urllib.request.urlretrieve(finalURL, str(i)+'ltr.pdf');
