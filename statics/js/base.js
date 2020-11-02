 function disableTrue() {
         document.getElementById("nome").disabled = false;
         document.getElementById("identidade").disabled = false;
         document.getElementById("inputCPF").disabled = false;
         document.getElementById("inputcep").disabled = false;
         document.getElementById("telefone").disabled = false;
         document.getElementById("endereco").disabled = false;
         document.getElementById("inputnumero").disabled = false;
         document.getElementById("bairro").disabled = false;
         document.getElementById("cidade").disabled = false;
         document.getElementById("estado").disabled = false;


    }

 function myFunction(imgs) {
  var expandImg = document.getElementById("expandedImg");
  var imgText = document.getElementById("imgtext");
  expandImg.src = imgs.src;
  imgText.innerHTML = imgs.alt;
  expandImg.parentElement.style.display = "block";

     }

 function calculaData(vigencia){

    var date = document.getElementById("id_data_entrada");
    console.log(document.getElementById("id_data_entrada").value);
    var dateEntered = new Date(date.value);
    console.log(dateEntered)
    dateEntered.setDate(dateEntered.getDate() + 1)
    var intVigencia = parseInt(vigencia);
    //var recebe = formatDate(date.value)
    console.log(dateEntered)
    var mes = dateEntered.getMonth()
    //console.log(mes)
    var soma = mes + intVigencia
    //console.log(soma)
    dateEntered.setMonth(soma);
    //console.log(dateEntered)
    //console.log(dateEntered)
    var recebe = formatDate(dateEntered)
    console.log(recebe)
    document.getElementById('id_vencimento').value = recebe;

   }

function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2)
        month = '0' + month;
    if (day.length < 2)
        day = '0' + day;

    return [year, month, day].join('-');
}



