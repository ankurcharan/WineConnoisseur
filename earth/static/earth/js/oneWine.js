function sortPriceAsc() {
	document.getElementById('desc').parentElement.classList.remove('active');
	document.getElementById('asc').parentElement.classList.add('active');

	window.location.href = window.location.href + '&sort=asc';
}

function sortPriceDesc() {
	document.getElementById('asc').parentElement.classList.remove('active');
	document.getElementById('desc').parentElement.classList.add('active');

	window.location.href = window.location.href + '&sort=desc';
}