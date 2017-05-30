

function valcadprod() {	// FUNÇÃO PARA VALIDAR FORMULÁRIO

        

		var nomeJS = document.getElementById("nomeprod").value;

		if (nomeJS == null || nomeJS == "") {

		alert("Informe o nome de produto!");
		document.getElementById("nomeprod").focus();
		return false;

									}
									
		var quantprodJS = document.getElementById("quantprod").value;

		if (quantprodJS == null || quantprodJS == "") {

		alert("Informe a quantidade!");
		document.getElementById("quantprod").focus();
		return false;

									}
		
		var precoprodJS = document.getElementById("precoprod").value;
		if (precoprodJS == "") {

		alert("Informe o preço unitário!");
		document.getElementById("precoprod").focus();
		return false;

									}
		

		else { 
				alert("Produto cadastrado com sucesso!");
				cadnovoprod();

			}
}
	function cadnovoprod() {
		
	var outroprod=confirm("Deseja cadastrar outro produto?")
	if (outroprod==true){
	location.reload();
	}
	else	{
	alert("Obrigado!")
	}
}