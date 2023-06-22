const list = new Array(60000).join('1.1').split('.');

function removeItemsFromList() {
	var item = list.pop();
	console.log(item)

	if (item) {
		setTimeout(removeItemsFromList , 0)
	}
};


setTimeout(() => console.log('1'), 0)
Promise.resolve('hi').then(() => console.log('2'))
console.log('3')


