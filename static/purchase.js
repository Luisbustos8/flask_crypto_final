function convertCurrency() {
    let from_currency = document.getElementById("from_currency").value;
    let to_currency = document.getElementById("to_currency").value;
    let form_quantity = document.getElementById("form_quantity").value;
    let url = `http://localhost:5000/calculate?form_quantity=${form_quantity}&from_currency=${from_currency}&to_currency=${to_currency}`;
    fetch(url)
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    console.log(myJson);
  });
    
}

//url_conversion = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert={}&CMC_PRO_API_KEY={}".format("form_quantity" "from_currency", "to_currency", API)