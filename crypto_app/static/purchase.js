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
    const converted_price = myJson.data.quote[to_currency].price;
    const converted_price_rounded = converted_price.toFixed(2);
    const to_quantity_element = document.getElementById("to_quantity").value = converted_price_rounded;
    const unit_price_element = document.getElementById("precio_unitario");
    const unit_price = (parseInt(form_quantity) / converted_price).toFixed(2);
    unit_price_element.value = unit_price;
  });
    
}
