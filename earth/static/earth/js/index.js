function filterWine() {
	let searchText = document.getElementById('searchText').value;
	let chooseField = document.getElementById('chooseField').value;

	if(searchText.length > 0)
		window.location.href = `/?field=${chooseField}&text=${searchText}`
}