function filterGrapesUsed() {
	let text = document.getElementById('searchText').value;	
	window.location.href = window.location.href + '?grape=' + text 
}